import asyncio
from bleak import BleakScanner

def detection_callback(device, advertisement_data):
    print(device.address, "RSSI:", device.rssi, advertisement_data)

async def main():
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(5.0)
    await scanner.stop()

    for d in scanner.discovered_devices:
        print(d)
        if (d.address) == 'E8:21:16:DE:40:03':
            print(d.address, d.rssi,d.metadata['uuids'])
            print('Found it')

asyncio.run(main())