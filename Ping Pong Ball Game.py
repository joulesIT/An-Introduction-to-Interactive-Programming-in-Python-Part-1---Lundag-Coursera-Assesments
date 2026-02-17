import pygame, random, sys
pygame.init()
W,H,PAD,BALL=600,400,10,8
s=pygame.display.set_mode((W,H))
pygame.display.set_caption("Pong")
clk=pygame.time.Clock()
f=pygame.font.SysFont(None,48)

def new_ball(d=1):
    global bx,by,vx,vy
    bx,by=W//2,H//2
    vx=random.randint(3,5)*d
    vy=random.choice([-1,1])*random.randint(2,4)

p1,p2,ph=H//2,H//2,40
v1=v2=0
s1=s2=0
new_ball()

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_w: v1=-5
            if e.key==pygame.K_s: v1=5
            if e.key==pygame.K_UP: v2=-5
            if e.key==pygame.K_DOWN: v2=5
            if e.key==pygame.K_r: s1=s2=0; new_ball()
        if e.type==pygame.KEYUP:
            if e.key in(pygame.K_w,pygame.K_s): v1=0
            if e.key in(pygame.K_UP,pygame.K_DOWN): v2=0

    p1=max(ph,min(H-ph,p1+v1))
    p2=max(ph,min(H-ph,p2+v2))
    bx+=vx; by+=vy

    if by<=BALL or by>=H-BALL: vy*=-1
    # left paddle
    if bx<=PAD*2+BALL and p1-ph<=by<=p1+ph: vx=abs(vx)+0.5
    elif bx<=BALL: s2+=1; new_ball(-1)
    # right paddle
    if bx>=W-PAD*2-BALL and p2-ph<=by<=p2+ph: vx=-(abs(vx)+0.5)
    elif bx>=W-BALL: s1+=1; new_ball(1)

    s.fill((20,20,20))
    pygame.draw.aaline(s,(80,80,80),(W//2,0),(W//2,H))
    pygame.draw.rect(s,(255,255,255),(0,p1-ph,PAD,ph*2))
    pygame.draw.rect(s,(255,255,255),(W-PAD,p2-ph,PAD,ph*2))
    pygame.draw.circle(s,(255,255,255),(int(bx),int(by)),BALL)
    s.blit(f.render(str(s1),True,(255,255,255)),(W//4,20))
    s.blit(f.render(str(s2),True,(255,255,255)),(3*W//4,20))
    s.blit(pygame.font.SysFont(None,20).render("W/S  Arrows  R=restart",True,(100,100,100)),(W//2-70,H-18))
    pygame.display.flip()
    clk.tick(60)