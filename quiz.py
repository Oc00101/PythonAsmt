'''
Create a dictionary of Science quiz
- write atleast 10 questions with answers
- create a quiz
'''

# Questions and Answers
Qa = {
    "What is the study of the universe?" : "Astronomy", 
    "What is the study of the earth?" : "Geology",
    "What is the study of the human body?" : "Anatomy",
    "What is the study of the brain?" : "Neurology",
    "What is the study of the heart?" : "Cardiology",
    "What is the study of the skin?" : "Dermatology",
    "What is the study of the eyes?" : "Ophthalmology",
    "What is the study of the ears?" : "Audiology",
    "What is the study of the lungs?" : "Pulmonology",
    "What is the study of the stomach?" : "Gastroenterology"
    }

# Quiz
# function to run the quiz
def quiz(Qa):
    score = 0 #set initial score to 0
    for k, v in Qa.items(): # using for-loop to go through the dictionary
        ans = input(k + " ")    
        if ans.lower() == v.lower(): # check if the answer is correct
            score += 1
            print("Correct!") 
        else:
            print("Incorrect!")

    print(f"You got {score}/{len(Qa)} correct!") # print the final score
    
    
#calling the function    
quiz(Qa)

































