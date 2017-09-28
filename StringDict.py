import os

fo=open("F:\\dict.txt","w")

for j in range(0,26):
		a=97
		for x in range(0,26):
			if(i==1):
				fo.write(chr(a)+chr(a+j)+chr(a+j)+chr(a+j)+chr(a+x)+"\n")
			if(i==2):
				fo.write(chr(a)+chr(a+j)+chr(a+j)+chr(a+x)+chr(a+j)+"\n")
			if(i==3):
				fo.write(chr(a)+chr(a+j)+chr(a+x)+chr(a+j)+chr(a+j)+"\n")
			if(i==4):
				fo.write(chr(a)+chr(a+x)+chr(a+j)+chr(a+j)+chr(a+j)+"\n")
			
		
fo.close()