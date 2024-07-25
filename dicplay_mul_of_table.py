#Python Program to Display the multiplication Table


num = 5
seq = 5

def print_mul(num,seq):
    
    for j in range(1, num+1):
        for i in range(1, seq+1):
            print(f"{str(j)} * {str(i)} = {j*i}")
        
        print("\n\n")

print_mul(num,seq)
