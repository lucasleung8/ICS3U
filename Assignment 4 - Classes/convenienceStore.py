class convenienceStore:
  def __init__(self, storeName, beverages, foods, streetAddress, openingHours, phoneNum, annualRevenue, annualExpenses):
    self.__storeName = storeName
    self.__beverages = beverages
    self.__foods = foods
    self.__streetAddress = streetAddress
    self.__openingHours = openingHours
    self.__phoneNum = phoneNum
    self.__annualRevenue = annualRevenue
    self.__annualExpenses = annualExpenses

  #getters for each attribute
  def getStoreName(self):
    return self.__storeName
    
  def getBeverages(self):
    return self.__beverages

  def getFoods(self):
    return self.__foods

  def getStreetAddress(self):
    return self.__streetAddress

  def getOpeningHours(self):
    return self.__openingHours

  def getPhoneNum(self):
    return self.__phoneNum

  def getAnnualRevenue(self):
    return self.__annualRevenue
  
  def getAnnualExpenses(self):
    return self.__annualExpenses
  
  #setters for each attribute
  def setStoreName(self, newStoreName):
    self.__storeName = newStoreName

  def setBeverages(self, newBeverages):
    self.__beverages = newBeverages

  def setFoods(self, newFoods):
    self.__foods = newFoods

  def setStreetAddress(self, newStreetAddress):
    self.__streetAddress = newStreetAddress

  def setOpeningHours(self, newOpeningHours):
    self.__openingHours = newOpeningHours
  
  def setPhoneNum(self, newPhoneNum):
    self.__phoneNum = newPhoneNum

  def setAnnualRevenue(self, newAnnualRevenue):
    self.__annualRevenue = newAnnualRevenue
  
  def setAnnualExpenses(self, newAnnualExpenses):
    self.__annualExpenses = newAnnualExpenses

  
  #calculate & return annual profit based on revenue and costs
  def annualProfit(self):
    profit = (self.__annualRevenue) - (self.__annualExpenses)
    return (f"${profit}")

  #returns the rounded average of the values (prices) in self.__foods and self.__beverages
  def averagePriceAllItems(self):
    sum = 0
    count = len(self.__foods) + len(self.__beverages)
    for foodsPrice in self.__foods.values():
      sum += foodsPrice
    for beveragePrice in self.__beverages.values():
      sum += beveragePrice
    avg = (f"${round(sum/count)}")
    return avg

  #returns meaningful print statement for the class
  def __str__(self):
    return (f"Your local {self.__storeName} is conveniently located at {self.__streetAddress} for all your everyday needs. Call us at {self.__phoneNum}. Our opening hours are as follows: {self.__openingHours}")

  #return availability of chosen item 
  def checkAvailability(self, reqItem):
    reqItem = reqItem.lower().replace(".","").replace(",","").replace("!","").replace("?","").replace(":","").replace(";","").replace("&","").replace("  "," ")
    #check if chosen item is in list of beverages or foods offered
    for beverage in self.__beverages.keys():
      if beverage == reqItem:
        return f"Yes, {reqItem} is in stock at {self.__storeName} at {self.__streetAddress}, for the low low price of ${self.__beverages[beverage]}."
    else:
      for food in self.__foods.keys():
        if food == reqItem:
          return (f"Yes, {reqItem} is in stock at {self.__storeName} at {self.__streetAddress}, for the low low price of ${self.__foods[food]}.")
      #return message if chosen item is not offered 
      else:
        return (f"Sorry, your desired item, {reqItem}, is out of stock")

  #returns highest price of food or drink offered by convenince store
  def highestPrice(self):
    #if highest priced food is more expensive than highest priced beverage, return price of foods
    if max(self.__foods.values()) > max(self.__beverages.values()):
      return(f"${max(self.__foods.values())}")
    #if highest priced food is cheaper than highest priced beverage, return price of beverage
    elif max(self.__foods.values()) < max(self.__beverages.values()):
      return(f"${max(self.__beverages.values())}")
    else:
    #if max price is tied, return highest food price
      return (f"${max(self.__foods.values())}")

  #returns store opening hours of the chosen day of week
  def hoursOpen(self, day):
    day = day.lower().replace(" ","").replace(".","").replace(",","").replace("!","").replace("?","").replace(":","").replace(";","").replace("&","").replace("  ","").replace(" ","")
    #if selected day is in opening hours, return the opening hours and whether its closed.
    if day in self.__openingHours and self.__openingHours[day] != "Closed":
      return (f"On {day}, {self.__storeName} at {self.__streetAddress} is open {self.__openingHours[day]}")
    elif day in self.__openingHours and self.__openingHours[day] == "Closed":
      return(f"On {day}, {self.__storeName} at {self.__streetAddress} is closed")
     # if chosen day is not a day of the week, return error
    else:
      return(f"{day} is invalid, please enter a valid day of the week")