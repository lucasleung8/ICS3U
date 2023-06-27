#import conveniencestore class from seperate file, for code organization
from convenienceStore import convenienceStore

#defining variables/dictionaries for each object (convenience store)
openingHours = {
  'monday' : "7AM-11PM",
  'tuesday' : "7AM-11PM",
  'wednesday' : "7AM-11PM",
  'thursday' : "7AM-11PM",
  'friday' : "3AM-12PM",
  'saturday' : "6AM-3AM",
  'sunday' : "6AM-3AM",
}

beverages = {
  'tea' : 0.50,
  'coffee' : 2.49,
  'gatorade' : 9.99,
}

foods = {
  'hamburger' : 5.99,
  'chips' : 1.95,
  'granola bar' : 3.50,
}

circleKBeverages = {
  'hot chocolate' : 20.99,
  'sparkling water' : 14.99,
  'root beer' : 979.99,
}

circleKFoods = {
  'nachos' : 123.00,
  'tacos' : 100.99,
  'oreos' : 12.99,
}

circleKOpeningHours = {
  'monday' : "Closed",
  'tuesday' : "9AM-9PM",
  'wednesday' : "9AM-9PM",
  'thursday' : "9AM-9PM",
  'friday' : "9AM-9PM",
  'saturday' : "6AM-1AM",
  'sunday' : "6AM-1AM",
}

kiwkEMartBeverages = {
  'buzz cola' : 9.99,
  'ginger ale' : 2.00,
}

kwikEMartFoods = {
  'pita' : 1.25,
  'doughnuts' : 11.99,
}

kwikEMartOpeningHours = {
  'monday' : "Closed",
  'tuesday' : "10AM-9PM",
  'wednesday' : "Closed",
  'thursday' : "10AM-9PM",
  'friday' : "Closed",
  'saturday' : "6AM-1AM",
  'sunday' : "Closed",
}

#objects for testing
sevenEleven = convenienceStore("7/11", beverages, foods, "742 Evergreen Terrace", openingHours, "416-439-0000", 100000, 80000)
circleK = convenienceStore("Circle K", circleKBeverages, circleKFoods, "123 sesame street", circleKOpeningHours, "647-999-9120", 200000, 190000)
kwikEMart = convenienceStore("Kwik-E-Mart", kiwkEMartBeverages, kwikEMartFoods, "234 oak ave", kwikEMartOpeningHours, "333-333-3333", 100, 200)

#tests for averagePriceAllItems method
assert sevenEleven.averagePriceAllItems() == "$4"
assert circleK.averagePriceAllItems() == "$209"
assert kwikEMart.averagePriceAllItems() == "$6"

#tests for annualProfit method
assert sevenEleven.annualProfit() == "$20000"
assert circleK.annualProfit() == "$10000"
assert kwikEMart.annualProfit() == "$-100"

#tests for checkAvailability method
assert sevenEleven.checkAvailability("tea") == "Yes, tea is in stock at 7/11 at 742 Evergreen Terrace, for the low low price of $0.5."
assert circleK.checkAvailability("oreos") == "Yes, oreos is in stock at Circle K at 123 sesame street, for the low low price of $12.99."
assert kwikEMart.checkAvailability("funnel cake") == "Sorry, your desired item, funnel cake, is out of stock"

#tests for highestPrice method
assert sevenEleven.highestPrice() == "$9.99"
assert circleK.highestPrice() == "$979.99"
assert kwikEMart.highestPrice() == "$11.99"

#tests for hoursOpen method
assert sevenEleven.hoursOpen("friday") == "On friday, 7/11 at 742 Evergreen Terrace is open 3AM-12PM"
assert circleK.hoursOpen("MOndAy") == "On monday, Circle K at 123 sesame street is closed"
assert circleK.hoursOpen("isernhuday") == "isernhuday is invalid, please enter a valid day of the week"

# print(circleK)
# print(sevenEleven)
# print(kwikEMart)