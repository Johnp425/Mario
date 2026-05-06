from gamelib import *

game = Game(800,600,"Mario")
mario = Animation("images/snake.png",48,game,1392/7,247/1,2)
scorpion = Animation("./Images/scorpion.jpg",3,game,288/3,106,3)
human = Animation("images/human.png",15, game, 440/5, 294/3,2)
bottle = Animation("images/bottle.png",24, game, 230/5, 516/5,2)
sand = Image("./images/sand.jpg",game)
emojis = Image("./images/emojis.png",game)
sand.resizeTo(game.width, game.height)
game.setBackground(sand)
human.y=game.height - 100
scorpion.y= -100
#snake.y=-100
#snake.x = randint(100, game.width - 100)
bottle.y=-100
snake.setSpeed(3,-90)
scorpion.setSpeed(3,180)
snake.rotateBy(90)
bottle.setSpeed(2,180)
die = Sound("Sounds/die.wav",2)
ouch = Sound("Sounds/ouch.wav",3)
drink = Sound("Sounds/drink.wav",4)
f=Font(white,40,black,"Comic Sans MS")

while not game.over:
  game.processInput()
  game.scrollBackground("down",5)
  game.drawText("Press [SPACE] to start", 310, 500)
  snake.move()

  if snake.y > game.height:
    snake.y= -100
    snake.x= randint(100, game.width - 100)
    snake.speed += 1

  if keys.Pressed[K_SPACE]:
    game.over = True
    


  game.update(30)
game.over = False
while not game.over:
  game.processInput()
  game.scrollBackground("up",5)
  scorpion.move()
  snake.move()
  human.move()
  bottle.move()

  if keys.Pressed[K_d]:
    human.x -= -2
    human.rotateTo(-20)

  if keys.Pressed[K_a]:
    human.x += -2
    human.rotateTo(+20)

  if snake.y > game.height:
    snake.y= -100
    snake.x= randint(100, game.width - 100)
    snake.speed += 1

  if scorpion.y > game.height:
    scorpion.y= -100
    scorpion.x= randint(100, game.width - 100)
    scorpion.speed += 1

  if bottle.y > game.height:
    bottle.y= -100
    bottle.x= randint(100, game.width - 100)
    bottle.speed += 1
    



  if snake.collidedWith(human):
    ouch.play()
    human.health -= 1

  if scorpion.collidedWith(human):
    ouch.play()
    human.health -= 1

  if bottle.collidedWith(human):
    drink.play()
    human.health += 10
    bottle.visible=False
    bottle.y= -100
    bottle.visible=True

  if human.health < 1:
    game.over  = True

  game.drawText(human.health, human.x, human.y + 50)

  if human.health < 0:
    game.over=True
    die.play()
    game.over =True
 
  game.update(30)
game.over = False

while not game.over:
  game.processInput()
  game.scrollBackground("down",5)
  emojis.draw()
  game.drawText("Game Over", 310, 500,f)
  game.drawText("Press [SPACE] to Close", 300,400,f)
  scorpion.move()

  if keys.Pressed[K_SPACE]:
    game.over = True
  game.update(30)

game.quit()
