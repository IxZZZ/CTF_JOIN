from pwn import *
import os
#clear = lambda: os.system('clear')
#clear()



#data = open('/mages_tower/cool_wizard_meme.png', 'rb').read()
#x = list(data)
#for i1 in range(0, 256):
#	for i2 in range(0, 256):
#		for i3 in range(0, 256):
#			tmp += bytes([i1, i2, i3])

#-----------------------------------------------------------------
sv = listen(6667)
data = sv.recv(timeout = Timeout.forever).split(b"\r\n")
print(data)
name = data[1].replace(b"NICK ", b"")
sentData = open('communication.txt', 'rb').read()
sentData = sentData.replace(b"__NAME__", name) 
sentData = sentData.split(b"#-------------------")

for i in range(0, len(sentData)):
	if sentData[i][:2] == b"\r\n":
		sentData[i] = sentData[i][2:]

file_brute = open('brute_out.txt','w')

for i in range(0, len(sentData)):
	#if i == 0:
	sv.send(sentData[i])
	# print('i = ', i)
	if i == 0:
		# print(i)
		rep = sv.recv()
		# print(rep)
		while b"Hello, I am" not in rep:
			rep = sv.recv()
			# print(rep)

	elif i == 4:
		# print(i, ' - ', sentData[i])
		rep1 = sv.recv()
		# print(rep1)
		rep2 = sv.recv()
		# print(rep2)
		rep2 = sv.recv()
		# print(rep2)
	elif i == 7:
		print(i)
		rep = sv.recv()
		print(rep)
		while b"I do believe I have slain the Wyvern" not in rep:
			rep = sv.recv()
			file_brute.write(rep.decode())
			print(rep)

	else:

		response = sv.recv()
		# print(response)
		input("Enter de tiep tuc")
	#print("\n\t\t----------------------\t\t\n")



