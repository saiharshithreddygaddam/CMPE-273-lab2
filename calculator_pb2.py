# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto

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
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_pb=_b('\n\x10helloworld.proto\x12\nhelloworld\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x18\n\x08\x41\x64\x64Reply\x12\x0c\n\x04num3\x18\x01 \x01(\x05\x32@\n\x07Greeter\x12\x35\n\x03\x41\x64\x64\x12\x16.helloworld.AddRequest\x1a\x14.helloworld.AddReply\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='helloworld.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='helloworld.AddRequest.num1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num2', full_name='helloworld.AddRequest.num2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=72,
)


_ADDREPLY = _descriptor.Descriptor(
  name='AddReply',
  full_name='helloworld.AddReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num3', full_name='helloworld.AddReply.num3', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddReply'] = _ADDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddReply = _reflection.GeneratedProtocolMessageType('AddReply', (_message.Message,), dict(
  DESCRIPTOR = _ADDREPLY,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.AddReply)
  ))
_sym_db.RegisterMessage(AddReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'))

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=100,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='helloworld.Greeter.Add',
    index=0,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
