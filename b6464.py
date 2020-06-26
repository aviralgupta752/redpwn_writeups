f=open("cipher.txt").read()
while(True):
	try:
		f=f.decode('base64')
	except:
		print f
		break
 
#flag{l00ks_l1ke_a_l0t_of_64s}
