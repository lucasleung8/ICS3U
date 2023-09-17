from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      #black filled circle
      p.blackEllipseX = 0
      p.blackEllipseY = 0
      p.blackEllipseDiam = 15
      #white filled circle
      p.whiteEllipseX = 0
      p.whiteEllipseY = p.height
      p.whiteEllipseDiam = 60
      p.whiteEllipsePrevX = 0
      #bg
      p.createCanvas(320, 626)
      p.background(150)

    #custom function
    def blackCircle():
      p.stroke(255)
      p.strokeWeight(1)
      p.fill('black')
      if (p.blackEllipseY <= p.height/2) and (p.blackEllipseX <= p.width):
        p.ellipse(p.blackEllipseX, p.blackEllipseY, p.blackEllipseDiam)
        p.blackEllipseX += 4
        p.blackEllipseY += 4
        p.blackEllipseDiam += 1
      else:
        p.blackEllipseX = p.random(0, p.width)
        p.blackEllipseY = p.random(0, p.height/2)
        p.blackEllipseDiam = 15

  #white circle function
    def whiteCircle():
      p.stroke(0)
      p.strokeWeight(1)
      p.fill('white')
      p.ellipse(p.whiteEllipsePrevX + p.whiteEllipseX, p.whiteEllipseY, p.whiteEllipseDiam)
      #continuously increase the X and Y value of white circle, also decrease diameter
      p.whiteEllipseX += 0.5
      p.whiteEllipseY -= 4
      p.whiteEllipseDiam -= 0.2

      #if circle reaches line, increment stored X value by 5 and reset posY to bottom of screen
      if (p.whiteEllipseY <= p.height/2):
        p.whiteEllipsePrevX += 5
        p.whiteEllipseY = p.height
        p.whiteEllipseDiam = 60

      #when circle reaches other side of window, return it to initial starting posX & posY
      if (p.whiteEllipseX >= p.width):
        p.whiteEllipsePrevX = 0
        p.whiteEllipseX = 0
        p.whiteEllipseY = p.height
        p.whiteEllipseDiam = 60
            
    def draw():
     #line
      p.stroke('green')
      p.strokeWeight(4)
      p.line(0, p.height/2, p.width, p.height/2)
      
    #create the circles 
      blackCircle()
      whiteCircle()
      
    def mousePressed(self):
      pass
    

    def keyPressed(self):
      pass
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
