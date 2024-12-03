import os
import time
import nats
import asyncio
import uuid
import sys
sys.path.append(os.path.abspath('openfmb'))
import solarmodule.solarmodule_pb2 as solar
import evsemodule.evsemodule_pb2 as evse
import commonmodule.commonmodule_pb2 as common

nats_url = "nats://192.168.86.51:4222"
solar_mrid = "97e1fa97-6915-4608-8ab5-0cd05b11cd11"
evse_mrid = "7f590280-6154-4258-89e0-2babb69fbe74"

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

def create_evse_control_profile():
    ts = time.time()
    seconds = int(ts)

    # Create EVSEControlProfile message
    profile = evse.EVSEControlProfile()
    profile.controlMessageInfo.messageInfo.identifiedObject.mRID.value = str(uuid.uuid4())
    profile.controlMessageInfo.messageInfo.messageTimeStamp.seconds = seconds
    profile.evse.conductingEquipment.mRID = evse_mrid

    return profile

async def publish_evse_control_profile(profile):
    # publish the message
    nc = await nats.connect(nats_url)
    await nc.publish(f"openfmb.evsemodule.EVSEControlProfile.{evse_mrid}", profile.SerializeToString())

    # wait a bit
    await asyncio.sleep(1)

async def evse_set_max_active_power():
    profile = create_evse_control_profile()

    # Set maximum active power
    max_active_power = float(input("Enter maximum active power: "))

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.limitWOperation.wMaxSptVal = max_active_power

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_voltage_reactive_power_curve_points():
    profile = create_evse_control_profile()

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

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltVarOperation.crvPts[0].voltVal
    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())

    if curve_points:
        print("Sending the following curve points:") 

        for x, y in curve_points:
            print(f"({x}, {y})") 
            pt = crvPts.control.voltVarOperation.crvPts.add()        
              
            pt.voltVal = float(x)
            pt.varVal = float(y)  

        # Publish the message
        await publish_evse_control_profile(profile)

async def evse_set_reference_voltage():
    profile = create_evse_control_profile()

    # Set reference voltage
    reference_voltage = float(input("Enter reference voltage: "))

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltVarOperation.vVarParameter.VRef

    dese = profile.evseControl.controlDESE.add()
    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.voltVarOperation.vVarParameter.VRef = reference_voltage

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_response_time_to_ramp_up_reactive_power():
    profile = create_evse_control_profile()

    # Set response time
    response_time = int(input("Enter response time: "))

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltVarOperation.vVarParameter.OplTmmsMax.seconds

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.voltVarOperation.vVarParameter.OplTmmsMax.seconds = response_time

    # Publish the message
    await publish_evse_control_profile(profile)


async def evse_set_voltage_active_power_curve_points():
    profile = create_evse_control_profile()

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

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltWOperation.crvPts[0].voltVal

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())

    if curve_points:
        print("Sending the following curve points:")

        for x, y in curve_points:
            print(f"({x}, {y})") 
            pt = crvPts.control.voltWOperation.crvPts.add()        
              
            pt.voltVal = float(x)
            pt.wVal = float(y)  

        # Publish the message
        await publish_evse_control_profile(profile)

async def evse_set_response_time_to_ramp_up_active_power():
    profile = create_evse_control_profile()

    # Set response time
    response_time = int(input("Enter response time: "))

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltWOperation.voltWParameter.OplTmmsMax.seconds

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.voltWOperation.voltWParameter.OplTmmsMax.seconds = response_time

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_constant_reactive_power_setting():
    profile = create_evse_control_profile()

    # Set constant reactive power
    constant_reactive_power = float(input("Enter constant reactive power: "))

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.vArOperation.varParameter.varTgtSpt

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.vArOperation.varParameter.varTgtSpt = constant_reactive_power

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_constant_power_factor_setting():
    profile = create_evse_control_profile()

    # Set constant power factor
    constant_power_factor = float(input("Enter constant power factor: "))

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.pFOperation.pFParameter.pFGnTgtMxVal

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    crvPts.control.pFOperation.pFParameter.pFGnTgtMxVal = constant_power_factor

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_output_active_power_setpoint():
    profile = create_evse_control_profile()

    # Set output active power setpoint
    output_active_power_setpoint = float(input("Enter output active power setpoint: "))

    # EVSEControlProfile.evseControl.controlDESE[0].controlDEAO.controlDEEV.deevControlScheduleFSCH.ValACSG.schPts[0].scheduleParameter[0].scheduleParameterType

    dese = profile.evseControl.controlDESE.add()
    schPts = dese.controlDEAO.controlDEEV.deevControlScheduleFSCH.ValACSG.schPts.add()
    schPts.startTime.seconds = int(time.time())
    params = schPts.scheduleParameter.add()
    params.scheduleParameterType = 40 # w_net_mag
    params.value = output_active_power_setpoint 

    # Publish the message
    await publish_evse_control_profile(profile)   


async def evse_set_output_reactive_power_setpoint():
    profile = create_evse_control_profile()

    # Set output reactive power setpoint
    output_reactive_power_setpoint = float(input("Enter output reactive power setpoint: "))

    # EVSEControlProfile.evseControl.controlDESE[0].controlDEAO.controlDEEV.deevControlScheduleFSCH.ValACSG.schPts[0].scheduleParameter[0].scheduleParameterType

    dese = profile.evseControl.controlDESE.add()
    schPts = dese.controlDEAO.controlDEEV.deevControlScheduleFSCH.ValACSG.schPts.add()
    schPts.startTime.seconds = int(time.time())
    params = schPts.scheduleParameter.add()
    params.scheduleParameterType = 35 # var_net_mag
    params.value = output_reactive_power_setpoint

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_limit_active_power_enable():
    profile = create_evse_control_profile()

    # Set limit active power enable
    limit_active_power_enable = input("Enable limit active power? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.limitWOperation.maxLimParameter.modEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if limit_active_power_enable == 'no':
        crvPts.control.limitWOperation.maxLimParameter.modEna = False
    else:
        crvPts.control.limitWOperation.maxLimParameter.modEna = True

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_enable_disable_autonomous_vref_adjustment():
    profile = create_evse_control_profile()

    # Set enable/disable autonomous VRef adjustment
    enable_disable_autonomous_vref_adjustment = input("Enable/disable autonomous VRef adjustment? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltVarOperation.vVarParameter.VRefAdjEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if enable_disable_autonomous_vref_adjustment == 'no':
        crvPts.control.voltVarOperation.vVarParameter.VRefAdjEna = False
    else:
        crvPts.control.voltVarOperation.vVarParameter.VRefAdjEna = True
    
    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_enable_voltage_reactive_power_mode():
    profile = create_evse_control_profile()

    # Set enable voltage-reactive power mode
    enable_voltage_reactive_power_mode = input("Enable voltage-reactive power mode? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltVarOperation.vVarParameter.modEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if enable_voltage_reactive_power_mode == 'no':
        crvPts.control.voltVarOperation.vVarParameter.modEna = False
    else:
        crvPts.control.voltVarOperation.vVarParameter.modEna = True

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_enable_voltage_active_power_mode():
    profile = create_evse_control_profile()

    # Set enable voltage-active power mode
    enable_voltage_active_power_mode = input("Enable voltage-active power mode? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.voltWOperation.voltWParameter.modEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if enable_voltage_active_power_mode == 'no':
        crvPts.control.voltWOperation.voltWParameter.modEna = False
    else:
        crvPts.control.voltWOperation.voltWParameter.modEna = True

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_enable_constant_reactive_power_mode():
    profile = create_evse_control_profile()

    # Set enable constant reactive power mode
    enable_constant_reactive_power_mode = input("Enable constant reactive power mode? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.vArOperation.modEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if enable_constant_reactive_power_mode == 'no':
        crvPts.control.vArOperation.modEna = False
    else:
        crvPts.control.vArOperation.modEna = True

    # Publish the message
    await publish_evse_control_profile(profile)

async def evse_set_enable_constant_power_factor_mode():
    profile = create_evse_control_profile()

    # Set enable constant power factor mode
    enable_constant_power_factor_mode = input("Enable constant power factor mode? (yes/no)[yes]: ").lower()

    # EVSEControlProfile.evseControl.controlDESE[0].deseControlScheduleFSCH.ValDCSG.crvPts[0].control.pFOperation.pFParameter.modEna

    dese = profile.evseControl.controlDESE.add()

    crvPts = dese.deseControlScheduleFSCH.ValDCSG.crvPts.add()
    crvPts.startTime.seconds = int(time.time())
    if enable_constant_power_factor_mode == 'no':
        crvPts.control.pFOperation.pFParameter.modEna = False
    else:
        crvPts.control.pFOperation.pFParameter.modEna = True

    # Publish the message
    await publish_evse_control_profile(profile)

async def main():
    setpoints = None
    while True:
        print("\nMenu:")
        print("1. Reading profile")
        print("2. Status profile")
        print("3. Send Curve Points")
        print("4. Send Forecast")
        print("5. Reading Forecast")
        # begin EVSE
        print("6. Maximum active power setting")
        print("7. Voltage-reactive power curve points")
        print("8. Reference voltage (VRef)")
        print("9. Response time: Time to ramp up to 90% of the new reactive power")
        print("10. Voltage-active power curve points")
        print("11. Response time: Time to ramp up to 90% of the new active power")
        print("12. Constant reactive power setting (reactive power priority)")
        print("13. Constant power factor setting")
        print("14. Output active power setpoint")
        print("15. Output reactive power setpoint")
        print("16. Limit active power enable")
        print("17. Enable/disable autonomous VRef adjustment")
        print("18. Enable voltage-reactive power mode")
        print("19. Enable voltage-active power mode")
        print("20. Enable constant reactive power mode")
        print("21. Enable constant power factor mode")
        print("100. Exit")
        choice = input("Enter your choice (1-21) or 100 to exit: ")

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
        # begin EVSE
        elif choice == '6':
            await evse_set_max_active_power()
        elif choice == '7':
            await evse_set_voltage_reactive_power_curve_points()
        elif choice == '8':
            await evse_set_reference_voltage()
        elif choice == '9':
            await evse_set_response_time_to_ramp_up_reactive_power()
        elif choice == '10':
            await evse_set_voltage_active_power_curve_points()
        elif choice == '11':
            await evse_set_response_time_to_ramp_up_active_power()
        elif choice == '12':
            await evse_set_constant_reactive_power_setting()
        elif choice == '13':
            await evse_set_constant_power_factor_setting()
        elif choice == '14':
            await evse_set_output_active_power_setpoint()
        elif choice == '15':
            await evse_set_output_reactive_power_setpoint()
        elif choice == '16':
            await evse_set_limit_active_power_enable()
        elif choice == '17':
            await evse_set_enable_disable_autonomous_vref_adjustment()
        elif choice == '18':
            await evse_set_enable_voltage_reactive_power_mode()
        elif choice == '19':
            await evse_set_enable_voltage_active_power_mode()
        elif choice == '20':
            await evse_set_enable_constant_reactive_power_mode()
        elif choice == '21':
            await evse_set_enable_constant_power_factor_mode()
        # Exiting
        elif choice == '100':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())
