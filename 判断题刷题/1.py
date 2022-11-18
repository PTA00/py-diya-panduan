import random
import os


random.seed()
f = open("低压判断题.txt",encoding = "utf-8")
ff=f.read().split("\n")
f.close()
for i in range(50):
	print("第",i+1,"题：\n")
	n=random.randint(1,525)
	ss=ff[n-1]
	print(ss[:-1],"\n")
	os.system("pause >nul")
	print(ss[-1])
	os.system("pause >nul")
	os.system("cls")




