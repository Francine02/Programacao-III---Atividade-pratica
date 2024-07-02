class Nodo:  #Classe com a definição do nodo e seus respectivos atributos
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return f"[{self.cor},{self.numero}]"

class ListaEncadeada:  #Classe com a criação da lista e suas funções
    def __init__(self):  #Inicializa com um ponteiro que aponta inicialmente - none
        self.head = None

    def __repr__(self):  #Percorre a lista e adiciona cada nodo que os junta com ", "
        nodos = []
        nodo = self.head
        while nodo is not None:
            nodos.append(str(nodo))
            nodo = nodo.proximo
        return ", ".join(nodos)

    def inserirSemPrioridade(self, nodo):
        if self.head is None:   #Se estiver vazia, é definido o self.head como o novo nodo
            self.head = nodo
        else:  #Se não estiver vazia, percorre a lista e é adicionado no final da lista o nodo
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":  #Verifica se o self.head está vazio ou se o self.head possui a cor verde e assim o novo nodo é adicionado no inicio da lista
            nodo.proximo = self.head
            self.head = nodo
        else: #Percorre a lista até encontrar o primeiro nodo verde, ou até o final da lista, e é adicionado antes dos nodos verdes.
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self, cor, numero):
        novo_nodo = Nodo(cor, numero)  #Cria um novo nodo

        if cor == "V":  #Pra controlar qual função será chamada e onde o nodo vai ser inserido
            self.inserirSemPrioridade(novo_nodo)
        else:
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        if self.head is None:
            print("A lista está vazia!")
        else:  #Percorre a lista e imprime ela
            atual = self.head
            print("Lista:")
            while atual is not None:
                print(atual, end=", " if atual.proximo else "\n")
                atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na lista para atendimento.")
        else:  #Imprime o paciente que é chamado e remove ele, atualizando o self.head para o próximo nodo
            print(f"Chamando paciente: {self.head}")
            self.head = self.head.proximo


lista = ListaEncadeada()

print("RU: 3664781")
print(" ------------------")
print("|Sistema de Triagem|")
print(" ------------------")

while True:  #Fica em um loop continuamente mostrando as opções para o usuário e executando as funcionalidades
    print("1 - Adicionar paciente a fila \n"  #Menu
          "2 - Mostrar pacientes na fila \n"
          "3 - Chamar paciente \n"
          "4 - Sair")
    opcao = input(">>")

    if opcao == "1":
        cor = input("Informe a cor do cartão (A/V): ")
        numero = int(input("Informe o número do cartão: "))
        corMaiuscula = cor.upper()  #Passei a cor para maiúsula para não haver questão de dualidade

        if corMaiuscula == "V" or corMaiuscula == "A":  #Controla para só funcionar com A/V
            lista.inserir(corMaiuscula, numero)
        else:
            print("A cor do cartão só pode ser (A/V)! \nTente novamente:")
    elif opcao == "2":  #Chama a função e mostra para o usuário a lista
        lista.imprimirListaEspera()
    elif opcao == "3":
        lista.atenderPaciente()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!! Escolha uma das opções de acordo com o menu. \n")