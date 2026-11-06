from gpiozero import LED
from time import sleep  

#North:Red,Yellow,Green
NR,NY,NG=LED(13),LED(12),LED(11)

#South
SR,SY,SG=LED(8),LED(7),LED(6)

#East
ER,EY,EG=LED(24),LED(22),LED(26)

#West
WR,WY,WG=LED(17),LED(18),LED(16)

roads=[
  (NR,NY,NG),
  (SR,SY,SG),
  (ER,EY,EG),
  (WR,WY,WG),
]
def all_red():
 for red,yellow,green in roads:
   red.on()
   yellow.off()
   green.off()
   
try:
   while True:
    for current in roads:
      #All roads red
      all_red()
      sleep(1)
      
      #current road green,others red
      red,yellow,green=current
      red.off()
      green.on()
      sleep(5)
      
      #current road yellow for 1 seconds
      green.off()
      yellow.on()
      sleep(2)
      
      #current road red again
      yellow.off()
      red.on()
      
      
      
except Keyboardinterrupt:
      pass
        
finally:
  for red,yellow,green in roads:
            red.off()
            yellow.off()
            green.off()






