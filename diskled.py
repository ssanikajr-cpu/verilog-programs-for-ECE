import psutil
from gpiozero import LED

red = LED(17)
yellow = LED(27)
green = LED(22)

print("LED Control and Disk Partition Monitoring")

while True:

    colour = input("Enter LED colour (red/yellow/green/exit): ").lower()

    # Turn OFF all LEDs
    red.off()
    yellow.off()
    green.off()

    if colour == "red":
        red.on()
        print("Red LED is ON")

    elif colour == "yellow":
        yellow.on()
        print("Yellow LED is ON")

    elif colour == "green":
        green.on()
        print("Green LED is ON")

    elif colour == "exit":
        print("Program stopped")
        break

    else:
        print("Invalid colour! Try again.")
        continue

    # Display disk partitions
    print("\nDisk Partition Information:")

    partitions = psutil.disk_partitions()

    for partition in partitions:
        print("Device:", partition.device)
        print("Mount Point:", partition.mountpoint)
        print("File System:", partition.fstype)

        try:
            usage = psutil.disk_usage(partition.mountpoint)

            print("Total Storage:", round(usage.total / (1024**3), 2), "GB")
            print("Used Storage:", round(usage.used / (1024**3), 2), "GB")
            print("Free Storage:", round(usage.free / (1024**3), 2), "GB")
            print("Disk Usage:", usage.percent, "%")

        except PermissionError:
            print("Permission denied")

        print("--------------------------")

red.close()
yellow.close()
green.close()
