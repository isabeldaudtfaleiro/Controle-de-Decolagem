# a) Permitir a decolagem do primeiro avião na fila.
# b) Adicionar um avião na fila de decolagem.
# c) Mostrar o total de aviões aguardando na fila de colagem.
# d) Lista todos os aviões na fila de decolagem.
# e) Listar as características do próximo a decolar (o avião que está na frente da fila).
# f) Mostrar a posição de um avião conforme o número do voo.


class Aviao:

    def __init__(self, numero, companhia, destino):
        self.numero = numero
        self.companhia = companhia
        self.destino = destino

    def __str__(self) -> str:
        return f'O avião: {self.numero}, da companhia {self.companhia}, tem destino para: {self.destino}'
    
    def __repr__(self) -> str:
        return f'O avião: {self.numero}, da companhia {self.companhia}, tem destino para: {self.destino}'


class Torre(Aviao):

    def __init__(self, numero=None, companhia=None, destino=None):
        self.lista_ordem = []

    # Função para adicionar o avião na lista de ordem vazia acima
    def adicionar(self, object):
        self.lista_ordem.append(object)
        print("Avião adicionado à fila com sucesso.")

    # Função para mostrar o número de aviões na fila
    def quantidade_fila(self):
        tamanho = len(self.lista_ordem)
        print(f"Existem {tamanho} aviões na fila de decolagem.")
        return tamanho
    
    # Função para exibir os aviões na fila de decolagem
    def exibicao(self):
        print(f"Os aviões constantes na fila para decolagem são: {self.lista_ordem}")

    # Função para autorizar a decolagem do avião
    def decolagem(self):
        tamanho = len(self.lista_ordem)
        if tamanho > 0:
            print(f"O avião que irá decolar é {self.lista_ordem[0]}")
        else:
            print("Nenhum avião está na lista de decolagem")

    # Função para mostrar qual é o próximo avião da lista (quando mandar o avião decolar, retirar da lista de ordem)
    def proximo(self):
        tamanho = len(self.lista_ordem)
        if tamanho > 0:
            print(f"O próximo avião a decolar é {self.lista_ordem[1]}")
        del (self.lista_ordem[0])
        print(f"A lista de aviões é: {self.lista_ordem}")
        
    # Função para verificar o avião que o usuário digitou
    def posicao(self, localizar_voo):
        contador = 0
        for i in self.lista_ordem:
            if i.numero == str(localizar_voo):
                return contador + 1
            contador += 1        

print("****** Bem-vindo(a) à Central de Comando do Aeroporto de Guarulhos ******")
print("Escolha uma das opções abaixo para manusear a Central de Comando: \n 1. Tecle 1 se deseja adicionar um avião à fila de decolagem. \n 2. Tecle 2 se deseja exibir a quantidade de aviões na fila de decolagem. \n 3. Tecle 3 se deseja listar todos os aviões na lista de decolagem. \n 4. Tecle 4 se deseja autorizar o primeiro avião da fila a decolar. \n 5. Tecle 5 se deseja exibir o próximo avião da lista para decolar. \n 6. Tecle 6 se deseja buscar a posição do avião na lista de decolagem. \n 7. Tecle 7 se deseja sair do programa.")


controlar = Torre()


while True:

    comando = input("Digite o comando que você deseja: ")

    # Adicionar um avião à fila
    if comando == "1":
        numero = input("Digite o número do avião: ")
        companhia = input("Digite a companhia do avião: ")
        destino = input("Digite o destino do avião: ")
        aviao = Aviao(numero, companhia, destino)
        controlar.adicionar(aviao)
        aviao.__str__()

    # Exibir a quantidade de aviões na fila de decolagem
    elif comando == "2":
        controlar.quantidade_fila()

    # Listar todos os aviões na fila
    elif comando == "3":
        controlar.exibicao()

    # Autorizar o primeiro avião da fila para decolar
    elif comando == "4":
        controlar.decolagem()

    # Exibir o próximo avião para decolar
    elif comando == "5":
        controlar.proximo()

    # Exibir o avião e sua respectiva posição
    elif comando == "6":
        localizar_voo = int(input("Digite o voo que você deseja localizar: "))
        posicao = controlar.posicao(localizar_voo) 
        print(f"O avião selecionado está na posição: {posicao}")

    # Encerrar o programa
    elif comando == "7":
        print("Programa encerrado.")
        break

    else:
        print("Comando inválido.")

