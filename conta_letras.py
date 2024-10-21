def contar_letras_a(s):
    # Converte a string para minúsculas
    s = s.lower()
    # Conta a ocorrência da letra 'a'
    count = s.count('a')
    return count

# String para verificar
string = input("Informe uma string: ")

# Chama a função e exibe o resultado
total = contar_letras_a(string)
print(f"A letra 'a' aparece {total} vez(es) na string.")