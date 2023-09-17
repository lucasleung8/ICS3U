from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(700, 410)
      p.frameRate(999)

    def draw():
      rando = random.randint(0, 1)
      p.fill(p.random(0, 255), p.random(0,255), p.random(0, 255))
      if rando == 1:
        p.ellipse(p.random(0, p.width), p.random(0, p.height), 30)
      else:
        p.rect(p.random(0, p.width), p.random(0, p.height), 30, 30)

    def mousePressed(self):
      p.background(255)
    

    def keyPressed(self):
      p.fill(p.random(0, 255), p.random(0,255), p.random(0, 255))
      p.rect(0, 0, p.random(0, p.width), p.random(0, p.height))
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)