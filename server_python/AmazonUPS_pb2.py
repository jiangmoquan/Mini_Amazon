# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AmazonUPS.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AmazonUPS.proto',
  package='AmazonUPSProto',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x41mazonUPS.proto\x12\x0e\x41mazonUPSProto\"t\n\x13\x41request_package_id\x12\r\n\x05wh_id\x18\x01 \x02(\x05\x12\x13\n\x0bups_user_id\x18\x02 \x01(\x03\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x12#\n\x05items\x18\x05 \x03(\x0b\x32\x14.AmazonUPSProto.Item\"5\n\x0e\x41request_truck\x12\r\n\x05wh_id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\"G\n\x10\x41packages_loaded\x12\x10\n\x08truck_id\x18\x01 \x02(\x05\x12\r\n\x05wh_id\x18\x02 \x02(\x05\x12\x12\n\npackage_id\x18\x03 \x03(\x03\".\n\x0c\x41\x61\x63knowledge\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"1\n\x0eUtruck_arrival\x12\x10\n\x08truck_id\x18\x01 \x02(\x05\x12\r\n\x05wh_id\x18\x02 \x02(\x05\"&\n\x10Upackage_deliver\x12\x12\n\npackage_id\x18\x01 \x02(\x03\"9\n\x14Uresponse_package_id\x12\x12\n\npackage_id\x18\x01 \x02(\x03\x12\r\n\x05\x65rror\x18\x02 \x01(\t\".\n\x0cUacknowledge\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"<\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x02(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x05\"\xbe\x01\n\tAcommands\x12?\n\x12request_package_id\x18\x01 \x01(\x0b\x32#.AmazonUPSProto.Arequest_package_id\x12\x35\n\rrequest_truck\x18\x02 \x01(\x0b\x32\x1e.AmazonUPSProto.Arequest_truck\x12\x39\n\x0fpackages_loaded\x18\x03 \x01(\x0b\x32 .AmazonUPSProto.Apackages_loaded\"\x82\x01\n\nUresponses\x12\x41\n\x13response_package_id\x18\x01 \x01(\x0b\x32$.AmazonUPSProto.Uresponse_package_id\x12\x31\n\x0b\x61\x63knowledge\x18\x02 \x01(\x0b\x32\x1c.AmazonUPSProto.Uacknowledge\"}\n\tUcommands\x12\x35\n\rtruck_arrival\x18\x01 \x01(\x0b\x32\x1e.AmazonUPSProto.Utruck_arrival\x12\x39\n\x0fpackage_deliver\x18\x02 \x01(\x0b\x32 .AmazonUPSProto.Upackage_deliver\"?\n\nAresponses\x12\x31\n\x0b\x61\x63knowledge\x18\x01 \x01(\x0b\x32\x1c.AmazonUPSProto.Aacknowledge')
)




_AREQUEST_PACKAGE_ID = _descriptor.Descriptor(
  name='Arequest_package_id',
  full_name='AmazonUPSProto.Arequest_package_id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wh_id', full_name='AmazonUPSProto.Arequest_package_id.wh_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ups_user_id', full_name='AmazonUPSProto.Arequest_package_id.ups_user_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='AmazonUPSProto.Arequest_package_id.x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='AmazonUPSProto.Arequest_package_id.y', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='AmazonUPSProto.Arequest_package_id.items', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=151,
)


_AREQUEST_TRUCK = _descriptor.Descriptor(
  name='Arequest_truck',
  full_name='AmazonUPSProto.Arequest_truck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wh_id', full_name='AmazonUPSProto.Arequest_truck.wh_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='AmazonUPSProto.Arequest_truck.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='AmazonUPSProto.Arequest_truck.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=206,
)


_APACKAGES_LOADED = _descriptor.Descriptor(
  name='Apackages_loaded',
  full_name='AmazonUPSProto.Apackages_loaded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='AmazonUPSProto.Apackages_loaded.truck_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_id', full_name='AmazonUPSProto.Apackages_loaded.wh_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='AmazonUPSProto.Apackages_loaded.package_id', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=279,
)


_AACKNOWLEDGE = _descriptor.Descriptor(
  name='Aacknowledge',
  full_name='AmazonUPSProto.Aacknowledge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='AmazonUPSProto.Aacknowledge.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='AmazonUPSProto.Aacknowledge.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=327,
)


_UTRUCK_ARRIVAL = _descriptor.Descriptor(
  name='Utruck_arrival',
  full_name='AmazonUPSProto.Utruck_arrival',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='AmazonUPSProto.Utruck_arrival.truck_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_id', full_name='AmazonUPSProto.Utruck_arrival.wh_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=378,
)


_UPACKAGE_DELIVER = _descriptor.Descriptor(
  name='Upackage_deliver',
  full_name='AmazonUPSProto.Upackage_deliver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='AmazonUPSProto.Upackage_deliver.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=418,
)


_URESPONSE_PACKAGE_ID = _descriptor.Descriptor(
  name='Uresponse_package_id',
  full_name='AmazonUPSProto.Uresponse_package_id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='AmazonUPSProto.Uresponse_package_id.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='AmazonUPSProto.Uresponse_package_id.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=477,
)


_UACKNOWLEDGE = _descriptor.Descriptor(
  name='Uacknowledge',
  full_name='AmazonUPSProto.Uacknowledge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='AmazonUPSProto.Uacknowledge.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='AmazonUPSProto.Uacknowledge.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=525,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='AmazonUPSProto.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='AmazonUPSProto.Item.item_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='AmazonUPSProto.Item.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='AmazonUPSProto.Item.amount', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=587,
)


_ACOMMANDS = _descriptor.Descriptor(
  name='Acommands',
  full_name='AmazonUPSProto.Acommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_package_id', full_name='AmazonUPSProto.Acommands.request_package_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_truck', full_name='AmazonUPSProto.Acommands.request_truck', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages_loaded', full_name='AmazonUPSProto.Acommands.packages_loaded', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=780,
)


_URESPONSES = _descriptor.Descriptor(
  name='Uresponses',
  full_name='AmazonUPSProto.Uresponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_package_id', full_name='AmazonUPSProto.Uresponses.response_package_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledge', full_name='AmazonUPSProto.Uresponses.acknowledge', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=783,
  serialized_end=913,
)


_UCOMMANDS = _descriptor.Descriptor(
  name='Ucommands',
  full_name='AmazonUPSProto.Ucommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_arrival', full_name='AmazonUPSProto.Ucommands.truck_arrival', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_deliver', full_name='AmazonUPSProto.Ucommands.package_deliver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=1040,
)


_ARESPONSES = _descriptor.Descriptor(
  name='Aresponses',
  full_name='AmazonUPSProto.Aresponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acknowledge', full_name='AmazonUPSProto.Aresponses.acknowledge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1105,
)

_AREQUEST_PACKAGE_ID.fields_by_name['items'].message_type = _ITEM
_ACOMMANDS.fields_by_name['request_package_id'].message_type = _AREQUEST_PACKAGE_ID
_ACOMMANDS.fields_by_name['request_truck'].message_type = _AREQUEST_TRUCK
_ACOMMANDS.fields_by_name['packages_loaded'].message_type = _APACKAGES_LOADED
_URESPONSES.fields_by_name['response_package_id'].message_type = _URESPONSE_PACKAGE_ID
_URESPONSES.fields_by_name['acknowledge'].message_type = _UACKNOWLEDGE
_UCOMMANDS.fields_by_name['truck_arrival'].message_type = _UTRUCK_ARRIVAL
_UCOMMANDS.fields_by_name['package_deliver'].message_type = _UPACKAGE_DELIVER
_ARESPONSES.fields_by_name['acknowledge'].message_type = _AACKNOWLEDGE
DESCRIPTOR.message_types_by_name['Arequest_package_id'] = _AREQUEST_PACKAGE_ID
DESCRIPTOR.message_types_by_name['Arequest_truck'] = _AREQUEST_TRUCK
DESCRIPTOR.message_types_by_name['Apackages_loaded'] = _APACKAGES_LOADED
DESCRIPTOR.message_types_by_name['Aacknowledge'] = _AACKNOWLEDGE
DESCRIPTOR.message_types_by_name['Utruck_arrival'] = _UTRUCK_ARRIVAL
DESCRIPTOR.message_types_by_name['Upackage_deliver'] = _UPACKAGE_DELIVER
DESCRIPTOR.message_types_by_name['Uresponse_package_id'] = _URESPONSE_PACKAGE_ID
DESCRIPTOR.message_types_by_name['Uacknowledge'] = _UACKNOWLEDGE
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Acommands'] = _ACOMMANDS
DESCRIPTOR.message_types_by_name['Uresponses'] = _URESPONSES
DESCRIPTOR.message_types_by_name['Ucommands'] = _UCOMMANDS
DESCRIPTOR.message_types_by_name['Aresponses'] = _ARESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Arequest_package_id = _reflection.GeneratedProtocolMessageType('Arequest_package_id', (_message.Message,), dict(
  DESCRIPTOR = _AREQUEST_PACKAGE_ID,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Arequest_package_id)
  ))
_sym_db.RegisterMessage(Arequest_package_id)

Arequest_truck = _reflection.GeneratedProtocolMessageType('Arequest_truck', (_message.Message,), dict(
  DESCRIPTOR = _AREQUEST_TRUCK,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Arequest_truck)
  ))
_sym_db.RegisterMessage(Arequest_truck)

Apackages_loaded = _reflection.GeneratedProtocolMessageType('Apackages_loaded', (_message.Message,), dict(
  DESCRIPTOR = _APACKAGES_LOADED,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Apackages_loaded)
  ))
_sym_db.RegisterMessage(Apackages_loaded)

Aacknowledge = _reflection.GeneratedProtocolMessageType('Aacknowledge', (_message.Message,), dict(
  DESCRIPTOR = _AACKNOWLEDGE,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Aacknowledge)
  ))
_sym_db.RegisterMessage(Aacknowledge)

Utruck_arrival = _reflection.GeneratedProtocolMessageType('Utruck_arrival', (_message.Message,), dict(
  DESCRIPTOR = _UTRUCK_ARRIVAL,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Utruck_arrival)
  ))
_sym_db.RegisterMessage(Utruck_arrival)

Upackage_deliver = _reflection.GeneratedProtocolMessageType('Upackage_deliver', (_message.Message,), dict(
  DESCRIPTOR = _UPACKAGE_DELIVER,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Upackage_deliver)
  ))
_sym_db.RegisterMessage(Upackage_deliver)

Uresponse_package_id = _reflection.GeneratedProtocolMessageType('Uresponse_package_id', (_message.Message,), dict(
  DESCRIPTOR = _URESPONSE_PACKAGE_ID,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Uresponse_package_id)
  ))
_sym_db.RegisterMessage(Uresponse_package_id)

Uacknowledge = _reflection.GeneratedProtocolMessageType('Uacknowledge', (_message.Message,), dict(
  DESCRIPTOR = _UACKNOWLEDGE,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Uacknowledge)
  ))
_sym_db.RegisterMessage(Uacknowledge)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Item)
  ))
_sym_db.RegisterMessage(Item)

Acommands = _reflection.GeneratedProtocolMessageType('Acommands', (_message.Message,), dict(
  DESCRIPTOR = _ACOMMANDS,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Acommands)
  ))
_sym_db.RegisterMessage(Acommands)

Uresponses = _reflection.GeneratedProtocolMessageType('Uresponses', (_message.Message,), dict(
  DESCRIPTOR = _URESPONSES,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Uresponses)
  ))
_sym_db.RegisterMessage(Uresponses)

Ucommands = _reflection.GeneratedProtocolMessageType('Ucommands', (_message.Message,), dict(
  DESCRIPTOR = _UCOMMANDS,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Ucommands)
  ))
_sym_db.RegisterMessage(Ucommands)

Aresponses = _reflection.GeneratedProtocolMessageType('Aresponses', (_message.Message,), dict(
  DESCRIPTOR = _ARESPONSES,
  __module__ = 'AmazonUPS_pb2'
  # @@protoc_insertion_point(class_scope:AmazonUPSProto.Aresponses)
  ))
_sym_db.RegisterMessage(Aresponses)


# @@protoc_insertion_point(module_scope)
