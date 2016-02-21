import maya.cmds as cmds
import maya.mel as mel
import random
import time

random.seed(0)



def GenCity (w, h, d):
	cityGrid = [[False for x in range(w)] for z in range(d)]
	
	x = 0
	while (x < w):
		
		z = 0
		while (z < d):

			# if a city is already here or near, ignore
			if (cityGrid[x][z] or 
					(x > 1 and cityGrid[x -1][z]) or 
					(z > 1 and cityGrid[x][z - 1]) or 
					(x > 1 and z > 1 and cityGrid[x -1][z - 1])):
				z = z + 1
				continue

			dx = random.randint(3, 6)
			dy = random.randint(h/7, h)
			dz = random.randint(3, 6)

			dx = (w-x) if (x+dx > w) else dx
			dz = (d-z) if (z+dz > d) else dz

			# don't allow super narrow buildings
			if (dx < 3 or dz < 3):
				z = z + 1
				continue
			
			#mel.eval("polyCube -w (" + str(dx) + ") -h " + str(dy) + " -d " + str(dz) + ";")
			#mel.eval("move -y " + str(dy/2.0) + ";")
			mel.eval("GenBuilding("+ str(dx) + ","+ str(dy) + "," + str(dz) + ");")
			mel.eval("move -x " + str(x + dx/2.0) + " -z " + str(z + dz/2.0) + ";")

						

			for cx in range(x, min(w, x + dx)):
				for cz in range(z, min(d, z + dz)):
					cityGrid[cx][cz] = True

			

			z = z + 1

		x = x + 1



t = time.time()
GenCity(30, 25, 30)
print(time.time() - t)