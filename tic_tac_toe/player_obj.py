import tkinter as tk

class Player:
	def __init__(self, background, master):
		self.background = background
		self.master = master
		self.own_boxes = list()
		self.made_move = False

		self.x_image = tk.PhotoImage(file='img/X.png')
		self.x_mini_image = tk.PhotoImage(file='img/X_mini.png')


	def move(self, event):
		vertical = int(event.x / 151) + 1
		horizontal = int(event.y / 151) + 1
		box_index = [vertical, str(horizontal)]
		self.made_move = False
			
		try:
			self.master.occupated_boxes.index(box_index)
		except:
			self.master.background.create_image(self.master.calc_pos(vertical), self.master.calc_pos(horizontal), image=self.x_image)
			self.own_boxes.append(box_index)
			self.made_move = True
