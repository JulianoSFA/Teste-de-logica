encontrado = [False]
listaCaminho = []
stringCaminho = ""
entrada = input("Escolha um nó para procurar: ")


class Node:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def Caminho(self, chaveBusca):
        if self.chave == chaveBusca:
            encontrado[0] = True

        if self.esquerda is not None and encontrado[0] is not True:
            self.esquerda.Caminho(chaveBusca)

        if self.direita is not None and encontrado[0] is not True:
            self.direita.Caminho(chaveBusca)

        if encontrado[0]:
            listaCaminho.insert(0, self.chave)


#Cria a árvore binaria
raiz = Node("Maça", Node("Morango", Node("Goiaba"), Node("Limão")), Node("Pera"))
raiz.direita.direita = Node("Abacaxi")
raiz.direita.direita.direita = Node("Laranja", Node("Banana"), Node("Cebola"))

raiz.Caminho(entrada)

if encontrado[0]:
    for i in listaCaminho:
        stringCaminho += i + " -> "

    stringCaminho = stringCaminho[:-4]
    print(stringCaminho)

else:
    print("O nó digitado não existe")
