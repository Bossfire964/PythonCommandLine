import sys
import os
import arguments

commandname = []
commandarguements = []

commandwriting = []



def delete(item):
	try:
		value = commandname.index(item)
		temp = commandname
		temp.pop(value)
		temp2 = commandarguements
		temp2.pop(value)
		value1 = ','.join(commandname) + "," + "NULL"
		value2 = ','.join(commandarguements)

		f = open("contents.csv", "w")
		f.write(value1)
		f.write("\n")
		f.write(value2)
		f.close()
		os.remove(item + ".py")
		print("Deleted %s from command list" % (item))
	except Exception as e:
		print("Error: Command does not exist")

def updatevalues():
	global commandname
	global commandarguements
	for i in commandname:
		commandname.pop(commandname.index(i))
	for i in commandarguements:
		commandarguements.pop(commandarguements.index(i))
	f = open("contents.csv", "r")
	contents = f.readlines()
	temp = contents[0].split(',')
	temp.pop()
	value1 = temp
	value2 = contents[1].split(',')
	commandname = value1
	commandarguements = value2
	if len(commandname) != len(commandarguements):
		commandarguements.pop()


def newvalue(name, arg):
	f = open("contents.csv", "r")
	contents = f.readlines()
	temp = contents[0].split(',')
	temp.pop()
	value1 = ','.join(temp)

	value2 = contents[1]

	value1 = value1 + "," + name + "," + "NULL"
	value2 = value2 + "," + arg

	f.close()
	f = open("contents.csv", "w")
	f.write(value1)
	f.write("\n")
	f.write(value2)
	f.close()



def decode(currentinput):
	if lineinput == "/e":
		sys.exit()
	
	if currentinput.split()[0] == "fd":
		try:
			commandname.index(currentinput.split()[1])
			if commandarguements[commandname.index(currentinput.split()[1])] == str(len(currentinput.split()) - 2):
				if commandarguements[commandname.index(currentinput.split()[1])] != "0":
					for i in range(len(arguments.args)):
							arguments.args.pop()
					for i in range(int(commandarguements[commandname.index(currentinput.split()[1])])):
						arguments.args.append(currentinput.split()[i + 2])
				exec(open(currentinput.split()[1] + ".py").read())
			else :
				print("Error: This needs %s arguments not %s" % (commandarguements[commandname.index(currentinput.split()[1])], len(currentinput.split()) - 2))
		except Exception as e:
			print("Error: That is not a current command")
	if currentinput.split()[0] == "new":
		if len(currentinput.split()) == 3:
			i = 0
			while (True):
				i += 1
				writeinput = input("Line %d>> " % (i))
				if writeinput == "/e":
					break
				else:
					commandwriting.append(writeinput)
			f = open(currentinput.split()[1] + ".py","w+")
			for i in range(len(commandwriting)):
				f.write(commandwriting[i])
				f.write("\r")
			f.close()
			newvalue(currentinput.split()[1], currentinput.split()[2])
			updatevalues()
			

		else:
			print("Error: You need 2 arguments")
	if currentinput.split()[0] == "del":
		delete(currentinput.split()[1])

while (True):
	updatevalues()
	lineinput = input("cmd>> ")
	decode(lineinput)




	
