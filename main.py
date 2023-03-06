import ff
import DisplayList as Display

continueloop = True
while continueloop:

  userDetails = ff.GetDetails()
  Display.DisplayDetails(userDetails)

  choice = input("Are You Happy With these!? Y or N\n")

  if choice.lower() == "y" or choice.lower() == "n":
    print("Great man!")
    continueloop = False

  else:
    print("Invalid input, try again.")


  


  

