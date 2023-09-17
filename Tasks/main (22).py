from browser import document, window, alert
import random 

def sketch(p):
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(800, 600)
      p.background(255)
        
    def quadrants():
      #top left
      if p.mouseX < p.height/2 and p.mouseY < p.height/2:
        p.fill("red")
        p.rect(0, 0, p.width/2, p.height/2)
        #top right
      elif p.mouseX > p.width/2 and p.mouseY < p.height/2:
        p.fill("blue")
        p.rect(p.width/2, 0, p.width/2, p.height/2)
      #bottom left
      elif p.mouseX < p.width/2 and p.mouseY > p.height/2:
        p.fill("green")
        p.rect(0, p.height/2, p.width/2, p.height/2)
      #bottom right
      elif p.mouseX > p.width/2 and p.mouseY > p.height/2:
        p.fill("yellow")
        p.rect(p.width/2, p.height/2, p.width/2, p.height/2)

    def draw():
      p.background(0)
      quadrants()
    
    
    def mousePressed(self):
      pass
    

    def keyPressed(self):
      pass
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)