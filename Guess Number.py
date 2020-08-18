import random
num = random.randint(1,20)
i = 0

while i <5:
  ans = int(input ("Guess a number between one and twenty:"))
  if ans == num:
      print("Good job! You guessed correctly. It only took you",i+1 ,"try/tries")
      break
  elif ans > num:
      print ("Guess a smaller number")
  elif ans < num:
      print ("Guess a bigger number")
  i= i+1
else:
      print("Haha, you guessed incorrectly.")
     
                  