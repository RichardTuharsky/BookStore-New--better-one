from tkinter import*
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox
from tkcalendar import*
import datetime
import pymysql


class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Kniznica")
        self.root.geometry("1350x750+0+0")
        self.root.configure(bg='lightsteelblue')

        MType = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Member = StringVar()
        Adress = StringVar()
        Adress2 = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        BookISBN = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()

        MainFrame = Frame(self.root, bg='cadetblue')
        MainFrame.grid()
        TitleFrame = Frame(MainFrame, bd=10, width=1350, padx=60, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame, width=38, font=(
            'arial', 40, 'bold'), text="Kniznica")
        self.lblTitle.grid()


if __name__ == '__main__':
    root = Tk()
    appliaction = Library(root)
    root.mainloop()
