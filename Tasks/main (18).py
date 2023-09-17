from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
      p.createCanvas(700, 410)
      p.background(150)
      # reset = 1

    def draw():
      # colorlist = ['purple','red', 'yellow', 'turquoise', 'orange']
      # while reset == 1:
      #   for i in colorlist:
      #     p.fill(i)
      #     if colorlist[i] == len(colorlist):
      #       i = colorlist[0]
      #       reset = 1
      p.fill(p.mouseX, p.mouseY,255)
      p.circle(p.mouseX, p.mouseY, p.width/38)



    

    p.setup = setup
    p.draw = draw
      
myp5 = window.p5.new(sketch)
