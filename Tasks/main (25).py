from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(700, 410)
      p.background(120)
      p.a = 5
      p.fillColor = 'black'

    def draw():
      print(p.a)

      if (p.mouseIsPressed):
        p.stroke("black")
      else:
        p.stroke("white")

      if (p.keyIsPressed and (p.key == 'r' or p.key == 'E')):
        p.fillColor = "red"
      elif (p.keyIsPressed and (p.key == 'g' or p.key == 'G')):
       p.fillColor = "green"
      elif (p.keyIsPressed and (p.key == 'b' or p.key == 'B')):
        p.fillColor = "blue"
      elif p.keyIsPressed and p.keyCode == 13:
        p.fillColor = "black"
      elif p.keyIsPressed and p.keyCode == 187 and p.a <= 20:
          p.strokeWeight(p.a)
          p.a += 1
      elif p.keyIsPressed and p.keyCode == 189 and p.a >= 5:
          p.strokeWeight(p.a)
          p.a -= 1
      p.fill(p.fillColor)
      p.ellipse(p.width/2, p.height/2, 100, 100)


    
    def mousePressed(self):
      pass
    
  
    def keyPressed(self):
      pass
      # if p.key==" ":
      #   print("Hallo")
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
