
import pyxel


class Jogo:
    def __init__(self):

        # Tela atual
        self.tela = "continue"

        # -------------------------
        # Configuração da Batalha Naval
        # -------------------------
        self.tamanho_tabuleiro = 14

        # Primeiro tabuleiro
        self.x1 = 105
        self.y1 = 10

        # Segundo tabuleiro
        self.x2 = 10
        self.y2 = 10

        # Tabuleiro 1 e 2
        self.tabuleiro_1 = [[0 for _ in range(6)] for _ in range(6)]
        self.tabuleiro_2 = [[0 for _ in range(6)] for _ in range(6)]

        # 0 = primeira imagem
        # 1 = segunda imagem
        self.imagem_fundo = 0

        # -------------------------
        # Configuração do Pyxel
        # -------------------------
        pyxel.init(200, 200, title="Batalha Naval")

        # Imagem Continue
        pyxel.images[2].load(
            0, 0,
            "continue_200x200.png"
        )

        # Imagens dos tabuleiros
        pyxel.images[0].load(
            0, 0,
            "tabuleiro_200x200.png"
        )

        pyxel.images[1].load(
            0, 0,
            "tabuleiro_laranja_200x200.png"
        )

        pyxel.run(self.update, self.draw)

    # -------------------------
    # Atualização
    # -------------------------
    def update(self):

        # Tecla Q fecha o jogo
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # =========================
        # TELA CONTINUE
        # =========================
        if self.tela == "continue":

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):

                x = pyxel.mouse_x
                y = pyxel.mouse_y

                # SOMENTE o quadrado/botão Continue
                if 50 <= x <= 150 and 80 <= y <= 120:

                    print("Continue")
                    self.iniciar_jogo()

        # =========================
        # JOGO
        # =========================
        elif self.tela == "jogo":

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):

                mx = pyxel.mouse_x
                my = pyxel.mouse_y

                # -------------------------
                # Primeiro tabuleiro
                # -------------------------
                if self.imagem_fundo == 0:

                    coluna = (
                        mx - self.x1
                    ) // self.tamanho_tabuleiro

                    linha = (
                        my - self.y1
                    ) // self.tamanho_tabuleiro

                    # Verifica se clicou dentro do tabuleiro
                    if 0 <= linha < 6 and 0 <= coluna < 6:

                        if self.tabuleiro_1[linha][coluna] == 1:
                            self.tabuleiro_1[linha][coluna] = 3

                        elif self.tabuleiro_1[linha][coluna] == 0:
                            self.tabuleiro_1[linha][coluna] = 2

                    # Passa para o segundo tabuleiro
                    self.imagem_fundo = 1

                # -------------------------
                # Segundo tabuleiro
                # -------------------------
                else:

                    coluna = (
                        mx - self.x2
                    ) // self.tamanho_tabuleiro

                    linha = (
                        my - self.y2
                    ) // self.tamanho_tabuleiro

                    # Verifica se clicou dentro do tabuleiro
                    if 0 <= linha < 6 and 0 <= coluna < 6:

                        if self.tabuleiro_2[linha][coluna] == 1:
                            self.tabuleiro_2[linha][coluna] = 3

                        elif self.tabuleiro_2[linha][coluna] == 0:
                            self.tabuleiro_2[linha][coluna] = 2

                    # Volta para o primeiro tabuleiro
                    self.imagem_fundo = 0

    # -------------------------
    # Iniciar o jogo
    # -------------------------
    def iniciar_jogo(self):

        self.tela = "jogo"
        self.imagem_fundo = 0

    # -------------------------
    # Desenhar tabuleiro
    # -------------------------
    def desenhar_tabuleiro(
        self,
        tabuleiro,
        x,
        y
    ):

        for linha in range(6):

            for coluna in range(6):

                valor = tabuleiro[linha][coluna]

                if valor == 0:
                    cor = 12       # Água

                elif valor == 1:
                    cor = 11       # Navio

                elif valor == 2:
                    cor = 13       # Tiro na água

                else:
                    cor = 8        # Tiro certo

                pos_x = (
                    x +
                    coluna * self.tamanho_tabuleiro
                )

                pos_y = (
                    y +
                    linha * self.tamanho_tabuleiro
                )

                pyxel.rect(
                    pos_x,
                    pos_y,
                    self.tamanho_tabuleiro - 1,
                    self.tamanho_tabuleiro - 1,
                    cor
                )

    # -------------------------
    # Desenhar
    # -------------------------
    def draw(self):

        pyxel.cls(0)

        # =========================
        # TELA CONTINUE
        # =========================
        if self.tela == "continue":

            pyxel.blt(
                0,
                0,
                2,
                0,
                0,
                200,
                200
            )

        # =========================
        # BATALHA NAVAL
        # =========================
        elif self.tela == "jogo":

            if self.imagem_fundo == 0:

                pyxel.blt(
                    0,
                    0,
                    0,
                    0,
                    0,
                    200,
                    200
                )

                self.desenhar_tabuleiro(
                    self.tabuleiro_1,
                    self.x1,
                    self.y1
                )

            else:

                pyxel.blt(
                    0,
                    0,
                    1,
                    0,
                    0,
                    200,
                    200
                )

                self.desenhar_tabuleiro(
                    self.tabuleiro_2,
                    self.x2,
                    self.y2
                )

        # Mostrar mouse
        pyxel.mouse(True)


# Inicia o jogo
Jogo()