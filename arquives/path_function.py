from pathlib import Path
import os
Path('curso_python', 'arquives')
str(Path('curso_python', 'arquives'))

Path('curso_python') / 'arquives'

'curso_python' / Path('arquives')

#Imprimir a pasta corrente
print(Path.cwd())

#Mudar pasta corrente
#os.chdir('D:\\dev\\GitHub\\curso_python\\basic')

#Criando Pastas
#os.makedirs('arquives\\teste')
#Path('arquives2\\teste').mkdir(parents=True)

#Listando arquivos em uma pasta
print(os.listdir('.'))

#Listando arquivos específicos
p = Path('.')
for filename in p.glob('*.py'):
  print(filename)


