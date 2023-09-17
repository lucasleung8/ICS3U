from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(320, 626)
      p.background(150)
      p.firstDiam = 40
      p.firstPosX = p.width/2
      p.firstPosY = p.height
      p.secondPosX = 0
      p.secondPosY = 0
      p.secondDiam = 5

    def draw():
      #top left circle
      p.circle(p.secondPosX, p.secondPosY, p.secondDiam)
      p.secondPosX += 1
      p.secondPosY += 1.5
      p.secondDiam += 0.07

      #middle  circlke
      p.circle(p.firstPosX, p.firstPosY, p.firstDiam)
      p.firstPosY -= 7
      p.firstPosX += 0.18
      if p.firstDiam >= 5:
        p.firstDiam -= 0.4

    
    def mousePressed(self):
      #reset and start over - just copy of setup()
      p.background(150)
      p.firstDiam = 40
      p.firstPosX = p.width/2
      p.firstPosY = p.height
      p.secondPosX = 0
      p.secondPosY = 0
      p.secondDiam = 5
    

    def keyPressed(self):
      pass
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
