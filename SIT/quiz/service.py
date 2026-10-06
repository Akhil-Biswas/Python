import json

# questions = [
#     {
#       "id": 1,
#       "question": "What is the capital of France?",
#       "options": ["Berlin", "Madrid", "Paris", "Rome"],
#       "answer": "Paris"
#     },
#     {
#       "id": 2,
#       "question": "How many days are in a leap year?",
#       "options": ["364", "365", "366", "367"],
#       "answer": "365"
#     },
#     {
#       "id": 3,
#       "question": "What color is a clear daytime sky?",
#       "options": ["Green", "Blue", "Yellow", "Red"],
#       "answer": "Blue"
#     },
#     {
#       "id": 4,
#       "question": "How many planets are in our solar system?",
#       "options": ["7", "8", "9", "10"],
#       "answer": "8"
#     },
#     {
#       "id": 5,
#       "question": "What is H2O commonly known as?",
#       "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Water"],
#       "answer": "Water"
#     }
# ]

class Quize:

    def __init__(self,file: str = "src/quize/question.json"):
        with open(file,"r") as f:
            self.questions = json.load(f)["questions"]
        
        self.score: int = 0
    def ask_question(self,question_number: int):
        print(self.questions[question_number]["question"])

    def display_options(self,question_number: int):
        for i in self.questions[question_number]["options"]:
            print(i)


    def answer(self,question_number: int):
        return self.questions[question_number]["answer"]

    def start(self):
        for i in range(len(self.questions)):
            self.ask_question(i)
            self.display_options(i)
            print("For Exit Enter N")
            answer = input("Answer:").lower()
            
            if answer == "n":
                print("Your Score:",self.score)
                break
            
            if answer == self.answer(i).lower():
                print("U are correct")
                self.score += 1
        
    
if __name__ == "__main__":
    session = Quize()
    session.start()