# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protofiles/file.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protofiles/file.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15protofiles/file.proto\x12\x02pb\"%\n\x07\x45lement\x12\n\n\x02_z\x18\x01 \x01(\x03\x12\x0e\n\x06_compo\x18\x02 \x03(\t\"8\n\x03Map\x12\n\n\x02_x\x18\x01 \x01(\x03\x12\n\n\x02_y\x18\x02 \x01(\x03\x12\x19\n\x04_map\x18\x03 \x03(\x0b\x32\x0b.pb.Elementb\x06proto3'
)




_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='pb.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_z', full_name='pb.Element._z', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_compo', full_name='pb.Element._compo', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=66,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='pb.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_x', full_name='pb.Map._x', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_y', full_name='pb.Map._y', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_map', full_name='pb.Map._map', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=124,
)

_MAP.fields_by_name['_map'].message_type = _ELEMENT
DESCRIPTOR.message_types_by_name['Element'] = _ELEMENT
DESCRIPTOR.message_types_by_name['Map'] = _MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), {
  'DESCRIPTOR' : _ELEMENT,
  '__module__' : 'protofiles.file_pb2'
  # @@protoc_insertion_point(class_scope:pb.Element)
  })
_sym_db.RegisterMessage(Element)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'protofiles.file_pb2'
  # @@protoc_insertion_point(class_scope:pb.Map)
  })
_sym_db.RegisterMessage(Map)


# @@protoc_insertion_point(module_scope)
