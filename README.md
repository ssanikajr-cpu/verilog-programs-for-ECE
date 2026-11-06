# ECE Verilog & Python Programs

This repository contains Python scripts for hardware interface projects and laboratory experiments, including ultrasonic distance sensing, traffic light control, LED operations, and file handling.

---

## 📁 Repository Files

* **`ultrasonic_sensor.py`**: Interface code for the HC-SR04 ultrasonic distance sensor.
* **`dht11_temperature.py`**: Reads temperature and humidity data.
* **`traffic.py`**: Logic for traffic light control sequence.
* **`led.py`** & **`3 led.py`**: LED output control modules.
* **`disk.py`** & **`diskled.py`**: Storage log monitoring and LED indicators.
* **`file_py.py`**, **`file_read.py`**, **`file_append.py`**, **`txtfile.py`**: File I/O management scripts.

---

## 📡 Ultrasonic Sensor (HC-SR04)

### Distance Formula
$$\text{Distance} = \frac{\text{Speed of Sound (343 m/s)} \times \text{Time Elapsed}}{2}$$

### Pin Connections
* **VCC:** 5V DC Power
* **Trig:** Trigger Input (10µs pulse to start measurement)
* **Echo:** Signal Output (Pulse width proportional to distance)
* **GND:** Ground

---

## 🚀 Execution

Run any script directly using Python 3:

```bash
python ultrasonic_sensor.py
