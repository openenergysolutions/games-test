import os
import time
import nats
import asyncio
import uuid
import sys
sys.path.append(os.path.abspath('openfmb'))
import capbankmodule.capbankmodule_pb2 as capbank
import commonmodule.commonmodule_pb2 as common
from google.protobuf.json_format import MessageToJson

nats_url = "nats://192.168.86.54:4222"
capbank_mrid = "21a1e1f5-2a2a-4e60-b54f-c37ff48e8157"

def create_discrete_control_profile():
    ts = time.time()
    seconds = int(ts)

    # Create CapBankDiscreteControlProfile message
    profile = capbank.CapBankDiscreteControlProfile()
    profile.controlMessageInfo.messageInfo.identifiedObject.mRID.value = str(uuid.uuid4())
    profile.controlMessageInfo.messageInfo.messageTimeStamp.seconds = seconds
    profile.capBankSystem.conductingEquipment.mRID = capbank_mrid

    return profile

async def publish_capbank_discrete_control(profile):
    # publish the message
    nc = await nats.connect(nats_url)
    await nc.publish(f"openfmb.capbankmodule.CapBankDiscreteControlProfile.{capbank_mrid}", profile.SerializeToString())

    # wait a bit
    await asyncio.sleep(1)

async def cbc_set_enable_autonomous_vref_adjustment():
    profile = create_discrete_control_profile()    

    # Set enable autonomous VRef adjustment
    enable_phasA_voltage_control = input("Enable phase A voltage control? (yes/no)[yes]: ").lower()

    # CapBankDiscreteControlProfile.capBankControl.capBankDiscreteControlYPSH.control.VolLmt.phsA.ctlVal
    if enable_phasA_voltage_control == 'no':
        profile.capBankControl.capBankDiscreteControlYPSH.control.VolLmt.phsA.ctlVal = False
    else:
        profile.capBankControl.capBankDiscreteControlYPSH.control.VolLmt.phsA.ctlVal = True

    # Publish the message
    await publish_capbank_discrete_control(profile)

async def main():
    await cbc_set_enable_autonomous_vref_adjustment()

if __name__ == "__main__":
    asyncio.run(main())
