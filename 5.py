from mcpi.minecraft import Minecraft
import time
print('hallo')
#mc=Minecraft.create("127.0.0.1",4711)
mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("x"+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))
for x in range (10):
    for z in range (10):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,1)

while True:
    time.sleep(1)
    pos1=mc.player.getTilePos()
    mc.postToChat("x"+str(pos1.x)+"y="+str(pos1.y)+"z="+str(pos1.z))
    if pos.x+9>pos1.x and pos1.x>pos.x and pos.z+9>pos1.z and pos1.z>pos.z:
        mc.postToChat("welcome home")
        
