import re

number = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
result = number.search('Meu número é (99) 99999-9999')
print('Telefone encontrado: ' + result.group())

#Grupos
number = re.compile(r'(\(\d{2}\)) (\d{5}-\d{4})')
result = number.search('Meu número é (99) 99999-9999')
print('DDD:', result.group(1))
print('Número:', result.group(2))
print('DDD + Número:', result.group(0))
ddd, telefone = result.groups()

#Classes
frutas = re.compile(r'\d+\s\w+')
print(frutas.findall('10 maças, 7 peras, 2 bananas'))

#(.) e (*)
atoRegex = re.compile('.ato')
print(atoRegex.findall('O gato entrou no mato e encontrou o rato dentro do jatobá'))

nomeRegex = re.compile(r'Primeiro Nome: (.*) Sobrenome: (.*)')
print(nomeRegex.findall('Primeiro Nome: Allan Sobrenome: Gabriel'))

#Ignorando maísculo minúsculo
texto = re.compile('python', re.I)
print(texto.search('Curso de Python').group())
