import RPi.GPIO as GPIO
import time
import requests
# ---------------- GPIO Configuration ----------------
TRIG = 15
ECHO = 14
# ---------------- ThingSpeak Configuration ----------------
WRITE_API_KEY = "D2XG6XPL8635BTUA"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)

def measure_distance():
    # Send a 10-microsecond trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo pulse to start
    start_wait = time.monotonic()
    while GPIO.input(ECHO) == 0:
        if time.monotonic() - start_wait > 0.03:
            return None

    pulse_start = time.monotonic()

    # Wait for the echo pulse to end
    while GPIO.input(ECHO) == 1:
        if time.monotonic() - pulse_start > 0.03:
            return None

    pulse_end = time.monotonic()

    # Distance = (time × speed of sound) / 2
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 34300 / 2

    return round(distance, 2)

def upload_to_thingspeak(distance):
    params = {
        "api_key": WRITE_API_KEY,
        "field1": distance
    }

    try:
        response = requests.get(
            THINGSPEAK_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()

        # ThingSpeak returns a nonzero entry ID on success
        entry_id = response.text.strip()

        if entry_id.isdigit() and int(entry_id) > 0:
            print("Uploaded successfully. Entry ID:", entry_id)
        else:
            print("Upload failed. Check the API key and channel.")

    except requests.RequestException as error:
        print("ThingSpeak connection error:", error)


try:
    print("Ultrasonic Distance Monitoring Started")

    while True:
        distance = measure_distance()

        if distance is not None and 2 <= distance <= 400:
            print("Distance: {:.2f} cm".format(distance))
            upload_to_thingspeak(distance)
        else:
            print("Invalid reading or object out of range")

        # ThingSpeak free channels require at least
        # 15 seconds between successive updates
        time.sleep(16)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

finally:
    GPIO.cleanup()
