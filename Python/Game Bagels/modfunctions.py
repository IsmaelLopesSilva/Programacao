import random

def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida
    False --> Entrada Inválida
    """
    if 1023<= num <= 9876:
        return True
    else:
        return False

def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]

    1*1000 + 7*100 + 8*10 + 3*1 = 1783

    OBS: O NUMERO NAO PODE TER DIGITOS REPETIDOS
    """

    numeros = list(range(10))
    secretNum = 0

    # Sorteia a lista a lista cujo os primeiros quatro elemesntos compõem o numero secreto.
    # Também não deixa o primeiro digito ser zero (0)
    while numeros[0] == 0:
        random.shuffle(numeros)

    # Monta o numero secreto unindo unidade, dezena, centeza e milhar
    for i in range(4):
        dig = numeros[i]
        secretNum += dig*(10**(3-i))

    return secretNum, numeros[:4] # Retorna com o números secreto e uma lista com quatro digitos representando-os

def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o número escolhido e o número secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Código
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi

    1234
    1783
    Retorna uma lista vazia caso os dois números sejam iguais
    """
    ult_dig = (lambda x: x % 10) # Extrai somente o ultimo digito do número passado
    
    if secretNum == num:
        return []

    dica = []

    for i in range(4):
        if ult_dig(num) == ult_dig(secretNum):
            #Fermi
            dica.append(2)
        elif ult_dig(num) in secretNumList:
            #Pico
            dica.append(1)

        num //= 10 # A cada passagem reduz o numero de milhar, centena, dezena e unidade
        secretNum //= 10 # A cada passagem reduz o numero de milhar, centena, dezena e unidade

    if len(dica) == 0:
        #Bagels
        dica.append(0)

    dica.sort()

    return dica
    
