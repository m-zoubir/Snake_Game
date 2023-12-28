import tkinter as tk
import random

APP_HEIGHT = 700
APP_WIDTH = 700
SPEED=150
ITEM_SIZE = 25
BODY_PARTS = 3
BACKGROUND_COLOR = "#000000"
FOOD_COLOR = "#FFFF00"
SNAKE_COLOR= "#0000FF"

class  Snake :
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates =[]
        self.parts =[]

        for i in range(0 , BODY_PARTS):
            self.coordinates.append([0,0])

        for x , y in self.coordinates :
            part = game.create_rectangle(x,y,x+ITEM_SIZE ,y+ITEM_SIZE , fill=SNAKE_COLOR , tag= "snake")
            self.parts.append(part)


class Food :
    def __init__(self):
        x = random.randint(0, int(APP_WIDTH/ITEM_SIZE - 1)) * ITEM_SIZE
        y = random.randint(0, int(APP_HEIGHT/ITEM_SIZE - 1)) * ITEM_SIZE

        self.coordinates = [x,y]

        game.create_oval(x,y , x+ITEM_SIZE , y+ITEM_SIZE , fill=FOOD_COLOR , tag="food")

def next(snake , food):
    x,y = snake.coordinates[0]

    if(direction == "up" ):
        y-=ITEM_SIZE
    elif(direction == "down" ):
        y+=ITEM_SIZE
    elif(direction == "left" ):
        x-=ITEM_SIZE
    elif(direction == "right" ):
        x+=ITEM_SIZE

    snake.coordinates.insert(0,[x,y])
    square= game.create_rectangle(x,y , x+ITEM_SIZE , y+ITEM_SIZE , fill=SNAKE_COLOR , tag="snake")
    snake.parts.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global  score
        score+=1
        score_label.config( text="Score : {}".format(score))
        game.delete("food")
        food = Food()
    else :
        game.delete(snake.parts[-1])
        del snake.parts[-1]
        del snake.coordinates[-1]

    if not check_collision(snake):
        game_over()

    app.after(SPEED - 2*score ,next , snake , food)
def change_direction(newDirection):
    global direction

    if newDirection == "left" and direction != "right":
        direction = newDirection
    if newDirection == "right" and direction != "left":
        direction = newDirection
    if newDirection == "up" and direction != "down":
        direction = newDirection
    if newDirection == "down" and direction != "up":
        direction = newDirection


def check_collision(snake):
    x,y = snake.coordinates[0]

    if x >= APP_WIDTH or y >= APP_HEIGHT or y < 0 or x < 0:
        return False

    for body_parts in snake.coordinates[1:] :
        if x == body_parts[0] and y == body_parts[1] :
            return False
    return True

def game_over():
    game.delete(tk.ALL)
    game.create_text( APP_WIDTH/2 , APP_HEIGHT/2-70 , text="GAME OVER" , font= ('Helvetica 50 bold'), fill=FOOD_COLOR , tag="gameOver")
    game.create_text( APP_WIDTH/2 , APP_HEIGHT/2 , text="Your score : {}".format(score)  , font= ('Helvetica 20 normal'), fill="white" , tag="lastScore")
    return


app = tk.Tk()
app.title("Snake Game")
app.resizable(False,    False)
score = 0
direction = "down"
score_label = tk.Label(app , text="Score : {}".format(score)   , font=('Helvetica 15 bold'))
score_label.pack()
game = tk.Canvas(app , width=APP_WIDTH , height=APP_HEIGHT , bg=BACKGROUND_COLOR  )
game.pack()

app.bind('<Left>' , lambda  events : change_direction("left"))
app.bind('<Right>', lambda  events : change_direction("right"))
app.bind('<Up>' , lambda  events : change_direction("up"))
app.bind('<Down>' , lambda  events : change_direction("down"))
food = Food()
snake=Snake()
next(snake , food)
app.mainloop()