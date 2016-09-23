x={'a':'aaa','b':'bbb','c':12}
print(x['a'])
print(x['b'])
print(x['c'])
for key in x:
    print("key is %s and value is %s"%(key,x[key]))



s=input("输入你的中文名，按回车键继续");
print("你的名字是："+s)
l=len(s)
print("你中文名字的长度是："+str(l))
