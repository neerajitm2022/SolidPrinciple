#Python Program to Print all Prime Numbers in an Interval

num = 14
count = 0
is_prime = True
for i in range(2,num):
    if num % i == 0:
        is_prime = False
        break
    

if is_prime:
    print(f"Number id prime")
else:
    print("Number is not Prime")