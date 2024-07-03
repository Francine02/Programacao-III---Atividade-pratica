class Node:  #Classe com o nodo da lista encadeada
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  #Tabela com uma lista com 10 posições

    def inserir(self, sigla, nomeEstado):  #Insere um novo estado na tabela
        index = self.hash_funcao(sigla) #Chama a função e determina a posição na tabela que o novo estado vai ir
        novo_nodo = Node(sigla, nomeEstado)  #Criação do novo nodo
        novo_nodo.next = self.tabela[index]  #Faz com que o ponteiro aponte para o primeiro nodo atual na posição do index da tabela
        self.tabela[index] = novo_nodo  #Atualiza a posição, para que aponte para o novo nodo e insere ele no inicio

    def hash_funcao(self, sigla):
        if sigla == 'DF':
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10  #Calcula os valores ASCII das duas letras do estado, para assim retornar a posição que deve ser inserida

    def __str__(self):  #Imprime a tabela
        resultado = ""
        for i, node in enumerate(self.tabela):
            resultado += f"Posição {i}: "
            atual = node
            while atual is not None:
                resultado += f"{atual.sigla}--> "
                atual = atual.next
            resultado += "None\n"
        return resultado

estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

hash_tabela = TabelaHash()

print("RU: 3664781")
print("Tabela Hash antes de inserir qualquer informação:")
print(hash_tabela)

# Inseri os estados e o Distrito Federal na tabela hash
for sigla, nome in estados:
    hash_tabela.inserir(sigla, nome)
print("Tabela Hash após inserir os estados e o Distrito Federal:")
print(hash_tabela)

# Inseri um estado fictício
estado_ficticio = ("FC", "Francine Carolina Oliveira Cruz")
hash_tabela.inserir(*estado_ficticio)

print("Tabela Hash após inserir os estados, o Distrito Federal e o estado fictício:")
print(hash_tabela)