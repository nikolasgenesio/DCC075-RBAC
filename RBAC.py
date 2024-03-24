class RBAC:
    def __init__(self, nome, permissoes):
        self.nome = nome
        self.permissoes = permissoes

    def can_read(self):
        return 'read' in self.permissoes

    def can_write(self):
        return 'write' in self.permissoes