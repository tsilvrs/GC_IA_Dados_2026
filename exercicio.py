def verifica_numero (numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

entrada = input ("Digite um número: ")
numero_usuario = float (entrada)
resultado = verifica_numero (numero_usuario)
print (resultado)