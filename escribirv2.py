import time
import keyboard

mebros = int(input("Digite a quantidade de infelizes: \n"))
print("Após digitar o numero, voce tera 3 segundos para ir para o forms \n")
numeros = int(input("Digite o primeiro numero da sequencia: \n"))
time.sleep(3) #esperar 3 segundps

for m in range (0, mebros, 1):

    for i in range (numeros, numeros+35 , 1):
        fn = '{:0>4}'.format(i) #Formatar com zeros e 4 casas no total
        keyboard.write(fn, delay=0.15) #escrever com 150ms de delay
        keyboard.press('enter') #apertar enter
        print(fn)   #print p garantir
        print("Fim do preenchimento")

    for l in range (1, 38, 1):
        keyboard.press('tab')
        time.sleep(0.15)
        print("taaaab :" ,+ l)
    numeros += 35
    

print("ja sentiu??")