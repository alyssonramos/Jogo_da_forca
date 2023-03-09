from time import perf_counter, sleep

palavra = input("Insira uma palavra secreta: ")
start = perf_counter()
erros = 0
while(1):
    char = input("Digite 1 letra: ") 
    if char in palavra:
        print("Esta")
        palavra = palavra.replace(char, '')
        if(palavra == ''):
            print("você ganhou! :D")
            break
    else:
        print("nao esta")
        erros +=1
        if(erros == 1):
            print("cabeça")
            print('''
               ___
              |   |
              |   o
              |  
              |  
              |
              |
            __|__ ''')
        elif erros == 2:
            print("tronco")
            print('''
               ___
              |   |
              |   o
              |   |
              |  
              |
              |
            __|__ ''')
        elif erros == 3:
            print("braço esquerdo")
            print('''
               ___
              |   |
              |   o
              |   |l
              |   
              |
              |
            __|__ ''')
        elif erros == 4:
            print("braço direito")
            print('''
               ___
              |   |
              |   o
              |  /|l
              |   
              |
              |
            __|__ ''')
        elif erros == 5:
            print("perna esquerda")
            print('''
               ___
              |   |
              |   o
              |  /|l
              |    l
              |
              |
            __|__ ''')
        elif erros == 6:
            print("perna direita")
            print('''
               ___
              |   |
              |   o
              |  /|l
              |  / l
              |
              |
            __|__ ''')

            print("Voce perdeu! :(")
             
            break
end = perf_counter()
print(f"O tempo jogado foi, em segundos, de: {end - start}")