from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(415, 438)
      p.colorMode("RGB")
      p.background(200)
      p.thickness = 4

      #draw lines
      p.strokeWeight(p.thickness)
      #increment the range by thickness of line, so they don't overlap
      for yPos in range(0, p.height, p.thickness):
        p.line(0, yPos, p.random(0, p.width), yPos)

    def draw():
      pass

    
    def mousePressed(self):
      pass
    

    def keyPressed(self):
      pass
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
