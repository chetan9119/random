x = 152
y = 354

print(x==y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x!=y)

if x >= y:
    print("X is larger")
elif x <= y :
    print("Y is larger")
else:
    print("None is larger")
    
    
no1 = 4875555555
no2 = 7451
no3 = 84777755




if no1 > no2 and no1 > no3:
    print(no1)
elif no2 > no1 and no2 > no3:
    print(no2)
elif no3 > no1 and no3 > no2:
    print(no3)
else:
    # print(no3)
    print("Alog got failed !")

if no1 > no2:
    if no1 > no3:
        print(no1)
elif no2 > no1:
    if no2 > no3:
        print(no2)
else: 
    print(no3)
    
x = 25
y = 55
if x > y: print(x)
elif y > x : print(y)
else: print("X == Y")


a = 2
b = 330
print(a) if a > b else print(b)


a = 330
b = 331
print(a) if a > b else print("None") if a == b else print(b)

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
else:
    print("You are wrong")
    
if a > b and a > c:
  print("At least one of the conditions is True")
else:
    print("You are wrong")
    
    
if not a > b or not a > c:
  print("At least one of the conditions is True")
else:
    print("You are wrong")
    
if not a > b and not a > c:
  print("At least one of the conditions is True")
else:
    print("You are wrong")
    
    
numb1 = 550
numb2 = 150

if numb2 > numb1:
    pass
elif numb1 > numb2:
    pass
