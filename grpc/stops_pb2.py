# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FinamPy/grpc/stops.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from FinamPy.proto import stops_pb2 as FinamPy_dot_proto_dot_stops__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x46inamPy/grpc/stops.proto\x12\x10grpc.tradeapi.v1\x1a\x19\x46inamPy/proto/stops.proto2\x83\x02\n\x05Stops\x12Q\n\x08GetStops\x12\".proto.tradeapi.v1.GetStopsRequest\x1a!.proto.tradeapi.v1.GetStopsResult\x12W\n\nCancelStop\x12$.proto.tradeapi.v1.CancelStopRequest\x1a#.proto.tradeapi.v1.CancelStopResult\x12N\n\x07NewStop\x12!.proto.tradeapi.v1.NewStopRequest\x1a .proto.tradeapi.v1.NewStopResultB\x19\xaa\x02\x16\x46inam.TradeApi.Grpc.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FinamPy.grpc.stops_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\026Finam.TradeApi.Grpc.V1'
  _globals['_STOPS']._serialized_start=74
  _globals['_STOPS']._serialized_end=333
# @@protoc_insertion_point(module_scope)
