import turtle

turtle.bgcolor("black")

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

a = turtle.Turtle()
a.penup()
a.speed(80)
a.pencolor("cyan")
a.goto(-500,260)
a.pendown()
a.width(5)
a.write("THANK YOU FOR USING!!",font=("agency fb",100,"normal"))
a.forward(1000)
a.penup()
a.forward(-1100)
a.right(90)
a.forward(100)
a.pendown()
a.write("CREATED BY:-",font=("arial",40,"normal"))
a.penup()
a.forward(100)
a.write("1.SWAYAM PRAKASH BEHERA ",font=("agency fb",35,"normal"))
a.forward(50)
a.write("2.SHUBHAM NAYAK ",font=("agency fb",35,"normal"))
a.forward(50)
a.write("3.SAHARA DAS",font=("agency fb",35,"normal"))
a.forward(50)
a.write("4.AYUSH BARMAN MANDAL ",font=("agency fb",35,"normal"))
a.penup()
a.forward(200)
a.left(90)
a.forward(300)
a.pendown()
a.write("(PRESS ALT+F4 TO END THE PROGRAM)",font=("Arial",25,"normal"))




turtle.done()
