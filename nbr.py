N = int(input("entrer un nombre : "))
D = 0
for i in range(1,N + 1):
    if N % i == 0 :
        D = D + 1
    
if D == 2 :
    print("premier")
else:
    print("non premier")
    