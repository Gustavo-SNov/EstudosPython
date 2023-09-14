def vogal(c):
    x = c.lower()
    if(x == 'a' or x=='e' or x=='i' or x=='o' or x == 'u'):
        return True
    else:
        return False
    
c = input("Digite um caractere:")
print(vogal(c))