import pygame, sys, random

pygame.init()

# criando tela do jogo (x, y)
screen = pygame.display.set_set_mode((400, 300))

# posição inicial da bolinha

x = 200
y = 150
raio = 20  

# posição aleatorio da comida
food_x = random.randint(20, 380) # meu limite é 400
food_Y = random.randint(20, 280) # meu limite é 300

while True:
    # verifica todos os eventos
    for event in pygame.event.get():
        # o jogador clicou no X da guia e saiu do jogo
        if event.type == pygame.QUIT:
            sys.exit()
        # pega as teclas do jogador
    keys = pygame.key.get_pressed()
        # anda para a esquerda    
    if keys[pygame.k_LEFT]:
        x -= 0.2

    # andar para a direita 
    if keys[pygame.K_RIGHT]:
        x += 0.2

    if keys[pygame.K_UP]:    
        y -= 0.2

    if keys[pygame.K_DOWN]:
        y -= 0.2

# se x for menor que zero, colocamos do tamanho da bolinha
if x < raio:
    x = raio
# se x for maior que 400, colocamos menos o tamanho da bolinha
if x > 400 - raio:
    x = 400 - raio
if y < raio:
    y = raio
if y > 300 - raio:
    y = 300 -raio 

# diferença da posição vertical e horizontal
diferenca_x = x - food_x
diferenca_y = y - food_y

# Quadrado das diferenças, ², para não termos numero negativos
quadrado_x = diferenca_x ** 2
quadrado_y = diferenca_y ** 2

soma_quadrados = quadrado_x + quadrado_y

# Raiz quadrada da soma ( distancia final entre centros), 0.5
distancia = soma_quadrados ** 0.5

if distancia < raio + 10: # se encostar ( o raio 10 é o tamanho da bolinha amarela )
    raio += 3 # aumenta a bolinha vermelha

    # reposiciona a comida
    food_x = random.randint(20, 380)
    food_y = random.randint(20, 280)

# pintar o fundo do jogo RGB (0, 0, 0)
screen.fill((0, 0, 0))

# desenhar um circulo vermelho, RGB (255, 0, 0)
# cor RGB, posição x e y, com raio 20
pygame.draw.circle(screen, (255, 0, 0, 0), (x, y), raio)

# Bolinha amarela (food)
pygame.draw.circle(screen, (255, 255, 0), (food_x, food_y), 10)

# para trocar o frame do jogo
pygame.display.flip()