from pathlib import Path

# with open('exemple.txt', encoding='utf8') as f:
#   contents = f.read()
#   print(contents)

#Retornando String de Linhas
lines = []
with open('exemple.txt', encoding='utf8') as f:
  lines = f.readlines()

count = 0
for line in lines:
  count += 1
  print(f'line {count}: {line}')

#Retornando as linhas
with open('exemple.txt', encoding='utf8') as f:
  line = f.readline()
  while line:
    print(line)
    line = f.readline()

#Escrevendo em arquivos
lines = ['Readme', 'How to write text files in Python']
with open('readm.txt', 'w') as f:
  f.write('\n'.join(lines))

#Utilizando o writelines
lines = ['Readme', 'How to write text files in Python']
with open('readm.txt', 'w') as f:
  f.writelines(lines)

#Atualizar um arquivo
with open('readm.txt', 'a') as f:
  f.write('\n\nNew line')

f.close()
