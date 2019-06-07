from tkinter import * 
from tkinter import filedialog
from tkinter import Tk

class SearchBox(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

# Title bar of search box GUI
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(595, 190))
        self.master.title('Directory Search')
        self.master.config(bg='#ffa500')
        
# Browse section of search box
        self.btnBrowse1 = Button(self.master, text='Browse...', width=15, height=2, command = self.browseDirectory)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(50,0))
        self.txtBox1 = Entry(self.master, font=('Arial', 10), fg='black', width=60)
        self.txtBox1.grid(row=0, column=1, padx=(10,0), pady=(45,0))
        self.lblMsg = Label(self.master, text='', font=('Arial', 10), fg='black', width=55, bg='#ffa500')
        self.lblMsg.grid(row=1, column=1, padx=(5,0), pady=(0,20))

# Close program row of search box
        self.btnCloseProg = Button(self.master, text='Close Program', width=15, height=2, command=self.close)
        self.btnCloseProg.grid(row=2, column=1, sticky=SE)

#---------------------------------Button Functions --------------------------------------

    def browseDirectory(self):
        test = self.txtBox1.get() 
        print(test)

        test1 = self.txtBox1.delete(0, END)
        print(test1)
        
        dirVariable = filedialog.askdirectory()
        self.lblMsg.config(text='Above is the selected directory path...')
        self.txtBox1.insert(0, dirVariable)
        print(self.txtBox1.get())

    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = SearchBox(root)
    root.mainloop()
