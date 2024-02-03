from tkinter import *
from tkinter import ttk
def get_data():
    try:
        weight = float(weightt.get())
        height = float(heightt.get()) / 100  # Convert height to meters
        bmi = weight / (height * height)

        if bmi < 18.5:
            output.config(text=f"BMI: {bmi:.1f} - UNDERWEIGHT")
        elif 18.5 <= bmi <= 24.9:
            output.config(text=f"BMI: {bmi:.1f} - NORMAL WEIGHT")
        elif 25 <= bmi <= 29.9:
            output.config(text=f"BMI: {bmi:.1f} - OVERWEIGHT")
        else:
            output.config(text=f"BMI: {bmi:.1f} - OBESITY")

    except ValueError:
        output.config(text="invalid numbers")

# GUI setup
win = Tk()
win.title("BMI Calculator")
win.geometry('500x500')
win.configure(bg='pink')
name_label=Label(win,text="BMI calculator",font=("Freestyle Script",35))
name_label.place(x=10,y=55,height=50,width=500)
weight_label = ttk.Label(win, text='Enter your weight (kg):')
weight_label.place(x=5, y=200, height=40, width=200)

weightt = ttk.Entry(win)
weightt.place(x=5, y=250, height=40, width=200)

height_label = ttk.Label(win, text='Enter your height (cm):')
height_label.place(x=250, y=200, height=40, width=200)

heightt = ttk.Entry(win)
heightt.place(x=250, y=250, height=40, width=200)

result_button = ttk.Button(win, text='Calculate BMI', command=get_data)
result_button.place(x=5, y=300, height=40, width=200)

output = ttk.Label(win, text='')
output.place(x=5, y=350, height=40, width=450)
win.mainloop()