class Cliente:
    def __init__(self):
        self.codigo=""
        self.nome=""
        self.email=""

    def cadastrar(self,codigo,nome,email):
        self.codigo=codigo
        self.nome=nome
        self.email=email

    def listarCliente(self):
        print(self.codigo)
        print(self.nome)
        print(self.email)

    def inputCadastro(self):
        codigo = input("\nCodigo do Cliente: ")
        nome = input("\nNome do Cliente: ")
        email = input("\nEmail do Cliente: ")
        self.cadastrar(codigo, nome, email)