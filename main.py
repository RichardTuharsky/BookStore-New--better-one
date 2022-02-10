from tkinter import*
from tkinter import ttk
from datetime import datetime
from tkinter import font
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
        self.lblTitle = Label(TitleFrame, width=43, font=(
            'arial', 40, 'bold'), text="Kniznica")
        self.lblTitle.grid()
        ButtonFrame = Frame(MainFrame, bd=10, width=1350,
                            height=50, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=10, width=1300,
                          height=400, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFTCover = LabelFrame(
            DataFrame, bd=10, width=800, height=300, padx=13, pady=2, relief=RIDGE, bg='cadetblue', font=('arial', 12, 'bold'), text="Informacie o uzivateloch")
        DataFrameLEFTCover.pack(side=LEFT, padx=10)
        DataFrameLEFT = Frame(DataFrameLEFTCover, bd=10,
                              width=800, height=300, padx=13, pady=2, relief=RIDGE)
        DataFrameLEFT.pack(side=TOP)
        DataFrameLEFTb = LabelFrame(DataFrameLEFTCover, bd=10, width=800, height=100, pady=4,
                                    padx=10, relief=RIDGE, font=('arial', 12, 'bold'), text="Informacie o uzivateloch")
        DataFrameLEFTb.pack(side=TOP)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=10,
                                    relief=RIDGE, bg='cadetblue', font=('arial', 12, 'bold'), text="Detaily o knihach")
        DataFrameRIGHT.pack(side=RIGHT)


if __name__ == '__main__':
    root = Tk()
    appliaction = Library(root)
    root.mainloop()
