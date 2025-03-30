from tkinter import *
import random
import time

class Ball:
    def_init_(self, canvas, paddle, color) :
    
    self.canvas = Canvas
    self.paddle = paddle
    self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
    random.shuffle(starts)
    self.x = starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_wight = self.canvas.winfo_widht()
    self.hit_bottom = False
    def hit_paddle(self, pos) :
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
        def_init_(self, canvas, color): self.canvas = Canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_widht = self.canvas.winfo_widht()
        self.canvas.blind_all('<Keypress-Left', self.turn_left)
        self.canvas.blind_all('<Keypress-Right', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0
            self.x = 0
        elif pos[2] >= self.canvas_width:
             self.x = 0

    def turn_left(self, evt) :
     self.x = -2
    def  turn_right(self, evt) :
     self.x = 2
tk = Tk()
tk.title("Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
     if ball.hit_bottom == False:
          ball.draw()
          paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

