
import tkinter as tk

class Memory():
    def __init__(self):
        window = tk.Tk()
        window.title("Memory")
        window.geometry('800x600')

        # value
        self.stage1 = tk.IntVar()
        self.stage2 = tk.IntVar()
        self.stage3 = tk.IntVar()
        self.stage4 = tk.IntVar()
        self.stage5 = tk.IntVar()
        
        self.stage1_number = tk.IntVar()
        self.stage2_number = tk.IntVar()
        self.stage3_number = tk.IntVar()
        self.stage4_number = tk.IntVar()
        self.stage5_number = tk.IntVar()

        # label & entry

        lable1 = tk.Label(window, text="stage1: Number displayed").grid(row=0)
        text1 = tk.Entry(window,bd=4, textvariable=self.stage1)
        text1.bind("<Return>", self.bind_callback)
        text1.grid(row=0,column=1)
        number1 = tk.Entry(window,bd=4, textvariable=self.stage1_number)
        number1.bind("<Return>", self.bind_callback)
        number1.grid(row=0,column=3)
        

        lable2 = tk.Label(window, text="stage2: Number displayed").grid(row=1)
        text2 = tk.Entry(window,bd=4, textvariable=self.stage2)
        text2.bind("<Return>", self.bind_callback)
        text2.grid(row=1,column=1)
        number2 = tk.Entry(window,bd=4, textvariable=self.stage2_number)
        number2.bind("<Return>", self.bind_callback)
        number2.grid(row=1,column=3)

        lable3 = tk.Label(window, text="stage3: Number displayed").grid(row=2)
        text3 = tk.Entry(window,bd=4, textvariable=self.stage3)
        text3.bind("<Return>", self.bind_callback)
        text3.grid(row=2,column=1)
        number3 = tk.Entry(window,bd=4, textvariable=self.stage3_number)
        number3.bind("<Return>", self.bind_callback)
        number3.grid(row=2,column=3)

        lable4 = tk.Label(window, text="stage4: Number displayed").grid(row=3)
        text4 = tk.Entry(window,bd=4, textvariable=self.stage4)
        text4.bind("<Return>", self.bind_callback)
        text4.grid(row=3,column=1)
        number4 = tk.Entry(window,bd=4, textvariable=self.stage4_number)
        number4.bind("<Return>", self.bind_callback)
        number4.grid(row=3,column=3)

        lable5 = tk.Label(window, text="stage5: Number displayed").grid(row=4)
        text5 = tk.Entry(window,bd=4, textvariable=self.stage5)
        text5.bind("<Return>", self.bind_callback)
        text5.grid(row=4,column=1)
        number5 = tk.Entry(window,bd=4, textvariable=self.stage5_number)
        number5.bind("<Return>", self.bind_callback)
        number5.grid(row=4,column=3)

        # label --> show result

        self.result1 = tk.Label(window, text="error", fg="red", font=56)
        self.result1.grid(row=0, column=2)

        self.result2 = tk.Label(window, text="error", fg="red", font=56)
        self.result2.grid(row=1, column=2)

        self.result3 = tk.Label(window, text="error", fg="red", font=56)
        self.result3.grid(row=2, column=2)

        self.result4 = tk.Label(window, text="error", fg="red", font=56)
        self.result4.grid(row=3, column=2)

        self.result5 = tk.Label(window, text="error", fg="red", font=56)
        self.result5.grid(row=4, column=2)

        window.mainloop()

    def bind_callback(self, event):
        self.process()

    def process(self):
        self.stage1_process()
        self.stage2_process()
        self.stage3_process()
        self.stage4_process()
        self.stage5_process()
        return 0

    def stage1_process(self):
        if self.stage1.get() == 1:
            self.result1.configure(text="second postion")
        elif self.stage1.get() == 2:
            self.result1.configure(text="second postion")
        elif self.stage1.get() == 3:
            self.result1.configure(text="third postion")
        elif self.stage1.get() == 4:
            self.result1.configure(text="forth postion")

    def stage2_process(self):
        if self.stage2.get() == 1:
            self.result2.configure(text="number [4]")
        elif self.stage2.get() == 2:
            self.result2.configure(text=self.result1["text"])
        elif self.stage2.get() == 3:
            self.result2.configure(text="first postion")
        elif self.stage2.get() == 4:
            self.result2.configure(text=self.result1["text"])

    def stage3_process(self):
        if self.stage3.get() == 1:
            self.result3.configure(text="number [%i]" % self.stage2_number.get())
        elif self.stage3.get() == 2:
            self.result3.configure(text="number [%i]" % self.stage1_number.get())
        elif self.stage3.get() == 3:
            self.result3.configure(text="third postion")
        elif self.stage3.get() == 4:
            self.result3.configure(text="number [4]")

    def stage4_process(self):
        if self.stage4.get() == 1:
            self.result4.configure(text=self.result1["text"])
        elif self.stage4.get() == 2:
            self.result4.configure(text="first postion")
        elif self.stage4.get() == 3:
            self.result4.configure(text=self.result2["text"])
        elif self.stage4.get() == 4:
            self.result4.configure(text=self.result2["text"])

    def stage5_process(self):
        if self.stage5.get() == 1:
            self.result5.configure(text="number [%i]" % self.stage1_number.get())
        elif self.stage5.get() == 2:
            self.result5.configure(text="number [%i]" % self.stage2_number.get())
        elif self.stage5.get() == 3:
            self.result5.configure(text="number [%i]" % self.stage4_number.get())
        elif self.stage5.get() == 4:
            self.result5.configure(text="number [%i]" % self.stage3_number.get())
Memory()