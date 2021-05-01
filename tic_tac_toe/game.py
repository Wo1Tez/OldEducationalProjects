import tkinter as tk
from tik_tac_toe_obj import *

def main():
	root = tk.Tk()
	root.geometry("452x452")
	root.resizable(False, False)
	background = tk.Canvas(root, bg='#111112')
	background.place(relwidth=1, relheight=1)

	game = TikTacToe(background)
	
	root.bind("<Button-1>", game.player_move)
	root.mainloop()


if __name__ == "__main__":
	main()