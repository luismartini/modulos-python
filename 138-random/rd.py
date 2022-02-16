import random
import string

#inteiro = random.randint(10, 20)

inteiro = random.randrange(900, 1000, 10)

#flutuante = random.uniform(10, 20)
flutuante = random.random()

lista = ['Luís', 'Francisco', 'Martini', 'Jonice', 'Adele']

#sorteio = random.choices(lista, k=2)
#sorteio = random.sample(lista, 2)
#sorteio = random.choice(lista)
#random.shuffle(lista)

#Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*_-'
geral = letras + digitos + caracteres

senha = ''.join(random.choices(geral, k=20))
print(senha)