

from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

  def setup():
    p.createCanvas(320, 626)
    p.background(230)
    p.size = 20
    p.alpha = 255
    p.y = 0
    p.x = 0

  def draw():
    p.background(230)
    p.fill(255, 0, 179, p.alpha) #change later to use %
    print(p.mouseX, p.mouseY)
    p.y = 10
    p.x = 0

      
    while p.x <= p.mouseX:
      while p.y <= p.mouseY:
        p.alpha = (p.width % p.mouseX)
        p.ellipse(p.x, p.y, 5)
          
        p.y += 10
        p.x += 10
        p.y = 10
        

      # p.maxX = p.mouseX % p.size
      # p.maxY = p.mouseY % p.size
      # print(f"{p.mouseX}, {p.mouseY}, maxX: {p.maxX}, maxY: {p.maxY}")
      # for x in range (0, p.mouseX, p.size):
          
    def mousePressed(self):
      pass
    

    def keyPressed(self):
      pass
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
