

#（1） 普通推导式
varset = {1,2,3,4}
newset = {i << 1 for i in varset}

#(2) 带有条件表达式的推导式

newset1 = {i << 1 for i in varset if i%2==0}

#(3) 多循环的集合推导式

vars1 = {1,2,3}
vars2 = {4,5,6}

newset2 = {i+j for i in vars1 for j in vars2}
print(newset2)

#(4) 带条件表达式的多信号灯集合推导式
