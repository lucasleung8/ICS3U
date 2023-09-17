from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(800, 800)
      p.colorMode("RGB")
      p.background(255)
      #red rectangles
      p.rectY = p.height - 125
      p.rectX = 50
      p.redAlpha = 255
      #triangles
      p.triAlpha = 0
      #ellipses
      p.circleCol = 150
      #line
      p.lineCol = 0
      
      #rectangles
      for i in range (0,7):
        p.fill(p.redAlpha, 0, 0)
        p.rect(p.rectX, p.rectY, 125, 125)
        p.rect(p.rectX + 600, p.rectY, 125, 125)
        p.rectY -= 125
        p.redAlpha -= 50
        
      #lines
      for linePosY in range(0, 800, 41):
        p.stroke(p.lineCol)
        p.line(p.rectX + 125, linePosY, p.width/2, p.height)
        p.line(650, linePosY, p.width/2, p.height)
        p.lineCol += 15
        
      #triangles
      for triX in range (p.rectX + 200, 600, 100):
        p.fill(0, 0, p.triAlpha)
        p.triangle(triX, 5, triX-25, 100, triX+25, 100)
        p.triAlpha += 75
      
      #ellipses
      p.stroke(0)
      for circlePos in range (p.rectX + 250, 550, 50):
        p.fill(0, p.circleCol, 0)
        p.ellipse(circlePos, 200, 50)
        p.circleCol += 10

    def draw():
      print(p.mouseX, p.mouseY)

    def mousePressed(self):
      pass

    def keyPressed(self):
      pass
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
