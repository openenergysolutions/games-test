import os
import time
import nats
import asyncio
import uuid
import sys
sys.path.append(os.path.abspath('python-openfmb-ops-protobuf/openfmb'))
import solarmodule.solarmodule_pb2 as solar

nats_url = "nats://127.0.0.1:4222"
solar_mrid = "7e821d42-4e11-4d7f-be4a-f741f2d741e9"

running = True

async def reading():
    nc = await nats.connect(nats_url)
    global running  

    running = True  

    async def message_handler(msg):
        global running
        profile = solar.SolarReadingProfile()
        profile.ParseFromString(msg.data)
        print(f"Received solar reading: {profile}")
        running = False

    await nc.subscribe(f"openfmb.solarmodule.SolarReadingProfile.{solar_mrid}", cb=message_handler)

    while running:
        await asyncio.sleep(1)

async def status():
    nc = await nats.connect(nats_url)

    global running

    running = True

    async def message_handler(msg):
        global running
        profile = solar.SolarStatusProfile()
        profile.ParseFromString(msg.data)
        print(f"Received solar status: {profile}")
        running = False

    await nc.subscribe(f"openfmb.solarmodule.SolarStatusProfile.{solar_mrid}", cb=message_handler)

    while running:
        await asyncio.sleep(1)

async def send_curve_points():
    curve_points = []
    while True:
        try:
            x_value = float(input("Enter X value (or type 'done' to finish): "))
            y_value = float(input(f"Enter Y value corresponding to X={x_value}: "))
            curve_points.append((x_value, y_value))
        except ValueError:
            print("Invalid input. Please enter numeric values or type 'done'.")
        cont = input("Do you want to add more points? (yes/no)[yes]: ").lower()
        if cont != 'yes' and cont != '':
            break

    if curve_points:
        print("Sending the following curve points:")

        ts = time.time()
        seconds = int(ts)

        # Create SolarControlProfile message
        profile = solar.SolarControlProfile()
        profile.controlMessageInfo.messageInfo.identifiedObject.mRID.value = str(uuid.uuid4())
        profile.controlMessageInfo.messageInfo.messageTimeStamp.seconds = seconds
        profile.solarInverter.conductingEquipment.mRID = solar_mrid

        pt = solar.SolarPoint()
        pt.control.voltVarOperation.crvPts.append();

        profile.solarControl.solcarControlFSCC.SolarControlShceduleFSCH.ValDCSG.crvPts.append(pt);

        for x, y in curve_points:
            print(f"({x}, {y})")

        # publish the message
        nc = await nats.connect(nats_url)
        await nc.publish("openfmb.solarmodule.SolarControlProfile.{solar_mrid}", profile.SerializeToString())
        
        # Simulate sending the curve points
        print("Curve points sent successfully!")
    else:
        print("No curve points were added.")


async def main():
    setpoints = None
    while True:
        print("\nMenu:")
        print("1. Reading profile")
        print("2. Status profile")
        print("3. Send Curve Points")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            await reading()
        elif choice == '2':
            await status()
        elif choice == '3':
            await send_curve_points()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())
