a = eval(input("Height(in m) = "))
b = eval(input("Weight(in kg)= "))

c = b/(a**2)
print('Your BMI is',c) 
if c <= 25:
    print('You are under weight')

elif 25 < c <= 35:
    print('You are normal')

else:
    print('You are over weight')
