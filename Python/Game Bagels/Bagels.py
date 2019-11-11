# Modulo grafico do python
from tkinter import *

# Modulo externo para modularizar o projeto
from modfunctions import *

class Bagels:
    def __init__(self, toplevel):
        """
        Método construtor da classe bagels. Recebe
        uma toplevel criada a partir do modulo
        tkinker que contem a app
        """
        self.frame1 = Frame(toplevel) # Essa frame conterá o título do jogo

        # Essa frame contem a caixa de texto onde
        # serão colocados os palpites do usuário a direita
        # e colocaremos o número de palpites
        # feitos / o limite de palpites a esquerda
        self.frame2 = Frame(toplevel)

        # Coloca um botão mandando o palpite do player
        self.frame3 = Frame(toplevel)


        # Nessa frame colocaremos a mensagem bagels
        # pico e fermi para o usuário ver como
        # foi o palpite dele
        self.frame4 = Frame(toplevel, height = 200, width = 800)

        # Nessa frame colocaremos um botão jogar
        # e o botão com as instruções sobre como se joga
        self.frame5 = Frame(toplevel)

        # Por fim empacotamos todas as frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack(expand = True)
        self.frame5.pack()

        self.font1 = ('Verdana', '12', 'bold') # Criamos uma tupla configurando uma fonte 1

        Label(self.frame1, text='UM JOGO DE RACIOCÍNIO', fg='darkblue',
              font = self.font1, height=3).pack() # Colocamos o título do jogo na tela

        self.font2 = ('Verdana', '10', 'bold') # Váriavel que contem a tupla com as configurações da fonte

        self.palp = Entry(self.frame2, width=20, font=self.font2)
        self.palp.pack(side = LEFT) # Colocamos na frame 2 a nossa entrada do palpite do usuário

        # Criamos a caixa com o número de palpites feitos/possiveis
        self.jgds = Label(self.frame2, text = '0/10', font = self.font2,
                          width = 8)
        self.jgds.pack(side = RIGHT)

        # Colocamos o botão que manda o chute do player
        self.go = Button(self.frame3, font = self.font2, text = 'GO!',
                            bg = 'lightgray', command = self.GO)
        self.go.pack()

        # Criamos o texto que será divulgado para o usuário
        self.msg = Label(self.frame4, text = 'Digite um número com 4 dígitos',
                         font = self.font1, height = 10)
        self.msg.pack()

        # Colocamos o botão jogar
        self.jogar = Button(self.frame5, font = self.font2, text = 'Jogar',
                            bg = 'green', command = self.InitJogo)
        self.jogar.pack(side=LEFT)

        # E também o botao com as instruções
        self.inst = Button(self.frame5, font = self.font2, text = 'Instruções',
                            bg = 'green', command = self.Inst)
        self.inst.pack(side=RIGHT)

        # Gera uma lista contendo o nosso codigo de dicas
        self.codigo = ['Bagels', 'Pico', 'Fermi']

        # Criamos um novo jogo
        self.InitJogo()

    def InitJogo(self):
        """
        Método usado para lidar quando o player
        aperta a tecla jogar, ou seja, inicia o jogo
        """

        # Inicializa as variáveis do jogo
        self.jogadas = 0 # Zeramos o número de jogadas
        self.jgds['text'] = '0/10' # Zeramos o número de jogadas

        self.msg['text'] = '*** Digite um número com 4 dígitos ***' # Recolocamos a mensagem inicial
        self.msg['fg'] = 'black'

        self.palpites = [] # Gera uma lista vazia que conterá todos os palpites

        self.jogando = True # E uma variável booleana dizendo se o programa está em execução

        # Gera o numero secreto e a lista contendo esses números
        self.secretNum, self.secretNumList = GeraSecretNum()

    def Inst(self):
        """
        Muda a mensagem na tela do colocando
        as informações sobre como o jogo funciona
        """
        self.msg['text'] = 'O jogo sorteia um número com quatro dígitos\n'
        self.msg['text'] += 'Esse número será >= 1023 e <= 9876\n'
        self.msg['text'] += 'Cada digito é um número diferente\n'
        self.msg['text'] += 'O jogador deve tentar acertar que número é este\n'
        self.msg['text'] += 'Para isso ele pode chutar um valor qualquer,\n'
        self.msg['text'] += 'e então o programa colocara mensagens\n de acordo com os dígitos escolhidos\n'
        self.msg['text'] += 'Pico: Significa que um digíto está correto, mas na posição errada\n'
        self.msg['text'] += 'Fermi: Significa que um dígito está correto e na posição correta\n'
        self.msg['text'] += 'Bagels: Significa que nenhum dígito está correto'
        self.msg['fg'] = 'green'

    def GO(self):
        """
        Método que manda tudo o que o usuário digitou
        para o programa, e processa o que foi digitado
        """
        # Só devemos fazer qualquer coisa se o player estiver jogando
        if self.jogando:
            
            palpite = self.palp.get() # Primeiro nós pegamos o que foi digitado
            
            # Tentamos converter em inteiro
            try:
                palpite = int(palpite)
            except ValueError:
                # Caso haja uma letra colocada por acidente mandamos uma mensagem adequada para o usuário
                self.msg['text'] = 'Entrada Inválida\n Digite apenas números!'
                self.msg['fg'] = 'red'
                return

            # Verificamos se o número de dígitos do palpite está correto 1023 >= e <=9876
            if not VerificaEntrada(palpite):
                self.msg['text'] = 'Digite números com 4 dígitos!'
                self.msg['fg'] = 'red'
            else:
                dicas = GeraDicas(palpite, self.secretNum, self.secretNumList) # Pegamos quais são as dicas

                self.ImprimeDicas(palpite, dicas) # Imprime as dicas para o usuário

                self.jogadas += 1 # Aumenta o número de jogadas

                self.jgds['text'] = '%i/10'%self.jogadas # Também muda o texto de jogadas

                # Por fim verificamos se o player chegou ao limite de jogadas
                if self.jogadas == 10 and self.jogando:
                    self.jogando = False # O player perdeu, e portanto parou de jogar
                    self.Perdeu() # E a mensagem de derrota é mostrada

                self.palpites.append((palpite, dicas))

        self.palp.focus_force() # A caixa de texto fica em evidência

        self.palp.delete(0, END) # Apaga tudo o que foi digitado

    def Perdeu(self):
        """
        Imprime a mensagem identificando
        que o player perdeu
        """
        self.msg['text'] = 'Você Perdeu! =/\n'
        self.msg['text'] = 'O número era %i'%self.secretNum
        self.msg['fg'] = 'red'

    def ImprimeDicas(self, palpite, dicas):
        """
        Muda a mensagem de acordo com o palpite do usuário   
        """
        # Se dicas for um booleano então devemos imprimir a mensagem de que o usuário ganhou
        if len(dicas) == 0:
            self.msg['text'] = 'Parabens!\nVocê Venceu!\nO número era %i'%self.secretNum
            self.msg['fg'] = 'blue'
            self.jogando = False
            return

        self.msg['text'] = '' # Primeiro nós deletemos o texto anterior

        i = 1 # Imprimimos os resultados das jogadas anteriores
        for jogada in self.palpites: 
            self.msg['text'] += 'Palpite %i: %i --> '%(i, jogada[0])
            self.AdcionaDicas(jogada[1])
            self.msg['text'] += '\n'
            i+=1

        # Por fim adcionamos a msg do player
        self.msg['text'] += 'Sua Jogada: %i\n'%palpite
        self.AdcionaDicas(dicas)

        # Mudamos a cor do texto para preto
        self.msg['fg'] = 'black'

    def AdcionaDicas(self, dicas):
        """
        Adciona dicas a mensagem
        """
        for dica in dicas:
            self.msg['text'] += self.codigo[dica] + ' ' # Depois vamos adicionando mensagens de acordo com as dicas

janela = Tk()
Bagels(janela)
janela.title('*** Bagels ***')
janela.geometry("800x400")
janela.mainloop()
