#-------------------
def new_game(): 
  Guesses = []
  correct_gusses = 0
  question_num = 1 

  for key in questions:
      print("-------------------")
      print(key) 
      for i in options[question_num-1]: 
          print(i)
      guess = input("Enter(A,B,C,D):") 
      guess = guess.upper()
      Guesses.append(guess)

      correct_gusses += cheeck_answer(questions.get(key),(guess)) 
      question_num += 1
  display_score(correct_gusses,Guesses) 




#-----------------
def cheeck_answer(answer,guess):  
    if answer == guess:  
        print("correct")
        return 1
    else: 
        print("wrong answer")
        return 0
#-----------------
def display_score (correct_gusses,Guesses):  
    print("---------------------")
    print("Score: ") 
    print("---------------------")
    print("correct answer: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("your answer: ",end="")
    for i in Guesses:
        print(i,end=" ")
    print()
    score = int((correct_gusses/len(questions))*100
    print("your score is :"+str(score)+"%")




#-----------------
def play_agine(): 
    response = input("do you like play agin? (yes or no):")
    response=response.upper()

    if response == "YES": 
        return  True
    else:
        return False
#-----------------

questions = {
    "ما هو اول جامع تم بناءه في مصر؟" : "A",
    "ما هي أطول سورة مدنية في عدد آياتها؟" : "C",
    "متى وقع صُلح الحُديبية؟" : "D",
    "ما هو عدد القلوب لدى حيوان الاخطبوط؟" : "A"
}

options = [["A.مسجد عمرو بن العاص","B. مسجد سادات قريش","C. مسجد السيدة زين","D. مسجد ابن طولون"], # القوائم الخاصة بالاختيارات 
           ["A. ال عمران","B.النساء","C.البقرة","D.المائدة"],
           ["A. 8هجري","B. 10 هجري","C.11 هجري","D.6هجري"],
           ["A.قلوب 3","B.قلب واحد ","C.6 قلوب ","D.5 قلوب"]]

new_game()  

while play_agine():
    new_game()

print("Byyyyeee🥰")
