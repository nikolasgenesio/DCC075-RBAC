class File:
    # Função para iniciar
    def __init__(self, nome):
        self.nome = nome
        
    # Função para ler o arquivo    
    def read(self, usuario):
        if usuario.papel.can_read():
            with open(self.nome, 'r') as f:
                print(f.read())
        else:
            print(f"{usuario.nome} não tem permissões de leitura")
            
    #Função para escrever no arquivo
    def write(self, usuario, texto):
        if usuario.papel.can_write():
            with open(self.nome, 'w') as f:
                f.write(texto)
        else:
            print(f"{usuario.nome} não tem permissões de escrita")