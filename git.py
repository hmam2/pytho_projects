#-------------------
def new_game(): #finction for the game
  Guesses = []  #التخميين بحيث يقوم هذا الامر بتقسيم الاسئلة والخيارات ليكون كل سؤال خياراته تحته
  correct_gusses = 0 # رقم الخيار
  question_num = 1 # رقم السؤال

  for key in questions: # حلقة تكرارية للسؤال
      print("-------------------")
      print(key) # طباعة الاسئلة على الشاشة
      for i in options[question_num-1]: # امر خاص بالاختيارات للأسئلة
          print(i) # طباعة الاختيارات
      guess = input("Enter(A,B,C,D):") #امر يقوم بؤال اللاعب ليختار رقم الاجابة
      guess = guess.upper()
      Guesses.append(guess)

      correct_gusses += cheeck_answer(questions.get(key),(guess)) #التخممين الصحيح = التحقق من الاجابة
      question_num += 1 # رقم السؤال
  display_score(correct_gusses,Guesses) # امر خاص لظهوؤ نتيجة اللاعب على الشاشة




#-----------------
def cheeck_answer(answer,guess):  #الدالة الخاصةللتحقق من السؤال
    if answer == guess: # شرط للتحقق من ان الجواب = التخممين 
        print("correct")
        return 1
    else: 
        print("wrong answer")
        return 0
#-----------------
def display_score (correct_gusses,Guesses): # دالة خاصة لظهور النتيجة على الشاشة 
    print("---------------------")
    print("Score: ") 
    print("---------------------")
    print("correct answer: ",end="") # امر خاص لطباعة الاجوبة الصحيحة للاعب 
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("your answer: ",end="") # الاجوبة التي جاوب علىيها المستخدم
    for i in Guesses:
        print(i,end=" ")
    print()
    score = int((correct_gusses/len(questions))*100)  #الامر الخاص باظهار النتيجة 
    print("your score is :"+str(score)+"%")




#-----------------
def play_agine(): # الدالة الخاصة اذا اراد اللاعب اللعب مرة اخرى 
    response = input("do you like play agin? (yes or no):")
    response=response.upper()

    if response == "YES": # اذا جاوب اللاعب بنعم يعيد اللعبة اذا جاوب لا يخرج من اللعبة
        return  True
    else:
        return False
#-----------------

questions = {  # القاموس الخاص بالاسئلة
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