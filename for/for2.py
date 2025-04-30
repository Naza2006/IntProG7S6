#La tabla de multiplicar de un numero culaquiera
import os
def obtener_tabla(num):
    for i in range(9999):
        print(f"{i} * {num} = {i * num }")
        

def main():
    os.system("cls || clear")
    number = int(input("Dime un #: "))
    obtener_tabla(number)
    
main()
    