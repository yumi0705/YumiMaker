from mcpi.minecraft import Minecraft
import time

#mc=Minecraft.create("127.0.0.1",4711)
mc=Minecraft.create()


stayed_time=0
pos=mc.player.getTilePos()
mc.setBlock(pos.x,pos.y,pos.z,57)
mc.setBlock(pos.x-1,pos.y,pos.z,57)
mc.setBlock(pos.x-2,pos.y,pos.z,57)
mc.setBlock(pos.x-2,pos.y,pos.z-1,57)
mc.setBlock(pos.x-2,pos.y,pos.z-2,57)
mc.setBlock(pos.x,pos.y,pos.z-2,57)
mc.setBlock(pos.x-1,pos.y,pos.z-2,57)
mc.setBlock(pos.x,pos.y,pos.z-1,57)
mc.setBlock(pos.x-1,pos.y,pos.z-1,57)
mc.setBlock(pos.x-1,pos.y+1,pos.z-1,138)
#pos.x=-148,pos.y=4,pos.z=7
