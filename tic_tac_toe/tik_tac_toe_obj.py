import tkinter as tk
import random
from bot_obj import *

class TikTacToe:

	def __init__(self, background):
		self.WINDOW_DIMENSION = 452

		self.background = background
		self.winner = False
		self.x_boxes = list()
		self.images()
		self.bot = Bot(self.background, self)
		self.end_button = tk.Button(self.background, bg='#111112', activebackground='#161618', 
			fg='#696969', activeforeground='#696969', text="Play again", command=self.game_reset)

		self.create_lines()

	# CREATING STARTING LINES ON BOARD
	def create_lines(self):
		for n in range(2):
			cord = (n+1)*151
			self.background.create_line(0, cord, self.WINDOW_DIMENSION, cord, fill='#161618')
			self.background.create_line(cord, 0, cord, self.WINDOW_DIMENSION, fill='#161618')	


	def player_move(self, event):
		if not self.winner:
			vertical = int(event.x / 151) + 1
			horizontal = int(event.y / 151) + 1
			box_index = list()
			box_index.append(vertical)
			box_index.append(str(horizontal))
			
			try:
				(self.bot.own_boxes+self.x_boxes).index(box_index)
			except:
				self.background.create_image(self.calc_pos(vertical), self.calc_pos(horizontal), image=self.x_image)
				self.x_boxes.append(box_index)
				self.winner = self.check_winner(self.x_boxes)
				if not self.winner:
					self.bot.move()
					self.winner = self.check_winner(self.bot.own_boxes)

		if len(self.bot.all_boxes) == 9:
			self.finish_window(None)


	def calc_pos(self, direction):
		return direction*76+75*(direction-1)


	def check_winner(self, boxes_to_check):
		straight = self.check_straight_lines
		diagonal = self.check_diagonal_lines
		if straight(boxes_to_check, 0) or straight(boxes_to_check, 1) or diagonal(boxes_to_check, 0) or diagonal(boxes_to_check, 1):
			return True


	def check_straight_lines(self, boxes_to_check, option):
		for value_to_check in range(3):
			counter = 0		
			for box in boxes_to_check:
				if int(box[option]) == (value_to_check+1):
					counter += 1
			if counter == 3:
				self.winner_straight_line(option, value_to_check+1)
				self.finish_window(boxes_to_check)
				return True


	def check_diagonal_lines(self, boxes_to_check, option):
		counter = 0
		for box in boxes_to_check:
			if box == [1, str(1+option*2)] or box == [2, '2'] or box == [3, str(3-option*2)]:
				counter += 1
			if counter == 3:
				self.winner_diagonal_line(option)
				self.finish_window(boxes_to_check)
				return True


	def winner_straight_line(self, number_of_index, value):
		if number_of_index == 1:
			self.background.create_line(25, self.calc_pos(value), self.WINDOW_DIMENSION-25, self.calc_pos(value), fill='#D6B672', width=2)
			
		elif number_of_index == 0:
			self.background.create_line(self.calc_pos(value), 25, self.calc_pos(value), self.WINDOW_DIMENSION-25, fill='#D6B672', width=2)


	def winner_diagonal_line(self, option):
		option_scaler = option*402
		self.background.create_line(25, 25+option_scaler, 427, 427-option_scaler, fill='#D6B672', width=2)


	def images(self):
		self.x_image = tk.PhotoImage(file='img/X.png')
		self.x_mini_image = tk.PhotoImage(file='img/X_mini.png')
		self.end_image = tk.PhotoImage(file='img/end.png')


	def finish_window(self, winner):
		self.background.create_image(227, 225, image=self.end_image)
		if winner == self.x_boxes:
			self.background.create_image(189, 226, image=self.x_mini_image)
		elif winner == self.bot.own_boxes:
			self.background.create_image(189, 226, image=self.bot.o_mini_image)
		self.background.create_window(260, 240, width=70, height=30, window=self.end_button)


	def game_reset(self):
		self.background.delete("all")
		self.x_boxes.clear()
		self.bot = Bot(self.background, self)
		self.winner = False
		self.create_lines()
