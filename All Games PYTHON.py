import time
import random
def allgames():  
  wongames = 0
  #1.  Hangman

  def hangman():
    nonlocal wongames
    choices = ["apples", "tree", "dinosaur", "life", "idk", "random", "words", "bored", "fr", "helppp"]
    word = random.choice(choices)
    wordsplit = list(word)
    alreadyusedletters = []
    guessed = ["_"] * len(wordsplit)
    count = len(wordsplit) * 2
    x = ""
    print(f"Welcome to Hangman! For every mistake made you get an x, {count} x's and you lose.")
    print("Word:", " ".join(guessed))
    while count > 0:
      print("Used letters:", ", ".join(sorted(alreadyusedletters)))
      user = input("Enter a letter: ").strip().lower()
      if len(user) != 1 or not user.isalpha():
        continue
      if user in alreadyusedletters:
        print("You have already used that letter")
        continue
      alreadyusedletters.append(user)
      if user in wordsplit:
        print("That letter is in the word, well done!")
        for i in range(len(word)):
          if word[i] == user:
              guessed[i] = user
        print("Word:", " ".join(guessed))
        if "_" not in guessed:
          print(f"Yay you found the word, it was {word}!")
          wongames +=1
          break
      else:
        print("Sorry, that letter is not in the word")
        print("Word", " ".join(guessed))
        count = count - 1
        x += "x"
        print(x)
        print(f"Incorrect guesses:({count} remaining)")
    if count == 0:
      print(f"Unfortunately you lost, the word was {word}")
  
  #2. Higher or lower
  
  def higherorlower():
      nonlocal wongames
      number = random.randint(1, 10)
      attempts = 0
      guesses = 0
      while True:
          difficulty = input("Choose gamemode; Easy, Medium or Difficult: ").strip().lower()
          numrange = 0
          hintneeded = 0
          if difficulty == "easy":
            numrange = 10
            hintneeded = 2
            guesses = 5
            number = random.randint(1, numrange)
            break
          elif difficulty == "medium":
            numrange = 100
            hintneeded = 5
            guesses = 10
            number = random.randint(1, numrange)
            break
          elif difficulty == "difficult":
            numrange = 1000
            hintneeded = 7
            guesses = 15
            number = random.randint(1, numrange)
            break
          else:
            print("Please select a gamemode")
      toomanyguesses = guesses
      correct = False
      while correct == False:
        guess = int(input(f"Pick a number from 1 to {numrange}, you have {guesses} guesses."))
        attempts += 1
        guesses -=1
        if guess < number:
          print("Too small...")
        elif guess > number:
          print("Too big...")
        elif guess == number:
          print("Correct!")
          correct = True
          break
        if attempts == hintneeded:
          hint = input("Do you want a hint? Yes or No: ").strip().lower()
          if hint == "no":
            print("Ok!")
          elif hint == "yes":
                if number % 2 == 0:
                  print("Hint: The number is even.")
                else:
                  print("Hint: The number is odd.")
        if attempts > toomanyguesses:
          print("You took too many guesses, you have lost!")
          break
      if correct == True:
        print(f"Yay you got it right and it took {attempts} guesses")
        wongames +=1

  #3. Rock, Paper, Scissors

  def rockpaperscissors():
    nonlocal wongames
    goes = int(input("How many goes do you want"))
    for goes in range(0, goes):
      choices = ["rock", "paper", "scissors"]
      while True:
        player = input("Choose rock, paper, or scissors: ").strip().lower()
        computer = random.choice(choices)
        if player in choices:
          break
      print(f"You chose {player}")
      print(f"The computer chose {computer}")
      if player == computer:
        print("It's a draw!")
      elif (player == "scissors" and computer == "paper") or (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock"):
        print("Yay you won!")
        wongames +=1
      else:
        print("Sorry you lost.")
    #4. Anagram game

  def anagram():
    def scramble(word):
      scrambled = ''.join(random.sample(word, len(word)))
      while scrambled == word:
          scrambled = ''.join(random.sample(word, len(word)))
      return scrambled
    nonlocal wongames
    words = ["apple", "trees", "life", "bored", "tempermental", "behaviour", "defibrillator"]
    word = random.choice(words)
    scrambled = scramble(word)
    correct = False
    count = 0
    hint_given = False
    while correct == False:
      guess = input(f"This is an anagram game! You have 5 goes to unscramble {scrambled}: ").strip().lower()
      count +=1
      if guess == word:
        print(f"Yay you got it right, it took you {count} tries!")
        wongames +=1
        correct = True
      else:
        if count == 3 and not hint_given:
          hint = input("Do you want a hint, yes or no? ").strip().lower()
          if hint == "yes":
            splitword = list(word)
            letter = splitword[0]
            print(f"The first letter is {letter}")
          else:
            print("Ok!")
          hint_given = True
        print("No... Try again")
        if count == 5:
          print("You took too many goes, you have lost.")
          break
  
  #5. Maths problems

  def maths():
    nonlocal wongames
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    one = random.choice(numbers)
    two = random.choice(numbers)
    symbols = ["+", "-", "×"]
    count = 0
    operator = random.choice(symbols)
    result = 0
    if operator == "×":
      result = one * two
    elif operator == "+":
      result = one + two
    else:
      result = one - two
    while True:
      guess = int(input(f"Here's your daily dose of maths! You have 3 goes to answer {one} {operator} {two}?: "))
      if guess == result:
        print("Yay you got it right!")
        wongames +=1
        break
      else:
        print("No.. Try again: ")
        count +=1
        if count == 3:
          print("You took too many goes, you have lost.")
          break
  
  #Typing Speed

  def spell():
    nonlocal wongames
    choices = ["apple", "banana", "trees", "defibrillator", "dinosaur", "behaviour", "three"]
    howmanywords = int(input("How many words do you want to spell? "))
    count = 0
    totaltime = 0
    for i in range(howmanywords):
      start = time.time()
      word = random.choice(choices)
      while True:
        speed = input(f"Type {word} as quickly as you can.. GO! ").strip().lower()
        if speed == word:
          end = time.time()
          typing = round(end - start, 2)
          totaltime += typing
          totaltime = round(totaltime, 2)
          print(f"You took {typing} seconds to type {word}")
          count += 1
          break
        else:
          print("Try again")
    perminute = totaltime / 60
    wpm = round(count / perminute, 2)
    print(f"You spelt {count} words correctly and took {totaltime} seconds altogether. You typed at {wpm} WPM")
    wongames +=1
  
  #########################################################
  
  def game_selection():
    menu = """
There are 6 games to choose from;
1. Hangman
2. Higher or Lower
3. Rock Paper Scissors
4. Anagram puzzle
5. Maths puzzle
6. Typing speed
"""
    while True: 
      menuoption = input("Would you like to see the menu again? Y or N: ").strip().lower()
      if menuoption == "y":
        print(menu)
      whichgame = int(input("Choose game 1, 2, 3, 4, 5 or 6: "))
      if whichgame == 1:
        hangman()
        break
      elif whichgame == 2:
        higherorlower()
        break
      elif whichgame == 3:
        rockpaperscissors()
        break
      elif whichgame == 4:
        anagram()
        break
      elif whichgame == 5:
        maths()
        break
      elif whichgame == 6:
        spell()
        break
      else:
        print("Please choose one of the options")
  game_selection()
 
  def again():
    while True:
      again = input(f"Would you like to play another game, you have won {wongames} games so far. Yes or No: ").strip().lower()
      if again == "yes":
        game_selection()
      else:
        print("Ok, thank you for playing!")
        break
  again()
menu = """
There are 6 games to choose from;
1. Hangman
2. Higher or Lower
3. Rock Paper Scissors
4. Anagram puzzle
5. Maths puzzle
6. Typing speed
"""
print(menu)

allgames()