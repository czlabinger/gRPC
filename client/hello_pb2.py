# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\"\x1e\n\x10WarehouseRequest\x12\n\n\x02id\x18\x01 \x01(\t\"S\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\"\x98\x01\n\rWarehouseData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0e\n\x06street\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0b\n\x03plz\x18\x07 \x01(\t\x12\x1e\n\x0cproduct_data\x18\x08 \x03(\x0b\x32\x08.Product2;\n\tWarehouse\x12.\n\x07getData\x12\x11.WarehouseRequest\x1a\x0e.WarehouseData\"\x00\x42\x10\n\x0ewarehouseProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016warehouseProto'
  _globals['_WAREHOUSEREQUEST']._serialized_start=15
  _globals['_WAREHOUSEREQUEST']._serialized_end=45
  _globals['_PRODUCT']._serialized_start=47
  _globals['_PRODUCT']._serialized_end=130
  _globals['_WAREHOUSEDATA']._serialized_start=133
  _globals['_WAREHOUSEDATA']._serialized_end=285
  _globals['_WAREHOUSE']._serialized_start=287
  _globals['_WAREHOUSE']._serialized_end=346
# @@protoc_insertion_point(module_scope)
