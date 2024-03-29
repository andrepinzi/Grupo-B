from class_endereco import Endereco
import os
lista = []
class Contacto():
    def __init__(self, nome, numero, email, cod_postal, obj_endereco):
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cod_post = cod_postal
        self.localizacao = obj_endereco

class Agenda (Contacto):
    def __init__(self, nome, numero, email, cod_postal, obj_endereco):
        super().__init__(nome, numero, email, cod_postal, obj_endereco)

    def adicionar (self):
        print("=== == ADICIONANDO CONTACTO == ===\n")
        nome = input("Digite o nome: ")
        numero = int(input("Digite o número de telefone: "))
        email = input("Digite o e-mail: ")
        cod_postal = input("Digite o codigo postal: ")
        pais = input("Informe o país:  ")
        provincia = input("Informe a província: ")
        municipio = input("Informe o município: ")
        rua = input("Informe a rua: ")
        casa = input("Informe o nº da casa: ")
        obj_endereco = Endereco(pais, provincia, municipio, rua, casa)
        obj = Agenda(nome, numero, email, cod_postal, obj_endereco)
        lista.append(obj)
        os.system("cls")
        print("Contacto Adicionado!\n")
        opcao = input("Qualquer Voltar para o Menu\n")
        os.system("cls")
        return True

    def editar (self):
            print("\n=== == EDITANDO CONTACTO == ===\n")
            valor = 0 
            nome = input("Insira nome do contacto que deseja editar: ")
            for elemento in lista:
                if elemento.nome == nome:
                    print(f"\n{nome} Encontrado\n")
                    novo_nome = input("Insira novo nome: ")
                    novo_numero = int(input("Insira Novo Numero:"))
                    elemento.nome = novo_nome
                    elemento.numero = novo_numero
                    print(f"{elemento.nome}: {elemento.numero}")
                    print(f"Concluido!")
                else:
                    valor += 1
                    if valor == (len(lista)):
                        print(f"\n{nome} nao foi encontrado!")
                    
    def remover(self):
        print("\n=== == REMOVENDO CONTACTO == ===\n")
        valor = 0
        for elemento in lista:
            if valor <= (len(lista)):
                print(f"{valor}. {elemento.nome}: {elemento.numero}")
            valor += 1
        position = int(input("Insira a posição do contacto: "))
        while position > (len(lista)):
            print(f"Insira uma das posições sugeridas")
            position = int(input("\nInsira a posição do contacto: "))
        lista.pop(position)
        print(f"\nContacto Removido!")

    def procurar(self):
        print("\n=== == PESQUISANDO CONTACTO == ===\n")
        n = 0
        valor = 0
        while n == 0:
            opc = int(input(f"Procurar a partir de: \n1. Nome\n2. Numero\n"))
            if opc == 1:
                nome = input("Insira nome: ")
                for elemento in lista:
                    if elemento.nome == nome:
                        if elemento.localizacao.pais == "Angola":
                            print(f"\n{elemento.nome}: +244 {elemento.numero}")
                        else:
                            print(f"\n{elemento.nome}: +00 {elemento.numero}")
                        n = 1
                    else:
                        valor += 1
                        if valor == (len(lista)):
                            print(f"\n{nome} nao foi encontrado!")
                            n = 1
            elif opc == 2:
                numero = int(input("Insira numero: "))
                for elemento in lista:
                    if elemento.numero == numero:
                        if elemento.localizacao.pais == "Angola":
                            print(f"\n{elemento.nome}: +244 {elemento.numero}")
                        else:
                            print(f"\n{elemento.nome}: +00 {elemento.numero}")
                        n = 1
                    else:
                        valor += 1
                        if valor == (len(lista)):
                            print(f"\n{numero} nao foi encontrado!")
                            n = 1
            else:
                n = 0
                print(f"Escolha simplismente umas das opções: ")                        

    def listar(self):
        print("\n=== == MOSTRANDO CONTACTOS == ===\n")
        print(f"Todos contactos: {len(lista)}\n")
        for elemento in lista:
            print(f"{elemento.nome}: {elemento.numero}\n{elemento.email}\n")

obj_endereco = Endereco ("Canadá", "Quebec", "Querry", "17", "s/n")
obj = Agenda ("Andre", 925848946, "andrepinzi@gmail.com", "4319XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "belas", "zona_verde", "153")
obj = Agenda ("Antunes", 935847946, "antunesvitae@gmail.com", "009XA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "cacuaco", "nova_urbanizaçaõ", "1453")
obj = Agenda ("Esperanca", 944471642, "esperanaatito@gmail.com", "0094A", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Angola", "luanda", "Viana", "nova_urbanizaçaõ", "1453")
obj = Agenda ("arlindo", 932897312, "arlindo09@gmail.com", "001YA", obj_endereco)
lista.append(obj)

obj_endereco = Endereco ("Brazil", "Sao Paulo", "Santo Joao", "Quebrada", "14/3")
obj = Agenda ("Cristina", 934877942, "cristina34@gmail.com", "209R2", obj_endereco)
lista.append(obj)

print("««««««« «««««« ««« «« « » »» »»» »»»»»» »»»»»»»")
print(f"  «««--««    AGENDA TELEFÓNICA    »»--»»»»»")
while True:
    print(" \n       =========== == == ===========\n")
    print(f"1. ADICIONAR\n2. EDITAR\n3. REMOVER\n4. PROCURAR\n5. LISTAR")
    opcao = int(input("\nEscolha uma das opções de 1 - 5:\n"))
    match opcao:
        case 1:
            obj.adicionar()
        case 2:
            obj.editar()
        case 3:
            obj.remover()
        case 4:
            obj.procurar()
        case 5:
            obj.listar()