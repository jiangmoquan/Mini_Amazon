import queue
import struct
import sys
import threading
import socket
import psycopg2
import tutorial_pb2
import AmazonUPS_pb2
import AmazonWorld_pb2
import socketserver
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint



WORLD_IP = "vcm-2464.vm.duke.edu"
WORLD_PORT = 23456

UPS_IP = "localhost"
UPS_PORT = 20000

SIM_SPEED = 5

LISTEN_PORT = 10000
LISTEN_IP = "localhost"

MAX_CONNECTION = 100
RECEIVE_BYTES = 4

conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", port= "5433")




def socket_read_n(sock, n):
    """ Read exactly n bytes from the socket.
        Raise RuntimeError if the connection closed before
        n bytes were read.
    """
    buf = ''
    while n > 0:
        data = sock.recv(n)
        if data == b'':
            raise RuntimeError('unexpected connection close')
        buf += data.decode(sys.stdout.encoding)
        n -= len(data)
    return buf


def get_message(sock, msgtype):
    """ Read a message from a socket. msgtype is a subclass of
        of protobuf Message.
    
    len_buf = socket_read_n(sock, 4)

    (length, pos) = _DecodeVarint32(len_buf, 0)

    msg_buf = socket_read_n(sock, length - (4-pos))

    new_msg = len_buf + msg_buf

    real_msg = new_msg[pos:pos+length]

    #msg_len = struct.unpack('>L', len_buf.encode())[0]
    #msg_buf = socket_read_n(sock, msg_len)

    msg = msgtype()
    msg.ParseFromString(real_msg)
    return msg
    """
    recvmsg = sock.recv(4096)
    (length, pos) = _DecodeVarint32(recvmsg, 0)

    msg = msgtype()
    msg.ParseFromString(recvmsg[pos:pos+length])
    return msg






def send_message(sock, message):
    """ Send a serialized message (protobuf Message interface)
        to a socket, prepended by its length packed in 4
        bytes (big endian).
    """
    s = message.SerializeToString()
    #print("before pack, the len is ", len(s))
    _EncodeVarint(sock.sendall, len(s), None)

    #packed_len = struct.pack('>L', len(s))
    sock.sendall(s)


def sendandrecvUPS(command_msg):
    ups_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    ups_sock.connect((UPS_IP, UPS_PORT))

    send_message(ups_sock, command_msg)

    response_msg = get_message(ups_sock, AmazonWorld_pb2.Uresponses)  
        
    ups_sock.close() 

    return response_msg


def toBuy(world_sock,package_id):
    command_msg = AmazonWorld_pb2.ACommands()
    command_msg.simspeed = SIM_SPEED
    buying = command_msg.buy.add()
    try:
        cur = conn.cursor()                                                                                                                                                                                 
        cur.execute("SELECT wh_id_id FROM order_order WHERE id = %s;", (package_id, ))                                                                                                                      
        row = cur.fetchone()                                                                                                                                                                                

        buying.whnum = row[0]                                                                                                                                                                               

        cur.execute("SELECT product_id, quantity FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()                                                                                                                                                                               
        for row in rows:                                                                                                                                                                                    
            cur.execute("SELECT description FROM product_product WHERE id = %s;", (row[0], ))
            des = fetchone()                                                                                                                                                                                

            item = buying.things.add()                                                                                                                                                               
            item.id = row[0]
            item.count = row[1]                                                                                                                                                                             
            item.description = des[0]                                                                                                                                                                       


        send_message(world_sock, command_msg)                                                                                                                                                           

        conn.commit()                                                                                                                                                                                    
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




def toPack(world_sock, package_id):
    command_msg = AmazonWorld_pb2.ACommands()
    command_msg.simspeed = SIM_SPEED
    pack = command_msg.topack.add()

    try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, tracking_num FROM order_order WHERE id = %s;", (package_id, ))
        row = cur.fetchone()

        pack.whnum = row[0]
        pack.shipid = row[1]


        cur.execute("SELECT product_id, quantity FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()
        for row in rows:
            cur.execute("SELECT open_quantity FROM order_inventory WHERE product_id_id = %s AND wh_id_id = %s;", (row[0], pack.whnum, ))
            open = fetchone()

            cur.execute("UPDATE order_inventory SET open_quantity = %s WHERE product_id_id = %s AND wh_id_id = %s;", (open - row[1], row[0], pack.whnum, ))
            cur.execute("SELECT description FROM product_product WHERE id = %s;", (row[0], ))
            des = cur.fetchone()

            item = APack.things.add()
            item.id = row[0]
            item.count = row[1]
            item.description = des[0]

        
        send_message(world_sock, command_msg)
        cur.execute("UPDATE order_order SET status = 'K' WHERE id = %s;", (package_id, ))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def toLoad(world_sock, package_id, truck_id):
    command_msg = AmazonWorld_pb2.ACommands()
    command_msg.simspeed = SIM_SPEED
    loading = command_msg.load.add()
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, tracking_num FROM order_order WHERE id = %s;", (package_id, ))
        row = cur.fetchone()
        
        loading.whnum = row[0]
        loading.shipid = row[1]
        loading.truckid = truck_id
        
        cur.execute("UPDATE order_order SET status = 'L', truck_id = %s WHERE id = %s;", (truck_id, package_id, ))

        send_message(world_sock, command_msg)     
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
                                


def letTruckGo(truckid, whid):
    loaded = AmazonUPS_pb2.Apackages_loaded()
    loaded.truck_id = truckid
    loaded.wh_id = whid

    try:
        cur = conn.cursor()
        cur.execute("SELECT tracking_num FROM order_order WHERE wh_id_id = %s AND truck_id = %s AND status = 'D';", (whid, truckid, ))
        rows = cur.fetchall()

        for row in rows:
            cur.execute("UPDATE order_order SET status = 'S'  WHERE  tracking_num = %s;", (row[0], ))
            tracking = loaded.package_id.add()
            tracking = row[0]

        cur.execute("DELETE FROM order_truck WHERE wh_id_id = %s AND truck_id = %s;", (whid,truckid ))

        conn.commit()
        cur.close()

        command_msg = AmazonUPS_pb2.Acommands()
        command_msg.packages_loaded = loaded

        response_msg = sendandrecvUPS(command_msg) 
        
        response_acknowledge = response_msg.acknowledge
        
        if response_acknowledge.error != "":
            print(response_acknowledge.error) 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    




###############################  Handle the UPS #############################################

def handleTruckArrived(world_sock, Utruck_arrival):
    truck_id = Utruck_arrival.truck_id
    wh_id = Utruck_arrival.wh_id
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO order_truck (truck_id, wh_id_id) VALUES (%s, %s);", (truck_id, wh_id))


        cur.execute("SELECT id  FROM order_order WHERE status = 'T' AND wh_id_id = %s;", ( wh_id, ))
        rows = cur.fetchall()
        for row in rows:
            toload(world_sock, row[0], truck_id)


        conn.commit()
        cur.close()

        return 1, ""

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 0, error


def handlePackageDelivered(Upackage_deliver):
    package_id = Upackage_deliver.package_id
    try:
        cur = conn.cursor()
        cur.execute("UPDATE order_order SET status = 'E'  WHERE  id = %s;", (package_id, ))

        conn.commit()
        cur.close()
        return 1, ""
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 0, error


class UPSHandler(socketserver.BaseRequestHandler):
    def __init__(self, world_sock):
        self.world_sock = world_sock

    def handle(self):

        ups_commands = get_message(self.request, AmazonUPS_pb2.Ucommands)

        if ups_commands.HasField('truck_arrival'):
            success, error = handleTruckArrived(world_sock, ups_commands.truck_arrival)

        if ups_commands.HasField('package_deliver'):
            success, error = handleTruckArrived(ups_commands.package_deliver)


        response = AmazonUPS_pb2.Aacknowledge()
        if success == 1:
            response.success = True
        else:
            response.success = False
            response.error = error

        send_message(self.request, response)


def handleUPS(worldsock):
    
    HOST, PORT = LISTEN_IP, LISTEN_PORT

    # Create the server, binding to localhost on port
    server = socketserver.TCPServer((HOST, PORT), UPSHandler(worldsock))

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()






###############################  Handle the World #############################################
def checkAvalibility(package_id, wh_id):
    try:
        cur = conn.cursor()
        
        cur.execute("SELECT product_id, quantity  FROM order_orderitem WHERE order_id = %s;", (package_id))
        rows = cur.fetchall()

        for row in rows:
            cur.execute("SELECT open_quantity  FROM order_inventory WHERE wh_id_id = %s AND product_id_id = %s;", (wh_id, row[0]))
            open = cur.fetchone()
            if open < row[1]:
                return False

        conn.commit()
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)   


def handlePurchased(world_sock, purchase):
    try:
        cur = conn.cursor()

        whid = purchase.whnum
        for item in purchase.things:
            cur.execute("SELECT open_quantity  FROM order_inventory WHERE wh_id_id = %s AND product_id_id = %s;", (whid, item.id))
            quantity = cur.fetchone()

            cur.execute("UPDATE order_inventory SET open_quantity = %s  WHERE wh_id_id = %s AND product_id_id = %s;", (quantity[0]+item.count, whid, item.id))
         

        conn.commit()
        cur.close()


        cur2 = conn.cursor()
        cur2.execute("SELECT  id  FROM order_order WHERE status = 'H';")
        rows = cur2.fetchall()

        for row in rows:
            if checkAvalibility(row[0], whid) == True:
                toPack(world_sock, row[0])

        conn.commit()
        cur2.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




def handlePacked(world_sock, tracking_num):
    try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, id  FROM order_order WHERE tracking_num = %s;", (tracking_num, ))
        row = cur.fetchone()

        whnum = row[0]
        package_id = row[1]

        cur.execute("UPDATE order_order SET status = 'T'  WHERE  tracking_num = %s;", (tracking_num, ))

        cur.execute("SELECT * FROM order_truck WHERE wh_id_id = %s;", (whnum, ))
        hastruck = fetchone()
        if hastruck is not None:
            toload(world_sock, package_id)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




def handleLoaded(tracking_num):
    try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, id, truck_id  FROM order_order WHERE tracking_num = %s;", (tracking_num, ))
        row = cur.fetchone()

        whnum = row[0]
        package_id = row[1]
        truckid = row[2]

        cur.execute("UPDATE order_order SET status = 'D'  WHERE  tracking_num = %s;", (tracking_num, ))

        cur.execute("SELECT * FROM order_order WHERE wh_id_id = %s AND truck_id = %s AND status = 'L';", (whnum, truckid, ))
        hasloading = fetchone()
        if hasloading is None:
            letTruckGo(truckid, whnum)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def handleWorld(worldsock):
    while ():
        response = get_message(worldsock, AmazonWorld_pb2.AResponses)
        if response.error != "":
            print(response.error)
            print("error response from world!")
        
        for puchase in response.arrived:
            handlePurchased(worldsock, puchase)

        for packed_package in response.ready:
            handlePacked(worldsock, packed_package)

        for loaded_package in response.loaded:
            handleLoaded(loaded_package)

        if response.finished == True:
            print("finish handle the world, close connection...")
            worldsock.close()



def requestTrackingNum(package_id):

        request_message = AmazonUPS_pb2.Arequest_package_id()

    #try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, owner_id, delivery_x, delivery_y FROM order_order WHERE id = %s;", (package_id, ))
        row = cur.fetchone()

        request_message.wh_id = row[0]
        request_message.x = row[2]
        request_message.y = row[3]

        cur.execute("SELECT ups_num FROM account_profile WHERE id = %s;", (row[1], ))
        row = cur.fetchone()
        if row is not None:
            request_message.ups_user_id = row[0]


        cur.execute("SELECT product_id, quantity FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()
        for row in rows:
            cur.execute("SELECT description FROM product_product WHERE id = %s;", (row[0], ))
            des = cur.fetchone()

            item = request_message.items.add()
            item.item_id = row[0]
            item.amount = row[1]
            item.description = des[0]

        
        command_msg = AmazonUPS_pb2.Acommands()
        command_msg.request_package_id.CopyFrom(request_message)

        response_msg = sendandrecvUPS(command_msg) 
        
        response_tracking_num = response_msg.response_package_id
        if response_tracking_num.error == "":
            tracking_num = response_tracking_num.package_id
            cur.execute("UPDATE order_order SET tracking_num = %s, status = 'H' WHERE id = %s;", (tracking_num, package_id))
            conn.commit()
        else:
            print(response_tracking_num.error)

        cur.close()
    #except (Exception, psycopg2.DatabaseError) as error:
    #    print(error)


def requestTruck(package_id):

        request_message = AmazonUPS_pb2.Arequest_truck()

    #try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id FROM order_order WHERE id = %s;", (package_id, ))
        row = cur.fetchone()

        request_message.wh_id = row[0]


        cur.execute("SELECT location_x, location_y FROM order_warehouse WHERE id = %s;", (row[0], ))
        row = cur.fetchone()
        request_message.x = row[0]
        request_message.y = row[1]

        conn.commit()
        cur.close()

        command_msg = AmazonUPS_pb2.Acommands()
        command_msg.request_truck.CopyFrom(request_message)

        response_msg = sendandrecvUPS(command_msg) 
        


        response_acknowledge = response_msg.acknowledge
        
        if response_acknowledge.error != "":
            print(response_acknowledge.error) 

    #except (Exception, psycopg2.DatabaseError) as error:
    #    print(error)


def handleWeb(worldsock):
    print("handleing the web")
    while (1):
        #try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM order_order WHERE status = 'P';")
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print("there is a new order! Start processing")

                cur.execute("SELECT id FROM order_warehouse;")
                nearest_wh_id = cur.fetchone()

                cur.execute("UPDATE order_order SET wh_id_id = %s WHERE id = %s;", (nearest_wh_id[0], row[0], ))
                requestTrackingNum(row[0])
                requestTruck(row[0])
                toBuy(worldsock, row[0])
          
            conn.commit()
            cur.close()
        #except (Exception, psycopg2.DatabaseError) as error:
        #    print(error) 




def init():
    print("init the server")


    cur = conn.cursor()
    cur.execute("INSERT INTO order_warehouse (location_x, location_y)  VALUES (500, 500);")
    cur.execute("INSERT INTO order_warehouse (location_x, location_y) VALUES (0, 0);")
    conn.commit()

    cur.execute("SELECT id FROM order_warehouse;")
    warehouses= cur.fetchall()

    cur.execute("SELECT id FROM product_product;")
    products= cur.fetchall()

    for wh in warehouses:
        for product in products:
            cur.execute("INSERT INTO order_inventory (open_quantity, product_id_id, wh_id_id) VALUES (0, %s, %s);", (product[0], wh[0]))



    world_sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    world_sock_fd.connect((WORLD_IP, WORLD_PORT))



    connect_mag = AmazonWorld_pb2.AConnect()
    connect_mag.worldid = 111112
    print("worldid len :", len(connect_mag.SerializeToString()))
    warehouse = connect_mag.initwh.add()
    warehouse.x = int(500)
    warehouse.y = int(500)
    
    warehouse = connect_mag.initwh.add()
    warehouse.x = int(0)
    warehouse.y = int(0)

    print(connect_mag)
    send_message(world_sock_fd, connect_mag)

    connected = get_message(world_sock_fd, AmazonWorld_pb2.AConnected)

    print(connected.error )
    print ("received ")


if __name__ == '__main__':


    world = init()

    threads = []
    t1 = threading.Thread(target = handleWorld, args=(world, ))
    threads.append(t1)
    t2 = threading.Thread(target = handleUPS, args=(world, ))
    threads.append(t2)
    t3 = threading.Thread(target = handleWeb, args=(world, ))
    threads.append(t3)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    conn.close()
