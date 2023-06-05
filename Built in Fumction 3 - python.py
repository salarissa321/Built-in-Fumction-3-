


#---------------------------------------
#----- Bult in Function 3 -----
#--------------------------------------
# abs()
# pow()
# min()
# max()
# slice()
#--------------------------------------------


# abs()

print(abs(100)) # 100
print(abs(-100)) # 100
print(abs(10.19)) # 10.19
print(abs(-10.19)) # 10.19

print("-" * 50) # --------------------------------------------------

# pow(base , exp , mod) => power

print(pow(2 , 5)) # 2 * 2 * 2 * 2 * 2 = 32
print(pow(2 , 5 , 10)) # ( 2 * 2 * 2 * 2 * 2) / 10 = 2


print("-" * 50) # --------------------------------------------------

# min(Item , item , item or iterator)

myNumber = (1,20, -50, -100 , 100)
print(min(myNumber)) # -100
print(min(1,20,30,10,-50)) # -50
print(min("A" , "X" , "Z" , "Salar")) # A
print(min( "X" , "Z" , "Salar")) # Salar


print("-" * 50) # --------------------------------------------------


# max(Item , item , item or iterator)

myNumber = (1,20, -50, -100 , 100) 
print(max(myNumber)) # 100
print(max(1,20,30,10,-50)) # 30
print(max("A" , "X" , "Z" , "Salar")) # z
print(max( "X" , "Z" , "Salar")) # z


print("-" * 50) # --------------------------------------------------

# slice(Start , End , Step)

a = ["A" , "B" , "C" , "D" , "E" , "F"]

print(a[:5]) # ['A', 'B', 'C', 'D', 'E']
print(a[slice(5)]) # ['A', 'B', 'C', 'D', 'E']
print(a[slice(2,5)]) # ['C', 'D', 'E']






