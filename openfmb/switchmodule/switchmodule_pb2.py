# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: switchmodule/switchmodule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uml_pb2 as uml__pb2
from commonmodule import commonmodule_pb2 as commonmodule_dot_commonmodule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fswitchmodule/switchmodule.proto\x12\x0cswitchmodule\x1a\tuml.proto\x1a\x1f\x63ommonmodule/commonmodule.proto\"\xc3\x01\n\x19SwitchDiscreteControlXSWI\x12H\n\x15logicalNodeForControl\x18\x01 \x01(\x0b\x32#.commonmodule.LogicalNodeForControlB\x04\x80\xb5\x18\x01\x12#\n\x03Pos\x18\x02 \x01(\x0b\x32\x16.commonmodule.PhaseDPC\x12\x37\n\x15ResetProtectionPickup\x18\x03 \x01(\x0b\x32\x18.commonmodule.ControlSPC\"\xc9\x01\n\x15SwitchDiscreteControl\x12\x36\n\x0c\x63ontrolValue\x18\x01 \x01(\x0b\x32\x1a.commonmodule.ControlValueB\x04\x80\xb5\x18\x01\x12,\n\x05\x63heck\x18\x02 \x01(\x0b\x32\x1d.commonmodule.CheckConditions\x12J\n\x19switchDiscreteControlXSWI\x18\x03 \x01(\x0b\x32\'.switchmodule.SwitchDiscreteControlXSWI\"W\n\x0fProtectedSwitch\x12\x44\n\x13\x63onductingEquipment\x18\x01 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x04\x80\xb5\x18\x01\"\xf8\x01\n\x1cSwitchDiscreteControlProfile\x12\x42\n\x12\x63ontrolMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ControlMessageInfoB\x04\x80\xb5\x18\x01\x12@\n\x0fprotectedSwitch\x18\x02 \x01(\x0b\x32\x1d.switchmodule.ProtectedSwitchB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12L\n\x15switchDiscreteControl\x18\x03 \x01(\x0b\x32#.switchmodule.SwitchDiscreteControlB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xc6\x01\n\x0fSwitchEventXSWI\x12V\n\x1clogicalNodeForEventAndStatus\x18\x01 \x01(\x0b\x32*.commonmodule.LogicalNodeForEventAndStatusB\x04\x80\xb5\x18\x01\x12\x36\n\x0b\x44ynamicTest\x18\x02 \x01(\x0b\x32!.commonmodule.ENS_DynamicTestKind\x12#\n\x03Pos\x18\x03 \x01(\x0b\x32\x16.commonmodule.PhaseDPS\"y\n\x0bSwitchEvent\x12\x32\n\neventValue\x18\x01 \x01(\x0b\x32\x18.commonmodule.EventValueB\x04\x80\xb5\x18\x01\x12\x36\n\x0fswitchEventXSWI\x18\x02 \x01(\x0b\x32\x1d.switchmodule.SwitchEventXSWI\"\xd6\x01\n\x12SwitchEventProfile\x12>\n\x10\x65ventMessageInfo\x18\x01 \x01(\x0b\x32\x1e.commonmodule.EventMessageInfoB\x04\x80\xb5\x18\x01\x12@\n\x0fprotectedSwitch\x18\x02 \x01(\x0b\x32\x1d.switchmodule.ProtectedSwitchB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x38\n\x0bswitchEvent\x18\x03 \x01(\x0b\x32\x19.switchmodule.SwitchEventB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xb3\x02\n\rSwitchReading\x12\x62\n\"conductingEquipmentTerminalReading\x18\x01 \x01(\x0b\x32\x30.commonmodule.ConductingEquipmentTerminalReadingB\x04\x80\xb5\x18\x01\x12\x32\n\x0f\x64iffReadingMMXU\x18\x02 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\x12*\n\tphaseMMTN\x18\x03 \x01(\x0b\x32\x17.commonmodule.PhaseMMTN\x12.\n\x0breadingMMTR\x18\x04 \x01(\x0b\x32\x19.commonmodule.ReadingMMTR\x12.\n\x0breadingMMXU\x18\x05 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\"\xe4\x01\n\x14SwitchReadingProfile\x12\x42\n\x12readingMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ReadingMessageInfoB\x04\x80\xb5\x18\x01\x12@\n\x0fprotectedSwitch\x18\x02 \x01(\x0b\x32\x1d.switchmodule.ProtectedSwitchB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12@\n\rswitchReading\x18\x03 \x03(\x0b\x32\x1b.switchmodule.SwitchReadingB\x0c\x88\xb5\x18\x01\x90\xb5\x18\x01\x98\xb5\x18\x02:\x04\xc0\xf3\x18\x01\"\x83\x02\n\x10SwitchStatusXSWI\x12V\n\x1clogicalNodeForEventAndStatus\x18\x01 \x01(\x0b\x32*.commonmodule.LogicalNodeForEventAndStatusB\x04\x80\xb5\x18\x01\x12\x36\n\x0b\x44ynamicTest\x18\x02 \x01(\x0b\x32!.commonmodule.ENS_DynamicTestKind\x12#\n\x03Pos\x18\x04 \x01(\x0b\x32\x16.commonmodule.PhaseDPS\x12:\n\x10ProtectionPickup\x18\x05 \x01(\x0b\x32\x16.commonmodule.PhaseSPSB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"~\n\x0cSwitchStatus\x12\x34\n\x0bstatusValue\x18\x01 \x01(\x0b\x32\x19.commonmodule.StatusValueB\x04\x80\xb5\x18\x01\x12\x38\n\x10switchStatusXSWI\x18\x02 \x01(\x0b\x32\x1e.switchmodule.SwitchStatusXSWI\"\xdb\x01\n\x13SwitchStatusProfile\x12@\n\x11statusMessageInfo\x18\x01 \x01(\x0b\x32\x1f.commonmodule.StatusMessageInfoB\x04\x80\xb5\x18\x01\x12@\n\x0fprotectedSwitch\x18\x02 \x01(\x0b\x32\x1d.switchmodule.ProtectedSwitchB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12:\n\x0cswitchStatus\x18\x03 \x01(\x0b\x32\x1a.switchmodule.SwitchStatusB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\x42\x84\x01\n\x14openfmb.switchmoduleP\x01ZSgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/switchmodule\xaa\x02\x14openfmb.switchmoduleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'switchmodule.switchmodule_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024openfmb.switchmoduleP\001ZSgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/switchmodule\252\002\024openfmb.switchmodule'
  _SWITCHDISCRETECONTROLXSWI.fields_by_name['logicalNodeForControl']._options = None
  _SWITCHDISCRETECONTROLXSWI.fields_by_name['logicalNodeForControl']._serialized_options = b'\200\265\030\001'
  _SWITCHDISCRETECONTROL.fields_by_name['controlValue']._options = None
  _SWITCHDISCRETECONTROL.fields_by_name['controlValue']._serialized_options = b'\200\265\030\001'
  _PROTECTEDSWITCH.fields_by_name['conductingEquipment']._options = None
  _PROTECTEDSWITCH.fields_by_name['conductingEquipment']._serialized_options = b'\200\265\030\001'
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._options = None
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._serialized_options = b'\200\265\030\001'
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['protectedSwitch']._options = None
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['protectedSwitch']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['switchDiscreteControl']._options = None
  _SWITCHDISCRETECONTROLPROFILE.fields_by_name['switchDiscreteControl']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHDISCRETECONTROLPROFILE._options = None
  _SWITCHDISCRETECONTROLPROFILE._serialized_options = b'\300\363\030\001'
  _SWITCHEVENTXSWI.fields_by_name['logicalNodeForEventAndStatus']._options = None
  _SWITCHEVENTXSWI.fields_by_name['logicalNodeForEventAndStatus']._serialized_options = b'\200\265\030\001'
  _SWITCHEVENT.fields_by_name['eventValue']._options = None
  _SWITCHEVENT.fields_by_name['eventValue']._serialized_options = b'\200\265\030\001'
  _SWITCHEVENTPROFILE.fields_by_name['eventMessageInfo']._options = None
  _SWITCHEVENTPROFILE.fields_by_name['eventMessageInfo']._serialized_options = b'\200\265\030\001'
  _SWITCHEVENTPROFILE.fields_by_name['protectedSwitch']._options = None
  _SWITCHEVENTPROFILE.fields_by_name['protectedSwitch']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHEVENTPROFILE.fields_by_name['switchEvent']._options = None
  _SWITCHEVENTPROFILE.fields_by_name['switchEvent']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHEVENTPROFILE._options = None
  _SWITCHEVENTPROFILE._serialized_options = b'\300\363\030\001'
  _SWITCHREADING.fields_by_name['conductingEquipmentTerminalReading']._options = None
  _SWITCHREADING.fields_by_name['conductingEquipmentTerminalReading']._serialized_options = b'\200\265\030\001'
  _SWITCHREADINGPROFILE.fields_by_name['readingMessageInfo']._options = None
  _SWITCHREADINGPROFILE.fields_by_name['readingMessageInfo']._serialized_options = b'\200\265\030\001'
  _SWITCHREADINGPROFILE.fields_by_name['protectedSwitch']._options = None
  _SWITCHREADINGPROFILE.fields_by_name['protectedSwitch']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHREADINGPROFILE.fields_by_name['switchReading']._options = None
  _SWITCHREADINGPROFILE.fields_by_name['switchReading']._serialized_options = b'\210\265\030\001\220\265\030\001\230\265\030\002'
  _SWITCHREADINGPROFILE._options = None
  _SWITCHREADINGPROFILE._serialized_options = b'\300\363\030\001'
  _SWITCHSTATUSXSWI.fields_by_name['logicalNodeForEventAndStatus']._options = None
  _SWITCHSTATUSXSWI.fields_by_name['logicalNodeForEventAndStatus']._serialized_options = b'\200\265\030\001'
  _SWITCHSTATUSXSWI.fields_by_name['ProtectionPickup']._options = None
  _SWITCHSTATUSXSWI.fields_by_name['ProtectionPickup']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHSTATUS.fields_by_name['statusValue']._options = None
  _SWITCHSTATUS.fields_by_name['statusValue']._serialized_options = b'\200\265\030\001'
  _SWITCHSTATUSPROFILE.fields_by_name['statusMessageInfo']._options = None
  _SWITCHSTATUSPROFILE.fields_by_name['statusMessageInfo']._serialized_options = b'\200\265\030\001'
  _SWITCHSTATUSPROFILE.fields_by_name['protectedSwitch']._options = None
  _SWITCHSTATUSPROFILE.fields_by_name['protectedSwitch']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHSTATUSPROFILE.fields_by_name['switchStatus']._options = None
  _SWITCHSTATUSPROFILE.fields_by_name['switchStatus']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _SWITCHSTATUSPROFILE._options = None
  _SWITCHSTATUSPROFILE._serialized_options = b'\300\363\030\001'
  _SWITCHDISCRETECONTROLXSWI._serialized_start=94
  _SWITCHDISCRETECONTROLXSWI._serialized_end=289
  _SWITCHDISCRETECONTROL._serialized_start=292
  _SWITCHDISCRETECONTROL._serialized_end=493
  _PROTECTEDSWITCH._serialized_start=495
  _PROTECTEDSWITCH._serialized_end=582
  _SWITCHDISCRETECONTROLPROFILE._serialized_start=585
  _SWITCHDISCRETECONTROLPROFILE._serialized_end=833
  _SWITCHEVENTXSWI._serialized_start=836
  _SWITCHEVENTXSWI._serialized_end=1034
  _SWITCHEVENT._serialized_start=1036
  _SWITCHEVENT._serialized_end=1157
  _SWITCHEVENTPROFILE._serialized_start=1160
  _SWITCHEVENTPROFILE._serialized_end=1374
  _SWITCHREADING._serialized_start=1377
  _SWITCHREADING._serialized_end=1684
  _SWITCHREADINGPROFILE._serialized_start=1687
  _SWITCHREADINGPROFILE._serialized_end=1915
  _SWITCHSTATUSXSWI._serialized_start=1918
  _SWITCHSTATUSXSWI._serialized_end=2177
  _SWITCHSTATUS._serialized_start=2179
  _SWITCHSTATUS._serialized_end=2305
  _SWITCHSTATUSPROFILE._serialized_start=2308
  _SWITCHSTATUSPROFILE._serialized_end=2527
# @@protoc_insertion_point(module_scope)