from gpiozero import LED

led_red=LED(17)
led_amber=LED(27)
led_green=LED(22 )

def turn_on_only(target_led):
      led_red.off()
      led_amber.off()
      led_green.off()
      
      
while True:
      choice=input("which LED to turn on?(red/amber/greenoff):").strip().lower()
       
      if choice=="red":
             turn_on_only(led_red)
             print("Red LED ON,others OFF")
      elif choice=="amber":
            turn_on_only(led_amber)
            print("Amber LED ON,others OFF")
      elif choice=="green":
            turn_on_only(led_green)
            print("Green LED ON,others OFF")
      elif choice=="off":
            led_red.off()
            led_amber.off()
            led_green.off()
            print("All LEDs OFF")
      else:
            print("Invalid choice! choose red,amber,green, or off.")
      
            
             
      
            
      
