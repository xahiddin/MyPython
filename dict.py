fo = open("E:\\6n1alpha.txt","w")
zimu=["a","b","c","d","E","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,1000000):
	for a in zimu:
		if i<10:
			fo.write("00000%s%s\n"% (i,a))
		if i<100 and i>10:
			fo.write("0000%s%s\n"% (i,a))
		if i<1000 and i>100:
			fo.write("000%s%s\n"% (i,a))
		if  i<10000 and i>1000:
			fo.write("00%s%s\n"% (i,a))
		if  i<100000 and i>10000:
			fo.write("0%s%s\n"% (i,a))
		if  i>100000:
			fo.write("%s%s\n"% (i,a))
			
fo.close()