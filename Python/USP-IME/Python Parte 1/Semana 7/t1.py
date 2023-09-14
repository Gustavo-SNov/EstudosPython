from math import sqrt
ca=co=1
while(ca<=5):
    while(co<=5):
        ca = pow(ca,ca)
        co = pow(co,co)
        print(f"h={ca}+{co}")
        co +=1
    ca +=1
    co=1
    print()