#note to Mr. Marco: i did this exact same assignment in Mr. Fowler's TEJ3M Computer Engineering class so I used my previous code. But I understand how everything works
#
#https://github.com/mrworldwide1/Grade11processing/blob/main/Bouncing_Ball_Colour_Change.pde

from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.

  #bouncy ball class
  class Ball:
    def __init__(self):
      self.posX = random.randint(0, p.width)
      self.posY = random.randint(0, p.height)
      self.col = 'white'
      self.w = random.randint(15, 40)
      self.h = random.randint(15, 40)
      self.speedX = random.randint(1, 10)
      self.speedY = random.randint(1, 10)

    def drawBall(self):
      p.fill(255)
      p.stroke(0)
      p.ellipse(self.posX, self.posY, self.w, self.h)

    def moveBall(self):
      self.posX += self.speedX
      self.posY += self.speedY

      if self.posX >= p.width:
        self.speedX *= -1
      elif self.posX <= 0:
        self.speedX *= -1
      elif self.posY >= p.height:
        self.speedY *= -1
      elif self.posY <= 0:
        self.speedY *= -1
        
    
  def setup():
    p.background(0)
    p.createCanvas(800, 600)
    p.ballList = []
    for i in range(999):
      newBall = Ball()
      p.ballList.append(newBall)
    
  def draw():
      p.background(0)
      p.strokeWeight(5)

      for ball in p.ballList:
        ball.moveBall()
        ball.drawBall()

      
    
  def mousePressed(self):
    pass
    

  def keyPressed(self):
    pass
    

  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
