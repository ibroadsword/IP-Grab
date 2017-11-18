import socket
import tkinter as tk

class GUI(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	
	def create_widgets(self):
		self.label = tk.Label(self, text="Enter Hostname")
		self.label.pack()

		self.entry = tk.Entry(self, bd=4)
		self.entry.pack()

		self.ip_button = tk.Button(self, text="Get IP", command=lambda : self.get_ip(self.entry.get()))
		self.ip_button.pack(side="bottom")


	def get_ip(self, hostname):
		try:
			ip = socket.gethostbyname(hostname)
			self.entry.delete(0, len(self.entry.get()))
			self.entry.insert(0, ip)
		except ValueError:
			self.entry.delete(0, len(self.entry.get()))
			self.entry.insert(0, "Invalid Hostname")
		except:
			self.entry.delete(0, len(self.entry.get()))
			self.entry.insert(0, "Invalid Hostname")


def main():
	root = tk.Tk()
	gui = GUI(root)
	gui.mainloop()



if __name__ == '__main__':
	main()
