from collections import deque
# utilizado para remover valores de chaves menores que dois
def filter_dictionary(dictionary):
    filteredDictionary = {}
    for key, value in dictionary.items():
        if len(value) > 2:
            filteredDictionary[key] = value
    return filteredDictionary



def filter_dictionary2(dictionary, mean):
    filteredDictionary = {}
    for key, value in dictionary.items():
        if value > mean:
            filteredDictionary[key] = value
    return filteredDictionary


def coincidences_function(ciphertext):
    # procura os trios que se repetem
    dictionaryWithTriagrams = {}
    for i in range(len(ciphertext)):
        valueTriagram = ciphertext[i:i+3]  # 0 ao 2 # tps
        if len(valueTriagram) < 3:
            break
        if dictionaryWithTriagrams.get(valueTriagram): 
            dictionaryWithTriagrams[valueTriagram].append(
                i) 
        else:
            dictionaryWithTriagrams[valueTriagram] = [i]

    filtered_dictionary = filter_dictionary(dictionaryWithTriagrams)
    return gettingThePossibleKeyLength(filtered_dictionary)


def gettingThePossibleKeyLength(dictionary):
    dictionaryListed = list(dictionary)  
    dictionaryOfPossibleKeyLength = {}

    novoDicionario = {}

    for key in dictionaryListed:  
        listOfValues = dictionary[key]  
        for possiblekeys in range(3, 21):  
            for i in range(len(dictionary[key])):  
                try:
                    spacing = listOfValues[i] - listOfValues[i+1]  
                    if spacing % possiblekeys == 0:  
                        if dictionaryOfPossibleKeyLength.get(possiblekeys):
                            dictionaryOfPossibleKeyLength[possiblekeys].append(
                                i)
                            novoDicionario[possiblekeys] = len(
                                dictionaryOfPossibleKeyLength[possiblekeys])
                        else:
                            dictionaryOfPossibleKeyLength[possiblekeys] = [
                                i]  
                except:
                    break


    novoDicionario = dict(sorted(novoDicionario.items()))

    total = 0
    tamanhoNovoDicionario = len(novoDicionario)
    for key, value in novoDicionario.items():
        total += value
    mean = total/tamanhoNovoDicionario
    filteredDictionary = filter_dictionary2(novoDicionario, mean)

    return filteredDictionary

def encontrar_letra(dicionario1, dicionario2):
    # Converter o dicionário em um deque
    resultado_final = []
    deque_dicionario = deque(dicionario2.items())

    for y in range(0, 26):
        deque_dicionario.rotate(-1)
        dicionario_girado = dict(deque_dicionario)
        diferencas = []

        combinado = zip(dicionario1.values(), dicionario_girado.values())

        for i, (valor1, valor2) in enumerate(combinado):
            if i >= 10:
                break
            diferenca = abs(valor1 - valor2)
            diferencas.append(diferenca)
        
        resultado_final.append(sum(diferencas))
    posicao = (resultado_final.index(min(resultado_final)) + 1)
    
    if posicao == 26:
        posicao = 0
    letra = chr(65 + posicao)

    return letra

