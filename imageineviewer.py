from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os
from PIL import Image,ImageTk

class ImageineViewer:

	def __init__(self,root):

		self.root = root
		self.root.title("Imageine")
		self.dirname = filedialog.askdirectory()

		self.image_list = []

		for x in os.listdir(self.dirname):
			if os.path.isfile(os.path.join(self.dirname,x)):
				print(os.path.join(self.dirname,x))
				self.image_list.append(os.path.join(self.dirname,x))

		self.i = 0
		self.init_image = ImageTk.PhotoImage(Image.open(self.image_list[self.i]))
		
		self.image_label = Label(self.root,image=self.init_image)
		self.image_label.grid(row=0,column=0,columnspan=3)
		
		self.button_back = Button(root,text="<",command=self.backward)
		self.button_forward = Button(root,text=">",command=self.forward)
		self.button_exit = Button(root,text="exit",command=root.quit)

		self.button_back.grid(row=1,column=0)
		self.button_forward.grid(row=1,column=2)
		self.button_exit.grid(row=1,column=1)

		root.focus_force()
		root.mainloop()
	
	def forward(self):
		if self.i != len(self.image_list)-1:
			self.i += 1
			self.image_label.grid_forget()

			self.init_image = ImageTk.PhotoImage(Image.open(self.image_list[self.i]))

			self.image_label = Label(self.root,image=self.init_image)
			self.image_label.grid(row=0,column=0,columnspan=3)

	def backward(self):
		if self.i != 0:
			self.i += -1
			self.image_label.grid_forget()

			self.init_image = ImageTk.PhotoImage(Image.open(self.image_list[self.i]))

			self.image_label = Label(self.root,image=self.init_image)
			self.image_label.grid(row=0,column=0,columnspan=3)
	

