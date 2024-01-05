import pgzrun 
from random import randint

WIDTH = 800
HEIGHT = 600

all_bricks =[]
hard_bricks1 =[]
hard_bricks3 =[]
winner = False
is_game_over = False
score = 0
vie = 4

for y in range (100, 200, 30):
   for x in range (200, 600, 100):
      
        rnd = randint(1,10)
        if rnd <= 7:
            brick =Actor("brick", anchor=["left", "top"])
            all_bricks.append(brick)
        elif rnd <= 9:
            brick =Actor("brick1", anchor=["left", "top"])
            hard_bricks1.append(brick)
        else:
            brick =Actor("brick3", anchor=["left", "top"])
            hard_bricks3.append(brick)
        brick.pos = [x, y]
            
      
def create_brick(name, position, brick_list):
    brick = Actor(name, anchor=["left", "top"])
    brick.pos = position 
    brick_list.append(brick)


            
fastplayer = Actor("fastplayer")
fastplayer.pos = [WIDTH/2 , 530]

stock_balls = []   
for n in range (1, vie):
   ball = Actor("ball")
   ball.pos = [WIDTH/2, 500]
   stock_balls.append(ball)
     
play_ball = Actor("ball")
play_ball.pos = [WIDTH/2, 500]
play_ball.in_motion = False
play_ball_speed =[6, -6]


brick1 =Actor("brick1")
brick1.pos = [100, 90]

game_over_actor = Actor("gameover")
game_over_actor.pos = [400, 300]

winner_actor = Actor("winner")
winner_actor.pos = [400, 300]

#def on_mouse_down(pos):
    #if ball.collidepoint(pos):
        #sounds.sound1.play()
        #ball.image = 'brick'

def on_mouse_move(pos):
   #player.x= pos[0]
   fastplayer.pos = [pos[0], fastplayer.pos[1]]
   
def on_mouse_up():
    play_ball.in_motion = True

def invert_horizontal_speed():
   play_ball_speed[0] = play_ball_speed[0] * -1

def invert_vertical_speed():
   play_ball_speed[1] = play_ball_speed[1] * -1

def update():
    global is_game_over, score, vie, winner 
    
    n = -35 * len(stock_balls)/2
    for ball in stock_balls:
            ball.pos = [(100) + n, HEIGHT - 20]
            n += 35
    if play_ball.in_motion:
        new_x = play_ball.pos[0] + play_ball_speed[0]
        new_y = play_ball.pos[1] + play_ball_speed[1]
        play_ball.pos = [new_x, new_y]
        if play_ball.right > WIDTH or play_ball.left <0:
            invert_horizontal_speed()
        if play_ball.top < 0: 
            invert_vertical_speed()
            play_ball.pos = [play_ball.pos[0], 10]
        # if play_ball.bottom > HEIGHT:
        #      invert_vertical_speed()

        if play_ball.colliderect(fastplayer):
            invert_vertical_speed()
    else:
        play_ball.pos = [fastplayer.pos[0], fastplayer.pos[1] - 25]
   
    if play_ball.bottom >= HEIGHT:
        play_ball.in_motion = False
        vie -= 1
        if len(stock_balls) > 0:
            stock_balls.pop(-1)
            

    if vie <= 0:
       is_game_over = True 

    if len(all_bricks) == 0 and len(hard_bricks1) == 0 and len(hard_bricks3) == 0 and vie > 0:
       winner = True

    brick_collide = False 

    for brick in all_bricks:
        if play_ball.colliderect(brick):
            all_bricks.remove(brick)
            invert_vertical_speed()
            sounds.hardpop.play()
            score += 10
            brick_collide = True
            break

    if not brick_collide:    
        for brick3 in hard_bricks3:
            if play_ball.colliderect(brick3):
                hard_bricks3.remove(brick3)
                invert_vertical_speed()
                brick4 =Actor("brick4",anchor=["left","top"])
                brick4.pos = brick3.pos
                all_bricks.append(brick4)
                ball.pos=(400, 300)
                sounds.brisverre.play() 
                score += 20
                brick_collide = True
                break
           

#    for brick4 in hard_bricks3:
#        if  ball.colliderect(brick4):
#            brick4.pos = brick3.pos
#            hard_bricks3.remove(brick4)
       
    if not brick_collide:  
        for brick1 in hard_bricks1:
            if play_ball.colliderect(brick1):
                print("test")
                hard_bricks1.remove(brick1)
                invert_vertical_speed()
                brick2 =Actor("brick2" ,anchor=["left","top"])
                brick2.pos = brick1.pos
                all_bricks.append(brick2)
                ball.pos=(600, 200)
                sounds.brisverre.play()
                score += 20
                break
                
    if brick_collide:
        invert_vertical_speed

         
 #def drawscore():
    #screen.draw.text("SCORE: " + str(score), (350,400))
   
def draw():
   
   global is_game_over , winner
   screen.clear()
   for brick in all_bricks:
      brick.draw()
   for brick3 in hard_bricks3:
       brick3.draw()

   for brick1 in hard_bricks1:
       brick1.draw()
       
   for ball in stock_balls:
        ball.draw()

 
   fastplayer.draw()
   play_ball.draw()
   if not play_ball.in_motion: 
    screen.draw.text("Click to start", [(WIDTH/2) - 40, HEIGHT/2])
  
    if winner == True:
        screen.clear()
        winner_actor.draw()
        sounds.success.play()
        screen.draw.text("YOUR SCORE IS: " + str(score), (600,550))

    elif is_game_over:
        screen.clear()
        sounds.gameover.play()
        game_over_actor.draw()
        screen.draw.text("SCORE: " + str(score), (350,400))
      
#derniere ligne only
pgzrun.go()