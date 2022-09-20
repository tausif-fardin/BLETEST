# import asyncio
# from bleak import BleakScanner, BleakClient


# async def main():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)

# asyncio.run(main())


import asyncio
from bleak import BleakScanner, BleakClient

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        # printing device list
        print(d)
        #getting the details of specific device with its address
        if (d.address) == 'E8:21:16:DE:40:03':
            print(d.address, d.rssi,d.metadata['uuids'])
            print('Found it')

asyncio.run(main())

