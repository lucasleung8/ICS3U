from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

  def setup():
    p.createCanvas(800, 600)
    p.background(150)

  def draw():
    p.background(150)
    p.stroke(0)
    p.strokeWeight(3)
    p.line(p.width/2, 0, p.width/2, p.height)

    if p.mouseX < p.width/2:
      p.ellipse(p.mouseX, p.mouseY, 30, 30)
    else:
      p.ellipse(p.width/2, p.mouseY, 30, 30)
    
  def mousePressed(self):
    pass
    

  def keyPressed(self):
    pass
    

  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
