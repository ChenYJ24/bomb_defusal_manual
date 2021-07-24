import numpy as np
import tkinter as tk


lookup_table = np.array([[1,"about"],[2,"after"],[3,"again"],
                         [4,"below"],
                         [5,"could"],
                         [6,"every"],
                         [7,"first"],[8,"found"],
                         [9,"great"],
                         [10,"house"],
                         [11,"large"],[12,"learn"],
                         [13,"never"],
                         [14,"other"],
                         [15,"place"],[16,"plant"],[17,"point"],
                         [18,"right"],
                         [19,"small"],[20,"sound"],[21,"spell"],[22,"still"],[23,"study"],
                         [24,"their"],[25,"there"],[26,"these"],[27,"thing"],[28,"think"],[29,"three"],
                         [30,"water"],[31,"where"],[32,"which"],[33,"world"],[34,"would"],[35,"write"]])

class Passwords:
    def __init__(self):
        window = tk.Tk()
        window.title("password")
        window.geometry('1100x600')

        # table
        self.label_list = []
        for i in range(len(lookup_table)):
            label = tk.Label(window, padx=20, pady=10, text = lookup_table[i][1])
            label.grid(row=int(i/5 + 1), column =(i%5))
            self.label_list.append(label)
        # label & entry
        lable1 = tk.Label(window, text="Enter first letter:").grid(row=8,columnspan=2)
        self.entry1_txt = tk.StringVar()
        text1 = tk.Entry(window,bd=4, textvariable=self.entry1_txt)
        text1.bind("<Return>", self.on_change1)
        text1.grid(row=8,column=2, columnspan=2)

        lable2 = tk.Label(window, text="Enter second letter:").grid(row=9,columnspan=2)
        self.entry2_txt = tk.StringVar()
        text2 = tk.Entry(window,bd=4, textvariable=self.entry2_txt)
        text2.bind("<Return>", self.on_change2)
        text2.grid(row=9,column=2, columnspan=2)

        lable3 = tk.Label(window, text="Enter third letter:").grid(row=10,columnspan=2)
        self.entry3_txt = tk.StringVar()
        text3 = tk.Entry(window,bd=4, textvariable=self.entry3_txt)
        text3.bind("<Return>", self.on_change3)
        text3.grid(row=10,column=2, columnspan=2)

        lable4 = tk.Label(window, text="Enter forth letter:").grid(row=11,columnspan=2)
        self.entry4_txt = tk.StringVar()
        text4 = tk.Entry(window,bd=4, textvariable=self.entry4_txt)
        text4.bind("<Return>", self.on_change4)
        text4.grid(row=11,column=2, columnspan=2)

        lable5 = tk.Label(window, text="Enter fifth letter:").grid(row=12,columnspan=2)
        self.entry5_txt = tk.StringVar()
        text5 = tk.Entry(window,bd=4, textvariable=self.entry5_txt)
        text5.bind("<Return>", self.on_change5)
        text5.grid(row=12,column=2, columnspan=2)

        # label & listbox
        listbox1_label = tk.Label(window,text="first check").grid(row=1,column=6)
        self.listbox1 = tk.Listbox(window, height=20, width=12)
        self.listbox1.grid(row=2, rowspan=10, column=6, sticky=tk.N)

        listbox2_label = tk.Label(window,text="second check").grid(row=1,column=7)
        self.listbox2 = tk.Listbox(window, height=20, width=12)
        self.listbox2.grid(row=2, rowspan=10, column=7, sticky=tk.N)

        listbox3_label = tk.Label(window,text="third check").grid(row=1,column=8)
        self.listbox3 = tk.Listbox(window, height=20, width=12)
        self.listbox3.grid(row=2, rowspan=10, column=8, sticky=tk.N)

        listbox4_label = tk.Label(window,text="forth check").grid(row=1,column=9)
        self.listbox4 = tk.Listbox(window, height=20, width=12)
        self.listbox4.grid(row=2, rowspan=10, column=9, sticky=tk.N)

        listbox5_label = tk.Label(window,text="fifth check").grid(row=1,column=10)
        self.listbox5 = tk.Listbox(window, height=20, width=12)
        self.listbox5.grid(row=2, rowspan=10, column=10, sticky=tk.N)

        # member variable
        self.satisfy_first = []
        self.satisfy_second = []
        self.satisfy_third = []
        self.satisfy_forth = []
        self.satisfy_fifth = []

        self.first_letter = ""
        self.second_letter = ""
        self.third_letter = ""
        self.forth_letter = ""
        self.fifth_letter = ""

        window.mainloop()

    def process(self):
        print("process")
        self.first_check(self.first_letter)
        self.second_check(self.second_letter)
        self.third_check(self.third_letter)
        self.forth_check(self.forth_letter)
        self.fifth_check(self.fifth_letter)

    def first_check(self, first_letter):
        self.satisfy_first.clear()
        self.listbox1.delete(0,'end')
        for i in range(len(first_letter)):
            for j in range(len(lookup_table)):
                if first_letter[i] == lookup_table[j][1][0]:
                    self.satisfy_first.append(lookup_table[j])
        print(self.satisfy_first)
        for i in range(len(self.satisfy_first)):
            self.listbox1.insert(i,self.satisfy_first[i][1])

    def second_check(self, second_letter):
        self.satisfy_second.clear()
        self.listbox2.delete(0,'end')
        for i in range(len(second_letter)):
            for j in range(len(self.satisfy_first)):
                if second_letter[i] == self.satisfy_first[j][1][1]:
                    self.satisfy_second.append(self.satisfy_first[j])
        print(self.satisfy_second)
        for i in range(len(self.satisfy_second)):
            self.listbox2.insert(i,self.satisfy_second[i][1])

    def third_check(self, third_letter):
        self.satisfy_third.clear()
        self.listbox3.delete(0,'end')
        for i in range(len(third_letter)):
            for j in range(len(self.satisfy_second)):
                if third_letter[i] == self.satisfy_second[j][1][2]:
                    self.satisfy_third.append(self.satisfy_second[j])
        print(self.satisfy_third)
        for i in range(len(self.satisfy_third)):
            self.listbox3.insert(i,self.satisfy_third[i][1])
    
    def forth_check(self, forth_letter):
        self.satisfy_forth.clear()
        self.listbox4.delete(0,'end')
        for i in range(len(forth_letter)):
            for j in range(len(self.satisfy_third)):
                if forth_letter[i] == self.satisfy_third[j][1][3]:
                    self.satisfy_forth.append(self.satisfy_third[j])
        print(self.satisfy_forth)
        for i in range(len(self.satisfy_forth)):
            self.listbox4.insert(i,self.satisfy_forth[i][1])

    def fifth_check(self, fifth_letter):
        self.satisfy_fifth.clear()
        self.listbox5.delete(0,'end')
        for i in range(len(fifth_letter)):
            for j in range(len(self.satisfy_forth)):
                if fifth_letter[i] == self.satisfy_forth[j][1][4]:
                    self.satisfy_fifth.append(self.satisfy_forth[j])
        print(self.satisfy_fifth)
        for i in range(len(self.satisfy_fifth)):
            self.listbox5.insert(i,self.satisfy_fifth[i][1])

    def on_change1(self, text1):
        self.first_letter = self.entry1_txt.get()
        self.process()
    
    def on_change2(self, text2):
        self.second_letter = self.entry2_txt.get()
        self.process()
        
    def on_change3(self, text3):
        self.third_letter = self.entry3_txt.get()
        self.process()

    def on_change4(self, text4):
        self.forth_letter = self.entry4_txt.get()
        self.process()

    def on_change5(self, text5):
        self.fifth_letter = self.entry5_txt.get()
        self.process()
    
Passwords()