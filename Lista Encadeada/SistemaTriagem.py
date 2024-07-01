class Nodo:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return self.cor, self.numero

class ListaEncadeada:
    def __int__(self):
        self.head = None

    def inserir(self, cor, numero):
        novo_nodo = Nodo(cor, numero)

        if novo_nodo is None:
            novo_nodo.proximo = novo_nodo
            self.head = novo_nodo

    def inserirSemPrioridade(self, nodo):

    def inserirComPrioridade(self, nodo):

    def imprimirListaEspera(self):

    def atenderPaciente(self):


Lista_Encadeada = ListaEncadeada()

print("RU: 3664781")
print(" ------------------")
print("|Sistema de Triagem|")
print(" ------------------")

while True:
    print("1 - Adicionar paciente a fila \n"
          "2 - Mostrar pacientes na fila \n"
          "3 - Chamar paciente \n"
          "4 - Sair")
    opcao = input(">>")

    if opcao == "1":
        cor = input("Informe a cor do cartão (A/V): ")
        numero = int(input("Informe o número do cartão: "))
        Lista_Encadeada.inserir(cor, numero)
    elif opcao == "2":
        print("bb")
    elif opcao == "3":
        print("")
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!! Escolha uma das opções de acordo com o menu. \n")