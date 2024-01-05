from class_endereco import Endereco
#importando a classe endereço
print("««««««« «««««« ««« «« « » »» »»» »»»»»» »»»»»»»")
print(f" «««--««    Agenda Telefonica    »»--»»»»»")
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
        self.contactos.append(obj)

lista = [ ]

obj_endereco = Endereco ("Angola", "luanda", "cazenga", "17", "s/n")
obj=Agenda("Andre", 925848946, "andrepinzi@gmail.com", "4319XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "belas", "zona_verde", "153")
obj=Agenda("Antunes", 935847946, "antunesvitae@gmail.com", "009XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "cacuaco", "nova_urbanizaçaõ", "1453")
obj=Contacto("Patricia", 944897942, "patriciatito@gmail.com", "0094A", obj_endereco)
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