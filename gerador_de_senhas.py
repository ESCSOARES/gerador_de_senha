import string
from random import random, choice

print('qual é o tamanho de caracteres que sua senha deve ter? (ex: 5, 10 ou 20)')

tamanho = int(input())
combinacoes = string.ascii_letters
combinacoes += string.digits
combinacoes += string.punctuation
tamanho_senha = tamanho
senha = ""

for i in range(tamanho_senha):
    senha += choice(combinacoes)

print('a senha gerada é:', senha)

input('')