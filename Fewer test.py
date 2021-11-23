from tkinter import *
root = Tk()
root.title("Fever report")
root.geometry("600x600")

Question_1_radiobutton = StringVar(value = "0")
Question_1 = Label(root , text = "Do u have headace or soar throat?")
Question_1.pack()
question_1_r1 = Radiobutton(root , text = "yes" , variable = Question_1_radiobutton , value = "yes")
question_1_r1.pack()
question_1_r2 = Radiobutton(root , text = "no" , variable = Question_1_radiobutton , value = "no")
question_1_r2.pack()

Question_2_radiobutton = StringVar(value = "0")
Question_2 = Label(root , text = "Is ur body temperature high?")
Question_2.pack()
question_2_r1 = Radiobutton(root , text = "yes" , variable = Question_2_radiobutton , value = "yes")
question_2_r1.pack()
question_2_r2 = Radiobutton(root , text = "no" , variable = Question_2_radiobutton , value = "no")
question_2_r2.pack()

Question_3_radiobutton = StringVar(value = "0")
Question_3 = Label(root , text = "Are there any symptoms of eye redness ?")
Question_3.pack()
question_3_r1 = Radiobutton(root , text = "yes" , variable = Question_3_radiobutton , value = "yes")
question_3_r1.pack()
question_3_r2 = Radiobutton(root , text = "no" , variable = Question_3_radiobutton , value = "no")
question_3_r2.pack()

def fever_score():
    score = 0
    if Question_1_radiobutton.get() == "yes":
        score = score + 20
        print(score)
    if Question_2_radiobutton.get() == "yes":
        score = score + 20
        print(score)
    if Question_3_radiobutton.get() == "yes":
        score = score + 20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Report" , "U dont need to visit a doctor")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report" , "U might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report" , "I strongly advise u to visit a doctor")

btn = Button(root , text = "Click me" , command = fever_score)
btn.pack()

root.mainloop()