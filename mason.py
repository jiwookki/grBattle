import pickle, os, tkinter.messagebox, time, sys
from tkinter import *


class Display():
    def __init__(self, res, title, titleimage):
        self.res = res
        self.screen = Tk()
        self.screen.geometry(self.res)
        self.screen.title(title)
        if bool(titleimage) == False:
            self.titleimage = None
        else:
            self.screen.iconbitmap(titleimage)
    def change_res(self, res):
        self.res = "x".join(res)
        self.screen.geometry(self.res)
    def use_loop(self):
        self.screen.mainloop()
    def delete(self):
        self.screen.destroy()


class DispText():
    def __init__(self, screen, text, height, font, size, side):
        self.text = text
        self.screen = screen.screen
        self.height = height
        self.side = side
        self.font = font
        self.size = size
        self.sprite = Label(self.screen, text=self.text, height = self.height, font=(self.font, self.size))
        self.sprite.pack(side=self.side)
    def change_things(self, side, size, font, height, text):
        self.side = side
        self.text = text
        self.size = size
        self.font = font
        self.height = height
        self.sprite = Label(self.screen, text=self.text, height = self.height, font=(self.font, self.size))
        

class MultiLineEntry():
    def __init__(self, display, font, side):
        self.sprite = Text(display.screen, font=font)
        self.sprite.pack(side=side)
    def get_var(self):
        return self.sprite.get(1.0, END)
    def clear(self, column, end):
        if bool(end) == True:
            self.sprite.delete(column, end)
        else:
            self.sprite.delete(column)
    def paste_contents(self, newcontent, index):
        self.sprite.insert(index, newcontent)
    def change_contents(self, newcontent):
        self.sprite.delete(1, 1)
        self.sprite.insert(END, newcontent)
    def append_end(self, new):
        self.sprite.insert(END, new)
class button():
    def __init__(self, screen, text, command, side):
        self.screen = screen.screen
        self.text = text
        self.command = command
        self.side = side
        self.sprite = Button(self.screen, text=self.text, command=self.command)
        self.sprite.pack(side=self.side)
    def change_things(self, side, text):
        self.text = text
        self.side = side
        self.sprite = Button(self.screen, text=self.text, command=self.command)
        self.sprite.pack(side=self.side) 
class DropDownMenu():
    def __init__(self, screen, side, options):
        self.values = options 
        self.centerValue = StringVar()
        self.centerValue.set(self.values[0])
        self.sprite = OptionMenu(screen.screen, self.centerValue, *self.values)
        if bool(side) == True:
            self.sprite.pack(side)
        else:
            self.sprite.pack()
    def add_option(self, newvar):
        self.values.append(newvar)
    def set_selected(self, newvalue):
        self.centerValue.set(newvalue)
    def get_selected(self):
        return self.centerValue.get()

class SingleLineEntry():
    def __init__(self, display, side):
        self.sprite = Entry(display.screen)
        print(side)
        if bool(side) == True:
            self.sprite.pack(side)
        else:
            self.sprite.pack()
            
    def get_var(self): 
        return self.sprite.get()
    def clear(self, rowcolumn, end):
        if bool(end) == True:
            self.sprite.delete(rowcolumn, end)
        else:
            self.sprite.delete(rowcolumn, end)

def openFile():
    global pickerOfFiles
    odata = open(pickerOfFiles.get_selected(), "rb")
    ndata = pickle.load(odata)
    createTextWindow(ndata, pickerOfFiles.get_selected())

def createTextWindow(data, filename):
    global newdata
    def saveText():
        global newdata
        newdata = open(filename, 'wb')
        pickle.dump(fileEntry.get_var(), newdata)
        print(fileEntry.get_var())
    def autoSaveShut():
        global newdata
        saveText()
        newdata.close()
        textDisplay.delete()

    textDisplay = Display("640x480", "editing " + filename, None)
    fileEntry = MultiLineEntry(textDisplay, "Helvetica", None)
    fileEntry.append_end(data)
    saveButton = button(textDisplay, "Save", saveText, "bottom")
    textDisplay.screen.protocol("WM_DELETE_WINDOW", autoSaveShut)
    textDisplay.use_loop()


def old_thing():
    command = input("What command? [O] open a .dat file, [Q] quit app, [F] Format a file in pickle format, [V] print out a .dat file: ")
    if command == "O":
        filename = input("Which file would you like to open? >> ")
        data = open(filename, 'rb')
        ndata = pickle.load(data)
        createTextWindow(ndata, filename)

    if command == "Q":
        quit()
    if command == "F":
        filename = input("Which file would you like to format? ")
        data = open(filename, 'wb')
        pickle.dump("Hello, this is pickle format. New file", data)
        print("formatting complete")
        data.close()
    if command == "V":
        filename = input("Which file would you like to view? ")
        data = open(filename, 'rb')
        ndata = pickle.load(data)
        print(ndata)
    raise ValueError("custom error: Unknown command")


def AutoSearchFiles():
    global pickerOfFiles
    listOfFinds = []
    for file in os.listdir():
        if file.endswith(".dat"):
            listOfFinds.append(file)
    if bool(listOfFinds) == False:
        tkinter.messagebox.showerror("Error", "Sorry, no data files were detected in the local directory.")
    else:

        sWindow = Display("320x240", "File search", None)
        sInst = DispText(sWindow, "Pick a file to open", 2, "Helvetica", 10, None)
        pickerOfFiles = DropDownMenu(sWindow, None, listOfFinds)
        okButton = button(sWindow, "Open file", openFile, "bottom")
        sWindow.use_loop()

def autoInitFile():
    global pickerOfFiles
    def initFile():
        global pickerOfFiles
        data = open(pickerOfFiles.get_selected(), 'wb')
        pickle.dump("Hello, this is pickle format. New file", data)
        tkinter.messagebox.showinfo("Formatting complete", "Formatting of file was completed")
        data.close()
    listOfFinds = []
    for file in os.listdir():
        if file.endswith(".dat"):
            listOfFinds.append(file)
    if bool(listOfFinds) == False:
        tkinter.messagebox.showerror("Error", "Sorry, no data files were detected in the local directory.")
    else:

        sWindow = Display("320x240", "File search", None)
        sInst = DispText(sWindow, "Pick a file to open", 2, "Helvetica", 10, None)
        pickerOfFiles = DropDownMenu(sWindow, None, listOfFinds)
        okButton = button(sWindow, "Open file", initFile, "bottom")
        sWindow.use_loop()

def createFile():

    def NewCreate():
        newFileName = fileNameEntry.get_var() + ".dat"
        listOfFinds = []
        for file in os.listdir():
            if file.endswith(".dat"):
                listOfFinds.append(file)
        if newFileName in listOfFinds:
            tkinter.messagebox.showerror("Error", "A file with the name " + newFileName + " already exists. Please rename or delete the existing file or rename your new file.")
        else:
            newFile = open(newFileName, "wb")
            pickle.dump("this file created at " + time.asctime(), newFile)
            newFile.close()
            tkinter.messagebox.showinfo("Success!", "File successfully created.")

        
    openWindow = Display("320x240", "Name new file", None)
    titNew = DispText(openWindow, "Filename", 2, "Helvetica", 12, "top") 
    fileNameEntry = SingleLineEntry(openWindow, None)
    contButton = button(openWindow, "Create New File", NewCreate, "bottom")
    openWindow.use_loop()

def main():
    def showVer():
        tkinter.messagebox.showinfo("Version Info", "pickle-mason 1.0, 15/5/2020, all rights reserved. Copyright © 2020 Swordfish Games.")
    root = Display("640x480", "Pickle Mason binary data opener", None)
    titRoot = DispText(root, "Welcome to the Pickle Mason binary data editor.", 2, "Helvetica", 18, "top")
    findFileButton = button(root, "Auto-search local directory for .dat files", AutoSearchFiles, None)
    initButton = button(root, "Initialise an empty .dat file", autoInitFile, None)
    createButton = button(root, "Create an initialised .dat file", createFile, None)
    quitBt = button(root, "Quit", sys.exit, None)
    verBT = button(root,"Show version info", showVer, "bottom")
    root.use_loop()



main()
