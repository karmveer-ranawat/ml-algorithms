x=int(input("enter the value of X:"))
y=int(input("enter the value of Y:"))
while True:
rno=int(input("enter the rule number:"))
#fill jar 1
if rno==1:
if x<4: x=4
#fill jar 2
if rno==2:
if y<3: y=3
#empty jar 1
if rno==5:
if x>0: x=0
#empty jar 2
if rno==6:
if y<O: y=0
#pour water from jar2 to fill jar1
if rno==7:
if xty>=4 and y>0: x,y=4,y-(4-x)
if rno==8:
if x+y>=3 and y>0: x,y=x-(3-y),3
#pour water from jar2 to jar1
if rno==9:
if xty<=4 and y>0: x,y=x+y,0
#pour water from jar1 to fill jar2
if rno==10:
if x+y<=3 and y>0: x,y=2,(x+y)
print("the value of x:",x)
print("the value of y:",y)
if(x==2):
print("this is the goal state")
break






enter the value of X:0
enter the value of Y:0
enter the rule number:2
the value of x: 0
the value of y: 3
enter the rule number:9
the value of x: 3
the value of y: 0
enter the rule number:2
the value of x: 3
the value of y: 3
enter the rule number:7
the value of x: 4
the value of y: 2
enter the rule number:5
the value of x: 0
the value of y: 2
enter the rule number:9
the value of x: 2
the value of y: 0
this is the goalstate
