import os
from RBAC import RBAC
from usuario import Usuario
from file import File

# Criando os papeis
papel_admin = RBAC('admin', ['read', 'write'])
papel_convidado = RBAC('convidado', ['read'])
papel_recusado = RBAC('sem_permissao', [])

# Criando os usuarios
admin = Usuario('Nikolas', papel_admin)
convidado = Usuario('Jorge', papel_convidado)
recusado = Usuario('Mateus', papel_recusado)

# Criando o arquivo
file = File('Papeis.txt')

# Administrador escrevendo no arquivo
file.write(admin, 'Universidade Federal de Juiz de Fora')

# Administrador lendo o arquivo
file.read(admin)

# Convidado tentando escrever no arquivo
file.write(convidado, 'Universidade Federal de Minas Gerais')

# Convidado lendo o arquivo
file.read(convidado)

# Usuario sem permissão tentando ler o arquivo
file.read(recusado)

# Usuario sem permissão tentando escrever no arquivo
file.write(recusado, 'Universidade Federal do Rio de Janeiro')
