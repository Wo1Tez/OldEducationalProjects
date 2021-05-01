import tkinter as tk 
import random

class Bot:
	def __init__(self, background, master):
		self.master = master
		self.background = background
		self.made_move = False
		self.own_boxes = list()
		self.all_boxes = self.own_boxes + self.master.x_boxes

		self.o_image = tk.PhotoImage(file='img/O.png')
		self.o_mini_image = tk.PhotoImage(file='img/O_mini.png')

		self.random_move()


	def random_move(self):
		while not self.made_move:
			vertical = random.randrange(1, 4)
			horizontal = random.randrange(1, 4)
			self.move_execution(vertical, horizontal)


	def move(self):
		self.made_move = False
		self.all_boxes = self.own_boxes + self.master.x_boxes

		# COMPLETING OWN LINE
		self.complete_straight_line(self.own_boxes)
		self.complete_diagonal_lines(self.own_boxes, 0)
		self.complete_diagonal_lines(self.own_boxes, 1)

		# BLOCKING PLAYER LINE
		self.complete_straight_line(self.master.x_boxes)
		self.complete_diagonal_lines(self.master.x_boxes, 0)
		self.complete_diagonal_lines(self.master.x_boxes, 1)
		
		self.random_move()


	def move_execution(self, vertical, horizontal):
		try:
			self.all_boxes.index([int(vertical), str(horizontal)])
		except:
			self.background.create_image(self.master.calc_pos(vertical), self.master.calc_pos(horizontal), image=self.o_image)
			self.own_boxes.append([vertical, str(horizontal)])
			self.made_move = True
			self.all_boxes = self.own_boxes + self.master.x_boxes



	def complete_straight_line(self, boxes):
		if not self.made_move:
			lines = self.check_straight_lines(boxes, 0, 2)
			lines += self.check_straight_lines(boxes, 1, 2)
			for line in lines:
				if not self.made_move:
					z = self.search_free_boxes(line[0], line[1])
					if z != []:
						self.move_execution(int(z[0][0]), int(z[0][1]))
		return False


	def check_straight_lines(self, boxes_to_check, option, excepted_value):
		data = list()
		for line in range(3):
			counter = 0		
			for box in boxes_to_check:
				if int(box[option]) == (line+1):
					counter += 1
				if counter == excepted_value:
					try: 
						data.index([line+1, option])
					except:
						data.append([line+1, option])
		return data


	def complete_diagonal_lines(self, boxes_to_check, option):
		if not self.made_move:
			counter = 0
			free_box = [[1, str(1+option*2)], [2, '2'], [3, str(3-option*2)]]
			try:
				boxes_to_check.index([1, str(1+option*2)])
				free_box.remove([1, str(1+option*2)])
			except:
				pass

			try:
				boxes_to_check.index([2, '2'])
				free_box.remove([2, '2'])
			except:
				pass
			
			try:
				boxes_to_check.index([3, str(3-option*2)])
				free_box.remove([3, str(3-option*2)])
			except:
				pass

			if len(free_box) == 1:
				self.move_execution(int(free_box[0][0]), int(free_box[0][1]))


	# option == 0 : checking vertical lines; option == 1: horizontal
	def search_free_boxes(self, line, option):  
		free_boxes = list()

		for number in range(3):
			if option == 1:
				box = [number+1, str(line)]
			elif option == 0:
				box = [line, str(number+1)]
			try:
				self.all_boxes.index(box.copy())
			except:
				free_boxes.append(box.copy())
			box.clear()
		return free_boxes

