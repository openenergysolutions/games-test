# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metermodule/metermodule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uml_pb2 as uml__pb2
from commonmodule import commonmodule_pb2 as commonmodule_dot_commonmodule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmetermodule/metermodule.proto\x12\x0bmetermodule\x1a\tuml.proto\x1a\x1f\x63ommonmodule/commonmodule.proto\"\xae\x02\n\x0cMeterReading\x12\x62\n\"conductingEquipmentTerminalReading\x18\x01 \x01(\x0b\x32\x30.commonmodule.ConductingEquipmentTerminalReadingB\x04\x80\xb5\x18\x01\x12*\n\tphaseMMTN\x18\x02 \x01(\x0b\x32\x17.commonmodule.PhaseMMTN\x12.\n\x0breadingMMTR\x18\x03 \x01(\x0b\x32\x19.commonmodule.ReadingMMTR\x12.\n\x0breadingMMXU\x18\x04 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\x12.\n\x0breadingMMDC\x18\x05 \x01(\x0b\x32\x19.commonmodule.ReadingMMDC\"\xc8\x01\n\x13MeterReadingProfile\x12\x42\n\x12readingMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ReadingMessageInfoB\x04\x80\xb5\x18\x01\x12,\n\x05meter\x18\x02 \x01(\x0b\x32\x13.commonmodule.MeterB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x39\n\x0cmeterReading\x18\x03 \x01(\x0b\x32\x19.metermodule.MeterReadingB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\x42\x81\x01\n\x13openfmb.metermoduleP\x01ZRgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/metermodule\xaa\x02\x13openfmb.metermoduleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metermodule.metermodule_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023openfmb.metermoduleP\001ZRgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/metermodule\252\002\023openfmb.metermodule'
  _METERREADING.fields_by_name['conductingEquipmentTerminalReading']._options = None
  _METERREADING.fields_by_name['conductingEquipmentTerminalReading']._serialized_options = b'\200\265\030\001'
  _METERREADINGPROFILE.fields_by_name['readingMessageInfo']._options = None
  _METERREADINGPROFILE.fields_by_name['readingMessageInfo']._serialized_options = b'\200\265\030\001'
  _METERREADINGPROFILE.fields_by_name['meter']._options = None
  _METERREADINGPROFILE.fields_by_name['meter']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _METERREADINGPROFILE.fields_by_name['meterReading']._options = None
  _METERREADINGPROFILE.fields_by_name['meterReading']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _METERREADINGPROFILE._options = None
  _METERREADINGPROFILE._serialized_options = b'\300\363\030\001'
  _globals['_METERREADING']._serialized_start=91
  _globals['_METERREADING']._serialized_end=393
  _globals['_METERREADINGPROFILE']._serialized_start=396
  _globals['_METERREADINGPROFILE']._serialized_end=596
# @@protoc_insertion_point(module_scope)
