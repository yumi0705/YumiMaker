import serial
import serial.tools.list_ports
from mcpi.minecraft import Minecraft
import time

ser=serial.Serial(port='COM3')
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>-142 and pos.x<-129 and pos.z>-177 and pos.z<-171:
        mc.postToChat("welcome home")
        ser.write("1".encode())
        time.sleep(1)
        stayed_time=stayed_time+1
    if pos.x==-36 and pos.y==66 and pos.z==14:
        mc.postToChat("welcome home")
        ser.write("3".encode())
        time.sleep(1)
        stayed_time=stayed_time+1
    if pos.x==-53 and pos.y==-8 and pos.z==-26:
        mc.postToChat("welcome home")
        ser.write("4".encode())
        time.sleep(1)
        stayed_time=stayed_time+1
    if pos.x==-215 and pos.y==118 and pos.z==-101:
        mc.postToChat("welcome home")
        ser.write("5".encode())
        time.sleep(1)
        stayed_time=stayed_time+1

       
    else:
        stayed_time=0
        ser.write("2".encode())
        time.sleep(1)
     
