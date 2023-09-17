#TODO:
#proper fix of boundary
#change square to green only when mouse is in it, fix clicking top left


from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(1200, 600)
      p.rectMode("CENTER")
      p.col = "black"
      p.x = p.width/2
      p.y = p.height/2
      p.speed = 3

    def draw():
      #green fill
      if (p.mouseIsPressed) and (p.dist(p.mouseX, p.mouseY, p.x, p.y) <= 75):
        p.col = "green"
      else:
        p.col = "black"

      #press q to sprint
      if p.keyIsPressed and p.key == 'q':
        p.speed = 20
        print("turbo")
      else:
        p.speed = 3

      #move square
      if p.keyIsPressed and (p.key == 'w' or p.key == 'W') and p.y >= 0:
        p.y -= p.speed
      elif p.keyIsPressed and (p.key == 'w' or p.key == 'W') and (p.key == 'd') and p.y >= 0:
        p.y -= p.speed
        p.x += p.speed
      elif p.keyIsPressed and (p.key == 's' or p.key == 'S') and p.y <= p.height - 75:
        p.y += p.speed
      elif p.keyIsPressed and (p.key == 'a' or p.key == 'A') and p.x >= 0:
        p.x -= p.speed
      elif p.keyIsPressed and (p.key == 'd' or p.key == 'D') and p.x <= p.width - 75:
        p.x += p.speed
      
      p.background("blue")
      p.fill(p.col)
      p.rect(p.x, p.y, 75, 75)

    def mousePressed(self):
      pass

    def keyPressed(self):
      pass
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
