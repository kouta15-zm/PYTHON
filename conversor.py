Menu=""" 

 ██████  ██████  ███    ██ ██    ██ ███████ ██████  ███████  ██████  ██████      ██████  ███████     ███    ███  ██████  ███    ██ ███████ ██████   █████  ███████     
██      ██    ██ ████   ██ ██    ██ ██      ██   ██ ██      ██    ██ ██   ██     ██   ██ ██          ████  ████ ██    ██ ████   ██ ██      ██   ██ ██   ██ ██          
██      ██    ██ ██ ██  ██ ██    ██ █████   ██████  ███████ ██    ██ ██████      ██   ██ █████       ██ ████ ██ ██    ██ ██ ██  ██ █████   ██   ██ ███████ ███████     
██      ██    ██ ██  ██ ██  ██  ██  ██      ██   ██      ██ ██    ██ ██   ██     ██   ██ ██          ██  ██  ██ ██    ██ ██  ██ ██ ██      ██   ██ ██   ██      ██     
 ██████  ██████  ██   ████   ████   ███████ ██   ██ ███████  ██████  ██   ██     ██████  ███████     ██      ██  ██████  ██   ████ ███████ ██████  ██   ██ ███████     
                                                                                                                                                                       
                                                                                                                                                                       


1. Peso chileno
2. Peso argentino 
3. Euro
4. Yen

Elige una divisa: """
opcion = int(input(Menu))

if opcion == 1:
    pesos = input("¿cuantos pesos chilenos tienes ?: ")
    pesos = float (pesos)
    valor_dolar = 806
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dólares")
elif opcion == 2:
    pesos = input("¿cuantos pesos argentinos tienes ?: ")
    pesos = float (pesos)
    valor_dolar = 108
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dólares")
elif opcion == 3:
    pesos = input("¿cuantos Euros tienes ?: ")
    pesos = float (pesos)
    valor_dolar = 0.92
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dólares")
elif opcion == 4:
    pesos = input("¿cuantos Yen tienes ?: ")
    pesos = float (pesos)
    valor_dolar = 115
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dólares")
else : 
    print('ingresa la opcion correcta')
