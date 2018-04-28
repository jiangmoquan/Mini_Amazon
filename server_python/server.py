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
#from communicate import get_message, send_message
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintEncoder


WORLD_ID = 1024
WORLD_IP = "vcm-2464.vm.duke.edu"
WORLD_PORT = 23456

UPS_IP = "vcm-2464.vm.duke.edu"
UPS_PORT = 23333

SIM_SPEED = 999999

LISTEN_PORT = 10000
LISTEN_IP = "0.0.0.0"

#MAX_CONNECTION = 100
#RECEIVE_BYTES = 4

conn = psycopg2.connect(host="localhost",database="storedb", user="postgres", port= "5432")

global_world_sock = 0
"""

def socket_read_n(sock, n):

    buf = ''
    while n > 0:
        data = sock.recv(n)
        if data == b'':
            raise RuntimeError('unexpected connection close')
        buf += data.decode(sys.stdout.encoding)
        n -= len(data)
    return buf


def get_message(sock, msgtype):

    
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
    





    len_buf = socket_read_n(sock, 4)
    recvmsg = sock.recv(1024)
    (length, pos) = _DecodeVarint32(recvmsg, 0)

    msg = msgtype()
    msg.ParseFromString(recvmsg[pos:pos+length])

    print("getting:", msg)
    return msg



def send_message(sock, message):

    print("sending:", message)

    s = message.SerializeToString()
    #print("before pack, the len is ", len(s))
    _EncodeVarint(sock.sendall, len(s), None)

    #packed_len = struct.pack('>L', len(s))
    sock.sendall(s)


"""
# encode the data to be sent to the "world"
def encode_varint(value):
    """ Encode an int as a protobuf varint """
    data = []
    _VarintEncoder()(data.append, value, None)
    return b''.join(data)


# decode the data received from the "world"
def decode_varint(data):
    """ Decode a protobuf varint to an int """
    return _DecodeVarint32(data, 0)[0]


# send protocol buffer messages over TCP
def send_message(conn, msg):
    """ Send a message, prefixed with its size, to a TPC/IP socket """

    print("sending:", msg)

    data = msg.SerializeToString()
    size = encode_varint(len(data))
    conn.sendall(size + data)



# receive and parse message sent from the "world"
def get_message(conn, msg_type):
    """ Receive a message, prefixed with its size, from a TCP/IP socket """
    # Receive the size of the message data
    data = b''
    while True:
        try:
            data += conn.recv(1)
            size = decode_varint(data)
            break
        except IndexError:
            pass
    # Receive the message data
    data = conn.recv(size)
    # Decode the message
    msg = msg_type()
    msg.ParseFromString(data)

    print ("getting:", msg)
    return msg














def sendandrecvUPS(command_msg):
    ups_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    ups_sock.connect((UPS_IP, UPS_PORT))

    send_message(ups_sock, command_msg)

    response_msg = get_message(ups_sock, AmazonUPS_pb2.Uresponses)  
        
    ups_sock.close() 

    return response_msg


def toBuy(world_sock,package_id):
        command_msg = AmazonWorld_pb2.ACommands()
        command_msg.simspeed = SIM_SPEED
        buying = command_msg.buy.add()
    #try:
        cur = conn.cursor()                                                                                                                                                                                 
        cur.execute("SELECT wh_id_id FROM order_order WHERE id = %s;", (package_id, ))                                                                                                                      
        row = cur.fetchone()                                                                                                                                                                                

        buying.whnum = row[0]                                                                                                                                                                               

        cur.execute("SELECT product_id, quantity FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()                                                                                                                                                                               
        for row in rows:                                                                                                                                                                                    
            cur.execute("SELECT description FROM product_product WHERE id = %s;", (row[0], ))
            des = cur.fetchone()                                                                                                                                                                                

            item = buying.things.add()                                                                                                                                                               
            item.id = row[0]
            item.count = row[1]                                                                                                                                                                             
            item.description = des[0]                                                                                                                                                                       


        send_message(world_sock, command_msg)                                                                                                                                                           

        conn.commit()                                                                                                                                                                                    
        cur.close()

    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)




def toPack(world_sock, package_id):
        command_msg = AmazonWorld_pb2.ACommands()
        command_msg.simspeed = SIM_SPEED
        pack = command_msg.topack.add()

    #try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, tracking_num FROM order_order WHERE id = %s;", (package_id, ))
        row = cur.fetchone()

        pack.whnum = row[0]
        pack.shipid = row[1]


        cur.execute("SELECT product_id, quantity FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()
        for row in rows:
            cur.execute("SELECT open_quantity FROM order_inventory WHERE product_id_id = %s AND wh_id_id = %s;", (row[0], pack.whnum, ))
            open = cur.fetchone()

            cur.execute("UPDATE order_inventory SET open_quantity = %s WHERE product_id_id = %s AND wh_id_id = %s;", (open[0] - row[1], row[0], pack.whnum, ))
            cur.execute("SELECT description FROM product_product WHERE id = %s;", (row[0], ))
            des = cur.fetchone()

            item = pack.things.add()
            item.id = row[0]
            item.count = row[1]
            item.description = des[0]

        
        send_message(world_sock, command_msg)
        cur.execute("UPDATE order_order SET status = 'K' WHERE id = %s;", (package_id, ))
        conn.commit()
        cur.close()
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)


def toLoad(world_sock, package_id, truck_id):
        command_msg = AmazonWorld_pb2.ACommands()
        command_msg.simspeed = SIM_SPEED
        loading = command_msg.load.add()
    
    #try:
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
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
                                


def letTruckGo(truckid, whid):
        print("lettruckgo: truckid:", truckid)
        loaded = AmazonUPS_pb2.Apackages_loaded()
        loaded.truck_id = truckid
        loaded.wh_id = whid

    #try:
        cur = conn.cursor()
        cur.execute("SELECT tracking_num FROM order_order WHERE wh_id_id = %s AND truck_id = %s AND status = 'D';", (whid, truckid, ))
        rows = cur.fetchall()

        for row in rows:
            cur.execute("UPDATE order_order SET status = 'S'  WHERE  tracking_num = %s;", (row[0], ))
            tracking = loaded.package_id.add()
            tracking = row[0]

        cur.execute("DELETE FROM order_truck WHERE wh_id_id = %s AND truck_id = %s;", (whid, truckid, ))

        conn.commit()
        cur.close()

        command_msg = AmazonUPS_pb2.Acommands()
        command_msg.packages_loaded = loaded

        response_msg = sendandrecvUPS(command_msg) 
        
        response_acknowledge = response_msg.acknowledge
        
        if response_acknowledge.error != "":
            print(response_acknowledge.error) 

    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)    




###############################  Handle the UPS #############################################

def handleTruckArrived(world_sock, Utruck_arrival):
        truck_id = Utruck_arrival.truck_id
        wh_id = Utruck_arrival.wh_id
    #try:
        cur = conn.cursor()
        cur.execute("INSERT INTO order_truck (truck_id, wh_id_id) VALUES (%s, %s);", (truck_id, wh_id, ))


        cur.execute("SELECT id  FROM order_order WHERE status = 'T' AND wh_id_id = %s;", ( wh_id, ))
        rows = cur.fetchall()
        for row in rows:
            toLoad(world_sock, row[0], truck_id)


        conn.commit()
        cur.close()

        return 1, ""

    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        #return 0, error


def handlePackageDelivered(Upackage_deliver):
        package_id = Upackage_deliver.package_id
    #try:
        cur = conn.cursor()
        cur.execute("UPDATE order_order SET status = 'E'  WHERE  id = %s;", (package_id, ))

        conn.commit()
        cur.close()
        return 1, ""
    #except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 0, error


class UPSHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("Accept UPS, Handle this command.... ")

        ups_commands = get_message(self.request, AmazonUPS_pb2.Ucommands)

        if ups_commands.HasField('truck_arrival'):
            success, error = handleTruckArrived(global_world_sock, ups_commands.truck_arrival)

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
    server = socketserver.TCPServer((HOST, PORT), UPSHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()






###############################  Handle the World #############################################
def checkAvalibility(package_id, wh_id):
    #try:
        cur = conn.cursor()
        
        cur.execute("SELECT product_id, quantity  FROM order_orderitem WHERE order_id = %s;", (package_id, ))
        rows = cur.fetchall()

        for row in rows:
            cur.execute("SELECT open_quantity  FROM order_inventory WHERE wh_id_id = %s AND product_id_id = %s;", (wh_id, row[0], ))
            open = cur.fetchone()
            if open[0] < row[1]:
                return False

        conn.commit()
        cur.close()
        return True

    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)   


def handlePurchased(world_sock, purchase):
    #try:
        cur = conn.cursor()

        whid = purchase.whnum
        for item in purchase.things:
            cur.execute("SELECT open_quantity  FROM order_inventory WHERE wh_id_id = %s AND product_id_id = %s;", (whid, item.id, ))
            quantity = cur.fetchone()

            cur.execute("UPDATE order_inventory SET open_quantity = %s  WHERE wh_id_id = %s AND product_id_id = %s;", (quantity[0]+item.count, whid, item.id, ))
         

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
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)




def handlePacked(world_sock, tracking_num):
    #try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, id  FROM order_order WHERE tracking_num = %s;", (tracking_num, ))
        row = cur.fetchone()

        whnum = row[0]
        package_id = row[1]

        cur.execute("UPDATE order_order SET status = 'T'  WHERE  tracking_num = %s;", (tracking_num, ))

        cur.execute("SELECT truck_id FROM order_truck WHERE wh_id_id = %s;", (whnum, ))
        hastruck = cur.fetchone()
        if hastruck is not None:
            toLoad(world_sock, package_id, hastruck[0])

        conn.commit()
        cur.close()
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)




def handleLoaded(tracking_num):
    #try:
        cur = conn.cursor()
        cur.execute("SELECT wh_id_id, id, truck_id  FROM order_order WHERE tracking_num = %s;", (tracking_num, ))
        row = cur.fetchone()
	
        print("in handleloaded:", row)
        whnum = row[0]
        package_id = row[1]
        truckid = row[2]

        cur.execute("UPDATE order_order SET status = 'D'  WHERE  tracking_num = %s;", (tracking_num, ))

        cur.execute("SELECT * FROM order_order WHERE wh_id_id = %s AND truck_id = %s AND status = 'L';", (whnum, truckid, ))
        hasloading = cur.fetchone()
        if hasloading is None:
            letTruckGo(truckid, whnum)

        conn.commit()
        cur.close()
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)



def handleWorld(worldsock):
    while (1):
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



###############################  Handle the Web #############################################


def requestTrackingNum(package_id):

    request_message = AmazonUPS_pb2.Arequest_package_id()

    try:
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
            cur.execute("UPDATE order_order SET tracking_num = %s, status = 'H' WHERE id = %s;", (tracking_num, package_id, ))
            conn.commit()
        else:
            print(response_tracking_num.error)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def requestTruck(package_id):

    request_message = AmazonUPS_pb2.Arequest_truck()

    try:
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

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def handleWeb(worldsock):
    print("handleing the web")
    while (1):
        try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM order_order WHERE status = 'P';")
            rows = cur.fetchall()
            #print(rows)
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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error) 




def init():
    print("init the server")


    cur = conn.cursor()
    cur.execute("INSERT INTO order_warehouse (location_x, location_y)  VALUES (500, 500);")
    cur.execute("INSERT INTO order_warehouse (location_x, location_y) VALUES (100,100);")
    conn.commit()

    cur.execute("SELECT id FROM order_warehouse;")
    warehouses= cur.fetchall()

    cur.execute("SELECT id FROM product_product;")
    products= cur.fetchall()

    for wh in warehouses:
        for product in products:
            cur.execute("INSERT INTO order_inventory (open_quantity, product_id_id, wh_id_id) VALUES (0, %s, %s);", (product[0], wh[0]))



    world_sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    world_sock_fd.setsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    world_sock_fd.connect((WORLD_IP, WORLD_PORT))



    connect_mag = AmazonWorld_pb2.AConnect()
    connect_mag.worldid = WORLD_ID
    print("worldid len :", len(connect_mag.SerializeToString()))
    warehouse = connect_mag.initwh.add()
    warehouse.x = int(500)
    warehouse.y = int(500)
    
    warehouse = connect_mag.initwh.add()
    warehouse.x = int(100)
    warehouse.y = int(100)

    print(connect_mag)
    send_message(world_sock_fd, connect_mag)

    connected = get_message(world_sock_fd, AmazonWorld_pb2.AConnected)

    print(connected.error )
    print ("received ")
    
    global_world_sock = world_sock_fd
    return world_sock_fd


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
