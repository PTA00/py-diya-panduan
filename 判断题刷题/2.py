import random
import os
import win32api,win32con


ct=[0]*525
random.seed()
f = open("低压判断题.txt",encoding = "utf-8")
ff=f.read().split("\n")
f.close()
for i in range(50):
	print("第"+str(i+1)+"题：\n")
	n=random.randint(1,525)-1
	ss=ff[n]
	print(ss[:-1],"\n")
	re=win32api.MessageBox(0, ss[:-1], "第"+str(i+1)+"题",win32con.MB_YESNOCANCEL)
	#6是 7否 2取消
	if re==6 and ss[-1]=='√':
		ct[n]+=-1
		#win32api.MessageBox(0, ss, "第"+str(i+1)+"题",win32con.MB_OK)
	elif re==7 and ss[-1]=='×':
		ct[n]+=-1
		#win32api.MessageBox(0, ss, "第"+str(i+1)+"题",win32con.MB_OK)
	elif re==2:
		exit()
	else:
		ct[n]+=3
		win32api.MessageBox(0, ss, "第"+str(i+1)+"题",win32con.MB_OK|win32con.MB_ICONERROR)
	#os.system("pause >nul")
	print(ss[-1])#输出√或×
	#os.system("pause >nul")
	#os.system("cls")

cttxt = open("错题计数.txt",encoding = "utf-8",mode="r")
ctltemp=cttxt.read().split(",")
cttxt.close()
if ctltemp==['']:
	ctl=['0']*525
else:
	ctl=ctltemp

for i in range(525):
	temp=int(ctl[i])+ct[i]
	if temp<0:
		ctl[i]='0'
	else:
		ctl[i]=str(temp)

cttxt2 = open("错题计数.txt",encoding = "utf-8",mode="w")
cttxt2.write(",".join(ctl))
cttxt2.close()


os.system("pause >nul")


