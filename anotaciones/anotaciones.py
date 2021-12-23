a:str = 'hola mundo'
b:int = 30
c:float = 3.14
d: bool = True
valor3 : int
print(a)
print(b)
print(c)
print(d)

def suma(num1:int, num2:int) -> int :
    return num1 + num2
valor3 = input("Ingrese numero : ")
print(suma(10, 20))