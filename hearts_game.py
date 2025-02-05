hearts = ["Happiness", "Euphoria", "Admiration", "Romance", "Trust", "Support"] # list of HEARTS

name1 = input("Enter first name: ").lower() # INPUT FIRST NAME IN LOWER CASE
name2 = input("Enter second name: ").lower() # INPUT SECOND NAME IN LOWER CASE

set1 = set(name1) # TRANSFORM NAME TO SET
set2 = set(name2)

uniqueLetter1 = set1 - set2 # FIND DIFFERENCES IN LETTERS
uniqueLetter2 = set2 - set1

totalUnique = len(uniqueLetter1) + len(uniqueLetter2) # TOTAL UNIQUE LETTERS

index = (totalUnique - 1) % len(hearts) # WRAP AROUND HEARTS

print("Results:", hearts[index]) # PRINT KUNG SAAN TUMIGIL ANG INDEX