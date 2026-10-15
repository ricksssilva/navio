import pyxel
import random

class Jogo:
    def __init__(self):
        self.tela = "inicio"
        self.tamanho_tabuleiro = 14
        self.x1 = 105
        self.y1 = 10
        self.x2 = 10
        self.y2 = 10
        self.tabuleiro_jogador_1 = [ [0 for _ in range(6)] for _ in range(6) ]
        self.tabuleiro_jogador_2 = [ [0 for _ in range(6)] for _ in range(6) ]
        self.colocar_navios(self.tabuleiro_jogador_1)
        self.colocar_navios(self.tabuleiro_jogador_2)
        self.jogador_atual = 1
        self.acertos_jogador_1 = 0
        self.acertos_jogador_2 = 0
        self.total_partes_navios = 11
        pyxel.init(200, 200, title="Batalha Naval")
        pyxel.load("play.pyxres")
        pyxel.mouse(True)
        pyxel.images[0].load( 0, 0, "tabuleiro_200x200.png" )
        pyxel.images[1].load( 0, 0, "tabuleiro_laranja_200x200.png" )
        pyxel.images[2].load( 0, 0, "play2.png" )
        # Música de fundo adicionada aqui para tocar em loop infinito no canal 0
        # pyxel.play(90, 90, loop=True)
        pyxel.run(self.update, self.draw)

    def colocar_navios(self, tabuleiro):
        tamanhos = [4, 3, 2, 1, 1]
        for tamanho in tamanhos:
            colocado = False
            while not colocado:
                linha = random.randint(0, 5)
                coluna = random.randint(0, 5)
                direcao = random.choice( ["horizontal", "vertical"] )
                if direcao == "horizontal":
                    if coluna + tamanho <= 6:
                        livre = True
                        for i in range(tamanho):
                            if tabuleiro[linha][coluna + i] != 0:
                                livre = False
                        if livre:
                            for i in range(tamanho):
                                tabuleiro[linha][coluna + i] = 1
                            colocado = True
                else:
                    if linha + tamanho <= 6:
                        livre = True
                        for i in range(tamanho):
                            if tabuleiro[linha + i][coluna] != 0:
                                livre = False
                        if livre:
                            for i in range(tamanho):
                                tabuleiro[linha + i][coluna] = 1
                            colocado = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if self.tela == "inicio":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                x = pyxel.mouse_x
                y = pyxel.mouse_y
                if 85 <= x <= 110 and 53 <= y <= 76:
                    pyxel.images[2].load( 0, 0, "continue_200x200.png" )
                    self.tela = "continue"
        elif self.tela == "continue":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                x = pyxel.mouse_x
                y = pyxel.mouse_y
                if 66 <= x <= 136 and 87 <= y <= 104:
                    self.iniciar_jogo()
        elif self.tela == "jogo":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mx = pyxel.mouse_x
                my = pyxel.mouse_y
                if self.jogador_atual == 1:
                    coluna = ( mx - self.x2 ) // self.tamanho_tabuleiro
                    linha = ( my - self.y2 ) // self.tamanho_tabuleiro
                    if 0 <= linha < 6 and 0 <= coluna < 6:
                        valor = ( self.tabuleiro_jogador_2[ linha ][ coluna ] )
                        if valor == 1:
                            self.tabuleiro_jogador_2[ linha ][ coluna ] = 3
                            self.acertos_jogador_1 += 1
                            print( "Jogador 1 acertou!" )
                            if ( self.acertos_jogador_1 >= self.total_partes_navios ):
                                pyxel.images[2].load( 0, 0, "GO_voltar_200x200.png" )
                                self.tela = "vitoria"
                        elif valor == 0:
                            self.tabuleiro_jogador_2[ linha ][ coluna ] = 2
                            print( "Jogador 1 errou!" )
                            self.jogador_atual = 2
                elif self.jogador_atual == 2:
                    coluna = ( mx - self.x1 ) // self.tamanho_tabuleiro
                    linha = ( my - self.y1 ) // self.tamanho_tabuleiro
                    if 0 <= linha < 6 and 0 <= coluna < 6:
                        valor = ( self.tabuleiro_jogador_1[ linha ][ coluna ] )
                        if valor == 1:
                            self.tabuleiro_jogador_1[ linha ][ coluna ] = 3
                            self.acertos_jogador_2 += 1
                            print( "Jogador 2 acertou!" )
                            if ( self.acertos_jogador_2 >= self.total_partes_navios ):
                                pyxel.images[2].load( 0, 0, "GO_voltar_200x200.png" )
                                self.tela = "vitoria"
                        elif valor == 0:
                            self.tabuleiro_jogador_1[ linha ][ coluna ] = 2
                            print( "Jogador 2 errou!" )
                            self.jogador_atual = 1
        elif self.tela == "vitoria":
            if pyxel.btnp(pyxel.KEY_R):
                self.reiniciar_jogo()

    def iniciar_jogo(self):
        self.tela = "jogo"
        self.jogador_atual = 1

    def reiniciar_jogo(self):
        self.tabuleiro_jogador_1 = [ [0 for _ in range(6)] for _ in range(6) ]
        self.tabuleiro_jogador_2 = [ [0 for _ in range(6)] for _ in range(6) ]
        self.colocar_navios( self.tabuleiro_jogador_1 )
        self.colocar_navios( self.tabuleiro_jogador_2 )
        self.acertos_jogador_1 = 0
        self.acertos_jogador_2 = 0
        self.jogador_atual = 1
        self.tela = "jogo"
        pyxel.images[2].load( 0, 0, "play2.png" )

    def desenhar_tabuleiro(self, tabuleiro, x, y):
        for linha in range(6):
            for coluna in range(6):
                valor = tabuleiro[linha][coluna]
                if valor == 0:
                    cor = 12
                elif valor == 1:
                    cor = 12
                elif valor == 2:
                    cor = 13
                elif valor == 3:
                    cor = 8
                pos_x = ( x + coluna * self.tamanho_tabuleiro )
                pos_y = ( y + linha * self.tamanho_tabuleiro )
                pyxel.rect( pos_x, pos_y, self.tamanho_tabuleiro - 1, self.tamanho_tabuleiro - 1, cor )

    def draw(self):
        pyxel.cls(0)
        if self.tela == "inicio":
            pyxel.blt( 0, 0, 2, 0, 0, 200, 200 )
        elif self.tela == "continue":
            pyxel.blt( 0, 0, 2, 0, 0, 200, 200 )
        elif self.tela == "jogo":
            if self.jogador_atual == 1:
                pyxel.blt( 0, 0, 1, 0, 0, 200, 200 )
                self.desenhar_tabuleiro( self.tabuleiro_jogador_2, self.x2, self.y2 )
                pyxel.text( 140, 18, "jogador 1", 7 )
                pyxel.text( 140, 26, "acertos: " + str(self.acertos_jogador_1) + "/11", 7 )
            else:
                pyxel.blt( 0, 0, 0, 0, 0, 200, 200 )
                self.desenhar_tabuleiro( self.tabuleiro_jogador_1, self.x1, self.y1 )
                pyxel.text( 5, 18, "jogador 2", 7 )
                pyxel.text( 5, 26, "acertos: " + str(self.acertos_jogador_2) + "/11", 7 )
        elif self.tela == "vitoria":
            pyxel.blt( 0, 0, 2, 0, 0, 200, 200 )

Jogo()