#  Money Printing Sim
#  Description: ICS3U Final Project, an incremental game similar to Cookie Clicker, but printing money instead of cookies
#  Author: Lucas Leung
#  Date: 16 June 2023

#-----------------------Import Libraries-----------------------#
from browser import document, window, alert
import random
import math
import time
#import playsound - Does not work in this environment, otherwise would've added music, mute toggle, SFX, etc.

#-----------------------Setup-----------------------#
def sketch(p):

    def preload():
      # Access the game save
      p.save = open("saveFile.txt")
      # Ensure fonts/sprites load before being used
      p.moneyCounterFont = p.loadFont('BentonSansCond-Bold.ttf')
      p.gameTitleFont = p.loadFont('MonomaniacOne-Regular.ttf')
      p.mediumFont = p.loadFont('Geologica-Medium.ttf')
      p.regularFont = p.loadFont('Geologica-Regular.ttf')
      p.titleScreenMoney = p.loadImage('titleScreenMoney.png')
      p.printer = p.loadImage('printer.png')
      p.printer2 = p.loadImage('printer2.png')
      p.printer3 = p.loadImage('printer3.png')
      p.arrowKeys = p.loadImage('arrowKeys.png')
      p.cursor = p.loadImage('cursor.png')
      p.moneyIcon = p.loadImage('moneyStack.png')
      p.fiveBankNote = p.loadImage('$5.png')
      p.tenBankNote = p.loadImage('$10.png')
      p.twentyBankNote = p.loadImage('$20.png')
      p.fiftyBankNote = p.loadImage('$50.png')
      p.hundredBankNote = p.loadImage('$100.png')
      p.statsIcon = p.loadImage('stats.webp')

    def setup():
      # Basic setup such as window properties, allignment, etc.
      p.backgroundColor = 230
      p.createCanvas(1280, 720)
      p.background(p.backgroundColor)
      p.clickTextList = []; p.bankNoteList = []; p.achievementNotificationList = [];
      p.imageMode(p.CENTER); p.rectMode(p.CENTER); p.textAlign(p.CENTER, p.CENTER)
      p.gameState = 0
      p.selectedTitleScreenButton = 0
      p.selectedGameplayButton = 0
      p.printerMouseCollide = False
      p.storedMillis = 0
      p.startTime = time.time()
      p.autoSaveInterval = 10
      p.blackColor = 0
      # Lines of ordered text which appear on the About screen
      p.aboutText = ["Lucas Leung","June 16, 2023","Mr. Marco Arsenault","ICS3U", "Sem. 2"]

      # Title screen setup
      p.gameTitleSize = (p.width + p.height)/25
      p.gameTitlePosX = p.width/2
      p.gameTitlePosY = p.height/3.5
      p.gameTitleColor = 0
      # Title screen menu buttons
      p.selectedTitleScreenButton = 0
      p.titleScreenButtonsLocked = False
      p.titleScreenButtonMouseDist = 100
      # Size/fade values for menu button animations
      p.menuButtonFontSize = p.gameTitleSize/2
      p.minTitleScreenButtonWidth = p.width/7.5
      p.maxButtonWidth = p.minTitleScreenButtonWidth + p.minTitleScreenButtonWidth/2.5
      p.playButtonWidth = p.minTitleScreenButtonWidth; p.aboutButtonWidth = p.minTitleScreenButtonWidth; p.exitButtonWidth = p.minTitleScreenButtonWidth
      p.playButtonAlpha = 255; p.aboutButtonAlpha = 255; p.exitButtonAlpha = 255; 
      p.minTitleScreenButtonAlpha = 70
      p.buttonWidthSpeed = 13
      p.buttonAlphaSpeed = 20

      # Set height where printed bank note sprite is removed
      p.maxBankNoteHeight = 0

      # Values for displaying printer sprite
      p.printerMouseCollideDist = 100
      p.printerWidth = p.width/7.11
      p.printerHeight = p.height/4
      p.printerPosX = p.width/8
      p.printerPosY = p.height/1.2
      p.printerAlpha = 255
      
      # Values for mouse hover/click printer animation
      p.printerFadeAnimSpeed = 6
      p.printerSizeAnimSpeed = 8
      p.printerMaxFade = p.printerAlpha
      p.printerMinFade = p.printerAlpha - p.printerAlpha/4
      p.printerMaxWidth = p.printerWidth
      p.printerMinWidth = p.printerWidth - 0.10 * p.printerWidth
      p.printerMaxHeight = p.printerHeight
      p.printerMinHeight = p.printerHeight - 0.10 * p.printerHeight

      # Text showing money earned which pops up from cursor when printer is clicked
      p.clickTextSpeed = 3

      # Main number during gameplay that shows total money
      p.moneyCounterSize = 75
      p.moneyCounterPosX = p.width/2
      p.moneyCounterPosY = p.height/5
      p.moneyCounterColor = 0

      # Money/second (MpS) text shown during gameplay
      p.MpSSize = p.moneyCounterSize/2.5
      p.MpSPosX = p.moneyCounterPosX
      p.MpSPosY = p.moneyCounterPosY + 60
      p.MpSColor = 0

      # Upgrades/statistics buttons shown during gameplay
      p.statsButtonWidth = p.width/7
      p.upgradeButtonWidth = p.statsButtonWidth * 2
      p.gameplayButtonFontSize = p.gameTitleSize/3
      p.gameplayButtonMouseDist = 80
      p.upgradeButtonAlpha = 255; p.statsButtonAlpha = 255
      p.minGameplayButtonAlpha = 70      
      
      # Values for displaying achievement notification popups
      p.achievementColor = 176, 191, 207
      p.achievementFontSize = 24
      p.achievementSpeed = 10
      p.achievementDuration = 4

      # Load gameplay data from save file such as total money earned
      p.money = int(p.save.readlines()[1])
      p.moneyPerSecond = int(p.save.readlines()[3])
      p.moneyPerPrint = int(p.save.readlines()[5])
      p.currentPrinter = p.printer
      p.printDelay = int(p.save.readlines()[7])
      p.currentBankNote = p.fiveBankNote
      p.bankNoteSpeed = int(p.save.readlines()[11])
      p.totalPrints = int(p.save.readlines()[13])
      p.unlockedAchievements = []
      p.unlockedUpgrades = []
      p.save.close()

      # All unlockable achievements - format is num:name
      p.achievements = {
        "1": "Thanks for playing", # play the game at least once
        "2": "Avid reader", # open the about screen
        "3": "Humble beginnings", # print your first banknote
        "4": "Co-ordinated counterfeiting", # get $10/s
        "5": "Dedicated", # play game for at least 1 hour
        "6": "30 second mark", # play game for at least 30 seconds
        "7": "3 figures", # earn at least $100
      }
      p.numAchievements = 7
      
      # All buyable upgrades - format is name:description
      p.upgrades = {
        "Accurate sizing": "Banknotes are worth 3x more.",
        "Lighter paper": "Banknotes travel 2x faster.",
        "Color changing ink": "Squares your current MpP (money per print).",
        "$10 bill": "Banknotes are worth $10 more.",
        "$20 bill": "Banknotes are worth $20 more.",
        "$50 bill": "Banknotes are worth $50 more.",
        "$100 bill": "Banknotes are worth $100 more.",
        "Achievement bonus": "You gain more MpS (money per second) the more achievements you have.",
        "autoPrint.py": "Automatically print banknotes every 0.2s. You can still manually print.",
      }

    #-----------------------Classes-----------------------#
  
    # Text showing money earned that pops up from the cursor when bank note reaches the top
    class clickText:
      def __init__(self):
        self.posX = random.randint(p.mouseX-12, p.mouseX+12)
        self.posY = p.mouseY
        self.color = "green"
        self.size = (p.width+p.height)/111
        self.speedY = p.clickTextSpeed

      # Draw the click text
      def display(self):
        p.fill(self.color)
        p.textSize(self.size)
        p.textFont(p.moneyCounterFont)
        p.text(f"+{p.moneyPerPrint}", self.posX, self.posY)

      def move(self):
        self.posY -= self.speedY

      # remove the click text when target height is reached
      def maxHeightReached(self):
        if self.posY < p.height/3:
          return True
        else:
          return False

    # Bank note sprite which fires up out of the printer when printer is left-clicked or space is pressed
    class bankNote:
      def __init__(self):
        self.posX = p.printerPosX
        self.posY = p.printerPosY
        self.width = p.printerWidth/1.5
        self.height = p.printerHeight

      def display(self):
        p.image(p.currentBankNote, self.posX, self.posY, self.width, self.height)

      # Move banknote to top of screen
      def move(self):
        self.posY -= p.bankNoteSpeed

      # Return when banknote reaches top of screen
      def maxHeightReached(self):
        if self.posY < p.maxBankNoteHeight:
          return True
        else:
          return False

    # Popup which appears when achievements are earned by the player
    class achievementNotification:
      def __init__(self, name):
        self.name = name
        self.posX = p.width - p.width/8
        self.posY = p.height + p.height/7
        self.width = p.width/4
        self.height = p.height/5
        # Num of seconds popup will appear for
        self.timeLimit = timeElapsed() + p.achievementDuration

      # Draw the popup box and show name of the unlocked achievement
      def display(self):
        p.fill(p.achievementColor)
        p.rect(self.posX, self.posY, self.width, self.height)
        p.fill(p.blackColor)
        p.textSize(p.achievementFontSize)
        p.strokeWeight(1)
        p.textFont(p.mediumFont)
        p.text("Achievement Unlocked!", self.posX, self.posY - 40)
        p.textFont(p.regularFont)
        p.text(self.name, self.posX, self.posY)

      # Remove achievement box when it's hidden from view
      def remove(self):
        if (timeElapsed() > self.timeLimit) and (self.posY > p.height + p.height/7):
          return True
      
      # Move achievement popup up on screen and move back down after specified time limit
      def move(self):
        if timeElapsed() < self.timeLimit and (self.posY > p.height/1.08):
          self.posY -= p.achievementSpeed
        elif timeElapsed() > self.timeLimit:
          self.posY += p.achievementSpeed

    #-----------------------Custom Functions-----------------------#
  
    # Returns number of seconds since the program started
    def timeElapsed():
      return time.time() - p.startTime

    # Auto save game progress to save file at a set frequency
    # def autoSave():
    #   if p.autoSaveInterval < timeElapsed():
    #     # Returns a temporary list containing saved game data and overwrites the temp list with current game data
    #     p.save = open("saveFile.txt")
    #     p.newSave = p.save.readlines()
    #     p.newSave[1] = (f"{p.money}\n")
    #     p.newSave = "".join(p.newSave)
    #     p.save.close()
    #     # write current progress back to the savefile.txt
    #     p.save = open("saveFile.txt", "w")
    #     p.save.write(p.newSave)
    #     print(p.save.readlines())
    #     print(int(p.save.readlines()[1]))
    #     p.save.close()
    #     p.autoSaveInterval = timeElapsed() + 10

    # Determine when to unlock achievements and display them
    def achievementFunction():
      # Move and display each achievement notification box popup
      for achievement in p.achievementNotificationList:
        achievement.display()
        achievement.move()
        # remove popup when it goes below screen
        if achievement.remove():
          p.achievementNotificationList.remove(achievement)

      # Condition to unlock achievement 7
      if p.money >= 100 and p.achievements["7"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["7"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["7"])
      
      # Condition to unlock achievement 6
      if timeElapsed() >= 30 and p.achievements["6"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["6"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["6"])

      # Condition to unlock achievement 5
      if timeElapsed() >= 3600 and p.achievements["5"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["5"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["5"])

    # Game title/text & logo displayed on title screen
    def gameTitle():
      p.noStroke()
      p.fill(p.gameTitleColor)
      p.textSize(p.gameTitleSize)
      p.textFont(p.gameTitleFont)
      p.text("Money Printing Sim", p.gameTitlePosX, p.gameTitlePosY)
      p.image(p.titleScreenMoney, p.gameTitlePosX, p.gameTitlePosY - 90, p.gameTitleSize + 30, p.gameTitleSize + 30)
      
    # Show arrow key/enter menu controls in bottom left corner
    def titleScreenInstructions():
      p.noFill()
      p.rect(p.gameTitlePosX/7, p.gameTitlePosY * 3.2, p.arrowKeys.width/3, p.arrowKeys.height/7.5)
      p.image(p.arrowKeys, p.gameTitlePosX/4.2, p.gameTitlePosY * 3.2, p.arrowKeys.width/12, p.arrowKeys.height/12)
      p.image(p.cursor, p.gameTitlePosX/2.9, p.gameTitlePosY * 3.2, p.cursor.width/11, p.cursor.height/11)
      p.textSize(p.gameTitleSize/3)
      p.textFont(p.mediumFont)
      p.fill(p.blackColor)
      p.text("Select", p.gameTitlePosX/11, p.gameTitlePosY * 3.2)

    # Contains all the buttons on the title screen, functionality for selecting the buttons, and changing game state accordingly
    def titleScreenButtons():
      playButton()
      aboutButton()
      exitButton()

      # Ensure menu selection with arrow keys won't skip to the first or last button
      if p.keyIsPressed == False:
        p.titleScreenButtonsLocked = False

      # Change menu button selection via arrow keys - only once each time the up/down arrow is released
      if p.titleScreenButtonsLocked == False:
        if p.keyIsDown(p.UP_ARROW) and p.selectedTitleScreenButton != 0:
          p.selectedTitleScreenButton -= 1
          p.titleScreenButtonsLocked = True
        elif p.keyIsDown(p.DOWN_ARROW) and p.selectedTitleScreenButton != 2:
          p.selectedTitleScreenButton += 1
          p.titleScreenButtonsLocked = True

      # Hovering mouse over the title screen buttons highlights them
      if mouseTouchingPlayButton():
        p.selectedTitleScreenButton = 0
      elif mouseTouchingAboutButton():
        p.selectedTitleScreenButton = 1
      elif mouseTouchingExitButton():
        p.selectedTitleScreenButton = 2
  
      # When a button is highlighted, pressing Enter or left clicking it switches the screen accordingly
      if (p.keyIsPressed and p.keyCode == p.ENTER) or (p.mouseIsPressed and p.mouseButton == p.LEFT and mouseTouchingPlayButton()) or (p.mouseIsPressed and p.mouseButton == p.LEFT and mouseTouchingAboutButton()) or (p.mouseIsPressed and p.mouseButton == p.LEFT and mouseTouchingExitButton()):
        if p.selectedTitleScreenButton == 0:
          p.gameState = 1
        elif p.selectedTitleScreenButton == 1:
          p.gameState = 2
        elif p.selectedTitleScreenButton == 2:
          p.gameState = 3

    def playButton():
      p.strokeWeight(4)
      p.stroke(255)
      p.fill(87, 255, 95, p.playButtonAlpha)
      p.rect(p.gameTitlePosX, p.gameTitlePosY * 1.9, p.playButtonWidth, p.height/7.2)
      p.fill(p.blackColor)
      p.textSize(p.menuButtonFontSize)
      p.textFont(p.mediumFont)
      p.text("Play", p.gameTitlePosX, p.gameTitlePosY * 1.9)
      
      # Show size animation when play button selected
      if p.selectedTitleScreenButton == 0:
        if p.playButtonWidth < p.maxButtonWidth:
          p.playButtonWidth += p.buttonWidthSpeed
        # Shrink all other buttons
        if p.aboutButtonWidth > p.minTitleScreenButtonWidth:
          p.aboutButtonWidth -= p.buttonWidthSpeed
        elif p.exitButtonWidth > p.minTitleScreenButtonWidth:
          p.exitButtonWidth -= p.buttonWidthSpeed

        # Show fade animation when Play button selected, increase alpha of other buttons
        if p.playButtonAlpha > p.minTitleScreenButtonAlpha:
          p.playButtonAlpha -= p.buttonAlphaSpeed
        if p.aboutButtonAlpha < 255:
          p.aboutButtonAlpha += p.buttonAlphaSpeed
        elif p.exitButtonAlpha < 255:
          p.exitButtonAlpha += p.buttonAlphaSpeed

    def aboutButton():
      p.fill(38, 78, 255, p.aboutButtonAlpha)
      p.rect(p.gameTitlePosX, p.gameTitlePosY * 2.5, p.aboutButtonWidth, p.height/7.2)
      p.fill(p.blackColor)
      p.strokeWeight(4)
      p.stroke(255)
      p.textSize(p.menuButtonFontSize)
      p.textFont(p.mediumFont)
      p.text("About", p.gameTitlePosX, p.gameTitlePosY * 2.5)
      
      # Show size animation when About button selected
      if p.selectedTitleScreenButton == 1:
        if p.aboutButtonWidth < p.maxButtonWidth:
          p.aboutButtonWidth += p.buttonWidthSpeed
        # Shrink all other buttons
        if p.playButtonWidth > p.minTitleScreenButtonWidth:
          p.playButtonWidth -= p.buttonWidthSpeed
        if p.exitButtonWidth > p.minTitleScreenButtonWidth:
          p.exitButtonWidth -= p.buttonWidthSpeed

        # Show fade animation when About button selected, increase alpha of all other buttons
        if p.aboutButtonAlpha > p.minTitleScreenButtonAlpha:
          p.aboutButtonAlpha -= p.buttonAlphaSpeed
        if p.playButtonAlpha < 255:
          p.playButtonAlpha += p.buttonAlphaSpeed
        elif p.exitButtonAlpha < 255:
          p.exitButtonAlpha += p.buttonAlphaSpeed

    def exitButton():
      p.fill(255, 30, 0, p.exitButtonAlpha)
      p.rect(p.gameTitlePosX, p.gameTitlePosY * 3.1, p.exitButtonWidth, p.height/7.2)
      p.fill(p.blackColor)
      p.strokeWeight(4)
      p.stroke(255)
      p.textSize(p.menuButtonFontSize)
      p.textFont(p.mediumFont)
      p.text("Exit", p.gameTitlePosX, p.gameTitlePosY * 3.1)

      # Show size animation when Exit button selected
      if p.selectedTitleScreenButton == 2:
        if p.exitButtonWidth < p.maxButtonWidth:
          p.exitButtonWidth += p.buttonWidthSpeed
        # Shrink all other buttons
        if p.playButtonWidth > p.minTitleScreenButtonWidth:
          p.playButtonWidth -= p.buttonWidthSpeed
        if p.aboutButtonWidth > p.minTitleScreenButtonWidth:
          p.aboutButtonWidth -= p.buttonWidthSpeed
          
        # Show fade VFX when Exit button selected, increase alpha of all other buttons
        if p.exitButtonAlpha > p.minTitleScreenButtonAlpha:
          p.exitButtonAlpha -= p.buttonAlphaSpeed
        if p.playButtonAlpha < 255:
          p.playButtonAlpha += p.buttonAlphaSpeed
        elif p.aboutButtonAlpha < 255:
          p.aboutButtonAlpha += p.buttonAlphaSpeed

    # Detect mouse collision with Play button
    def mouseTouchingPlayButton():
      if p.dist(p.mouseX, p.mouseY, p.gameTitlePosX, p.gameTitlePosY * 1.9) < p.titleScreenButtonMouseDist:
        return True
      else:
        return False

    # Detect mouse collision with About button
    def mouseTouchingAboutButton():
      if p.dist(p.mouseX, p.mouseY, p.gameTitlePosX, p.gameTitlePosY * 2.5) < p.titleScreenButtonMouseDist:
        return True
      else:
        return False

    # Detect mouse collision with Exit button
    def mouseTouchingExitButton():
      if p.dist(p.mouseX, p.mouseY, p.gameTitlePosX, p.gameTitlePosY * 3.1) < p.titleScreenButtonMouseDist:
        return True
      else:
        return False

    # Perform money earning calculation and increment money
    def moneyPerSecond():
      if p.storedMillis + 100 <= p.millis():
        p.money += p.moneyPerSecond / 10
        p.storedMillis = p.millis()
      # Draw the money per second counter
      p.fill(p.MpSColor)
      p.textSize(p.MpSSize)
      p.textFont(p.moneyCounterFont)
      p.text(f"Money per second: ${p.moneyPerSecond}", p.MpSPosX, p.MpSPosY)

    # In-game text displaying total amount of money earned
    def moneyCounter():
      p.fill(p.moneyCounterColor)
      p.textSize(p.moneyCounterSize)
      p.textFont(p.moneyCounterFont)
      p.text(f"${round(p.money, 5)}", p.moneyCounterPosX, p.moneyCounterPosY)

    # Prints money sprite from the printer which moves towards top of screen
    def printBankNote():
      newBankNote = bankNote()
      p.bankNoteList.append(newBankNote)
      # Increment the amount of prints to show on Stats screen
      p.totalPrints += 1
  
    # Printer sprite which prints banknotes out of it when left-clicked or spacebar pressed
    def printer():
      p.tint(255, p.printerAlpha)
      p.image(p.currentPrinter, p.printerPosX, p.printerPosY, p.printerWidth, p.printerHeight)

      # Return if mouse colliding with printer
      if (p.dist(p.mouseX, p.mouseY, p.printerPosX, p.printerPosY) < p.printerMouseCollideDist):
        p.printerMouseCollide = True
      else:
        p.printerMouseCollide = False
      
      # Fade animation when hovering over printer with mouse
      if p.printerMouseCollide and p.printerAlpha > p.printerMinFade:
        p.printerAlpha -= p.printerFadeAnimSpeed
      elif p.printerMouseCollide == False and p.printerAlpha < p.printerMaxFade:
        p.printerAlpha += p.printerFadeAnimSpeed

      # Animate size of printer when clicked or spacebar pressed
      if ((p.mouseIsPressed and p.mouseButton == p.LEFT and p.printerMouseCollide) or p.keyIsDown(32)) and p.printerWidth >= p.printerMinWidth and p.printerHeight >= p.printerMinHeight:
        p.printerWidth -= p.printerSizeAnimSpeed
        p.printerHeight -= p.printerSizeAnimSpeed
      # Enlarge to max size when mouse isn't touching or spacebar released
      elif (p.mouseIsPressed == False or p.printerMouseCollide == False) and p.printerWidth <= p.printerMaxWidth and p.printerHeight <= p.printerMaxHeight:
        p.printerWidth += p.printerSizeAnimSpeed
        p.printerHeight += p.printerSizeAnimSpeed

      # Move/display each click text and remove when max height reached
      for text in p.clickTextList:
        text.move()
        text.display()
        if text.maxHeightReached():
          p.clickTextList.remove(text)

      # Move and display each printed bank note
      for bankNote in p.bankNoteList:
        bankNote.move()
        bankNote.display()
        # Remove bank note when target height reached and display popup text showing money earned
        if bankNote.maxHeightReached():
          p.money += p.moneyPerPrint
          p.bankNoteList.remove(bankNote)
          newText = clickText()
          p.clickTextList.append(newText)

    # Draw in-game Upgrade button - WIP
    def upgradeButton():
      p.fill(252, 140, 3, p.upgradeButtonAlpha)
      p.rect(p.width/1.06, p.height/2, p.upgradeButtonWidth, p.height/7, 15)
      p.fill(p.blackColor)
      p.stroke(255)
      p.textSize(p.gameplayButtonFontSize)
      p.textFont(p.mediumFont)
      p.text("Upgrade\n[U]", p.width/1.06, p.height/2)
      p.strokeWeight(4)

    # Draw in-game Stats button
    def statsButton():
      p.fill(186, 3, 252, p.statsButtonAlpha)
      p.rect(p.width/1.06, p.height/1.5, p.statsButtonWidth, p.height/7, 15)
      p.fill(p.blackColor)
      p.strokeWeight(3)
      p.stroke(255)
      p.textSize(p.gameplayButtonFontSize)
      p.textFont(p.mediumFont)
      p.text("Stats\n[S]", p.width/1.06, p.height/1.5)
      p.strokeWeight(4)

    # Detect mouse collision with Upgrade button
    def mouseTouchingUpgradeButton():
      if p.dist(p.mouseX, p.mouseY, p.width/1.06, p.height/2) < p.gameplayButtonMouseDist:
        return True
      else:
        return False

    # Detect mouse collision with Stats button
    def mouseTouchingStatsButton():
      if p.dist(p.mouseX, p.mouseY, p.width/1.06, p.height/1.5) < p.gameplayButtonMouseDist:
        return True
      else:
        return False
  
    # Contains all buttons that appear during gameplay. Displays upgrade/stats buttons, animates them, change game states
    def gameplayButtons():
      upgradeButton()
      statsButton()

      # Mouse hover fading animation for stats/upgrade, increases alpha of other buttons
      if p.selectedGameplayButton == "Upgrade":
        if p.upgradeButtonAlpha > p.minGameplayButtonAlpha:
          p.upgradeButtonAlpha -= p.buttonAlphaSpeed
        if p.statsButtonAlpha < 255:
          p.statsButtonAlpha += p.buttonAlphaSpeed
      elif p.selectedGameplayButton == "Stats":
        if p.statsButtonAlpha > p.minGameplayButtonAlpha:
          p.statsButtonAlpha -= p.buttonAlphaSpeed
        if p.upgradeButtonAlpha < 255:
          p.upgradeButtonAlpha += p.buttonAlphaSpeed      

      # Hovering mouse over menu buttons highlights them and left clicking chooses them
      if mouseTouchingUpgradeButton():
        p.selectedGameplayButton = "Upgrade"
        if p.mouseIsPressed and p.mouseButton == p.LEFT:
          pass # Upgrade screen WIP
      elif mouseTouchingStatsButton():
        p.selectedGameplayButton = "Stats"
        if p.mouseIsPressed and p.mouseButton == p.LEFT:
          p.gameState = 4

      # Keyboard shortcuts to open the Upgrade and Stats screens
      if p.keyIsPressed and (p.key == 'u' or p.key == 'U'):
        pass # Upgrade screen WIP
      elif p.keyIsPressed and (p.key == 's' or p.key == 'S'):
        p.gameState = 4
      

  #-----------------------Game States-----------------------#

  # Title screen with Play, About and Exit buttons, num of achievements, and menu navigation help
    def titleScreen():
      gameTitle()
      titleScreenButtons()
      titleScreenInstructions()
      # show copyright & number of unlocked achivements
      p.textSize(p.gameTitleSize/4)
      p.text("©Lucas Leung 2023", p.width - 100, p.height - 20)
      p.textSize(p.gameTitleSize/3)
      p.text(f"Achievements unlocked: {len(p.unlockedAchievements)} out of {p.numAchievements}", p.width - 1050, p.height - 200)

      # Clear all printer click text to ensure they don't remain when game is replayed
      for text in p.clickTextList:
        p.clickTextList.remove(text)

    # Main gameplay screen that starts when Play button is selected from the title screen
    def gameScreen():
      moneyPerSecond()
      moneyCounter()
      printer()
      gameplayButtons()
      #autoSave()
      
      # Pressing Esc returns to title screen
      if p.keyIsPressed and p.keyCode == 27:
        p.gameState = 0

    # Screen that shows extra info about the game when About button selected from the title screen
    def aboutScreen(): 
      p.aboutTextPosY = p.height/2
      p.noStroke()
      p.textSize(32)
      p.textFont(p.regularFont)
      p.text("Money Printing Sim is my first ever attempt at creating a somewhat polished game. As I've always been drawn to games that involve calculations, data, stats, etc., I was inspired by incremental games the likes of Cookie Clicker and Clicker Heroes.", 650, 150, p.width, p.height)
      # Display each string from list as a new line on-screen
      for line in p.aboutText:
        p.text(line, 650, p.aboutTextPosY, p.width-50, p.height-50)
        p.aboutTextPosY += 50
      p.textSize(24)
      p.text("Press Esc to return to title screen", 650, p.aboutTextPosY+50)

      # Pressing Esc key returns to title screen
      if p.keyIsPressed and p.keyCode == 27:
        p.gameState = 0

    # List icon and text showing gameplay statistics, appearing when Stats button is selected
    def statsScreen():
      p.noStroke()
      p.textSize(32)
      p.textFont(p.regularFont)
      p.image(p.statsIcon, 650, 100, 150, 150)
      p.text(f"Playtime (minutes): {round(timeElapsed() / 60)}", 650, 250, p.width, p.height)
      p.text(f"Money per print: ${p.moneyPerPrint}", 650, 300, p.width, p.height)
      p.text(f"Achievements unlocked: {len(p.unlockedAchievements)} out of {p.numAchievements} ({round((len(p.unlockedAchievements) / p.numAchievements) * 100)}%)", 650, 350, p.width, p.height)
      p.text(f"Total prints: {p.totalPrints}", 650, 400, p.width, p.height)
      p.text(f"Banknote speed: {p.bankNoteSpeed}", 650, 450, p.width, p.height)
      p.textSize(24)
      p.text("Press r to return to game", 650, 700)

      # Pressing r returns to gameplay screen
      if p.keyIsPressed and (p.key == 'r' or p.key == 'R'):
        p.gameState = 1
  
    #-----------------------Main Sketch | draw()-----------------------#

    def draw():
      p.background(p.backgroundColor)
      achievementFunction()
      
      # Change game screen according to whatever menu option is chosen by player (play, about, exit, stats)
      if p.gameState == 0: # starting screen
        titleScreen()
        #  Condition to unlock achievement 1
        if p.achievements["1"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["1"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["1"])
      elif p.gameState == 1:
        gameScreen()
      elif p.gameState == 2:
        aboutScreen()
        # Condition to unlock achievement 2
        if p.achievements["2"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["2"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["2"])
      elif p.gameState == 3:
        p.remove()
      elif p.gameState == 4:
        statsScreen()

    # Print bank note when printer is left clicked
    def mouseClicked(self):
      if p.printerMouseCollide:
        printBankNote()
        # unlock achievement 3
        if p.achievements["3"] not in p.unlockedAchievements:
          newAchievement = achievementNotification(p.achievements["3"])
          p.achievementNotificationList.append(newAchievement)
          p.unlockedAchievements.append(p.achievements["3"])

    def mousePressed(self):
      pass

    def keyPressed(self):
      pass

    # Print bank note when spacebar pressed in-game
    def keyReleased(self):
      if p.gameState == 1 and p.keyCode == 32:
        printBankNote()

    p.setup = setup
    p.draw = draw
    p.preload = preload
    p.mousePressed = mousePressed
    p.mouseClicked = mouseClicked
    p.keyPressed = keyPressed
    p.keyReleased = keyReleased

myp5 = window.p5.new(sketch)
