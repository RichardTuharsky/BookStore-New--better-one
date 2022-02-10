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

        MainFrame = Frame(self.root, bg='lightsteelblue')
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
            DataFrame, bd=10, width=800, height=300, padx=13, pady=2, relief=RIDGE, bg='lightsteelblue', font=('arial', 12, 'bold'), text="Informacie o uzivateloch")
        DataFrameLEFTCover.pack(side=LEFT, padx=10)
        DataFrameLEFT = Frame(DataFrameLEFTCover, bd=10,
                              width=800, height=300, padx=13, pady=2, relief=RIDGE)
        DataFrameLEFT.pack(side=TOP)
        DataFrameLEFTb = LabelFrame(DataFrameLEFTCover, bd=10, width=800, height=100, pady=4,
                                    padx=10, relief=RIDGE, font=('arial', 12, 'bold'), text="Informacie o uzivateloch")
        DataFrameLEFTb.pack(side=TOP)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=10,
                                    relief=RIDGE, bg='lightsteelblue', font=('arial', 12, 'bold'), text="Detaily o knihach")
        DataFrameRIGHT.pack(side=RIGHT)

        self.btnData = Button(ButtonFrame, text="Data", font=(
            'arial', 19, 'bold'), padx=4, width=16, bd=4, bg="lightsteelblue")
        self.btnData.grid(row=0, column=0, padx=3)
        self.btnDelete = Button(ButtonFrame, text="Vymaz", font=(
            'arial', 19, 'bold'), padx=4, width=16, bd=4, bg="lightsteelblue")
        self.btnDelete.grid(row=0, column=1, padx=3)
        self.btnSearch = Button(ButtonFrame, text="Hladaj", font=(
            'arial', 19, 'bold'), padx=4, width=16, bd=4, bg="lightsteelblue")
        self.btnSearch.grid(row=0, column=2, padx=3)
        self.btnReset = Button(ButtonFrame, text="Reset", font=(
            'arial', 19, 'bold'), padx=4, width=16, bd=4, bg="lightsteelblue")
        self.btnReset.grid(row=0, column=3, padx=3)
        self.btnExit = Button(ButtonFrame, text="Exit", font=(
            'arial', 19, 'bold'), padx=4, width=16, bd=4, bg="lightsteelblue")
        self.btnExit.grid(row=0, column=4, padx=3)


if __name__ == '__main__':
    root = Tk()
    appliaction = Library(root)
    root.mainloop()
