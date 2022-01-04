import datetime
import numpy as np
import pandas as pd


class ExamAssistant:

    def __init__(self, exam_size: int):
        self.exam_size = exam_size
        self.answers = []
        self.correct_answers = []
        self.marks = []
        self.wrong_answers = []

    def mark_answers(self):

        for i in range(1, self.exam_size + 1):
            if (i <= 9):
                a = input(f"Enter your answer for Q 0{i}: ")
                self.answers.append(a.upper())
            else:
                a = input(f"Enter your answer for Q {i}: ")
                self.answers.append(a.upper())

    def grade_result(self):
        for i in range(len(self.answers)):
            if (self.answers[i] != self.correct_answers[i]):
                self.wrong_answers.append(i+1)

    def enter_correct_answers(self):
        correct_answers = input("Enter correct answers: ").upper()
        self.correct_answers = list(correct_answers.split(" "))

    def report_performance(self):
        print(f"Your Answers   : {self.answers}")
        print(f"Correct Answers: {self.correct_answers}")
        #total_time = (end - start)
        #print(f"total time taken : {np.round(((total_time) / 60), 2)} minutes.")
        #print(f"Time per question: {np.round(total_time / self.exam_size, 3)} seconds")
        print("")
        print(f"======================= Result ======================= ")
        print(f"Correct: {len(self.correct_answers) - len(self.wrong_answers)}\nIncorrect: {len(self.wrong_answers)}")
        print(f"Questions for revision:\n{self.wrong_answers}")

    def save_answers(self):
        for i in range(len(self.answers)):
            if self.answers[i] == self.correct_answers[i]:
                self.marks.append("O")
            else:
                self.marks.append("X")

        data = {'user': self.answers, 'correct': self.correct_answers, 'mark': self.marks, 'topic': None, 'notes': None}
        df = pd.DataFrame(data)

        today = datetime.datetime.today()
        today = today.strftime("%m%d")

        df.index = np.arange(1, len(self.answers) + 1)
        df.to_csv(f'./exam ({today}).xlsx')


    def main(self):
        #start = datetime.datetime.now()
        self.mark_answers()
        #end = datetime.datetime.now()

        self.enter_correct_answers()
        self.grade_result()
        self.report_performance()


if __name__ == "__main__":
    ea = ExamAssistant(10)
    ea.main()
    ea.save_answers()

    
"""
Enter your answer for Q 01: c
Enter your answer for Q 02: b
Enter your answer for Q 03: d
Enter your answer for Q 04: d
Enter your answer for Q 05: b
Enter your answer for Q 06: b
Enter your answer for Q 07: c
Enter your answer for Q 08: a
Enter your answer for Q 09: a
Enter your answer for Q 10: b
Enter correct answers: C B D D B B C B A d
Your Answers   : ['C', 'B', 'D', 'D', 'B', 'B', 'C', 'A', 'A', 'B']
Correct Answers: ['C', 'B', 'D', 'D', 'B', 'B', 'C', 'B', 'A', 'D']

======================= Result ======================= 
Correct: 8
Incorrect: 2
Questions for revision:
[8, 10]

Process finished with exit code 0

"""
