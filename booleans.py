print(100>50)
print(100<50)
print(100==50) # comparison operator '=='

if 100<50:
    print("Yes")
elif 100 > 50:
    print("Another if condition works as its True")
elif 100 == 50:
    print("Both are equal")
else:
    print("No")



num1 = 550
num2 = 500
print("This is first condition")
print(num1>num2)
if num1 > num2:
    print("num1 is greater than num2")
elif num1 == num2:
    print("Both are equal")
else:
    print("num2 is greater than num1")
print("This is second condition")
print(num1<num2)   
if num1 < num2:
    print(num2)
else:
    print(num1)

a = True
b = False    
print(bool(a))
print(bool(b))

a = ""
b = "y"
print(bool(a))
print(bool(b))

a = 0
b = 1
print(bool(a))
print(bool(b))

# These all are false conditions
print("All false conditions !")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# These are all true conditions
print("All true conditions !")
print(bool(True))
print(bool('Null'))
print(bool(100))
print(bool("subhash"))
print(bool(("pranjal",)))
print(bool(["shivangi"]))
print(bool({"chetan":1}))
print(bool({"chetan","bhopal"}))

print(bool((None,)))
print(bool([None]))
print(bool({None:1}))
print(bool({None}))
print(bool({-1}))
