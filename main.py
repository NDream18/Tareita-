#nombre: Natalia Milla/ Curso: 4°D

n = (int(input("Por favor, ingrese un numero, solo números enteros: ")))
m = int(input("¿Cuántos multiplos?: "))
  
número = n  #numero entero a multiplicar
desde = m  #desde que numero desé que multiplique

for f in range (1,m+1):
  print(f'{número} x {f} = {número * f}')