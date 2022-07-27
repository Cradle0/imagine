from tkinter import *
from tkinter import ttk
import imageineviewer  as view


def main():
	root=Tk()
	view.ImageineViewer(root)
	root.focus_force()
	root.mainloop()

if __name__ == "__main__":
	main()