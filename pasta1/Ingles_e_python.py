"""
from deep_translator import GoogleTranslator

# dicionário para guardar palavras já traduzidas
memoria = {}

# criando um loop infinito, até usar a string "break"
while True:

    direcao = input("Digite 1 para traduzir do EN -> PT, 2 para PT -> EN, ou sair para encerrar:")


    #if = se
    #break, citado anteriormente, para o "while True"
    if direcao == "sair": 
        print("você que manda patrão")
        break


    #aqui eu crio a variavel "palavra" e faço ela ser igual ao que o usuario colocar. O input é usado para 
    #aparecer uma mensagem para o usuario. O strip(). 
    #O .strip é usado para manter as palavras sem espaços extra,  no inicio e no fim.
    #E o .lower deixa todas as letras minusculas 
    palavra = input("qual palavra você quer traduzir:").strip().lower()

    #aqui eu vejo se a palavra pedida está na memória, e mostro se ela já estava,
    # não precisando usar a internet para traduzir
    if palavra in memoria:
        print(f"Sua palavra é '{palavra}'sua palavra já está salva e é: {memoria[palavra]}")

    #else = se não
    #direcao 1 vai de ingles pra portugues
    #direcao 2 vai de portugues pra ingles
    #elfi = senão se
    #Basicamente, ele ve a direcao que vc escolher e traduz, depois mostra tanto a palavra que quer 
    #traduzir quanto a tradução, além de guardar a nova palavra na memoria
    else:
        if direcao == "1": 
            traducao = GoogleTranslator(source="en", target="pt").translate(palavra)
        elif direcao == "2":
            traducao = GoogleTranslator(source="pt", target="en").translate(palavra)
        else:
            print("Opcão invalida")
    memoria[palavra] = traducao
    print(f"A tradução de '{palavra}' é: {traducao}")

"""

#!/usr/bin/python3

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print("Mova disco 1 de " + origem + " para " + destino)
    else:
        hanoi(n - 1, origem, auxiliar, destino)
        print("Mova disco " + str(n) + " de " + origem + " para " + destino)
        hanoi(n - 1, auxiliar, destino, origem)

# Exemplo: 3 discos
hanoi(3, 'A', 'C', 'B')


