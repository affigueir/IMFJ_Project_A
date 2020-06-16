def Main():
	
	print("What problem do you want to solve?")
	print("1. Floatation")
	print("2. Springs")
	
	choice = int(input())

	if (choice == 1):
		Floatation()
	
	elif (choice == 2):
		Springs()
		

def Floatation():
	
	gravity = 9.81
	fluid_density = 1
	object_density = 10
	object_volume = 5

	object_mass = object_density * object_volume

	volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))

	object_side = object_volume**(1 / 3)

	height_under = volume_under / (object_side ** 2)

	while (True):
		
		print("Current Object Properties: 'mass' = {} , 'density' = {} , 'volume' = {}".format(object_mass, object_density, object_volume))
		print("Current 'fluid density' has a value of {} and 'gravity' is set to {}".format(fluid_density, gravity))
		print("The object would float at {} meters".format(height_under))
		print("To change any value, write: 'set' 'property' 'value' ")
		print("To exit the program type 'exit'")

		change_value = input()

		if ("exit" in change_value):
			break

		elif ("set gravity" in change_value):
			change_value = change_value.replace("set gravity", "")
			gravity = float(change_value)
			volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))
			height_under = volume_under / (object_side ** 2)

		elif ("set fluid density" in change_value):
			change_value = change_value.replace("set fluid density", "")
			fluid_density = float(change_value)
			volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))
			height_under = volume_under / (object_side ** 2)


		elif ("set density" in change_value):
			change_value = change_value.replace("set density", "")
			object_density = float(change_value)
			object_mass = object_density * object_volume
			volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))
			height_under = volume_under / (object_side ** 2)

		elif ("set volume" in change_value):
			change_value = change_value.replace("set volume", "")
			object_volume = float(change_value)
			object_mass = object_density * object_volume
			volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))
			object_side = object_volume ** (1 / 3)
			height_under = volume_under / (object_side ** 2)
		
		elif("set mass" in change_value):
			change_value = change_value.replace("set mass", "")
			object_mass = float(change_value)
			object_density = object_mass / object_volume
			volume_under = ((-gravity) * object_mass) / (fluid_density * (-gravity))
			height_under = volume_under / (object_side ** 2)


def Springs():
	gravity = 9.81
	object_mass = 1
	base_length = 10
	spring_constant = 0.5

	while(True):
		full_length = ((-gravity) * object_mass) / (-spring_constant) + base_length

		print("'object mass' is {}, 'gravity' is {}".format(object_mass, gravity))
		print("Spring's 'base length' is {} and 'spring constant' is {}".format(base_length, spring_constant))
		print("Spring would stretch to {} meters".format(full_length))
		print("To change any value, write: 'set' 'property' 'value' ")
		print("To exit the program type 'exit'")

		change_value = input()

		if ("exit" in change_value):
			break

		elif ("set gravity" in change_value):
			change_value = change_value.replace("set gravity", "")
			gravity = float(change_value)

		elif ("set mass" in change_value):
			change_value = change_value.replace("set mass", "")
			object_mass = float(change_value)

		elif ("set base length" in change_value):
			change_value = change_value.replace("set base length", "")
			base_length = float(change_value)

		elif ("set spring constant" in change_value):
			change_value = change_value.replace("set spring constant", "")
			spring_constant = float(change_value)


Main()