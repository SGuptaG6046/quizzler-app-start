from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterFace:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.gui = Tk()
        self.gui.title("Quizzer")
        self.gui.config(bg=THEME_COLOR)
        self.gui.config(padx=20,pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}",fg="white",font=("Tsuki", 20, "bold"), bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            150,
            width= 280,
            text="somthing",
            font=("Arial",20,"italic"),
            fill=THEME_COLOR,
            )
        self.canvas.grid(row=1, columnspan=2, pady=20)
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        true_button.grid(column=0, row=2)

        false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        false_button.grid(column=1, row=2)
        self.get_next_question()


        self.gui.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")

        self.gui.after(1000, self.get_next_question)
