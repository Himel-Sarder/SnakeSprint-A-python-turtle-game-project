import turtle
import time
import random

# Set the delay for the game
delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()  # Create a screen object
screen.title("Snake Game")  # Set the title of the window
screen.bgcolor("black")  # Set the background color
screen.setup(width=600, height=600)  # Set the dimensions of the window
screen.tracer(0)  # Turn off screen updates

# Snake head
head = turtle.Turtle()  # Create a turtle object for the snake head
head.speed(0)  # Set the animation speed
head.shape("square")  # Set the shape of the turtle
head.color("white")  # Set the color of the turtle
head.penup()  # Lift the pen up (no drawing when moving)
head.goto(0, 0)  # Move the turtle to the specified coordinates
head.direction = "stop"  # Initialize the direction of the snake head

# Snake food
food = turtle.Turtle()  # Create a turtle object for the food
food.speed(0)  # Set the animation speed
food.shape("circle")  # Set the shape of the turtle
food.color("red")  # Set the color of the turtle
food.penup()  # Lift the pen up (no drawing when moving)
food.goto(0, 100)  # Move the turtle to the specified coordinates

segments = []  # Initialize a list to store the snake segments

# Pen
pen = turtle.Turtle()  # Create a turtle object for the pen
pen.speed(0)  # Set the animation speed
pen.shape("square")  # Set the shape of the turtle
pen.color("white")  # Set the color of the turtle
pen.penup()  # Lift the pen up (no drawing when moving)
pen.hideturtle()  # Hide the turtle
pen.goto(0, 260)  # Move the turtle to the specified coordinates
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Write the initial score on the screen

# Functions
def go_up():  # Define a function to move the snake up
    if head.direction != "down":
        head.direction = "up"


def go_down():  # Define a function to move the snake down
    if head.direction != "up":
        head.direction = "down"


def go_left():  # Define a function to move the snake left
    if head.direction != "right":
        head.direction = "left"


def go_right():  # Define a function to move the snake right
    if head.direction != "left":
        head.direction = "right"


def move():  # Define a function to move the snake
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
screen.listen()  # Listen for keyboard input
screen.onkeypress(go_up, "Up")  # Bind the "Up" arrow key to the go_up function
screen.onkeypress(go_down, "Down")  # Bind the "Down" arrow key to the go_down function
screen.onkeypress(go_left, "Left")  # Bind the "Left" arrow key to the go_left function
screen.onkeypress(go_right, "Right")  # Bind the "Right" arrow key to the go_right function

# Main game loop
while True:  # Start the main game loop
    screen.update()  # Update the screen

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Pause the game for 1 second
        head.goto(0, 0)  # Move the snake head to the center of the screen
        head.direction = "stop"  # Stop the snake movement

        for segment in segments:  # Iterate over the segments of the snake
            segment.goto(1000, 1000)  # Move the segment off-screen

        segments.clear()  # Clear the segments list

        score = 0  # Reset the score to 0

        delay = 0.1  # Reset the delay for the game

        pen.clear()  # Clear the pen
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Update the score display

    # Check for a collision with the food
    if head.distance(food) < 20:  # If the snake head is close enough to the food
        x = random.randint(-290, 290)  # Generate a random x-coordinate for the food
        y = random.randint(-290, 290)  # Generate a random y-coordinate for the food
        food.goto(x, y)  # Move the food to the new coordinates

        new_segment = turtle.Turtle()  # Create a new turtle object for the snake segment
        new_segment.speed(0)  # Set the animation speed
        new_segment.shape("square")  # Set the shape of the turtle
        new_segment.color("grey")  # Set the color of the turtle
        new_segment.penup()  # Lift the pen up (no drawing when moving)
        segments.append(new_segment)  # Add the new segment to the segments list

        delay -= 0.001  # Decrease the delay for the game

        score += 1  # Increment the score by 1

        if score > high_score:  # If the score is higher than the high score
            high_score = score  # Update the high score

        pen.clear()  # Clear the pen
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Update the score display

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):  # Iterate over the segments of the snake in reverse order
        x = segments[index - 1].xcor()  # Get the x-coordinate of the previous segment
        y = segments[index - 1].ycor()  # Get the y-coordinate of the previous segment
        segments[index].goto(x, y)  # Move the current segment to the coordinates of the previous segment

    # Move segment 0 to where the head is
    if len(segments) > 0:  # If there are segments in the segments list
        x = head.xcor()  # Get the x-coordinate of the snake head
        y = head.ycor()  # Get the y-coordinate of the snake head
        segments[0].goto(x, y)  # Move the first segment to the coordinates of the snake head

    move()  # Move the snake

    # Check for head collisions with body segments
    for segment in segments:  # Iterate over the segments of the snake
        if segment.distance(head) < 20:  # If the snake head is close enough to a segment
            time.sleep(1)  # Pause the game for 1 second
            head.goto(0, 0)  # Move the snake head to the center of the screen
            head.direction = "stop"  # Stop the snake movement

            for segment in segments:  # Iterate over the segments of the snake
                segment.goto(1000, 1000)  # Move the segment off-screen

            segments.clear()  # Clear the segments list

            score = 0  # Reset the score to 0

            delay = 0.1  # Reset the delay for the game

            pen.clear()  # Clear the pen
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",  # Update the score display
                      font=("Courier", 24, "normal"))

    time.sleep(delay)  # Pause the game for the specified delay

screen.mainloop()  # Start the main event loop
