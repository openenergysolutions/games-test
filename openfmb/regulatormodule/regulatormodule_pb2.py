# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: regulatormodule/regulatormodule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uml_pb2 as uml__pb2
from commonmodule import commonmodule_pb2 as commonmodule_dot_commonmodule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%regulatormodule/regulatormodule.proto\x12\x0fregulatormodule\x1a\tuml.proto\x1a\x1f\x63ommonmodule/commonmodule.proto\"\x90\x02\n\x0f\x44irectionalATCC\x12&\n\x06\x42ndWid\x18\x01 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12)\n\tCtlDlTmms\x18\x02 \x01(\x0b\x32\x16.commonmodule.PhaseISC\x12$\n\x04LDCR\x18\x03 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12$\n\x04LDCX\x18\x04 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12&\n\x06VolSpt\x18\x05 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12\x36\n\x16voltageSetPointEnabled\x18\x06 \x01(\x0b\x32\x16.commonmodule.PhaseDPC\"\x8c\x05\n\x14RegulatorControlATCC\x12H\n\x15logicalNodeForControl\x18\x01 \x01(\x0b\x32#.commonmodule.LogicalNodeForControlB\x04\x80\xb5\x18\x01\x12\x30\n\x06\x44irFwd\x18\x02 \x01(\x0b\x32 .regulatormodule.DirectionalATCC\x12\x39\n\x07\x44irMode\x18\x03 \x01(\x0b\x32(.commonmodule.Optional_DirectionModeKind\x12\x30\n\x06\x44irRev\x18\x04 \x01(\x0b\x32 .regulatormodule.DirectionalATCC\x12&\n\x06\x44irThd\x18\x05 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12%\n\x05ParOp\x18\x06 \x01(\x0b\x32\x16.commonmodule.PhaseSPC\x12)\n\trampRates\x18\x07 \x01(\x0b\x32\x16.commonmodule.RampRate\x12/\n\x05state\x18\x08 \x01(\x0b\x32 .commonmodule.Optional_StateKind\x12&\n\x06TapOpL\x18\t \x01(\x0b\x32\x16.commonmodule.PhaseSPC\x12&\n\x06TapOpR\x18\n \x01(\x0b\x32\x16.commonmodule.PhaseSPC\x12(\n\x08VolLmtHi\x18\x0b \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12(\n\x08VolLmtLo\x18\x0c \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12<\n\nVolLmtMode\x18\r \x01(\x0b\x32(.commonmodule.Optional_VoltLimitModeKind\"~\n\x0eRegulatorPoint\x12\x36\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32%.regulatormodule.RegulatorControlATCC\x12\x34\n\tstartTime\x18\x08 \x01(\x0b\x32\x17.commonmodule.TimestampB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"I\n\x0cRegulatorCSG\x12\x39\n\x06\x63rvPts\x18\x01 \x03(\x0b\x32\x1f.regulatormodule.RegulatorPointB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"X\n\x1cRegulatorControlScheduleFSCH\x12\x38\n\x07ValDCSG\x18\x01 \x01(\x0b\x32\x1d.regulatormodule.RegulatorCSGB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\"\xa1\x01\n\x14RegulatorControlFSCC\x12\x34\n\x0b\x63ontrolFSCC\x18\x01 \x01(\x0b\x32\x19.commonmodule.ControlFSCCB\x04\x80\xb5\x18\x01\x12S\n\x1cregulatorControlScheduleFSCH\x18\x02 \x01(\x0b\x32-.regulatormodule.RegulatorControlScheduleFSCH\"\xbd\x01\n\x10RegulatorControl\x12\x36\n\x0c\x63ontrolValue\x18\x01 \x01(\x0b\x32\x1a.commonmodule.ControlValueB\x04\x80\xb5\x18\x01\x12,\n\x05\x63heck\x18\x02 \x01(\x0b\x32\x1d.commonmodule.CheckConditions\x12\x43\n\x14regulatorControlFSCC\x18\x03 \x01(\x0b\x32%.regulatormodule.RegulatorControlFSCC\"W\n\x0fRegulatorSystem\x12\x44\n\x13\x63onductingEquipment\x18\x01 \x01(\x0b\x32!.commonmodule.ConductingEquipmentB\x04\x80\xb5\x18\x01\"\xef\x01\n\x17RegulatorControlProfile\x12\x42\n\x12\x63ontrolMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ControlMessageInfoB\x04\x80\xb5\x18\x01\x12\x45\n\x10regulatorControl\x18\x02 \x01(\x0b\x32!.regulatormodule.RegulatorControlB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x43\n\x0fregulatorSystem\x18\x03 \x01(\x0b\x32 .regulatormodule.RegulatorSystemB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xc5\x01\n\x18RegulatorDiscreteControl\x12\x36\n\x0c\x63ontrolValue\x18\x01 \x01(\x0b\x32\x1a.commonmodule.ControlValueB\x04\x80\xb5\x18\x01\x12,\n\x05\x63heck\x18\x02 \x01(\x0b\x32\x1d.commonmodule.CheckConditions\x12\x43\n\x14regulatorControlATCC\x18\x03 \x01(\x0b\x32%.regulatormodule.RegulatorControlATCC\"\x87\x02\n\x1fRegulatorDiscreteControlProfile\x12\x42\n\x12\x63ontrolMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ControlMessageInfoB\x04\x80\xb5\x18\x01\x12U\n\x18regulatorDiscreteControl\x18\x02 \x01(\x0b\x32).regulatormodule.RegulatorDiscreteControlB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x43\n\x0fregulatorSystem\x18\x03 \x01(\x0b\x32 .regulatormodule.RegulatorSystemB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xa4\x07\n\x1bRegulatorEventAndStatusATCC\x12!\n\x06\x42ndCtr\x18\x01 \x01(\x0b\x32\x11.commonmodule.ASG\x12!\n\x06\x42ndWid\x18\x02 \x01(\x0b\x32\x11.commonmodule.ASG\x12(\n\x08\x42ndWidHi\x18\x03 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12(\n\x08\x42ndWidLo\x18\x04 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12)\n\tDirCtlRev\x18\x05 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12\'\n\x07\x44irIndt\x18\x06 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12&\n\x06\x44irRev\x18\x07 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12\x1f\n\x04LDCR\x18\x08 \x01(\x0b\x32\x11.commonmodule.ASG\x12\x1f\n\x04LDCX\x18\t \x01(\x0b\x32\x11.commonmodule.ASG\x12&\n\x05ParOp\x18\n \x01(\x0b\x32\x17.commonmodule.StatusSPS\x12)\n\trampRates\x18\x0b \x01(\x0b\x32\x16.commonmodule.RampRate\x12/\n\x05state\x18\x0c \x01(\x0b\x32 .commonmodule.Optional_StateKind\x12)\n\x08StDlTmms\x18\r \x01(\x0b\x32\x17.commonmodule.StatusINC\x12)\n\x08TapOpErr\x18\x0e \x01(\x0b\x32\x17.commonmodule.StatusSPS\x12&\n\x06TapPos\x18\x0f \x01(\x0b\x32\x16.commonmodule.PhaseINS\x12(\n\x08VolLmtHi\x18\x10 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12(\n\x08VolLmtLo\x18\x11 \x01(\x0b\x32\x16.commonmodule.PhaseSPS\x12&\n\x06VolSpt\x18\x12 \x01(\x0b\x32\x16.commonmodule.PhaseAPC\x12\x37\n\x16voltageSetPointEnabled\x18\x13 \x01(\x0b\x32\x17.commonmodule.StatusSPS\x12\x38\n\x06\x44irMod\x18\x14 \x01(\x0b\x32(.commonmodule.Optional_DirectionModeKind\x12<\n\nVolLmtMode\x18\x15 \x01(\x0b\x32(.commonmodule.Optional_VoltLimitModeKind\"\xf0\x01\n\x1bRegulatorEventAndStatusANCR\x12V\n\x1clogicalNodeForEventAndStatus\x18\x01 \x01(\x0b\x32*.commonmodule.LogicalNodeForEventAndStatusB\x04\x80\xb5\x18\x01\x12\x36\n\x0b\x44ynamicTest\x18\x02 \x01(\x0b\x32!.commonmodule.ENS_DynamicTestKind\x12\x41\n\x0bPointStatus\x18\x03 \x01(\x0b\x32,.regulatormodule.RegulatorEventAndStatusATCC\"\x97\x01\n\x0eRegulatorEvent\x12\x32\n\neventValue\x18\x01 \x01(\x0b\x32\x18.commonmodule.EventValueB\x04\x80\xb5\x18\x01\x12Q\n\x1bregulatorEventAndStatusANCR\x18\x02 \x01(\x0b\x32,.regulatormodule.RegulatorEventAndStatusANCR\"\xe5\x01\n\x15RegulatorEventProfile\x12>\n\x10\x65ventMessageInfo\x18\x01 \x01(\x0b\x32\x1e.commonmodule.EventMessageInfoB\x04\x80\xb5\x18\x01\x12\x41\n\x0eregulatorEvent\x18\x02 \x01(\x0b\x32\x1f.regulatormodule.RegulatorEventB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x43\n\x0fregulatorSystem\x18\x03 \x01(\x0b\x32 .regulatormodule.RegulatorSystemB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\xbb\x02\n\x10RegulatorReading\x12\x62\n\"conductingEquipmentTerminalReading\x18\x01 \x01(\x0b\x32\x30.commonmodule.ConductingEquipmentTerminalReadingB\x04\x80\xb5\x18\x01\x12*\n\tphaseMMTN\x18\x02 \x01(\x0b\x32\x17.commonmodule.PhaseMMTN\x12.\n\x0breadingMMTR\x18\x03 \x01(\x0b\x32\x19.commonmodule.ReadingMMTR\x12.\n\x0breadingMMXU\x18\x04 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\x12\x37\n\x14secondaryReadingMMXU\x18\x05 \x01(\x0b\x32\x19.commonmodule.ReadingMMXU\"\xf3\x01\n\x17RegulatorReadingProfile\x12\x42\n\x12readingMessageInfo\x18\x01 \x01(\x0b\x32 .commonmodule.ReadingMessageInfoB\x04\x80\xb5\x18\x01\x12I\n\x10regulatorReading\x18\x02 \x03(\x0b\x32!.regulatormodule.RegulatorReadingB\x0c\x88\xb5\x18\x01\x90\xb5\x18\x01\x98\xb5\x18\x02\x12\x43\n\x0fregulatorSystem\x18\x03 \x01(\x0b\x32 .regulatormodule.RegulatorSystemB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\"\x9a\x01\n\x0fRegulatorStatus\x12\x34\n\x0bstatusValue\x18\x01 \x01(\x0b\x32\x19.commonmodule.StatusValueB\x04\x80\xb5\x18\x01\x12Q\n\x1bregulatorEventAndStatusANCR\x18\x02 \x01(\x0b\x32,.regulatormodule.RegulatorEventAndStatusANCR\"\xea\x01\n\x16RegulatorStatusProfile\x12@\n\x11statusMessageInfo\x18\x01 \x01(\x0b\x32\x1f.commonmodule.StatusMessageInfoB\x04\x80\xb5\x18\x01\x12\x43\n\x0fregulatorStatus\x18\x02 \x01(\x0b\x32 .regulatormodule.RegulatorStatusB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01\x12\x43\n\x0fregulatorSystem\x18\x03 \x01(\x0b\x32 .regulatormodule.RegulatorSystemB\x08\x88\xb5\x18\x01\x90\xb5\x18\x01:\x04\xc0\xf3\x18\x01\x42\x8d\x01\n\x17openfmb.regulatormoduleP\x01ZVgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/regulatormodule\xaa\x02\x17openfmb.regulatormoduleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'regulatormodule.regulatormodule_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027openfmb.regulatormoduleP\001ZVgitlab.com/openfmb/psm/ops/protobuf/go-openfmb-ops-protobuf/v2/openfmb/regulatormodule\252\002\027openfmb.regulatormodule'
  _REGULATORCONTROLATCC.fields_by_name['logicalNodeForControl']._options = None
  _REGULATORCONTROLATCC.fields_by_name['logicalNodeForControl']._serialized_options = b'\200\265\030\001'
  _REGULATORPOINT.fields_by_name['startTime']._options = None
  _REGULATORPOINT.fields_by_name['startTime']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORCSG.fields_by_name['crvPts']._options = None
  _REGULATORCSG.fields_by_name['crvPts']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORCONTROLSCHEDULEFSCH.fields_by_name['ValDCSG']._options = None
  _REGULATORCONTROLSCHEDULEFSCH.fields_by_name['ValDCSG']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORCONTROLFSCC.fields_by_name['controlFSCC']._options = None
  _REGULATORCONTROLFSCC.fields_by_name['controlFSCC']._serialized_options = b'\200\265\030\001'
  _REGULATORCONTROL.fields_by_name['controlValue']._options = None
  _REGULATORCONTROL.fields_by_name['controlValue']._serialized_options = b'\200\265\030\001'
  _REGULATORSYSTEM.fields_by_name['conductingEquipment']._options = None
  _REGULATORSYSTEM.fields_by_name['conductingEquipment']._serialized_options = b'\200\265\030\001'
  _REGULATORCONTROLPROFILE.fields_by_name['controlMessageInfo']._options = None
  _REGULATORCONTROLPROFILE.fields_by_name['controlMessageInfo']._serialized_options = b'\200\265\030\001'
  _REGULATORCONTROLPROFILE.fields_by_name['regulatorControl']._options = None
  _REGULATORCONTROLPROFILE.fields_by_name['regulatorControl']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORCONTROLPROFILE.fields_by_name['regulatorSystem']._options = None
  _REGULATORCONTROLPROFILE.fields_by_name['regulatorSystem']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORCONTROLPROFILE._options = None
  _REGULATORCONTROLPROFILE._serialized_options = b'\300\363\030\001'
  _REGULATORDISCRETECONTROL.fields_by_name['controlValue']._options = None
  _REGULATORDISCRETECONTROL.fields_by_name['controlValue']._serialized_options = b'\200\265\030\001'
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._options = None
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['controlMessageInfo']._serialized_options = b'\200\265\030\001'
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['regulatorDiscreteControl']._options = None
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['regulatorDiscreteControl']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['regulatorSystem']._options = None
  _REGULATORDISCRETECONTROLPROFILE.fields_by_name['regulatorSystem']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORDISCRETECONTROLPROFILE._options = None
  _REGULATORDISCRETECONTROLPROFILE._serialized_options = b'\300\363\030\001'
  _REGULATOREVENTANDSTATUSANCR.fields_by_name['logicalNodeForEventAndStatus']._options = None
  _REGULATOREVENTANDSTATUSANCR.fields_by_name['logicalNodeForEventAndStatus']._serialized_options = b'\200\265\030\001'
  _REGULATOREVENT.fields_by_name['eventValue']._options = None
  _REGULATOREVENT.fields_by_name['eventValue']._serialized_options = b'\200\265\030\001'
  _REGULATOREVENTPROFILE.fields_by_name['eventMessageInfo']._options = None
  _REGULATOREVENTPROFILE.fields_by_name['eventMessageInfo']._serialized_options = b'\200\265\030\001'
  _REGULATOREVENTPROFILE.fields_by_name['regulatorEvent']._options = None
  _REGULATOREVENTPROFILE.fields_by_name['regulatorEvent']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATOREVENTPROFILE.fields_by_name['regulatorSystem']._options = None
  _REGULATOREVENTPROFILE.fields_by_name['regulatorSystem']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATOREVENTPROFILE._options = None
  _REGULATOREVENTPROFILE._serialized_options = b'\300\363\030\001'
  _REGULATORREADING.fields_by_name['conductingEquipmentTerminalReading']._options = None
  _REGULATORREADING.fields_by_name['conductingEquipmentTerminalReading']._serialized_options = b'\200\265\030\001'
  _REGULATORREADINGPROFILE.fields_by_name['readingMessageInfo']._options = None
  _REGULATORREADINGPROFILE.fields_by_name['readingMessageInfo']._serialized_options = b'\200\265\030\001'
  _REGULATORREADINGPROFILE.fields_by_name['regulatorReading']._options = None
  _REGULATORREADINGPROFILE.fields_by_name['regulatorReading']._serialized_options = b'\210\265\030\001\220\265\030\001\230\265\030\002'
  _REGULATORREADINGPROFILE.fields_by_name['regulatorSystem']._options = None
  _REGULATORREADINGPROFILE.fields_by_name['regulatorSystem']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORREADINGPROFILE._options = None
  _REGULATORREADINGPROFILE._serialized_options = b'\300\363\030\001'
  _REGULATORSTATUS.fields_by_name['statusValue']._options = None
  _REGULATORSTATUS.fields_by_name['statusValue']._serialized_options = b'\200\265\030\001'
  _REGULATORSTATUSPROFILE.fields_by_name['statusMessageInfo']._options = None
  _REGULATORSTATUSPROFILE.fields_by_name['statusMessageInfo']._serialized_options = b'\200\265\030\001'
  _REGULATORSTATUSPROFILE.fields_by_name['regulatorStatus']._options = None
  _REGULATORSTATUSPROFILE.fields_by_name['regulatorStatus']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORSTATUSPROFILE.fields_by_name['regulatorSystem']._options = None
  _REGULATORSTATUSPROFILE.fields_by_name['regulatorSystem']._serialized_options = b'\210\265\030\001\220\265\030\001'
  _REGULATORSTATUSPROFILE._options = None
  _REGULATORSTATUSPROFILE._serialized_options = b'\300\363\030\001'
  _DIRECTIONALATCC._serialized_start=103
  _DIRECTIONALATCC._serialized_end=375
  _REGULATORCONTROLATCC._serialized_start=378
  _REGULATORCONTROLATCC._serialized_end=1030
  _REGULATORPOINT._serialized_start=1032
  _REGULATORPOINT._serialized_end=1158
  _REGULATORCSG._serialized_start=1160
  _REGULATORCSG._serialized_end=1233
  _REGULATORCONTROLSCHEDULEFSCH._serialized_start=1235
  _REGULATORCONTROLSCHEDULEFSCH._serialized_end=1323
  _REGULATORCONTROLFSCC._serialized_start=1326
  _REGULATORCONTROLFSCC._serialized_end=1487
  _REGULATORCONTROL._serialized_start=1490
  _REGULATORCONTROL._serialized_end=1679
  _REGULATORSYSTEM._serialized_start=1681
  _REGULATORSYSTEM._serialized_end=1768
  _REGULATORCONTROLPROFILE._serialized_start=1771
  _REGULATORCONTROLPROFILE._serialized_end=2010
  _REGULATORDISCRETECONTROL._serialized_start=2013
  _REGULATORDISCRETECONTROL._serialized_end=2210
  _REGULATORDISCRETECONTROLPROFILE._serialized_start=2213
  _REGULATORDISCRETECONTROLPROFILE._serialized_end=2476
  _REGULATOREVENTANDSTATUSATCC._serialized_start=2479
  _REGULATOREVENTANDSTATUSATCC._serialized_end=3411
  _REGULATOREVENTANDSTATUSANCR._serialized_start=3414
  _REGULATOREVENTANDSTATUSANCR._serialized_end=3654
  _REGULATOREVENT._serialized_start=3657
  _REGULATOREVENT._serialized_end=3808
  _REGULATOREVENTPROFILE._serialized_start=3811
  _REGULATOREVENTPROFILE._serialized_end=4040
  _REGULATORREADING._serialized_start=4043
  _REGULATORREADING._serialized_end=4358
  _REGULATORREADINGPROFILE._serialized_start=4361
  _REGULATORREADINGPROFILE._serialized_end=4604
  _REGULATORSTATUS._serialized_start=4607
  _REGULATORSTATUS._serialized_end=4761
  _REGULATORSTATUSPROFILE._serialized_start=4764
  _REGULATORSTATUSPROFILE._serialized_end=4998
# @@protoc_insertion_point(module_scope)
