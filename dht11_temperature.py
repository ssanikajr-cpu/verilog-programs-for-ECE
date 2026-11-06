import time
import time
import board
import adafruit_dht

# Initialize DHT11 sensor on GPIO4
dht_device = adafruit_dht.DHT11(board.D4,use_pulseio=False)

print("DHT11 Temperature Monitoring")
print("----------------------------")

while True:
    try:
        # Read temperature
        temperature = dht_device.temperature

        # Display temperature
        print("Temperature: {:.1f} °C".format(temperature))

    except RuntimeError as error:
        print("Reading error:", error)

    time.sleep(2)
