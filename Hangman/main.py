import random
import art as art
import words as words



def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

list = words.word_list


rand_num = random.randint(0,len(list)-1)
word = list[rand_num].lower()
lives = 6
solved = False
answer = []
stage = art.stages[lives]

print(art.logo)
print(stage)

for space in word:
  answer.append('_')


while solved == False:
  
  letter = input("guess a letter: ").lower()
  counter = 0
  for x in word:
    
    if x == letter:
      answer[counter] = x
    else:
      pass

    if lives == 0:
      solved = True
    elif search(answer,'_') :
      pass
    else:
      solved = True
      print("WINNER")
    counter += 1

  if letter not in word:
    lives -= 1
    stage = art.stages[lives]

  print(stage)
  print(answer)

print("game over")
print(f"correct word was {word}")
