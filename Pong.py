import pygame
import math

width = 721
height = 721

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

pygame.display.set_caption('cow game 3')


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True

ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

ballx = ball_pos.x
bally = ball_pos.y

speed = 1

balldx = 2 * speed
balldy = -4 * speed

paddleWidth = 270
paddleHeight = 25


paddle_pos = pygame.Vector2((screen.get_width() / 2) - (paddleWidth/2), 600)

paddlex = paddle_pos.x
paddley = paddle_pos.y


ball = pygame.Rect(int(ballx - 40), int(bally - 40), 40*2, 40*2)
paddle = pygame.Rect(int(paddlex - (paddleWidth /2)), int(paddley - (paddleHeight/2) ), paddleWidth,paddleHeight)



hit_sound = pygame.mixer.Sound("hit.wav")


font = pygame.font.SysFont("Segoe UI", 35)

score = 0

bg = pygame.image.load("bg.png")

while running:
    #poll for events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballx += balldx *speed
    bally += balldy *speed

    
    

    screen.blit(bg, (0,0))

    mousePos = pygame.Vector2(pygame.mouse.get_pos())
    paddlex = mousePos.x
    paddley = mousePos.y

    if bally < 40 or bally > height - 40:
        balldy *= -1
    if ballx < 40 or ballx > width - 40:
        balldx *= -1
    
    if ball.colliderect(paddle):
        if bally < paddle.top:
            hit_sound.play()
            balldy *= -1 *speed
            bally = paddle.top - 40
            score += 1
            speed += 0.005
            
        elif bally > paddle.bottom:
            hit_sound.play()
            balldy *= -1 *speed
            bally = paddle.bottom + 40
            

        elif ballx < paddle.left:
            hit_sound.play()
            balldx *= -1 *speed
            ballx = paddle.left -40
            

        elif ballx > paddle.right:
            hit_sound.play()
            balldx *= -1 *speed
            ballx = paddle.right + 40
            
            
    
    if bally > 680:
        running = False

    paddle = pygame.Rect(int(paddlex - (paddleWidth /2)), 580, paddleWidth,paddleHeight)
    ball = pygame.Rect(int(ballx - 40), int(bally - 40), 40*2, 40*2)


    #RENDER  YOUR GAME HERE

    pygame.draw.circle(screen, pygame.Color(240, 185, 36), (int(ballx), int(bally)), 40)
    pygame.draw.rect(screen, pygame.Color(45, 209, 4), paddle)

    scoretxt = str(score)
    textsurface = font.render(scoretxt, False, pygame.Color(255,255,255))
    screen.blit(textsurface, (0,0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
