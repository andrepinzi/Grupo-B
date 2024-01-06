from class_endereco import Endereco
#importando a classe endereço
lista = [ ]
print("««««««« «««««« ««« «« « » »» »»» »»»»»» »»»»»»»")
print(f"  «««--««    Agenda Telefonica    »»--»»»»»")
# Inciando a classe Contacto
class Contacto():
    def __init__(self, nome, numero, email, cod_postal, obj_endereco):
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cod_post = cod_postal
        self.localizacao = obj_endereco

# Classe agenda herda de contacto
class Agenda (Contacto):
    def __init__(self, nome, numero, email, cod_postal, obj_endereco):
        super().__init__(nome, numero, email, cod_postal, obj_endereco)
        self.contactos = []

    def adicionar (self):
        nome = input("Digite o nome do contato: ")
        numero = int(input("Digite o número de telefone do contato: "))
        email = input("Digite o e-mail: ")
        cod_postal = input("Digite o codigo postal: ")
        pais = input("Digite o nome do pais: ")
        provincia = input("Digite o nome do provincia: ")
        municipio = input("Digite o nome do municipio: ")
        rua = input("Digite o nome do rua: ")
        casa = input("Digite o nome do casa: ")
        obj_endereco = Endereco(pais, provincia, municipio, rua, casa)
        obj = Agenda(nome, numero, email, cod_postal, obj_endereco)
        lista.append(obj)
        print("Contacto Adicionado!")


obj_endereco = Endereco ("Angola", "luanda", "cazenga", "17", "s/n")
obj=Agenda("Andre", 925848946, "andrepinzi@gmail.com", "4319XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "belas", "zona_verde", "153")
obj=Agenda("Antunes", 935847946, "antunesvitae@gmail.com", "009XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "cacuaco", "nova_urbanizaçaõ", "1453")
obj=Agenda("Patricia", 944897942, "patriciatito@gmail.com", "0094A", obj_endereco)
lista.append(obj)

for elemento in lista:
#listar detalhes dos contactos 
    print("   ««««« «««« ««« «« « » »» »»» »»»» »»»»»")
    print(f"{elemento.nome}")
    print(elemento.numero)
    print(elemento.email)

#listar detalhes do Endereço
    print(elemento.localizacao.pais)
    print(elemento.localizacao.provincia)
    print(elemento.localizacao.municipio)
    print(elemento.localizacao.rua)
    print(elemento.localizacao.casa)

obj.adicionar()