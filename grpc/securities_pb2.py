# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FinamPy/grpc/securities.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from FinamPy.proto import security_pb2 as FinamPy_dot_proto_dot_security__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x46inamPy/grpc/securities.proto\x12\x10grpc.tradeapi.v1\x1a\x1c\x46inamPy/proto/security.proto\x1a\x1egoogle/protobuf/wrappers.proto\"r\n\x14GetSecuritiesRequest\x12+\n\x05\x62oard\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07seccode\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"F\n\x13GetSecuritiesResult\x12/\n\nsecurities\x18\x01 \x03(\x0b\x32\x1b.proto.tradeapi.v1.Security2l\n\nSecurities\x12^\n\rGetSecurities\x12&.grpc.tradeapi.v1.GetSecuritiesRequest\x1a%.grpc.tradeapi.v1.GetSecuritiesResultB\x19\xaa\x02\x16\x46inam.TradeApi.Grpc.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FinamPy.grpc.securities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\026Finam.TradeApi.Grpc.V1'
  _globals['_GETSECURITIESREQUEST']._serialized_start=113
  _globals['_GETSECURITIESREQUEST']._serialized_end=227
  _globals['_GETSECURITIESRESULT']._serialized_start=229
  _globals['_GETSECURITIESRESULT']._serialized_end=299
  _globals['_SECURITIES']._serialized_start=301
  _globals['_SECURITIES']._serialized_end=409
# @@protoc_insertion_point(module_scope)
