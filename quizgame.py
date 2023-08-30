import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.current_question = 0
        self.score = 0
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Madrid", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            }
            # Add more questions here
        ]
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)
        
        self.next_question_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), command=self.next_question)
        self.next_question_button.pack(pady=10)
        
        self.refresh_question()
    
    def refresh_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
        else:
            self.show_result()
    
    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question]
        selected_option = question_data["options"][selected_index]
        correct_option = question_data["correct_answer"]
        
        if selected_option == correct_option:
            self.score += 1
        self.next_question()
    
    def next_question(self):
        self.current_question += 1
        self.refresh_question()
    
    def show_result(self):
        messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
