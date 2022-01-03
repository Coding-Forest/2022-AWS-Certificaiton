import datetime
import numpy as np
import pandas as pd


class ExamAssistant:

    def __init__(self):
        self.answers = []
        self.correct_answers = ['D', 'B', 'A', 'C', 'AD', 'AC', 'B', 'A', 'BC', 'B', 'C', 'B', 'B', 'BD', 'C', 'D', 'BD', 'C', 'AC', 'D', 'A', 'B', 'C', 'D', 'AB', 'BD', 'B', 'CD', 'B', 'C', 'D', 'AB', 'C', 'B', 'B', 'AD', 'BD', 'D', 'B', 'C', 'C', 'BC', 'C', 'B', 'A', 'B', 'A', 'BD', 'A', 'B', 'A', 'D', 'D', 'B', 'BD', 'A', 'C', 'C', 'D', 'BD', 'C', 'C', 'B', 'D', 'D']
        self.marks = []
        self.wrong_answers = []


    def mark_answers(self):

        for i in range(1, 65 + 1):
            if (i <= 9):
                a = input(f"Enter your answer for Q 0{i}: ")
                self.answers.append(a)
            else:
                a = input(f"Enter your answer Q {i}: ")
                self.answers.append(a)


    def grade_result(self):
        for i in range(len(self.answers)):
            if (self.answers[i] != self.correct_answers[i]):
                self.wrong_answers.append(i)


    def report_performance(self, start, end):
        print(f"Your Answers   : {self.answers}")
        print(f"Correct Answers: {self.correct_answers}")
        total_time = (end - start)
        print(f"total time taken : {np.round(((total_time) / 60), 2)} minutes.")
        print(f"Time per question: {np.round(total_time / 65, 3)} seconds")
        print("")
        print(f"======================= Result ======================= ")
        print(f"Correct: {65 - len(self.wrong_answers)}\nIncorrect: {len(self.wrong_answers)}")
        print(f"Questions for revision:\n{self.wrong_answers}")


    def save_answers(self):
        for i in range(len(self.answers)):
            if self.answers[i] == self.correct_answers[i]:
                self.marks.append("O")
            else:
                self.marks.append("X")

        data = {'user':self.answers, 'correct':self.correct_answers, 'mark': self.marks, 'topic': None, 'notes': None}
        df = pd.DataFrame(data)

        today = datetime.datetime.today()
        today = today.strftime("%m%d")

        df.index = np.arange(1, len(self.answers) + 1)
        df.to_csv(f'./exam ({today}).xlsx')


    def main(self):
        start = datetime.datetime.now()
        self.mark_answers()
        end = datetime.datetime.now()
        self.grade_result()

        self.report_performance(start, end)


if __name__ == "__main__":
    ea = ExamAssistant()
    ea.main()
    ea.save_answers()
    
    
    
"""

Your Answers   : ['D', 'B', 'A', 'C', 'AD', 'AC', 'B', 'A', 'BC', 'AB', 'C', 'B', ' ', 'D', 'D', 'D', 'BD', 'C', 'AC', 'D', 'A', 'B', 'C', 'D', 'AB', 'AD', 'A', 'CD', 'B', 'C', 'A', 'AB', 'A', 'A', 'B', 'A', 'BD', 'D', 'B', 'C', 'C', 'BC', 'C', 'A', 'A', 'A', 'A', 'BD', 'D', 'B', 'A', 'A', 'A', 'B', 'AB', 'A', 'C', 'C', 'D', 'BD', 'A', 'C', 'B', 'D', 'D']
Correct Answers: ['D', 'B', 'A', 'C', 'AD', 'AC', 'B', 'A', 'BC', 'B', 'C', 'B', 'B', 'BD', 'C', 'D', 'BD', 'C', 'AC', 'D', 'A', 'B', 'C', 'D', 'AB', 'BD', 'B', 'CD', 'B', 'C', 'D', 'AB', 'C', 'B', 'B', 'AD', 'BD', 'D', 'B', 'C', 'C', 'BC', 'C', 'B', 'A', 'B', 'A', 'BD', 'A', 'B', 'A', 'D', 'D', 'B', 'BD', 'A', 'C', 'C', 'D', 'BD', 'C', 'C', 'B', 'D', 'D']

======================= Result ======================= 
Correct: 48
Incorrect: 17
Questions for revision:
[9, 12, 13, 14, 25, 26, 30, 32, 33, 35, 43, 45, 48, 51, 52, 54, 60]

"""
