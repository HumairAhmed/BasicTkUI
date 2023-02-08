from tkinter import *
from tkinter import messagebox

window = Tk()


def executeAction1():
	#Action 1 Code
	messagebox.showinfo('Message', 'Action 1 Completed!')
	pass

def executeAction2():
	#Action 2 Code
	messagebox.showinfo('Message', 'Action 2 Completed!')
	pass

def executeAction3():
	#Action 3 Code
	messagebox.showinfo('Message', 'Action 3 Completed!')
	pass

def executeAction4():
        #Action 4 Code
	messagebox.showinfo('Message', 'Action 4 Completed!')
	pass


def main():
	window.geometry('400x200')
	window.title("Basic Tk UI Interface")

	btn_action1 = Button(window, text="Action 1", command = executeAction1)
	btn_action1.pack()

	btn_action2 = Button(window, text="Action 2", command = executeAction2)
	btn_action2.pack()

	btn_action3 = Button(window, text="Action 3", command = executeAction3)
	btn_action3.pack()

	btn_action4 = Button(window, text="Action 4", command = executeAction4)
	btn_action4.pack()

	window.mainloop()



if __name__ == "__main__":
	main()
