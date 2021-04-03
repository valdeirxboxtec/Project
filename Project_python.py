def exercicio1():
  palavra=input("Digite uma palavra: ")
  lista=list(palavra)
  segredo=""
  for x in lista:
    if (x=='z'):segredo+='a'
    elif(x=='z'):segredo+='A'
    else: segredo+=chr(ord(x)+1)
    printf(segredo)
