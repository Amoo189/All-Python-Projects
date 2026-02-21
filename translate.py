import googletrans
from tkinter import *
import sys
translator = googletrans.Translator()
class BaseFrame:
    def __init__(self, master):
        def clip():
            master.clipboard_clear()
            master.clipboard_append(translator.translate(self.box.get(1.0, END), self.var.get()).text)
        master = Frame(master)
        frame1 = LabelFrame(master, text="Enter your word:")
        frame1.pack()
        self.box = Text(frame1, width=25, height=10)
        self.box.pack(fill=BOTH)
        frame2 = LabelFrame(master, text="Choose your language:")
        frame2.pack()
        self.var = StringVar()
        self.var.set("fa")
        w = OptionMenu(frame2, self.var, "en", "fa")
        w.pack()
        Button(master, text="translat", command=self.translate).pack()
        frame3 = LabelFrame(master, text="natige")
        frame3.pack()
        self.result = Text(frame3, width=25, height=10)
        self.result.pack(fill=BOTH)
        Button(master, text="copy", command=clip).pack()
        Button(master, text="delete", command=self.clear).pack()
        master.pack(fill=BOTH)
    def translate(self):
        self.result.delete(1.0, END)
        self.result.insert(END, translator.translate(self.box.get(1.0, END), self.var.get()).text)
    def clear(self):
        self.result.delete(1.0, END)
        self.box.delete(1.0, END)
if __name__ == '__main__':
    root = Tk()
    root.title("Virus30")
    BaseFrame(root)
    root.mainloop()