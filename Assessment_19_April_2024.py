class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def show_question(self):
        current_question = self.questions[self.current_question]
        print(current_question["query"])
        for index, option in enumerate(current_question["options"], start =1):
            print(f"{index}.{option}")

    def answer_question(self,choice):
        current_question = self.questions[self.current_question]
        correct_answer = current_question["answer"]
        if choice == correct_answer:
            self.score +=1

    def next_question(self):
        self.current_question +=1

    def is_quiz_finished(self):
        return self.current_question == len(self.questions)

    def show_result(self):
        print(f"Your score is {self.score} out of {len(self.questions)}")


questions = [
    {
        "query": "India's First Prime Minister?",
        "options":["Subhash Chandra Bose","Sardar Vallabh Bhai Patel", "Pt. Nehru", "Indira Gandhi"],
        "answer": 2
    },

    {
        "query": "National Captial of India?",
        "options":[ "Hyderabad","New Delhi", "Srinagar", "Trivandrum"],
        "answer": 1
    },

    {
        "query": "Operating System owned by apple?",
        "options":["Windows","Linux", "Mac OS", "Android"],
        "answer": 2
    }
]                  

custom_quiz = Quiz(questions)

for question in custom_quiz.questions:
    custom_quiz.show_question()
    choice = int(input("Enter your choice: ")) -1

    custom_quiz.answer_question(choice)
    custom_quiz.next_question()

    custom_quiz.show_result()
