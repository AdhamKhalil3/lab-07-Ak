myVar = input("What is your answer to my 1st question? (yes/no) ")  
if myVar == "yes":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    myNextVar = input("Ok sounds great !")
  elif myNextVar == "no":
    myNextVar == "why not?"
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  myVar == "ok guess not"
else:
  print("Answer my question! You didn't type yes or no.")
