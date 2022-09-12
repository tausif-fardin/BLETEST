import asyncio

#Connect to a Bluetooth device and read its model number:
from bleak import BleakClient

address = "E8:21:16:DE:40:03"
MODEL_NBR_UUID = "50765cb7-d9ea-4e21-99a4-fa879613a492"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))