import tkinter as tk
import tkinter.ttk as ttk
import socket

class GUI(ttk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()


	def create_widgets(self):
		self.label = ttk.Label(self, text="Enter Hostname")
		self.label.pack()

		self.entry = ttk.Entry(self)
		self.entry.pack()

		self.ip_button = ttk.Button(self, text="Get IP", command=lambda : self.get_ip(self.entry.get()))
		self.ip_button.pack(side="bottom")


	def get_ip(self, hostname):
		try:
			ip = socket.gethostbyname(hostname)
			self.change_entry(self.entry.get(), ip)
		except:
			self.change_entry(self.entry.get(), "Invalid Hostname")

	def change_entry(self, original_entry, new_entry):
		self.entry.delete(0, len(original_entry))
		self.entry.insert(0, new_entry)


def main():
	root = tk.Tk()
	root.geometry("300x125")
	root.title("Hostname Resolver")

	gui = GUI(root)
	gui.mainloop()


if __name__ == '__main__':
	main()
