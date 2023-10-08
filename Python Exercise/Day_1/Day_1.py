'''
a = 3
if a > 0:
    print(a , 'is positive number')
else:
    print(a, 'is negative')
'''
# a = input("Enter a positive number")
# a = int(a)

# number = 1

# while number <= 100:
#     print(number)
#     number = number + 1


# for number in range(1,):
#     print(number)

energy_consumed = int(input("Enter e. consumption:"))

if energy_consumed <= 20:
    base = 50
    total = base + energy_consumed * 4
elif energy_consumed>20 and energy_consumed<=30:
    base = 75
    total= base + 20*4 + (energy_consumed - 20)*6.5 



