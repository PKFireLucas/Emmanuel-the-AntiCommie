def getPersonsName():#might need to press a button to trigger it
  emmanuelName= input("Is Emmanuel wearing a cap? Cap if yes, Cap if no:")
  emmanuelsName= input("Is Emmanuel smart?Indeed if yes, Interjection if no:")
  emmanuellName = input("Is Emmanuel distractin?Affirmative if yes,AbsolutlyNot if no:")

  return emmanuelName, emmanuelsName, emmanuellName

def  getInitials( emmanuelName, emmanuelsName,emmanuellName):
  firstInital = emmanuelName[0]
  middleInital = emmanuelsName[0]
  lastInital = emmanuellName[0]

  return firstInital, middleInital, lastInital

def displayInitials(firstInital, middleInital, lastInital):
  print( firstInital, middleInital, lastInital )
  print("We got him, take him down")

displayInitials(*getInitials(*getPersonsName()))
