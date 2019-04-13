import serial
import serial.tools.list_ports
from mcpi.minecraft import Minecraft
import time
print('hello')
ser=serial.Serial(port='COM3')
time.sleep(2)
ser.write("1".encode())
time.sleep(3)
ser.write("2".encode())
#mc=Minecraft.create("127.0.0.1",4711)
mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))


Bases=[[-142,-129,-177,-171,"1"]]

def house(a_x,a_y,a_z):
    global Bases    
    for z in range (10):
        for x in range (10):
            mc.setBlock(a_x+x,a_y,a_z+z,17)#地板
    mc.setBlock(a_x+5,a_y,a_z+5,20)        
    for y in range (6):
        for x in range (10):
            mc.setBlock(a_x+x,a_y+y,a_z,1)#墙壁
    for z in range (10):
        for y in range (6):
            mc.setBlock(a_x,a_y+y,a_z+z,1)#墙壁    
    for y in range (6):
        for x in range (10):
            mc.setBlock(a_x+x,a_y+y,a_z+9,1)#墙壁
    for z in range (10):
        for y in range (6):
            mc.setBlock(a_x+9,a_y+y,a_z+z,1)#墙壁        
    for z in range (10):
        for x in range (10):
            mc.setBlock(a_x+x,a_y+5,a_z+z,20)#天花板
    Base=[a_x,a_x+10,a_z,a_z+10,"1"]
    Bases.append(Base)

def opendoors():
    print("hhh open all doors hhh")
            
house(pos.x,pos.y,pos.z)
house(pos.x+20,pos.y,pos.z)
house(pos.x,pos.y,pos.z+20)
house(pos.x+20,pos.y,pos.z+20)

print(Bases)

Bases[1][4]="4"
Bases[2][4]="3"
Bases[3][4]="5"
Bases[4][4]="1"

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        print("got ON")
        opendoors()
    if 'OFF' in rs:
        print("got OFF")

    for Base in Bases:
        if pos.x>Base[0] and pos.x<Base[1] and pos.z>Base[2] and pos.z<Base[3]:
            mc.postToChat("Base[4]"+str(Base[4]))
            ser.write(Base[4].encode())
            time.sleep(1)
            mc.postToChat("send")
        else:
            mc.postToChat("outside")
