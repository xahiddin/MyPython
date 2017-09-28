import threading, time

def music(func):
	for i in range(3):
		print ("I was Listening to music %s %s" %(func,time.time()))
		time.sleep(2)

def movie(func):
	for i in range(3):
		print("I was at the movie %s %s"%(func,time.time()))
		time.sleep(2)

threads=[]
t1 = threading.Thread(target=music,args=("alo",))
threads.append(t1)
t2 = threading.Thread(target=music,args=("alo",))
threads.append(t2)

if __name__=='__main__':
	for t in threads:
		t.start()
	t.join()
	print("all over%s" %time.time())