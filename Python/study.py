#coding UTF-8
import tkinter as tk
import pandas as pd
from tkinter import messagebox as mbox




class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        x = 0
        # 問題文読込
        data = pd.read_csv('data.csv', header=None)
        quota = data[1][x]
        Q = "問題：" + str(quota)
        #記録
        log = pd.read_csv('log.csv', header=None)
        self.pack()
        self.main()


def main(self): #GUI
    win = tk.Tk()
    #問題文
    Question = tk.Label(win,text=Q)
    Question.grid(row=1,columnspan=2,sticky=tk.W,padx=5, pady=5)
    #解答入力欄
    AL = tk.Label(win,text="解答")
    AL.grid(row=2,column=0,sticky=tk.W,padx=5, pady=5)
    Answer = tk.Entry(win)
    Answer.grid(row=2,column=1,rowspan=2,sticky=tk.E + tk.W,padx=5, pady=5)
    #解答ボタン
    AnsButton = tk.Button(win, text="解答する", command=check)
    AnsButton.grid(row=4, columnspan=2, sticky=tk.W + tk.E, padx=5, pady=5)
    #skipボタン
    SkipButton = tk.Button(win, text="Skip", command=skip)
    SkipButton.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=5, pady=5)
    #維持
    win.mainloop()

#正誤判定
def check():
    if Answer.get() == data[3][x]:
        print("OK")
    else:
        yourAns = Answer.get()
        mbox.showinfo("check", "Ans:"+data[3][x]+"\nyourAns:"+yourAns)
#Skipボタン
def skip(x):
    x = x + 1
    quota = data[2][x]
    Q = "問題：" + str(quota)
    Question["text"] = Q
    return x
    print(x)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

main()
