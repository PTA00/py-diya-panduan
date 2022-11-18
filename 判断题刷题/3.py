import random
import os
import win32api,win32con

ctl=[]
ct=[]
def main():
	global ctl
	global ct
	cttxt = open("错题计数.txt",encoding = "utf-8",mode="r")
	ctltemp=cttxt.read().split(",")
	cttxt.close()
	ctl=ctltemp

	ct=list(map(int, ctltemp))

	random.seed()
	f = open("低压判断题.txt",encoding = "utf-8")
	ff=f.read().split("\n")
	f.close()
	for i in range(50):
		#print(ct)
		summax=sum(ct)
		if summax==0:
			win32api.MessageBox(0, "已刷完所有错题", "消息",win32con.MB_OK)
			okexit()
		print(summax)
		print("第"+str(i+1)+"题：\n")
		sumx=random.randint(1,summax)
		sum2=0
		n=0
		for j in range(525):
			sum2+=ct[j]
			if sum2>=sumx:
				n=j
				break

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
			okexit()
			#exit()
		else:
			ct[n]+=3
			win32api.MessageBox(0, ss, "第"+str(i+1)+"题",win32con.MB_OK|win32con.MB_ICONERROR)
		#os.system("pause >nul")
		print(ss[-1])#输出√或×
		#os.system("pause >nul")
		#os.system("cls")
	okexit()


def okexit():
	global ctl
	global ct
	
	for i in range(525):
		temp=ct[i]
		if temp<0:
			ctl[i]='0'
		else:
			ctl[i]=str(temp)

	cttxt2 = open("错题计数.txt",encoding = "utf-8",mode="w")
	cttxt2.write(",".join(ctl))
	cttxt2.close()


	os.system("pause >nul")
	exit()

main()
error0000()