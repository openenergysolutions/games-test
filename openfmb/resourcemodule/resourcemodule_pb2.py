# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resourcemodule/resourcemodule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uml_pb2 as uml__pb2
from commonmodule import commonmodule_pb2 as commonmodule_dot_commonmodule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#resourcemodule/resourcemodule.proto\x12\x0eresourcemodule\x1a\tuml.proto\x1a\x1f\x63ommonmodule/commonmodule.proto\"\xb2\x01\n\x12\x42ooleanControlGGIO\x12\x34\n\x0blogicalNode\x18\x01 \x01(\x0b\x32\x19.commonmodule.LogicalNodeB\x04\x80\xb5\x18\x01\x12\x33\n\x05Phase\x18\x02 \x01(\x0b\x32$.commonmodule.Optional_PhaseCodeKind\x12\x31\n\x05SPCSO\x18\x03 \x01(\x0b\x32\x18.commonmodule.ControlSPCB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"\xb2\x01\n\x12IntegerControlGGIO\x12\x34\n\x0blogicalNode\x18\x01 \x01(\x0b\x32\x19.commonmodule.LogicalNodeB\x04\x80\xb5\x18\x01\x12\x31\n\x05ISCSO\x18\x02 \x01(\x0b\x32\x18.commonmodule.ControlINCB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x33\n\x05Phase\x18\x03 \x01(\x0b\x32$.commonmodule.Optional_PhaseCodeKind\"\xab\x01\n\x11StringControlGGIO\x12\x34\n\x0blogicalNode\x18\x01 \x01(\x0b\x32\x19.commonmodule.LogicalNodeB\x04\x80\xb5\x18\x01\x12\x33\n\x05Phase\x18\x02 \x01(\x0b\x32$.commonmodule.Optional_PhaseCodeKind\x12+\n\x06StrOut\x18\x03 \x01(\x0b\x32\x11.commonmodule.VSCB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"\xb1\x01\n\x11\x41nalogControlGGIO\x12\x34\n\x0blogicalNode\x18\x01 \x01(\x0b\x32\x19.commonmodule.LogicalNodeB\x04\x80\xb5\x18\x01\x12\x31\n\x05\x41nOut\x18\x02 \x01(\x0b\x32\x18.commonmodule.ControlAPCB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x33\n\x05Phase\x18\x03 \x01(\x0b\x32$.commonmodule.Optional_PhaseCodeKind\"\x9b\x03\n\x17ResourceDiscreteControl\x12>\n\x10identifiedObject\x18\x01 \x01(\x0b\x32\x1e.commonmodule.IdentifiedObjectB\x04\x80\xb5\x18\x01\x12,\n\x05\x63heck\x18\x02 \x01(\x0b\x32\x1d.commonmodule.CheckConditions\x12\x42\n\x11\x61nalogControlGGIO\x18\x03 \x03(\x0b\x32!.resourcemodule.AnalogControlGGIOB\x04\x90\xb5\x18\x00\x12\x44\n\x12\x62ooleanControlGGIO\x18\x04 \x03(\x0b\x32\".resourcemodule.BooleanControlGGIOB\x04\x90\xb5\x18\x00\x12\x44\n\x12integerControlGGIO\x18\x05 \x03(\x0b\x32\".resourcemodule.IntegerControlGGIOB\x04\x90\xb5\x18\x00\x12\x42\n\x11stringControlGGIO\x18\x06 \x03(\x0b\x32!.resourcemodule.StringControlGGIOB\x04\x90\xb5\x18\x00\"\x88\x02\n\x1eResourceDiscreteControlProfile\x12\x42\n\x12\x63ontrolMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ControlMessageInfoB\x04\x80\xb5\x18\x01\x12H\n\x13\x63onductingEquipment\x18\x02 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12R\n\x17resourceDiscreteControl\x18\x03 \x01(\x0b\x32\'.resourcemodule.ResourceDiscreteControlB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\x81\x02\n\x0fResourceReading\x12\x62\n\"conductingEquipmentTerminalReading\x18\x01 \x01(\x0b\x32\x30.commonmodule.ConductingEquipmentTerminalReadingB\x04\x80\xb5\x18\x01\x12*\n\tphaseMMTN\x18\x02 \x01(\x0b\x32\x17.commonmodule.PhaseMMTN\x12.\n\x0breadingMMTR\x18\x03 \x01(\x0b\x32\x19.commonmodule.ReadingMMTR\x12.\n\x0breadingMMXU\x18\x04 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\"\xfc\x01\n\x16ResourceReadingProfile\x12\x42\n\x12readingMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ReadingMessageInfoB\x04\x80\xb5\x18\x01\x12H\n\x13\x63onductingEquipment\x18\x02 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x42\n\x0fresourceReading\x18\x03 \x01(\x0b\x32\x1f.resourcemodule.ResourceReadingB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01J\x04\x08\x14\x10\x15J\x04\x08\x16\x10\x17\"\x93\x03\n\rResourceEvent\x12>\n\x10identifiedObject\x18\x01 \x01(\x0b\x32\x1e.commonmodule.IdentifiedObjectB\x04\x80\xb5\x18\x01\x12N\n\x18\x61nalogEventAndStatusGGIO\x18\x02 \x03(\x0b\x32&.commonmodule.AnalogEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12P\n\x19\x62ooleanEventAndStatusGGIO\x18\x03 \x03(\x0b\x32\'.commonmodule.BooleanEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12P\n\x19integerEventAndStatusGGIO\x18\x04 \x03(\x0b\x32\'.commonmodule.IntegerEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12N\n\x18stringEventAndStatusGGIO\x18\x05 \x03(\x0b\x32&.commonmodule.StringEventAndStatusGGIOB\x04\x90\xb5\x18\x00\"\xe6\x01\n\x14ResourceEventProfile\x12>\n\x10\x65ventMessageInfo\x18\x01 \x01(\x0b\x32\x1e.commonmodule.EventMessageInfoB\x04\x80\xb5\x18\x01\x12H\n\x13\x63onductingEquipment\x18\x02 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12>\n\rresourceEvent\x18\x03 \x01(\x0b\x32\x1d.resourcemodule.ResourceEventB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\x94\x03\n\x0eResourceStatus\x12>\n\x10identifiedObject\x18\x01 \x01(\x0b\x32\x1e.commonmodule.IdentifiedObjectB\x04\x80\xb5\x18\x01\x12N\n\x18\x61nalogEventAndStatusGGIO\x18\x02 \x03(\x0b\x32&.commonmodule.AnalogEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12P\n\x19\x62ooleanEventAndStatusGGIO\x18\x03 \x03(\x0b\x32\'.commonmodule.BooleanEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12P\n\x19integerEventAndStatusGGIO\x18\x04 \x03(\x0b\x32\'.commonmodule.IntegerEventAndStatusGGIOB\x04\x90\xb5\x18\x00\x12N\n\x18stringEventAndStatusGGIO\x18\x05 \x03(\x0b\x32&.commonmodule.StringEventAndStatusGGIOB\x04\x90\xb5\x18\x00\"\xeb\x01\n\x15ResourceStatusProfile\x12@\n\x11statusMessageInfo\x18\x01 \x01(\x0b\x32\x1f.commonmodule.StatusMessageInfoB\x04\x80\xb5\x18\x01\x12H\n\x13\x63onductingEquipment\x18\x02 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12@\n\x0eresourceStatus\x18\x03 \x01(\x0b\x32\x1e.resourcemodule.ResourceStatusB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\x42\x8a\x01\n\x16openfmb.resourcemoduleP\x01ZUgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/resourcemodule\xaa\x02\x16openfmb.resourcemoduleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resourcemodule.resourcemodule_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026openfmb.resourcemoduleP\001ZUgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/resourcemodule\252\002\026openfmb.resourcemodule'
  _BOOLEANCONTROLGGIO.fields_by_name['logicalNode']._options = None
  _BOOLEANCONTROLGGIO.fields_by_name['logicalNode']._serialized_options = b'\200\265\030\001'
  _BOOLEANCONTROLGGIO.fields_by_name['SPCSO']._options = None
  _BOOLEANCONTROLGGIO.fields_by_name['SPCSO']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _INTEGERCONTROLGGIO.fields_by_name['logicalNode']._options = None
  _INTEGERCONTROLGGIO.fields_by_name['logicalNode']._serialized_options = b'\200\265\030\001'
  _INTEGERCONTROLGGIO.fields_by_name['ISCSO']._options = None
  _INTEGERCONTROLGGIO.fields_by_name['ISCSO']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _STRINGCONTROLGGIO.fields_by_name['logicalNode']._options = None
  _STRINGCONTROLGGIO.fields_by_name['logicalNode']._serialized_options = b'\200\265\030\001'
  _STRINGCONTROLGGIO.fields_by_name['StrOut']._options = None
  _STRINGCONTROLGGIO.fields_by_name['StrOut']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _ANALOGCONTROLGGIO.fields_by_name['logicalNode']._options = None
  _ANALOGCONTROLGGIO.fields_by_name['logicalNode']._serialized_options = b'\200\265\030\001'
  _ANALOGCONTROLGGIO.fields_by_name['AnOut']._options = None
  _ANALOGCONTROLGGIO.fields_by_name['AnOut']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEDISCRETECONTROL.fields_by_name['identifiedObject']._options = None
  _RESOURCEDISCRETECONTROL.fields_by_name['identifiedObject']._serialized_options = b'\200\265\030\001'
  _RESOURCEDISCRETECONTROL.fields_by_name['analogControlGGIO']._options = None
  _RESOURCEDISCRETECONTROL.fields_by_name['analogControlGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEDISCRETECONTROL.fields_by_name['booleanControlGGIO']._options = None
  _RESOURCEDISCRETECONTROL.fields_by_name['booleanControlGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEDISCRETECONTROL.fields_by_name['integerControlGGIO']._options = None
  _RESOURCEDISCRETECONTROL.fields_by_name['integerControlGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEDISCRETECONTROL.fields_by_name['stringControlGGIO']._options = None
  _RESOURCEDISCRETECONTROL.fields_by_name['stringControlGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._options = None
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._serialized_options = b'\200\265\030\001'
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['conductingEquipment']._options = None
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['conductingEquipment']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['resourceDiscreteControl']._options = None
  _RESOURCEDISCRETECONTROLPROFILE.fields_by_name['resourceDiscreteControl']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEDISCRETECONTROLPROFILE._options = None
  _RESOURCEDISCRETECONTROLPROFILE._serialized_options = b'\300\363\030\001'
  _RESOURCEREADING.fields_by_name['conductingEquipmentTerminalReading']._options = None
  _RESOURCEREADING.fields_by_name['conductingEquipmentTerminalReading']._serialized_options = b'\200\265\030\001'
  _RESOURCEREADINGPROFILE.fields_by_name['readingMessageInfo']._options = None
  _RESOURCEREADINGPROFILE.fields_by_name['readingMessageInfo']._serialized_options = b'\200\265\030\001'
  _RESOURCEREADINGPROFILE.fields_by_name['conductingEquipment']._options = None
  _RESOURCEREADINGPROFILE.fields_by_name['conductingEquipment']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEREADINGPROFILE.fields_by_name['resourceReading']._options = None
  _RESOURCEREADINGPROFILE.fields_by_name['resourceReading']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEREADINGPROFILE._options = None
  _RESOURCEREADINGPROFILE._serialized_options = b'\300\363\030\001'
  _RESOURCEEVENT.fields_by_name['identifiedObject']._options = None
  _RESOURCEEVENT.fields_by_name['identifiedObject']._serialized_options = b'\200\265\030\001'
  _RESOURCEEVENT.fields_by_name['analogEventAndStatusGGIO']._options = None
  _RESOURCEEVENT.fields_by_name['analogEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEEVENT.fields_by_name['booleanEventAndStatusGGIO']._options = None
  _RESOURCEEVENT.fields_by_name['booleanEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEEVENT.fields_by_name['integerEventAndStatusGGIO']._options = None
  _RESOURCEEVENT.fields_by_name['integerEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEEVENT.fields_by_name['stringEventAndStatusGGIO']._options = None
  _RESOURCEEVENT.fields_by_name['stringEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCEEVENTPROFILE.fields_by_name['eventMessageInfo']._options = None
  _RESOURCEEVENTPROFILE.fields_by_name['eventMessageInfo']._serialized_options = b'\200\265\030\001'
  _RESOURCEEVENTPROFILE.fields_by_name['conductingEquipment']._options = None
  _RESOURCEEVENTPROFILE.fields_by_name['conductingEquipment']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEEVENTPROFILE.fields_by_name['resourceEvent']._options = None
  _RESOURCEEVENTPROFILE.fields_by_name['resourceEvent']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCEEVENTPROFILE._options = None
  _RESOURCEEVENTPROFILE._serialized_options = b'\300\363\030\001'
  _RESOURCESTATUS.fields_by_name['identifiedObject']._options = None
  _RESOURCESTATUS.fields_by_name['identifiedObject']._serialized_options = b'\200\265\030\001'
  _RESOURCESTATUS.fields_by_name['analogEventAndStatusGGIO']._options = None
  _RESOURCESTATUS.fields_by_name['analogEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCESTATUS.fields_by_name['booleanEventAndStatusGGIO']._options = None
  _RESOURCESTATUS.fields_by_name['booleanEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCESTATUS.fields_by_name['integerEventAndStatusGGIO']._options = None
  _RESOURCESTATUS.fields_by_name['integerEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCESTATUS.fields_by_name['stringEventAndStatusGGIO']._options = None
  _RESOURCESTATUS.fields_by_name['stringEventAndStatusGGIO']._serialized_options = b'\220\265\030\000'
  _RESOURCESTATUSPROFILE.fields_by_name['statusMessageInfo']._options = None
  _RESOURCESTATUSPROFILE.fields_by_name['statusMessageInfo']._serialized_options = b'\200\265\030\001'
  _RESOURCESTATUSPROFILE.fields_by_name['conductingEquipment']._options = None
  _RESOURCESTATUSPROFILE.fields_by_name['conductingEquipment']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCESTATUSPROFILE.fields_by_name['resourceStatus']._options = None
  _RESOURCESTATUSPROFILE.fields_by_name['resourceStatus']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _RESOURCESTATUSPROFILE._options = None
  _RESOURCESTATUSPROFILE._serialized_options = b'\300\363\030\001'
  _BOOLEANCONTROLGGIO._serialized_start=100
  _BOOLEANCONTROLGGIO._serialized_end=278
  _INTEGERCONTROLGGIO._serialized_start=281
  _INTEGERCONTROLGGIO._serialized_end=459
  _STRINGCONTROLGGIO._serialized_start=462
  _STRINGCONTROLGGIO._serialized_end=633
  _ANALOGCONTROLGGIO._serialized_start=636
  _ANALOGCONTROLGGIO._serialized_end=813
  _RESOURCEDISCRETECONTROL._serialized_start=816
  _RESOURCEDISCRETECONTROL._serialized_end=1227
  _RESOURCEDISCRETECONTROLPROFILE._serialized_start=1230
  _RESOURCEDISCRETECONTROLPROFILE._serialized_end=1494
  _RESOURCEREADING._serialized_start=1497
  _RESOURCEREADING._serialized_end=1754
  _RESOURCEREADINGPROFILE._serialized_start=1757
  _RESOURCEREADINGPROFILE._serialized_end=2009
  _RESOURCEEVENT._serialized_start=2012
  _RESOURCEEVENT._serialized_end=2415
  _RESOURCEEVENTPROFILE._serialized_start=2418
  _RESOURCEEVENTPROFILE._serialized_end=2648
  _RESOURCESTATUS._serialized_start=2651
  _RESOURCESTATUS._serialized_end=3055
  _RESOURCESTATUSPROFILE._serialized_start=3058
  _RESOURCESTATUSPROFILE._serialized_end=3293
# @@protoc_insertion_point(module_scope)