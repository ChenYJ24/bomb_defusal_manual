import tkinter as tk
import os
from functools import partial

list_total = {}
list_total['list1'] = [1,2,3,4,5,6,7]
list_total['list2'] = [8,1,7,9,10,6,11]
list_total['list3'] = [12,13,9,14,15,3,10]
list_total['list4'] = [16,17,18,5,14,11,19]
list_total['list5'] = [20,19,18,21,17,22,23]
list_total['list6'] = [16,8,24,25,20,26,27]

class Keypads():
    def __init__(self):
        window = tk.Tk()
        window.title("Keypads")
        window.geometry('800x600')

        # value : 27
        self.value_dict = {}
        self.flag_dict = {}
        for i in range(1,28):
            self.value_dict["value"+str(i)] = 0
            self.flag_dict['flag'+str(i)] = False

        # Creating a photoimage object to use image
        # path
        path_dict = {}
        self.photo_dict = {}
        self.button_dict = {}
        for i in range(1,28):
            path_dict['path'+str(i)] = os.path.dirname(__file__) + '/png/'+str(i)+'.png'
            self.photo_dict['photo'+str(i)] = tk.PhotoImage(file = path_dict['path'+str(i)])
            self.button_dict['button'+str(i)] = tk.Button(window,image=self.photo_dict['photo'+str(i)],width=100,height=100, command=partial(self.callback, i))
            a = (i-1)%5
            b = (i-1)//5
            self.button_dict['button'+str(i)].grid(row=a,column=b)
        # result
        self.result_dict = {}
        for i in range(1,5):
            self.result_dict['result'+str(i)] = tk.Label(window,image=self.photo_dict['photo'+str(i)])
            self.result_dict['result'+str(i)].grid(row=i,column=7)

        window.mainloop()

    def callback(self,value):
        # print(value)
        self.flag_dict['flag'+str(value)] = not self.flag_dict['flag'+str(value)]
        if self.flag_dict['flag'+str(value)] == True:
            self.value_dict['value'+str(value)] = value
            self.button_dict['button'+str(value)].configure(bg='red')
        else:
            self.value_dict['value'+str(value)] = 0
            self.button_dict['button'+str(value)].configure(bg='grey95')
        
        self.process()
        
    def process(self):
        self.candidate = []
        for i in range(1,28):
            if self.value_dict['value'+str(i)] != 0:
                self.candidate.append(self.value_dict['value'+str(i)])
                print(self.value_dict['value'+str(i)])
        
        for i in range(1,7):
            list1_as_set = set(list_total['list'+str(i)])
            intersection = list1_as_set.intersection(self.candidate)
            intersection_as_list = list(intersection)
            if (len(intersection_as_list)) == 4:
                print(intersection_as_list)
                k = 0
                for j in list_total['list'+str(i)]:
                    if j in intersection_as_list:
                        k += 1
                        self.result_dict['result'+str(k)].configure(image=self.photo_dict['photo'+str(j)])

   

Keypads()