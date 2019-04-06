from mcpi.minecraft import Minecraft
import time

#mc=Minecraft.create("127.0.0.1",4711)
mc=Minecraft.create()
pos=mc.player.getTilePos()
for z in range (100):
    for x in range (100):
        for y in range (100): 
            mc.setBlock(pos.x+x,pos.y+y,pos.z+z,46)#地板
