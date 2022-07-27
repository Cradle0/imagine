from code import compile_command
from msilib.schema import ListBox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pathlib

import os
from PIL import Image,ImageTk


class ImageineExplorer:

	def changeDir(self,*event):
		
		dir = os.listdir(self.curr_dir.get())

		self.listbox.delete = (0,END)

		for x in dir:
			self.listbox.insert(0,x)
	
	
	def changeDirButton(self,event=None):
		selected = self.listbox.get(self.listbox.curselection()[0])

		path = os.path.join(self.curr_dir.get(),selected)

		if os.path.isfile(path):
			os.startfile(path)
		else:
			self.curr_dir.set(path)

	def upOne(self,event=None):

		new_dir = pathlib.Path(self.curr_dir.get()).parent
		self.curr_dir.set(new_dir)




	def __init__(self,root):
		
		self.root = root
		self.root.title("Imageine")
		
		self.listbox = Listbox(self.root)

		self.curr_dir = StringVar(self.root,name='curr_dir',value=filedialog.askdirectory())
		self.curr_dir.trace('w',self.changeDir)


		self.back_button = Button(self.root,text='Up one',command=self.upOne)
		self.back_button.grid(sticky='NSEW',column=0,row=0)

		self.curr_path = Entry(self.root,textvariable=self.curr_dir)
		self.curr_path.grid(sticky='NSEW',column=1,row=0,ipady=10,ipadx=10)


		self.listbox.grid(sticky="NSEW",column=1,row=1,ipady=10,ipadx=10)

		self.listbox.bind('<Double-1>', self.changeDirButton)
		self.listbox.bind('<Return>',self.changeDirButton)

		self.menu = Menu(self.root)

		self.menu.add_command(label="Quit",command=self.root.quit)

		self.root.config(menu = self.menu)


def main():
	root = Tk()
	x = ImageineExplorer(root)
	x.root.mainloop()

if __name__ == "__main__":
	main()







