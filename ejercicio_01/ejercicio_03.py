# numero a evaluar
numero = 8

# usamos el operador % (modulo) para obtener el residuo de dividir entre 2 
es_par = (numero % 2 == 0)

if es_par:
    print(f"El numero{numero} es PAR.")
else:
    print(f"El numero{numero} es IMPAR.");