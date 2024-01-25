print("Добро пожаловать в викторину на тему GTA5")
Questions=["сколько видов транспорта в игре гта5?","сколько всего вышло частей гта?","сколько персонажей в игре гта5?"]
Answers=[6,5,3]
score=0
print(Questions[0])
v1=int(input("введите ответ "))
if v1==Answers[0]:
 score=score+1
 print("вы ответили правильно")
else:
   print(f"ваш ответ {v1},а правильный ответ {Answers[0]}")
  
print(Questions[1])
v2=int(input("введите ответ "))
if v2==Answers[1]:
  score=score+1
  print("вы ответили правильно")
else:
  print(f"ваш ответ {v2},а правильный ответ {Answers[1]}")
  
print(Questions[2])
v3=int(input("введите ответ "))
if v3==Answers[2]:
 score=score+1
 print("вы ответили правильно")
else:
 print(f"ваш ответ {v3},а правильный ответ {Answers[2]}")

if score==0:
 print("вы набрали 0 баллов")
else:
  print(f"вы набрали {score} ,баллов")
