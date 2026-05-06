from gamelib import *

game = Game(800,600,"Mario")
background = Image("images/background.png",game)
marios = Animation("images/marios.png",2,game,720/2,472/1,9)
marioo = Animation("images/marioo.png",2,game,758/2,418/1,5)
mario1 = Animation("images/mario1.png",2,game,776/2,464/1,10)
mario2 = Animation("images/mario2.png",2,game,744/2,484/1,9)
rocks = Animation("images/rocks.png",48,game,2048/8,2048/8,2)
rocks2 = Animation("images/rocks2.png",48,game,1024/8,1024/8,2)
rocks3 = Animation("images/rocks3.png",48,game,1024/8,1024/8,2)
rocks4 = Animation("images/rocks4.png",48,game,1024/8,1024/8,2)
rocks5 = Animation("images/rocks.png",48,game,2048/8,2048/8,2)
flower = Image("images/flower.png",game)
star = Image("images/star.png",game)
emojis = Image("./images/emojis.png",game)
flower.resizeBy(-9)
flower.setSpeed(1,90)
flower.rotateBy(-90)
rocks.setSpeed(3,-90)
rocks.rotateBy(90)
rocks.resizeBy(-20)
rocks2.setSpeed(3,-90)
rocks2.rotateBy(90)
rocks2.resizeBy(-20)
rocks3.setSpeed(3,-90)
rocks3.rotateBy(90)
rocks3.resizeBy(-20)
rocks4.setSpeed(3,-90)
rocks4.rotateBy(90)
rocks4.resizeBy(-20)
rocks5.setSpeed(3,-90)
rocks5.rotateBy(90)
rocks5.resizeBy(-20)
star.resizeBy(-97)
star.setSpeed(2,90)
star.rotateBy(-90)

game.setBackground(background)
marios.y=game.height - 140
marios.resizeBy(-70)
marioo.y=game.height - 140
marioo.resizeBy(-70)
mario1.y=game.height - 140
mario1.resizeBy(-70)
mario2.y=game.height - 140
mario2.resizeBy(-70)
rocks.y=-10
rocks5.y=-10
rocks2.y=-10
rocks3.y=-10
rocks4.y=-10
flower.y=-1000
star.y=-2000
f=Font(white,40,black,"Comic Sans MS")






bullet = Animation("images/fireball.png",8,game,1164/8,396/1,3)
bullet.visible = True
bullet.setSpeed(-8,0)
bullet.resizeBy(-50)
bullet.rotateBy(-180)


while not game.over:
 game.processInput()
 background.draw()
 marios.move()
 game.drawText("Press [SPACE] to start", 310, 500)


 if keys.Pressed[K_SPACE]:
     game.over = True

 game.update(30)
game.over = False


while not game.over:
  game.processInput()
  background.draw()
  marios.move()
  flower.move()
  marioo.move()
  rocks.move()
  rocks2.move()
  rocks3.move()
  rocks4.move()
  flower.draw()
  rocks5.move()
  mario1.move()
  mario2.move()

  if rocks.y > game.height:
    rocks.y= -100
    rocks.x= randint(100, game.width - 100)
    rocks.speed = 1

  if rocks2.y > game.height:
    rocks2.y= -100
    rocks2.x= randint(100, game.width - 100)
    rocks2.speed += 0

  if rocks3.y > game.height:
    rocks3.y= -100
    rocks3.x= randint(100, game.width - 100)
    rocks3.speed += 0

  if rocks4.y > game.height:
    rocks4.y= -100
    rocks4.x= randint(100, game.width - 100)
    rocks4.speed = 2

  if rocks5.y > game.height:
    rocks5.y= -100
    rocks5.x= randint(100, game.width - 100)
    rocks5.speed = 2

  if flower.y > game.height:
    flower.y= -200
    flower.x= randint(100, game.width - 100)
    flower.speed = 5


  marioo.visible = False
  mario1.visible = False
  mario2.visible = False

  game.drawText(marioo.health, marioo.x, marioo.y + 50,f)

# mario movement

  if keys.Pressed[K_d]:
    marios.visible = False
    marioo.x -= -9
    marioo.rotateTo(-0)
    marioo.visible = True
    marioo.flipV = False
    marios.x -= -9
    marios.rotateTo(-0)

  elif keys.Pressed[K_a]:
    marios.visible = False
    marioo.visible = True
    marioo.flipV = True
    marioo.x += -9
    marioo.rotateTo(+0)
    marios.flipV = True
    marios.rotateTo(+0)
    marios.x += -9 
    marios.rotateTo(+0)
  else:
    marios.visible = True
# damage  


  if rocks.collidedWith(marioo):
     marioo.health -= 10
     rocks.visible=False
     rocks.y= -100
     rocks.visible=True

  if rocks.collidedWith(marios):
    marioo.health -= 10
    rocks.visible=False
    rocks.y= -100
    rocks.visible=True

  if rocks2.collidedWith(marioo):
    marioo.health -= 5
    rocks2.visible=False
    rocks2.y= -100
    rocks2.visible=True

  if rocks2.collidedWith(marios):
    marioo.health -= 5
    rocks2.visible=False
    rocks2.y= -100
    rocks2.visible=True
  
  if rocks3.collidedWith(marioo):
     marioo.health -= 5
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True

  if rocks3.collidedWith(marios):
     marioo.health -= 5
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True

  if rocks4.collidedWith(marioo):
     marioo.health -= 5
     rocks4.visible=False
     rocks4.y= -100
     rocks4.visible=True

  if rocks4.collidedWith(marios):
     marioo.health -= 5
     rocks4.visible=False
     rocks4.y= -100
     rocks4.visible=True

  if rocks5.collidedWith(marioo):
     marioo.health -= 10
     rocks5.visible=False
     rocks5.y= -100
     rocks5.visible=True

  if rocks5.collidedWith(marios):
     marioo.health -= 10
     rocks5.visible=False
     rocks5.y= -100
     rocks5.visible=True



  if marioo.collidedWith(flower):
    game.over =True

 


  game.update(30)
  
game.over = False
while not game.over:
  game.processInput()
  background.draw()
  game.drawText(mario2.health, mario2.x, mario2.y + 50,f)
  mario1.move()
  mario2.move()
  rocks.move()
  rocks2.move()
  rocks3.move()
  rocks4.move()
  rocks5.move()
  bullet.move()
  star.move()
 


  if keys.Pressed[K_SPACE] and bullet.visible:
      bullet.moveTo( mario1.x, mario1.y )
      bullet.visible = True





  mario2.visible = False
    
    

  if rocks.y > game.height: 
      rocks.y= -100
      rocks.x= randint(100, game.width - 100)
      rocks.speed += 3

  if rocks2.y > game.height:
     rocks2.y= -100
     rocks2.x= randint(100, game.width - 100)
     rocks2.speed += 3

  if rocks3.y > game.height:
     rocks3.y= -100
     rocks3.x= randint(100, game.width - 100)
     rocks3.speed += 3

  if rocks4.y > game.height:
     rocks4.y= -100
     rocks4.x= randint(100, game.width - 100)
     rocks4.speed +=3

  if rocks5.y > game.height:
     rocks5.y= -100
     rocks5.x= randint(100, game.width - 100)
     rocks5.speed += 3





  if rocks.collidedWith(mario2):
     mario2.health -= 10
     rocks.visible=False
     rocks.y= -100
     rocks.visible=True

  if rocks.collidedWith(mario1):
    mario2.health -= 10
    rocks.visible=False
    rocks.y= -100
    rocks.visible=True

  if rocks2.collidedWith(mario2):
    mario2.health -= 5
    rocks2.visible=False
    rocks2.y= -100
    rocks2.visible=True

  if rocks2.collidedWith(mario1):
    mario2.health -= 5
    rocks2.visible=False
    rocks2.y= -100
    rocks2.visible=True
  
  if rocks3.collidedWith(mario2):
     mario2.health -= 5
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True

  if rocks3.collidedWith(mario1):
     mario2.health -= 5
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True

  if rocks4.collidedWith(mario1):
     mario2.health -= 5
     rocks4.visible=False
     rocks4.y= -100
     rocks4.visible=True

  if rocks4.collidedWith(mario2):
     mario2.health -= 5
     rocks4.visible=False
     rocks4.y= -100
     rocks4.visible=True

  if rocks5.collidedWith(mario1):
     mario2.health -= 10
     rocks5.visible=False
     rocks5.y= -100
     rocks5.visible=True

  if rocks5.collidedWith(mario2):
     mario2.health -= 10
     rocks5.visible=False
     rocks5.y= -100
     rocks5.visible=True

  if rocks.collidedWith(bullet):
     rocks.visible=False
     rocks.y= -100
     rocks.visible=True

  if star.y > game.height:
    star.y= -200
    star.x= randint(100, game.width - 100)
    star.speed = 5


  if rocks2.collidedWith(bullet):

    rocks2.visible=False
    rocks2.y= -100
    rocks2.visible=True
  
  if rocks3.collidedWith(mario2):
     mario2.health -= 5
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True

  if rocks3.collidedWith(bullet):
     rocks3.visible=False
     rocks3.y= -100
     rocks3.visible=True


  if rocks4.collidedWith(bullet):

     rocks4.visible=False
     rocks4.y= -100
     rocks4.visible=True



  if rocks5.collidedWith(bullet):
     rocks5.visible=False
     rocks5.y= -100
     rocks5.visible=True



  if keys.Pressed[K_d]:
    mario1.visible = False
    mario2.x -= -9
    mario2.rotateTo(-0)
    mario2.visible = True
    mario2.flipV = False
    mario1.x -= -9
    mario1.rotateTo(-0)

  elif keys.Pressed[K_a]:
    mario1.visible = False
    mario2.visible = True
    mario2.flipV = True
    mario2.x += -9
    mario2.rotateTo(+0)
    mario1.flipV = True
    mario1.rotateTo(+0)
    mario1.x += -9
    mario1.rotateTo(+0)
  else:
    mario1.visible = True

  if mario2.health < 0:
    game.over=True

  if mario2.collidedWith(star):
    game.over =True

  game.update(30)
game.over = False
while not game.over:
  game.processInput()
  emojis.draw()
  game.drawText("Game Over", 310, 500,f)
  game.drawText("Press [SPACE] to Close", 300,400,f)


  if keys.Pressed[K_SPACE]:
    game.over = True
  game.update(30)


game.quit()

  
