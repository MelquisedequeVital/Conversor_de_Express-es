import numpy as np

class Pilha:
    def __init__(self, tamanho:int = 10):
        self.__elementos = np.full(tamanho, None)
        self.__topo = -1

    def push(self, carga) -> None:
        if Pilha.isFull(self):
            raise RuntimeError("Pilha Cheia")
        self.__topo += 1
        self.__elementos[self.__topo] = carga
        

    def pop(self) -> int:
        if Pilha.isEmpty(self):
            raise RuntimeError("Pilha Vazia")
        e = self.__elementos[self.__topo]
        self.__topo -= 1
        return e

    def top(self) -> int:
        return self.__elementos[self.__topo]
    

    def isFull(self) -> bool:
        return self.__topo == len(self.__elementos) - 1

    def isEmpty(self) -> bool:
        return self.__topo == -1
    
    
    def __str__(self):
        string = "["
        for i in self.__elementos:
            string += f"{i} "
        
        string += "]"

        return string