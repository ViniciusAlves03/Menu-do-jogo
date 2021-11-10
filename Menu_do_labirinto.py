import pygame
pygame.init

janela = pygame.display.set_mode ((500,550))                                 #Tamanho da janela
fundo = pygame.image.load('menu_labirintoplano_de_fundo1.jpeg')              #Definir o plano de fundo
pygame.display.set_caption('')                                               #Nome da janela

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 70)
textUsuarios = font.render("Usuários", True, (255, 255, 255))
textCreditos = font.render("Créditos", True, (255, 255, 255))


while janela != 0:
    janela.blit (fundo ,(0,0)) ; pygame.time.delay(100)

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            janela = 0

    comando1 = pygame.key.get_pressed()
    if comando1[pygame.K_SPACE]:
        fundo = pygame.image.load('menu_labirintoplano_de_fundo2.jpeg')
        pygame.time.delay(500)
        fundo.blit(textUsuarios,(100,85))
        fundo.blit(textCreditos,(100,300))

        #INÍCIO DO MENU (APÓS PRESSIONAR ESPAÇO)

    pygame.display.update()

#Menu e suas funções:Haverá duas opções: Jogar (Passa para a primeira fase do jogo) e Créditos (Mostra o nome da equipe, professora e campus)
