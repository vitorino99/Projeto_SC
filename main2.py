import os
import string
from collections import deque
from assets import lf_portuguese, lf_english
from functions_1 import filter_regex, decryption
from functions_2 import coincidences_function, encontrar_letra


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_language():
    print("Digite 1 para Português")
    print("Digite 2 para Inglês")

    while True:
        lf_option = int(input("Escolha a lingua da tabela de frequencias a ser utilizada: "))
        if lf_option == 2:
            return lf_english
        elif lf_option == 1:
            return lf_portuguese


def process_cipher_text():
    cipher_text = input("Coloque o texto a ser decifrado:")
    clear_screen()
    cipher_text_filtered = filter_regex(cipher_text).upper()
    return cipher_text_filtered


def create_frequency_dicts(cipher_text_filtered, key_size):
    dict_of_dicts = {}
    dict_of_dicts_frequency = {}
    iterator = 0

    while iterator < key_size:
        dict_of_lf_ciphertext = dict.fromkeys(string.ascii_uppercase, 0)
        dict_of_lf_ciphertext_freq = dict.fromkeys(string.ascii_uppercase, 0)

        for i in range(iterator, len(cipher_text_filtered), key_size):
            dict_of_lf_ciphertext_key = cipher_text_filtered[i]
            dict_of_lf_ciphertext[dict_of_lf_ciphertext_key] += 1

        dict_of_lf_ciphertext = dict(sorted(dict_of_lf_ciphertext.items()))
        total = sum(dict_of_lf_ciphertext.values())
        dict_of_dicts_frequency_key = 'F' + str(iterator)

        for letter, quantity in dict_of_lf_ciphertext.items():
            frequency = round(quantity * 100 / total, 2)
            dict_of_lf_ciphertext_freq[letter] = frequency

        dict_of_dicts_key = 'H' + str(iterator)
        dict_of_dicts_frequency[dict_of_dicts_frequency_key] = dict_of_lf_ciphertext_freq
        dict_of_dicts[dict_of_dicts_key] = dict_of_lf_ciphertext
        iterator += 1

    return dict_of_dicts, dict_of_dicts_frequency


def play_game(lf, dict_of_dicts_frequency):
    key = ""
    resultado = []
    remain_letters_of_key = len(dict_of_dicts_frequency.items())

    for letter, table_frequency in dict_of_dicts_frequency.items():
        operation = None

        while operation != 'quit':
            print("Falta escolher " + str(remain_letters_of_key) + " letras da chave\n")
            operation = input("Digite P para processar a proxima letra da chave: ")
            clear_screen()

            if operation == 'P':
                letra = encontrar_letra(lf, table_frequency)
                key += letra
                print("Letra adicionada:", letra)
                resultado.append(letra)
                print("Chave até o momento:", str(resultado))
                remain_letters_of_key -= 1
                operation = 'quit'

    return key


def main():
    cipher_text_filtered = process_cipher_text()
    possible_key_sizes = coincidences_function(cipher_text_filtered)
    print(possible_key_sizes)
    key_size = int(input("Escolha o tamanho de chave desejado com base no dicionário acima:"))
    clear_screen()
    lf = choose_language()
    dict_of_dicts, dict_of_dicts_frequency = create_frequency_dicts(cipher_text_filtered, key_size)
    lf = dict(sorted(lf.items()))
    key = play_game(lf, dict_of_dicts_frequency)
    decoded_text = decryption(cipher_text_filtered.lower(), key)
    print("\nTexto decodificado:\n\n", decoded_text)
    print("\nCaso o texto tenha sido decodificado errado, experimente utilizar um outro tamanho de chave")


if __name__ == "__main__":
    main()
