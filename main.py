from pilhaSequencial import Pilha
import util

pilha = Pilha(50)

infixa = str(input(" Escreva a expressão: "))

saida = ""

for simbolo in infixa:
    if util.eOperando(simbolo):
        saida += simbolo
    elif (util.eOperador(simbolo) and pilha.isEmpty()) or (util.eOperador(simbolo) and util.prioridade(pilha.top()) < util.prioridade(simbolo)) or (simbolo == "("):
        pilha.push(simbolo)
    elif simbolo == ")":
        while pilha.top() != "(":
            saida += pilha.pop()
        pilha.pop() #tirar o parenteses
    else:
        while not pilha.isEmpty() and util.prioridade(pilha.top()) >= util.prioridade(simbolo):
            saida += pilha.pop()
        pilha.push(simbolo)

while not pilha.isEmpty():
    saida += pilha.pop()

print(saida)