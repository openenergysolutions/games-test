# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: breakermodule/breakermodule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uml_pb2 as uml__pb2
from commonmodule import commonmodule_pb2 as commonmodule_dot_commonmodule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!breakermodule/breakermodule.proto\x12\rbreakermodule\x1a\tuml.proto\x1a\x1f\x63ommonmodule/commonmodule.proto\"b\n\x1a\x42reakerDiscreteControlXCBR\x12\x44\n\x13\x64iscreteControlXCBR\x18\x01 \x01(\x0b\x32!.commonmodule.DiscreteControlXCBRB\x04\x80\xb5\x18\x01\"\xcd\x01\n\x16\x42reakerDiscreteControl\x12\x36\n\x0c\x63ontrolValue\x18\x01 \x01(\x0b\x32\x1a.commonmodule.ControlValueB\x04\x80\xb5\x18\x01\x12,\n\x05\x63heck\x18\x02 \x01(\x0b\x32\x1d.commonmodule.CheckConditions\x12M\n\x1a\x62reakerDiscreteControlXCBR\x18\x03 \x01(\x0b\x32).breakermodule.BreakerDiscreteControlXCBR\"O\n\x07\x42reaker\x12\x44\n\x13\x63onductingEquipment\x18\x01 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x04\x80\xb5\x18\x01\"\xed\x01\n\x1d\x42reakerDiscreteControlProfile\x12\x42\n\x12\x63ontrolMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ControlMessageInfoB\x04\x80\xb5\x18\x01\x12\x31\n\x07\x62reaker\x18\x02 \x01(\x0b\x32\x16.breakermodule.BreakerB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12O\n\x16\x62reakerDiscreteControl\x18\x03 \x01(\x0b\x32%.breakermodule.BreakerDiscreteControlB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\x80\x01\n\x0c\x42reakerEvent\x12\x32\n\neventValue\x18\x01 \x01(\x0b\x32\x18.commonmodule.EventValueB\x04\x80\xb5\x18\x01\x12<\n\x12statusAndEventXCBR\x18\x02 \x01(\x0b\x32 .commonmodule.StatusAndEventXCBR\"\xcb\x01\n\x13\x42reakerEventProfile\x12>\n\x10\x65ventMessageInfo\x18\x01 \x01(\x0b\x32\x1e.commonmodule.EventMessageInfoB\x04\x80\xb5\x18\x01\x12\x31\n\x07\x62reaker\x18\x02 \x01(\x0b\x32\x16.breakermodule.BreakerB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12;\n\x0c\x62reakerEvent\x18\x03 \x01(\x0b\x32\x1b.breakermodule.BreakerEventB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xb4\x02\n\x0e\x42reakerReading\x12\x62\n\"conductingEquipmentTerminalReading\x18\x01 \x01(\x0b\x32\x30.commonmodule.ConductingEquipmentTerminalReadingB\x04\x80\xb5\x18\x01\x12\x32\n\x0f\x64iffReadingMMXU\x18\x02 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\x12*\n\tphaseMMTN\x18\x03 \x01(\x0b\x32\x17.commonmodule.PhaseMMTN\x12.\n\x0breadingMMTR\x18\x04 \x01(\x0b\x32\x19.commonmodule.ReadingMMTR\x12.\n\x0breadingMMXU\x18\x05 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\"\xd9\x01\n\x15\x42reakerReadingProfile\x12\x42\n\x12readingMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ReadingMessageInfoB\x04\x80\xb5\x18\x01\x12\x31\n\x07\x62reaker\x18\x02 \x01(\x0b\x32\x16.breakermodule.BreakerB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x43\n\x0e\x62reakerReading\x18\x03 \x03(\x0b\x32\x1d.breakermodule.BreakerReadingB\x0c\x88\xb5\x18\x01\x90\xb5\x18\x01\x98\xb5\x18\x02:\x04\xc0\xf3\x18\x01\"\x83\x01\n\rBreakerStatus\x12\x34\n\x0bstatusValue\x18\x01 \x01(\x0b\x32\x19.commonmodule.StatusValueB\x04\x80\xb5\x18\x01\x12<\n\x12statusAndEventXCBR\x18\x02 \x01(\x0b\x32 .commonmodule.StatusAndEventXCBR\"\xd0\x01\n\x14\x42reakerStatusProfile\x12@\n\x11statusMessageInfo\x18\x01 \x01(\x0b\x32\x1f.commonmodule.StatusMessageInfoB\x04\x80\xb5\x18\x01\x12\x31\n\x07\x62reaker\x18\x02 \x01(\x0b\x32\x16.breakermodule.BreakerB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12=\n\rbreakerStatus\x18\x03 \x01(\x0b\x32\x1c.breakermodule.BreakerStatusB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\x42\x87\x01\n\x15openfmb.breakermoduleP\x01ZTgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/breakermodule\xaa\x02\x15openfmb.breakermoduleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'breakermodule.breakermodule_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025openfmb.breakermoduleP\001ZTgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/breakermodule\252\002\025openfmb.breakermodule'
  _BREAKERDISCRETECONTROLXCBR.fields_by_name['discreteControlXCBR']._options = None
  _BREAKERDISCRETECONTROLXCBR.fields_by_name['discreteControlXCBR']._serialized_options = b'\200\265\030\001'
  _BREAKERDISCRETECONTROL.fields_by_name['controlValue']._options = None
  _BREAKERDISCRETECONTROL.fields_by_name['controlValue']._serialized_options = b'\200\265\030\001'
  _BREAKER.fields_by_name['conductingEquipment']._options = None
  _BREAKER.fields_by_name['conductingEquipment']._serialized_options = b'\200\265\030\001'
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._options = None
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._serialized_options = b'\200\265\030\001'
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['breaker']._options = None
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['breaker']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['breakerDiscreteControl']._options = None
  _BREAKERDISCRETECONTROLPROFILE.fields_by_name['breakerDiscreteControl']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKERDISCRETECONTROLPROFILE._options = None
  _BREAKERDISCRETECONTROLPROFILE._serialized_options = b'\300\363\030\001'
  _BREAKEREVENT.fields_by_name['eventValue']._options = None
  _BREAKEREVENT.fields_by_name['eventValue']._serialized_options = b'\200\265\030\001'
  _BREAKEREVENTPROFILE.fields_by_name['eventMessageInfo']._options = None
  _BREAKEREVENTPROFILE.fields_by_name['eventMessageInfo']._serialized_options = b'\200\265\030\001'
  _BREAKEREVENTPROFILE.fields_by_name['breaker']._options = None
  _BREAKEREVENTPROFILE.fields_by_name['breaker']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKEREVENTPROFILE.fields_by_name['breakerEvent']._options = None
  _BREAKEREVENTPROFILE.fields_by_name['breakerEvent']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKEREVENTPROFILE._options = None
  _BREAKEREVENTPROFILE._serialized_options = b'\300\363\030\001'
  _BREAKERREADING.fields_by_name['conductingEquipmentTerminalReading']._options = None
  _BREAKERREADING.fields_by_name['conductingEquipmentTerminalReading']._serialized_options = b'\200\265\030\001'
  _BREAKERREADINGPROFILE.fields_by_name['readingMessageInfo']._options = None
  _BREAKERREADINGPROFILE.fields_by_name['readingMessageInfo']._serialized_options = b'\200\265\030\001'
  _BREAKERREADINGPROFILE.fields_by_name['breaker']._options = None
  _BREAKERREADINGPROFILE.fields_by_name['breaker']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKERREADINGPROFILE.fields_by_name['breakerReading']._options = None
  _BREAKERREADINGPROFILE.fields_by_name['breakerReading']._serialized_options = b'\210\265\030\001\220\265\030\001\230\265\030\002'
  _BREAKERREADINGPROFILE._options = None
  _BREAKERREADINGPROFILE._serialized_options = b'\300\363\030\001'
  _BREAKERSTATUS.fields_by_name['statusValue']._options = None
  _BREAKERSTATUS.fields_by_name['statusValue']._serialized_options = b'\200\265\030\001'
  _BREAKERSTATUSPROFILE.fields_by_name['statusMessageInfo']._options = None
  _BREAKERSTATUSPROFILE.fields_by_name['statusMessageInfo']._serialized_options = b'\200\265\030\001'
  _BREAKERSTATUSPROFILE.fields_by_name['breaker']._options = None
  _BREAKERSTATUSPROFILE.fields_by_name['breaker']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKERSTATUSPROFILE.fields_by_name['breakerStatus']._options = None
  _BREAKERSTATUSPROFILE.fields_by_name['breakerStatus']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _BREAKERSTATUSPROFILE._options = None
  _BREAKERSTATUSPROFILE._serialized_options = b'\300\363\030\001'
  _BREAKERDISCRETECONTROLXCBR._serialized_start=96
  _BREAKERDISCRETECONTROLXCBR._serialized_end=194
  _BREAKERDISCRETECONTROL._serialized_start=197
  _BREAKERDISCRETECONTROL._serialized_end=402
  _BREAKER._serialized_start=404
  _BREAKER._serialized_end=483
  _BREAKERDISCRETECONTROLPROFILE._serialized_start=486
  _BREAKERDISCRETECONTROLPROFILE._serialized_end=723
  _BREAKEREVENT._serialized_start=726
  _BREAKEREVENT._serialized_end=854
  _BREAKEREVENTPROFILE._serialized_start=857
  _BREAKEREVENTPROFILE._serialized_end=1060
  _BREAKERREADING._serialized_start=1063
  _BREAKERREADING._serialized_end=1371
  _BREAKERREADINGPROFILE._serialized_start=1374
  _BREAKERREADINGPROFILE._serialized_end=1591
  _BREAKERSTATUS._serialized_start=1594
  _BREAKERSTATUS._serialized_end=1725
  _BREAKERSTATUSPROFILE._serialized_start=1728
  _BREAKERSTATUSPROFILE._serialized_end=1936
# @@protoc_insertion_point(module_scope)
