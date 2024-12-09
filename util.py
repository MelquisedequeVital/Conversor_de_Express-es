def prioridade(operador:str):
    priori = 0
    match operador:
        case "(":
            priori = 1
        case  "+" | "-":
            priori = 2
        case "*" | "/":
            priori = 3
        case "^":
            priori = 4
    
    return priori

def eOperando(simbolo:str):
    return simbolo.isalpha() 

def eOperador(simbolo:str):
    return simbolo.strip() in "+-*/^("
