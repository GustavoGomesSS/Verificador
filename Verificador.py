def contar_a(string):

    count_a = string.lower().count('a')

    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

entrada = input("Digite uma string: ")
print(contar_a(entrada))
