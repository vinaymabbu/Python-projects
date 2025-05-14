# list of questions
#store the ansewers 
#random questions
# ask the questons to the user
# check the answers
# keep track of the score
#tell the score to the user
import random


questions={
    "What is a list used for in Python?": "Collection",
    "What is the main difference between a tuple and a list?": "Immutable",
    "How do you create a loop that runs five times?": "For",
    "What is a dictionary (dict) in Python?": "KeyValue",
    "What does the range() function do?": "Sequence",
    "How is the break statement used inside a loop?": "Exit",
    "What is a set in Python, and what is special about it?": "Unique",
    "What is the purpose of a lambda function in Python?": "Anonymous",
    "How do you define a class in Python?": "Blueprint",
    "What is the purpose of the import statement?": "Module"

}

def python_trivia_game():
   questions_list=list(questions.keys())
   total_questions=5
   score=0

   selected_questons=random.sample(questions_list,total_questions)
   
   for idx,question in enumerate(selected_questons):
      print(f"{idx+1}.{question}")
      user_answer=input("your answer: ").lower().strip()

      correct_answer=questions[question]

      if user_answer==correct_answer.lower().strip():
         print("correct\n")
         score+=1
      else:
         print(f"wrong.The correct answer is : {correct_answer}")
         
   print(f"Game oveer!your final score is {score}/{total_questions}")
      



python_trivia_game()