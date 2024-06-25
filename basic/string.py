#Métodos Úteis para Strings

s = 'Curso Python'

#Tudo Maiúsculo
s1 = s.upper()
#teste
s1.isupper()

#Tudo minúsculo
s2 = s.lower()
#teste
s2.islower()

#Teste de apenas caracteres
s.isalpha()

#Teste apenas números
s.isdecimal()

#Teste se contem apenas letras e números
s.isalnum()

#Teste se começa com um parametro
s.startswith("Hello")

#Teste se finaliza com um parametro
s.endswith("Hello")

#Junta uma lista de strings em uma única
', '.join(['cats', 'rats', 'bats'])

#Divide uma string em várias
'Meu nome é Allan'.split()
'Meu.nome.é.Allan'.split('.')

#Remover espaços em branco
s.strip()

#Remove espaços em brancos a direita
s.rstrip()

#Remove espaços em branco a esquerda
s.lstrip()

#listas estilizadas
compras = {'refrigerantes': 4, 'maças': 12, 'laranjas': 400}
def imprimir(disc_itens, largura_col_esq, largura_col_dir):
  print('LISTA DE COMPRAS'.center(largura_col_esq + largura_col_dir, '-'))
  for k, v in disc_itens.items():
    print(k.ljust(largura_col_esq, '-') + str(v).rjust(largura_col_dir))

imprimir(compras, 40, 10)