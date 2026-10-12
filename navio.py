import pyxel
import random

class Jogo:
    def __init__(self):
        # inicio
        self.tela = "inicio" 
        self.tamanho_tabuleiro = 14
        # Tabuleiro Jogador 1
        self.x1 = 105
        self.y1 = 10
        # Tabuleiro Jogador 2
        self.x2 = 10
        self.y2 = 10
        # Criando tabuleiros (matriz) com lista (6x6)
        self.tabuleiro_jogador_1 = [[0 for _ in range(6)] for _ in range(6)]
        self.tabuleiro_jogador_2 = [[0 for _ in range(6)] for _ in range(6)]
        # Colocar navios
        self.colocar_navios(self.tabuleiro_jogador_1)
        self.colocar_navios(self.tabuleiro_jogador_2)
        # Jogador 1 começa
        self.jogador_atual = 1
        # Contador jogadores 1 e 2 zerados
        self.acertos_jogador_1 = 0
        self.acertos_jogador_2 = 0
        # Total de quadrados dos navios (11 partes)
        self.total_partes_navios = 11 
        
        pyxel.init(200, 200, title="Batalha Naval")
        pyxel.load("navio.py.pyxres")
        # Garante que o mouse fique visível desde o início para o clique funcionar
        pyxel.mouse(True) 
        # Jogador 1
        pyxel.images[0].load(0, 0, "tabuleiro_200x200.png")
        # Jogador 2
        pyxel.images[1].load(0, 0, "tabuleiro_laranja_200x200.png")
        # Tela inicial play (banco 2)
        pyxel.images[2].load(0, 0, "play2.png")
        
        pyxel.play(0, 0, loop=True)
        # tela return
        pyxel.run(self.update, self.draw)

    # coloca navios no tabuleiro (5 navios)
    def colocar_navios(self, tabuleiro):
        # 5 barcos e seus tamanhos
        tamanhos = [4, 3, 2, 1, 1]
        for tamanho in tamanhos:
            colocado = False
            # se ele encontrar uma posiçao valida ele para de colocar navios
            while not colocado:
                # pode escolher uma posiçao de 0 a 5 no tabuleiro pois ele e feito de 6 linhas e 6 colunas (0 a 5 para nao ocorrer problema)
                linha = random.randint(0, 5)
                coluna = random.randint(0, 5)
                # escolher aleatoriamente horizontal ou vertical
                direcao = random.choice(["horizontal", "vertical"])
                
                # verifica se o navio e valido na linha ou coluna para nao ultrapassar esse limete de (6x6)
                if direcao == "horizontal":
                    if coluna + tamanho <= 6:
                        livre = True
                        # verifica se ja esta ocupado
                        for i in range(tamanho):
                            if (tabuleiro[linha][coluna + i] != 0):
                                livre = False
                        if livre:
                            for i in range(tamanho):
                                tabuleiro[linha][coluna + i] = 1
                            colocado = True
                else:
                    if linha + tamanho <= 6:
                        livre = True
                        for i in range(tamanho):
                            if (tabuleiro[linha + i][coluna] != 0):
                                livre = False
                        if livre:
                            for i in range(tamanho):
                                tabuleiro[linha + i][coluna] = 1
                            colocado = True

    def update(self):
        # Q sai do jogo
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        # verificou se apertou no botao continue com o mause
        if self.tela == "inicio":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                x = pyxel.mouse_x
                y = pyxel.mouse_y
                # Área do botão play
                if (85 <= x <= 110 and 53 <= y <= 76):
                    # Carrega a tela continue no mesmo banco de imagem
                    pyxel.images[2].load(0, 0, "continue_200x200.png")
                    self.tela = "continue"
                    
        elif self.tela == "continue":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                x = pyxel.mouse_x
                y = pyxel.mouse_y
                # Área do botão Continue
                if (66 <= x <= 136 and 87 <= y <= 104):
                    self.iniciar_jogo()
                    
        elif self.tela == "jogo":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mx = pyxel.mouse_x
                my = pyxel.mouse_y
               
                if self.jogador_atual == 1:
                   
                    coluna = (mx - self.x2) // self.tamanho_tabuleiro
                    linha = (my - self.y2) // self.tamanho_tabuleiro
                   
                    if (0 <= linha < 6 and 0 <= coluna < 6):
                        valor = (self.tabuleiro_jogador_2[linha][coluna])

                        if valor == 1:
                            self.tabuleiro_jogador_2[linha][coluna] = 3
                            self.acertos_jogador_1 += 1
                            print("Jogador 1 acertou!")

                            if (self.acertos_jogador_1 >= self.total_partes_navios):
                                pyxel.stop(0) # para musica
                                # Carrega a imagem de Game Over no banco 2 logo quando vence
                                pyxel.images[2].load(0, 0, "GO_voltar_200x200.png")
                                self.tela = "vitoria"
                            
                        elif valor == 0:
                            self.tabuleiro_jogador_2[linha][coluna] = 2
                            print("Jogador 1 errou!")
                            self.jogador_atual = 2 # so muda se errar
                            
                elif self.jogador_atual == 2:
                    coluna = (mx - self.x1) // self.tamanho_tabuleiro
                    linha = (my - self.y1) // self.tamanho_tabuleiro

                    if (0 <= linha < 6 and 0 <= coluna < 6):
                        valor = (self.tabuleiro_jogador_1[linha][coluna])

                        if valor == 1:
                            self.tabuleiro_jogador_1[linha][coluna] = 3
                            self.acertos_jogador_2 += 1
                            print("Jogador 2 acertou!")
                     
                            if (self.acertos_jogador_2 >= self.total_partes_navios):
                                pyxel.stop(0) # para musica
                                # Carrega a imagem de Game Over no banco 2 logo quando vence
                                pyxel.images[2].load(0, 0, "GO_voltar_200x200.png")
                                self.tela = "vitoria" # fica no jogador 2 pois acertou
                            
                        elif valor == 0:
                            self.tabuleiro_jogador_1[linha][coluna] = 2
                            print("Jogador 2 errou!")
                            self.jogador_atual = 1
                            
        # tela aonde mostra vitoria
        elif self.tela == "vitoria":
            if pyxel.btnp(pyxel.KEY_R):
                # Recarrega a imagem de play original antes de reiniciar para o menu
                pyxel.images[2].load(0, 0, "play2.png")
                self.reiniciar_jogo()

    def iniciar_jogo(self):
        self.tela = "jogo"
        self.jogador_atual = 1

    # reinicia o jogo
    def reiniciar_jogo(self):
        self.tabuleiro_jogador_1 = [[0 for _ in range(6)] for _ in range(6)]
        self.tabuleiro_jogador_2 = [[0 for _ in range(6)] for _ in range(6)]
        self.colocar_navios(self.tabuleiro_jogador_1)
        self.colocar_navios(self.tabuleiro_jogador_2)
        # Zera os acertos
        self.acertos_jogador_1 = 0
        self.acertos_jogador_2 = 0
        # Começa pelo jogador 1 novamente
        self.jogador_atual = 1
        self.tela = "jogo"

    def desenhar_tabuleiro(self, tabuleiro, x, y):
        for linha in range(6):
            for coluna in range(6):
                valor = tabuleiro[linha][coluna]
                if valor == 0:
                    # quadrado escolhido
                    cor = 12
                elif valor == 1:
                    # navio
                    cor = 12
                elif valor == 2:
                    # errou (cor cinza)
                    cor = 13
                elif valor == 3:
                    # acertou (cor vermelha)
                    cor = 8
                # calcula a posiçao dos quadrados (matrizes)
                pos_x = (x + coluna * self.tamanho_tabuleiro)
                pos_y = (y + linha * self.tamanho_tabuleiro)
                # desenha cada quadrado
                pyxel.rect(pos_x, pos_y, self.tamanho_tabuleiro - 1, self.tamanho_tabuleiro - 1, cor)

    def draw(self):
        pyxel.cls(0)
        if self.tela == "inicio":
            pyxel.blt(0, 0, 2, 0, 0, 200, 200)
        elif self.tela == "continue":
            pyxel.blt(0, 0, 2, 0, 0, 200, 200)
        # verifica a vez de cada jogador
        elif self.tela == "jogo":
            if self.jogador_atual == 1:
                pyxel.blt(0, 0, 1, 0, 0, 200, 200)
                # tabuleiro sendo mostrado a cada jogada do jogador 1
                self.desenhar_tabuleiro(self.tabuleiro_jogador_2, self.x2, self.y2)
                pyxel.text(140, 18, "jogador 1", 7)
                pyxel.text(140, 26, "acertos: " + str(self.acertos_jogador_1) + "/11", 7)
            else:
                pyxel.blt(0, 0, 0, 0, 0, 200, 200)
                self.desenhar_tabuleiro(self.tabuleiro_jogador_1, self.x1, self.y1)
                pyxel.text(5, 18, "jogador 2", 7)
                pyxel.text(5, 26, "acertos: " + str(self.acertos_jogador_2) + "/11", 7)
        # mostra quem venceu        
        elif self.tela == "vitoria":
            pyxel.cls(0)
            # Desenha a imagem de Game Over 
            pyxel.blt(0, 0, 2, 0, 0, 200, 200)
            
            
            if (self.acertos_jogador_1 >= self.total_partes_navios):
                pyxel.text(65, 90, "jogador 1 venceu!", 7)
            else:
                pyxel.text(65, 90, "jogador 2 venceu!", 7)
                
            # reinicia o jogo apertando R
            pyxel.text(230, 230, "pressione R para reiniciar", 7)

Jogo()
