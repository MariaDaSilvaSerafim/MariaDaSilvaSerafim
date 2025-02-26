import pygame as pg
import random

# Código para inicializar função
pg.init()

PRETO= (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

ALTURA = 400
LARGURA = 600





# Código para Criar tela
                    #(tela) variavel criada para tamanho da tela
tela = pg.display.set_mode((LARGURA, ALTURA))
# Variável para o nome do Jogo
titulo = pg.display.set_caption('Snake')
# Variável do tamanho da cobra do Jogo
TAMANHO_COBRA = 20
clock = pg.time.Clock()
# Variável criada para atualização do game


# Código para aplicar cor na janela
#tela.fill(BRANCO)
def desenhar(cobra):
    for segmento in cobra:

        pg.draw.rect(tela, VERDE, [segmento[0], segmento[1], TAMANHO_COBRA, TAMANHO_COBRA], 0)

def jogo():

    x_cobra = LARGURA // 2
    y_cobra = ALTURA // 2
    movimento_x = 0
    movimento_y = 0
    cobra = []
    comprimento_cobra = 1

    comida_x = random.randrange(0, LARGURA - TAMANHO_COBRA, TAMANHO_COBRA)
    comida_y = random.randrange(0, ALTURA - TAMANHO_COBRA, TAMANHO_COBRA)


#Fução Loop (repetição)
    fim_de_jogo = False
    while not fim_de_jogo:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                fim_de_jogo = True
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_LEFT:
                    movimento_x = -TAMANHO_COBRA
                    movimento_y = 0
                elif evento.key == pg.K_RIGHT:
                    movimento_x = TAMANHO_COBRA
                    movimento_y = 0
                elif evento.key == pg.K_UP:
                    movimento_y = -TAMANHO_COBRA
                    movimento_x = 0
                elif evento.key == pg.K_DOWN:
                    movimento_y = TAMANHO_COBRA
                    movimento_x = 0

        if x_cobra >= LARGURA or x_cobra < 0 or y_cobra >= ALTURA or y_cobra < 0:
            fim_de_jogo = True

        x_cobra += movimento_x
        y_cobra += movimento_y

        cabeça_cobra = []
        cabeça_cobra.append(x_cobra)
        cabeça_cobra.append(y_cobra)
        cobra.append(cabeça_cobra)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verificar se a cobra colidiu com ela mesma
        for segmento in cobra[:-1]:
            if segmento == cabeça_cobra:
                fim_de_jogo = True

        tela.fill(PRETO)
        desenhar(cobra)
        pg.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_COBRA, TAMANHO_COBRA])

        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = random.randrange(0, LARGURA - TAMANHO_COBRA, TAMANHO_COBRA)
            comida_y = random.randrange(0, ALTURA - TAMANHO_COBRA, TAMANHO_COBRA)
            comprimento_cobra += 1

        
        pg.display.update()
        clock.tick(15)

    fonte = pg.font.SysFont(None, 55)
    texto_fim = fonte.render("Fim de Jogo", True, AZUL)
    tela.blit(texto_fim, [LARGURA // 3, ALTURA // 3])
    pg.display.update()
    pg.time.wait(2000)
# Código para finalizar função
    pg.quit()

jogo()
