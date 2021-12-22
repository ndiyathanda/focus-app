from tkinter import *
import time
import threading, sys, os, notify2, keyboard
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Focus")
root.geometry('500x400')
root.resizable(0, 0)

class UI:
    def __init__(self):
        thread = threading.Thread(target=self.check_keys)
        thread.daemon = True
        thread.start()
        print("init")
        self.color1 = "#684D86"
        self.color2 = "#735290"
        root['background'] = self.color2
        self.a = 1
        self.b = 1
        self.Pause = False
        self.v1 = DoubleVar()
        self.v2 = DoubleVar()
        self.img = PhotoImage(file="example.png")
        self.img2 = PhotoImage(file="siema.png")
        self.img3 = PhotoImage(file="apply.png")
        self.img5 = PhotoImage(file="images.png")
        self.img7 = PhotoImage(file="cancel.png")
        self.img7 = PhotoImage(file="cancel.png")
        self.img8 = PhotoImage(file="add.png")
        self.img9 = PhotoImage(file="delete.png")

    def check_keys(self):
        while True:
            time.sleep(0.05)
            try:
                if keyboard.is_pressed("del"):
                    ToDo1.delete_task()
                    time.sleep(0.5)
                if keyboard.is_pressed("enter"):
                    ToDo1.add_task()
                    time.sleep(0.5)
            except:
                print("problemy najmana")

    def draw_button(self):
        button = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=self.draw_pomodoro)
        button.config(image=self.img, bg=self.color1)
        button.place(x=0, y=0)

        button2 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=self.draw_todo)
        button2.config(image=self.img2, bg=self.color1)
        button2.place(x=0, y=70)

        button5 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=self.statistics)
        button5.config(image=self.img5, bg=self.color1)
        button5.place(x=0, y=140)

    def draw_todo(self):
        try:
            self.pozdrawiam = True
            self.button3.destroy()
            self.button4.destroy()
            self.s1.destroy()
            self.s2.destroy()
            self.T2.place_forget()
            self.T3.place_forget()
            self.T.place_forget()
            self.T5.place_forget()
        except:
            pass
        try:
            self.T13.destroy()
            self.T12.destroy()
            self.T15.destroy()
            self.T22.destroy()
            self.T23.destroy()
            self.T24.destroy()
            self.T25.destroy()
            self.T69.destroy()
            self.T70.destroy()
            self.T72.destroy()
            self.T73.destroy()
            self.T74.destroy()
            self.c = 1
        except:
            pass
        if self.a == 1:
            self.button6 = Button(root, text="Click me!", highlightthickness=0, bd=0, command=ToDo1.add_task)
            self.button6.config(image=self.img8, bg=self.color1, activebackground=self.color1)
            self.button6.place(x=100,y=15)
            self.button7 = Button(root, text="Click me!", highlightthickness=0, bd=0)
            self.button7.config(image=self.img9, bg=self.color1, activebackground=self.color1, command=ToDo1.delete_task)
            self.button7.place(x=430,y=15)
            self.T10 = Text(root, height=1, width=9, highlightthickness=0, bd=0, bg=self.color1, font=("Helvetica", 32))
            self.T10.place(x=190, y=15)
            self.T10.insert(END, "ToDo List")
            self.T10.configure(state=DISABLED)
            ToDo1.load_tasks()
            self.listbox = Listbox(
                root,
                listvariable=ToDo1.tasks_v,
                height=17,
                width=52,
                bg=self.color2,
                highlightthickness=0,
                highlightcolor=self.color1,
                selectmode='extended',
                font=("Helvetica", 11))
            self.listbox.place(x=65, y=73)
            self.l2 = Label(root, text='Task name', bg=self.color2)
            self.l2.place(x=65, y=380)
            self.entry = Entry(root, width=44, bg=self.color2, highlightthickness=0)
            self.entry.place(x=140, y=380)
            self.a = 0
            self.b = 1

    def draw_pomodoro(self):
        try:
            self.button6.destroy()
            self.button7.destroy()
            self.T10.destroy()
            self.listbox.destroy()
            self.entry.destroy()
            self.l2.destroy()
            self.a = 1
        except:
            pass
        try:
            self.T13.destroy()
            self.T12.destroy()
            self.T15.destroy()
            self.T22.destroy()
            self.T23.destroy()
            self.T24.destroy()
            self.T25.destroy()
            self.T69.destroy()
            self.T70.destroy()
            self.T72.destroy()
            self.T73.destroy()
            self.T74.destroy()
            self.c = 1
        except:
            pass

        if self.Pause == True:
            self.img4 = PhotoImage(file="play.png")
        else:
            self.img4 = PhotoImage(file="pause.png")
        if self.b == 1:
            self.s1 = Scale(root, variable=self.v1,
                            from_=1, to=60,
                            orient=HORIZONTAL,
                            bg=self.color2,
                            highlightthickness=0,
                            bd=0,
                            activebackground=self.color2,
                            foreground="black")
            self.s2 = Scale(root, variable=self.v2,
                            from_=1, to=30,
                            orient=HORIZONTAL,
                            bg=self.color2,
                            highlightthickness=0,
                            bd=0,
                            activebackground=self.color2,
                            foreground="black")
            self.button3 = Button(root, text="Click me!", highlightthickness=0, bd=0, command=self.countdown)
            self.button3.config(image=self.img3, bg=self.color2, activebackground=self.color2)
            self.button3.place(x=245,y=250)
            self.button4 = Button(root, text="Click me!", highlightthickness=0, bd=0, command=self.reset)
            self.button4.config(image=self.img7, bg=self.color2, activebackground=self.color2)
            self.button4.place(x=252, y=320)
            self.s1.place(x=100, y=250)
            self.s2.place(x=352, y=250)
            self.T2 = Text(root, height=1, width=5, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 40))
            self.T2.place(x=210, y=120)
            self.T2.insert(END, "00:00")
            self.T2.configure(state=DISABLED)
            self.T3 = Text(root, height=1, width=12, highlightthickness=0, bd=0, bg=self.color1, font=("Helvetica", 32))
            self.T3.place(x=222, y=20)
            self.T3.insert(END, "")
            self.T = Text(root, height=2, width=10, highlightthickness=0, bd=0, bg=self.color2)
            self.T.place(x=370, y=300)
            self.T.insert(END, "Rest time")
            self.T.configure(state=DISABLED)
            self.T5 = Text(root, height=2, width=10, highlightthickness=0, bd=0, bg=self.color2)
            self.T5.place(x=110,y=300)
            self.T5.insert(END, "Focus time")
            self.T5.configure(state=DISABLED)
            self.b = 0
            self.c = 1

    def reset(self):
   #     self.Enable = False
        os.execl(sys.executable, sys.executable, *sys.argv)

    def countdown(self):
        thread = threading.Thread(target=self.timer)
        thread.daemon = True
        thread.start()

    def statistics(self):
        s.load()
        try:
            self.button6.destroy()
            self.button7.destroy()
            self.T10.destroy()
            self.listbox.destroy()
            self.entry.destroy()
            self.l2.destroy()
        except:
            pass
        try:
            self.button3.destroy()
            self.button4.destroy()
            self.s1.destroy()
            self.s2.destroy()
            self.T2.place_forget()
            self.T3.place_forget()
            self.T.place_forget()
            self.T5.place_forget()
        except:
            pass
        if self.c == 1:
            self.T12 = Text(root, height=1, width=19, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T12.place(x=70, y=85)
            self.T12.insert(END, "Focus time")
            self.T12.configure(state=DISABLED)
            self.T13 = Text(root, height=1, width=5, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T13.place(x=210, y=85)
            self.T13.insert(END, s.s_1)
            self.T15 = Text(root, height=1, width=3, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T15.place(x=270, y=85)
            self.T15.insert(END, "min")
            self.T22 = Text(root, height=1, width=10, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T22.place(x=70, y=130)
            self.T22.insert(END, "Brake time")
            self.T23 = Text(root, height=1, width=5, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T23.place(x=210, y=130)
            self.T23.insert(END, s.s_2)
            self.T24 = Text(root, height=1, width=3, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T24.place(x=270, y=130)
            self.T24.insert(END, "min")
            self.T25 = Text(root, height=1.2, width=8, highlightthickness=0, bd=0, bg=self.color1, font=("Helvetica", 32))
            self.T25.place(x=190, y=18)
            self.T25.insert(END, "Statistics")
            self.T70 = Text(root, height=1, width=10, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T70.place(x=70, y=175)
            k = float(s.s_1) + float(s.s_2)
            self.T70.insert(END, "Total time")
            self.T69 = Text(root, height=1, width=3, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T69.place(x=210, y=175)
            self.T69.insert(END, k)
            self.T72 = Text(root, height=1, width=3, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T72.place(x=270, y=175)
            self.T72.insert(END, "min")
            self.T73 = Text(root, height=1, width=19, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T73.place(x=70, y=220)
            self.T73.insert(END, "Added tasks")
            self.T74 = Text(root, height=1, width=19, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T74.place(x=220, y=220)
            self.T74.insert(END, s.t_1)

            self.T12.configure(state=DISABLED)
            self.T13.configure(state=DISABLED)
            self.T15.configure(state=DISABLED)
            self.T22.configure(state=DISABLED)
            self.T23.configure(state=DISABLED)
            self.T24.configure(state=DISABLED)
            self.T25.configure(state=DISABLED)
            self.T69.configure(state=DISABLED)
            self.T70.configure(state=DISABLED)
            self.T72.configure(state=DISABLED)
            self.a = 1
            self.b = 1
            self.c = 0

    def timer(self):
        self.Enable = True
        while self.Enable:
            t4 = self.v1.get()
            t5 = self.v2.get()
            t = t4 * 60
            while t and self.Enable:
                try:
                    self.button3.configure(state=DISABLED)
                except:
                    pass
                mins, secs = divmod(int(t), 60)
                self.timer1 = '{:02d}:{:02d}'.format(mins, secs)
                self.T3.configure(state=NORMAL)
                self.T2.configure(state=NORMAL)
                self.T2.delete(1.0,END)
                self.T2.insert(END, self.timer1)
                self.T3.delete(1.0, END)
                self.T3.insert(END, "Focus!")
                self.T2.configure(state=DISABLED)
                self.T3.configure(state=DISABLED)
                time.sleep(1)
                t -= 1
                n=1
            if t == 0 and self.Enable:
                if n==1:
                    s.add(t4, 0)
                    n=0
                try:
                    notify2.init("Focus App")
                    notice = notify2.Notification("Timer", "Facus time has passed. Take a break!")
                    notice.show()
                except:
                    print("Notification error")

                playsound('ding.mp3')
                t2 = t5 * 60
                while t2 and self.Enable:
                    self.button3.configure(state=DISABLED)
                    mins, secs = divmod(int(t2), 60)
                    self.timer1 = '{:02d}:{:02d}'.format(mins, secs)
                    self.T3.configure(state=NORMAL)
                    self.T2.configure(state=NORMAL)
                    self.T2.delete(1.0, END)
                    self.T2.insert(END, self.timer1)
                    self.T3.delete(1.0, END)
                    self.T3.insert(END, "Brake")
                    self.T3.configure(state=DISABLED)
                    self.T2.configure(state=DISABLED)
                    time.sleep(1)
                    t2 -= 1
                    if t2 == 1:
                        s.add(0, t5)
            playsound('ding.mp3')
            try:
                notify2.init("Focus App")
                notice = notify2.Notification("Timer", "Break time has passed. Time to focus!")
                notice.show()
            except:
                print("Notification error")

class ToDo:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        self.tasks.clear()
        try:
            self.file = open("tasks.txt", "r")
            for a in self.file:
                self.tasks.append(a.strip())
            self.file.close()
            self.tasks_v = StringVar(value=self.tasks)
        except:
            messagebox.showinfo("Focus App", "Tasks file error!")

    def add_task(self):
        self.task = ui.entry.get()
        if self.task == "":
            return
        self.tasks.append(self.task)
        self.save_tasks()
        self.tasks_v = StringVar(value=self.tasks)
        ui.listbox.delete(0, END)
        for a in self.tasks:
            b = a+"\n"
            b.strip()
            ui.listbox.insert(END, b)
        ui.entry.delete(0, END)
        s.add(0, 0, 1)

    def save_tasks(self):
        self.file = open("tasks.txt", "w")
        for task in self.tasks:
            self.file.write(task+"\n")
        self.file.close()

    def delete_task(self):
        self.selected_indices = ui.listbox.curselection()[0]
        self.tasks.pop(self.selected_indices)
        self.save_tasks()
        self.tasks_v = StringVar(value=self.tasks)
        ui.listbox.delete(0, END)
        for a in self.tasks:
            b = a+"\n"
            b.strip("\n")
            ui.listbox.insert(END, b)

class Stats:
    def __init__(self):
        self.s_1 = 0
        self.s_2 = 0
        self.t_1 = 0
        self.stats = []

    def save(self):
        self.file = open("stats.txt", "w")
        for a in self.stats:
            self.file.write(str(a)+"\n")
        self.file.close()

    def load(self):
        self.file = open("stats.txt", "r")
        for a in self.file:
            self.stats.append(a)
        self.s_1 = self.stats[0]
        self.s_2 = self.stats[1]
        self.t_1 = self.stats[2]

    def add(self, a, b, c):
        self.load()
        self.s_1 = float(self.s_1) + float(a)
        self.s_2 = float(self.s_2) + float(b)
        self.t_1 = float(self.t_1) + float(c)
        self.stats.clear()
        self.stats.append(self.s_1)
        self.stats.append(self.s_2)
        self.stats.append(self.t_1)
        self.save()

ToDo1 = ToDo()
ui = UI()
s = Stats()

canvas = Canvas(
    root,
    height=500,
    width=65,
    bg=ui.color1,
    highlightthickness = 0,
    bd = 0
)
canvas2 = Canvas(
    root,
    height=70,
    width=500,
    bg=ui.color1,
    highlightthickness = 0,
    bd = 0
)

canvas.place(x=0)
canvas2.place(x=0)

ui.draw_button()
ui.draw_pomodoro()

root.mainloop()