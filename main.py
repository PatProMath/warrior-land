print('''
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  / 
 __,-<_     )`-/  `./  /   
'  \   `---'   \   /  /   
    |           |./  /   
    /           //  /     
\_/' \         |/  /      
 |    |   _,^-'/  /     
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`  
   `Y-.____(__}
    |     {__)
          ()
''')
print('''                                                
                                                    88                         
                                                    ""                         
                                                                               
8b      db      d8 ,adPPYYba, 8b,dPPYba, 8b,dPPYba, 88  ,adPPYba,  8b,dPPYba,  
`8b    d88b    d8' ""     `Y8 88P'   "Y8 88P'   "Y8 88 a8"     "8a 88P'   "Y8  
 `8b  d8'`8b  d8'  ,adPPPPP88 88         88         88 8b       d8 88          
  `8bd8'  `8bd8'   88,    ,88 88         88         88 "8a,   ,a8" 88          
    YP      YP     `"8bbdP"Y8 88         88         88  `"YbbdP"'  88      
                                       
88                                 88  
88                                 88  
88                                 88  
88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 ""     `Y8 88P'   `"8a a8"    `Y88  
88 ,adPPPPP88 88       88 8b       88  
88 88,    ,88 88       88 "8a,   ,d88  
88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
                                       
''')
print("Welcome to Warrior Land.")
print("This is not a journey for the faint-hearted. You will be tried on your strength, faith and loyalty. Do you still wish to engage? Choose option 1, 2 or 3 below.")

destination = int(input("1 Yes, I\'ll ride on the storm! \n2 I may need to build more faith. \n3 No. I am not made for such. \n  "))

if destination == 1:
  yes = input("Welcome to the Land of Jericho. Yet, it is hardly a welcome as men are at war. Do you wish to still go on? Yes or No\n  ").lower()
  if yes == "yes":
    print("As you wish. Report to the commanding officer.")
    next_step = int(input("On your way, you find an injured friend. 1 Stop or\n                                         2 Go on\n  "))
    if next_step == 2:
      print("You reach the commander. But ... no admittance without the comrade. You lose. Back to Fighting School.")
    elif next_step == 1:
      print("What shall you do now? Are you a healer? This is a warzone, and you need to know the day's command.\n")
      next_step = int(input("What can you do for the brother in trouble? 1 Send him out of the warzone. Or \n                                       2 Take him with you to the commander.\n  "))
      if next_step == 2: 
        next_step = input("Good. The commander gives you two an instruction: Blow trumpet at the gates of the enemy! \nWill you accept this mission? accept or reject \n  ")
        if next_step == "accept":
          print("You go with the other soldier. But he incites you to rebel: 'The commander's instruction has no logic. Let's go infiltrate the city and steal their treasures.', he says.")
          next_step = int(input("What do you answer? 1 'Sure, sounds reasonable' \n2 'I am not sure what to do.' \n3 'He gave a command. Shall I kill you now for insubordination? Is your life or wit more pertinent than our mandate?'\n"))
          if next_step == 3:
            print("Your rebuke works and the other soldier regains his senses. You both continue the mission and blow the trumpets. The sound of the trumpets wakes the enemy and they aim arrows at you.")
            next_step = input("What is the state of your heart now? strong or small? \n").lower()
            if next_step == "strong":
              print("No sooner than the arrows are notched, the walls of the city sink. The archers die from the collapse. Your commander leads the army to victory and he rewards you for good service. Well done, you are crowned!")
            else: 
              print("You lose!")
      else:
        print("You will cause loss here. Go back to Fighting School. Hint: Know thy leader.")
    else: 
      print("Are you fully here? Back to Fighting School, boy.")
      destination = 3
  
  else:
    print("Where have you set your sights, soldier?  Off you go to Fighting School.")
    destination = 2
elif destination == 2:
  print("Welcome to Fighting School. We form warriors here.")
  next_step = input("Are you ready to learn? Yes or No\n  ").lower()
  if next_step == 'yes':
    print("Your first task is to build up faith! You can start at the 11th regiment in the Hebrews camp. Make sure to submit to the instructor first. He will give pointers! Remember submission is key.")
  else:
    print("What shall we then do for thee, oh goat?")
else:
  print("You are very much at ease in this place. Flee, now! You will surely be consumed as canon fodder.")

