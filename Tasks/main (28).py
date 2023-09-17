from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.noStroke()
      p.createCanvas(360, 530)
      p.background(200)
      p.finished = False
      p.pinkEllipseSize = 0
      p.pinkEllipseOpacity = 100
      #top half circles/rectangles
      p.rectCol = 255
      p.rectYPos = 0
      p.rectHeight=20
      p.circleSize = 15
      p.circleColor = 0
      p.spacing = 4
      p.circleX = -1 * p.circleSize/2 #radius. done so first circle is drawn without a gap
      p.circleY = p.rectHeight/2 #half of each rectYPos increment, circle draws from rect centre

      #bottom half circle
      while p.pinkEllipseSize <= 250:
        p.fill(255, 0, 170, p.pinkEllipseOpacity)
        p.ellipse(p.width/2, p.height/2 + p.height/4, p.pinkEllipseSize)
        p.pinkEllipseOpacity -= 3
        p.pinkEllipseSize += 6

    def draw():
      print(f"circle y: {p.circleY}, circle x: {p.circleX}")
      
      #top half rectangles
      while p.rectYPos <= p.height/2:
        p.fill(p.rectCol)
        p.rect(0, p.rectYPos, p.width, p.rectHeight)
        p.rectCol -= 20
        p.rectYPos += p.rectHeight
        
      #WIP: use nested for loop to create grid of circles for the top half of the sketch:
      #draw circles accross row then move to next row
      #repeat until p.height/2 reached
      #i could not figure out in time so i used nested ifs instead
      
      #top half circles - remember ellipse is drawn from centre. so half of rectangle height
      #using while instead of if so all circles are drawn at once rather than 1 by 1
      while p.finished == False:
        if (p.circleY <= (p.height/2) + p.rectHeight/2) and (p.circleX <= p.width):
          p.circleX += p.circleSize + p.spacing
        elif (p.circleX > p.width): 
          p.circleX = p.circleSize/2 #reset to beginning of row
          p.circleColor += 15
          if not (p.circleY > p.height/2): #failsafe so it doesnt go below last rectangle
            p.circleY += p.rectHeight 
          else: #stop generating when last row is done
            p.finished = True
            
        p.fill(p.circleColor)
        p.ellipse(p.circleX, p.circleY, p.circleSize)


    def mousePressed(self):
      pass
    
    def keyPressed(self):
      pass
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
