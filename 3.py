
from mcpi.minecraft import Minecraft
import time
print('hallo')
#mc=Minecraft.create("127.0.0.1",4711)
mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))
def house(a_x,a_y,a_z):
     
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
house(pos.x,pos.y,pos.z)



