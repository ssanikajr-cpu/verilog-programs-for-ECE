from gpiozero import LED

led_red=LED(20)

while True:
    s=input()
    if s=="off":
        led_red.off()
        print("LED OFF")
    elif s=="on":
        led_red.on()
        print("LED ON")
    
    else:
        print("invalid command")
