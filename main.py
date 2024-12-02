import os
import time
import nats
import asyncio
import uuid
import sys
sys.path.append(os.path.abspath('python-openfmb-ops-protobuf/openfmb'))
import solarmodule.solarmodule_pb2 as solar
import commonmodule.commonmodule_pb2 as common

nats_url = "nats://client:pzwa3prf@192.168.86.39:4222"
solar_mrid = "97e1fa97-6915-4608-8ab5-0cd05b11cd11"

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
 
        pt = solar.SolarCurvePoint()
        pt.startTime.seconds = seconds + 1
        curves = pt.control.voltVarOperation.crvPts
        

        for x, y in curve_points:
            print(f"({x}, {y})")            
            point = common.SchedulePoint()
            point.startTime.seconds = seconds

            # power
            param = common.ENG_ScheduleParameter()
            param.value = float(x)
            param.scheduleParameterType = 15 # phv_net_mag
            point.scheduleParameter.append(param)

            param2 = common.ENG_ScheduleParameter()
            param2.value = float(y)
            param2.scheduleParameterType = 35 # var_net_mag
            point.scheduleParameter.append(param2)

            profile.solarControl.solarControlFSCC.controlFSCC.controlScheduleFSCH.ValACSG.schPts.append(point) 

        # publish the message
        nc = await nats.connect(nats_url)
        await nc.publish(f"openfmb.solarmodule.SolarControlProfile.{solar_mrid}", profile.SerializeToString())

        # wait a bit
        await asyncio.sleep(1)
        
        # Simulate sending the curve points
        print("Curve points sent successfully!")
    else:
        print("No curve points were added.")

async def send_forecast():
    ts = time.time()
    seconds = int(ts)
    
    # Create SolarControlProfile message
    profile = solar.SolarControlProfile()
    profile.controlMessageInfo.messageInfo.identifiedObject.mRID.value = str(uuid.uuid4())
    profile.controlMessageInfo.messageInfo.messageTimeStamp.seconds = seconds
    profile.solarInverter.conductingEquipment.mRID = solar_mrid

    # Create SolarForecast using a list of SchedulePoint(s)
    # some random forecast points
    for i in range(1, 5):
        point = common.SchedulePoint()
        point.startTime.seconds = seconds + i

        # power
        param = common.ENG_ScheduleParameter()
        param.value = i * 100
        param.scheduleParameterType = 40 # w_net_mag
        point.scheduleParameter.append(param)

        # add more parameters if needed

        profile.solarControl.solarControlFSCC.controlFSCC.controlScheduleFSCH.ValACSG.schPts.append(point)

    # publish the message
    nc = await nats.connect(nats_url)
    await nc.publish(f"openfmb.solarmodule.SolarControlProfile.{solar_mrid}", profile.SerializeToString())

    # wait a bit
    await asyncio.sleep(1)

    # Simulate sending the forecast
    print("Forecast sent successfully!")

async def reading_forecast():
    nc = await nats.connect(nats_url)
    global running  

    running = True  

    async def message_handler2(msg):
        global running
        profile = solar.SolarControlProfile()
        profile.ParseFromString(msg.data)
        print(f"Received solar control: {profile}")
        running = False

    await nc.subscribe(f"openfmb.solarmodule.SolarControlProfile.{solar_mrid}", cb=message_handler2)

    while running:
        await asyncio.sleep(1)

async def main():
    setpoints = None
    while True:
        print("\nMenu:")
        print("1. Reading profile")
        print("2. Status profile")
        print("3. Send Curve Points")
        print("4. Send Forecast")
        print("5. Reading Forecast")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            await reading()
        elif choice == '2':
            await status()
        elif choice == '3':
            await send_curve_points()
        elif choice == '4':
            await send_forecast()
        elif choice == '5':
            await reading_forecast()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())
