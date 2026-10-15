import pyxel
class Jogo:
    def __init__(self):
        pyxel.init(200, 200, title="Fundo")
        pyxel.images[0].load(0, 0, "play2.png")
        pyxel.run(self.update, self.draw)
       
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            
            #area botao
            if (66 <= x <= 136 and 87 <= y <= 104):
                print("Play")
                self.iniciar_jogo()
                
    def iniciar_jogo(self):
        pyxel.cls(0)
                
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 200, 200)
        pyxel.mouse(True)

Jogo()