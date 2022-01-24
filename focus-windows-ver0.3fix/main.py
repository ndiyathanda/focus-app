#Focus app ver0.3 by ndiyathanda (Michał Zbiegień)
#https://github.com/ndiyathanda/focus-app
from tkinter import *
import time, os, sys
import threading, keyboard
from playsound import playsound
from tkinter import messagebox
from win10toast import ToastNotifier

noti = ToastNotifier()

root = Tk()
root.title("Focus")
root.geometry('510x400')
root.resizable(0, 0)

class UI:
    def __init__(self):
        self.y = True
        self.Enable = True
        thread = threading.Thread(target=self.check_keys)
        thread.daemon = True
        thread.start()
        print("init")
        self.load_settings()
        self.color1 = self.u_color1.strip()
        self.color2 = self.u_color2.strip()
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
        self.img10 = PhotoImage(file="settings.png")
        self.img11 = PhotoImage(file="c1.png")
        self.img12 = PhotoImage(file="c2.png")
        self.img13 = PhotoImage(file="c3.png")
        self.img14 = PhotoImage(file="c4.png")
        self.img15 = PhotoImage(file="pause.png")
        self.img16 = PhotoImage(file="play.png")

    def load_settings(self):
        self.file = open("settings.txt", "r")
        self.settings_l = []

        for a in self.file:
            self.settings_l.append(a)

        self.u_color1 = self.settings_l[0]
        self.u_color2 = self.settings_l[1]

    def save_settings(self, a, b):
        self.file = open("settings.txt", "w")
        self.file.write(a + "\n" + b)
        print(a, b)
        self.file.close()

    def check_keys(self):
        while True:
            time.sleep(0.02)
            try:
                if keyboard.is_pressed("del"):
                    ToDo1.delete_task()
                    time.sleep(0.5)
                if keyboard.is_pressed("enter"):
                    ToDo1.add_task()
                    time.sleep(0.5)
            except:
                pass

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

        button5 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=self.settings)
        button5.config(image=self.img10, bg=self.color1)
        button5.place(x=0, y=335)

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

        try:
            self.T100.place_forget()
            self.T101.place_forget()
            self.buttons1.destroy()
            self.buttons2.destroy()
            self.buttons3.destroy()
            self.buttons4.destroy()
            self.s3.destroy()
            self.ls.destroy()
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
                height=13,
                width=52,
                bg=self.color2,
                highlightthickness=0,
                highlightcolor=self.color1,
                selectmode='extended',
                font=("Helvetica", 15))
            self.listbox.place(x=65, y=68)
            self.l2 = Label(root, text='Task name', bg=self.color2)
            self.l2.place(x=65, y=382)
            self.entry = Entry(root, width=61, bg=self.color2, highlightthickness=0)
            self.entry.place(x=140, y=382)
            self.a = 0
            self.b = 1
            self.d = 1

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
        try:
            self.T100.place_forget()
            self.T101.place_forget()
            self.buttons1.destroy()
            self.buttons2.destroy()
            self.buttons3.destroy()
            self.buttons4.destroy()
            self.s3.destroy()
            self.ls.destroy()
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
            self.button3 = Button(root, text="Click me!", highlightthickness=0, bd=0, command=self.countdown, disabledforeground=self.color2)
            self.button3.config(image=self.img3, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)
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
            self.T3 = Text(root, height=1, width=20, highlightthickness=0, bd=0, bg=self.color1, font=("Helvetica", 32))
            self.T3.place(x=66, y=20)
            self.T3.insert(END, "")
            self.T = Text(root, height=2, width=10, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 11))
            self.T.place(x=370, y=300)
            self.T.insert(END, "Rest time")
            self.T.configure(state=DISABLED)
            self.T5 = Text(root, height=2, width=10, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 11))
            self.T5.place(x=110,y=300)
            self.T5.insert(END, "Focus time")
            self.T5.configure(state=DISABLED)
            self.buttonP = Button(root, text="Click me!", highlightthickness=0, bd=0, command=self.pause, disabledforeground=self.color2)
            self.buttonP.config(image=self.img15, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)
            self.buttonP.place(x=250,y=180)
            if self.Enable == False:
                self.buttonP.config(image=self.img16, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)
            else:
                self.buttonP.config(image=self.img15, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)

            self.b = 0
            self.c = 1
            self.d = 1

    def reset(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def countdown(self):
        self.buttonP.configure(state=NORMAL)
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
            self.buttonP.place_forget()
        except:
            pass

        try:
            self.T100.place_forget()
            self.T101.place_forget()
            self.buttons1.destroy()
            self.buttons2.destroy()
            self.buttons3.destroy()
            self.buttons4.destroy()
            self.s3.destroy()
            self.ls.destroy()
        except:
            pass

        if self.c == 1:
            self.T12 = Text(root, height=1, width=19, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T12.place(x=70, y=85)
            self.T12.insert(END, "Focus time")
            self.T12.configure(state=DISABLED)
            self.T13 = Text(root, height=1, width=5, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T13.place(x=210, y=85)
            self.T13.insert(END, round(float(s.s_1)))
            self.T15 = Text(root, height=1, width=3, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T15.place(x=270, y=85)
            self.T15.insert(END, "min")
            self.T22 = Text(root, height=1, width=10, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T22.place(x=70, y=130)
            self.T22.insert(END, "Brake time")
            self.T23 = Text(root, height=1, width=5, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T23.place(x=210, y=130)
            self.T23.insert(END, round(float(s.s_2)))
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
            self.T74.insert(END, round(float(s.t_1)))
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
            self.d = 1

    def settings(self):
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
            self.buttonP.destroy()
        except:
            pass
        try:
            self.T12.place_forget()
            self.T13.place_forget()
            self.T15.place_forget()
            self.T22.place_forget()
            self.T23.place_forget()
            self.T24.place_forget()
            self.T25.place_forget()
            self.T69.place_forget()
            self.T70.place_forget()
            self.T72.place_forget()
            self.T73.place_forget()
            self.T74.place_forget()
        except:
            pass
        if self.d == 1:
            self.T100 = Text(root, height=1, width=6, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 24))
            self.T100.place(x=100, y=75)
            self.T100.insert(END, "Theme")
            self.T100.configure(state=DISABLED)
            self.T101 = Text(root, height=1, width=20, highlightthickness=0, bd=0, bg=self.color2, font=("Helvetica", 18))
            self.T101.place(x=100, y=190)
            self.T101.insert(END, "Pomodoro sessions")
            self.T101.configure(state=DISABLED)
            self.buttons1 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=lambda: self.change_ui(1))
            self.buttons1.config(image=self.img11, bg=self.color1)
            self.buttons1.place(x=100, y=120)
            self.buttons2 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=lambda: self.change_ui(2))
            self.buttons2.config(image=self.img12, bg=self.color1)
            self.buttons2.place(x=180, y=120)
            self.buttons3 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=lambda: self.change_ui(3))
            self.buttons3.config(image=self.img13, bg=self.color1)
            self.buttons3.place(x=260, y=120)
            self.buttons4 = Button(root, text="Click me!", highlightthickness=0, bd=0, activebackground=self.color2, command=lambda: self.change_ui(4))
            self.buttons4.config(image=self.img14, bg=self.color1)
            self.buttons4.place(x=340, y=120)
            self.selected = DoubleVar()
            self.ls = Label(root, text="ver0.3", bd=0, bg=self.color2, font=("Helvetica", 10))
            self.ls.place(x=470, y=380)
            self.s3 = Scale(root, variable=self.selected,
                            from_=1, to=10,
                            orient=HORIZONTAL,
                            bg=self.color2,
                            highlightthickness=0,
                            bd=0,
                            activebackground=self.color2,
                            foreground="black")
            self.s3.place(x=100, y=220)
            self.a = 1
            self.b = 1
            self.c = 1
            self.d = 0
    def change_ui(self, n):
        if n==1:
            self.save_settings("#32373B", "#353C3F")
            messagebox.showinfo("Focus", "You need to restart app to fully apply changes")
        if n==2:
            self.save_settings("#400B72", "#440D78")
            messagebox.showinfo("Focus", "You need to restart app to fully apply changes")
        if n==3:
            self.save_settings("#7962A5", "#9172C1")
            messagebox.showinfo("Focus", "You need to restart app to fully apply changes")
        if n==4:
            self.save_settings("#F6E9E9", "#F6EFEE")
            messagebox.showinfo("Focus", "You need to restart app to fully apply changes")

    def pause(self):
        if self.Enable==True:
            self.Enable = False
            self.buttonP.config(image=self.img16, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)
            time.sleep(0.2)
        else:
            self.buttonP.config(image=self.img15, bg=self.color2, activebackground=self.color2, disabledforeground=self.color2)
            self.Enable = True
            time.sleep(0.2)


    def timer(self):
        self.h = 1
        try:
            self.z = int(self.selected.get())
            self.g = self.z
        except:
            self.z = 4
            self.g = self.z
        while True:
            time.sleep(0.01)
            if self.y == False:
                pass
            else:
                print(self.z)
                self.t4 = self.v1.get()
                self.t5 = self.v2.get()
                self.t = self.t4 * 60
                self.y = False
            while self.t and self.Enable and self.z != 0:
                try:
                    self.buttonP.configure(state=NORMAL)
                except:
                    pass
                try:
                    self.button3.configure(state=DISABLED)
                except:
                    pass
                mins, secs = divmod(int(self.t), 60)
                self.timer1 = '{:02d}:{:02d}'.format(mins, secs)
                self.T3.configure(state=NORMAL)
                self.T2.configure(state=NORMAL)
                self.T2.delete(1.0,END)
                self.T2.insert(END, self.timer1)
                self.T3.delete(1.0, END)
                self.T3.insert(END, "Focus! Session " + str(self.h) + " of " + str(self.g))
                self.T2.configure(state=DISABLED)
                self.T3.configure(state=DISABLED)
                time.sleep(1)
                self.t -= 1
                n=1

            if self.t == 0 and self.Enable:
                if n==1:
                    s.add(self.t4, 0, 0)
                    n=0
                self.z -= 1
                try:
                    playsound(u'ding.mp3')
                except:
                    pass
                noti.show_toast("Focus","Focus time has passed. Take a break!!")
                if self.z == 0:
                    playsound(u'ding.mp3')
                    noti.show_toast("Focus", "You have finished your sessions.")
                    self.Enable = False
                    time.sleep(2)
                    self.reset()

                self.t2 =self.t5 * 60

                while self.t2 and self.Enable and self.z != 0:
                    try:
                        self.button3.configure(state=DISABLED)
                        self.buttonP.configure(state=DISABLED)
                    except:
                        pass
                    mins, secs = divmod(int(self.t2), 60)
                    self.timer1 = '{:02d}:{:02d}'.format(mins, secs)
                    self.T3.configure(state=NORMAL)
                    self.T2.configure(state=NORMAL)
                    self.T2.delete(1.0, END)
                    self.T2.insert(END, self.timer1)
                    self.T3.delete(1.0, END)
                    self.T3.insert(END, "Brake Session " + str(self.h) + " of " + str(self.g))
                    self.T3.configure(state=DISABLED)
                    self.T2.configure(state=DISABLED)
                    time.sleep(1)
                    self.t2 -= 1
                    if self.t2 == 1:
                        s.add(0, self.t5, 0)
                        noti.show_toast("Focus", "Break time has passed. Time to focus!")
                        self.h += 1
                        print(self.h)
                        self.t = self.t4 * 10

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
    width=530,
    bg=ui.color1,
    highlightthickness = 0,
    bd = 0
)

canvas.place(x=0)
canvas2.place(x=0)

ui.draw_button()
ui.draw_pomodoro()

root.mainloop()
