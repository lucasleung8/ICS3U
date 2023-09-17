## do not touch this import
from browser import document, window, alert

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(800, 600)
      p.background(0, 204, 255)

    def house(xpos, ypos, housewidth, househeight):
       #house box
      p.stroke("black")
      p.strokeWeight(1)
      p.fill(203,65,84)
      p.rect(xpos, ypos, housewidth, househeight)
      #door
      p.fill("white")
      doorWidth = housewidth / 5
      doorHeight = househeight / 2.5
      doorX = xpos+housewidth / 2.5
      doorY = ypos+househeight / 1.75
      p.rect(doorX, doorY, doorWidth, doorHeight)
      #doorknob WIP
      p.fill("black")
      p.ellipse(doorX+housewidth/6, doorY+househeight/4, househeight/13, househeight/13)
   #   roof
      p.triangle(xpos, ypos, xpos+housewidth/2, ypos-househeight/2, xpos+housewidth, ypos)
    
    def draw():
      print(p.mouseX, p.mouseY)
      #sun
      p.noStroke()
      p.fill("yellow")
      p.ellipse(159, 303, 100, 100)
      #ground grass 
      p.fill(0, 255, 72)
      p.rect(0, p.height/2, p.width, 605)
      #sun lines
      p.stroke("yellow")
      p.strokeWeight(3)
      p.line(108, 290, 70, 290)
      p.line(114, 280, 69, 267)
      p.line(122, 267, 81, 247)
      p.line(132, 258, 105, 225)
      p.line(149, 252, 143, 210)
      p.line(176, 255, 184, 210)
      p.line(193, 267, 218, 220)
      p.line(205, 282, 249, 242)
      p.line(208, 292, 250, 289)
      #custopm fuynction
      house(150, 80, 150, 100)

    ## do not touch these
    p.setup = setup
    p.draw = draw

## do not touch these
myp5 = window.p5.new(sketch)
