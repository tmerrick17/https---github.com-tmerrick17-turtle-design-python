import turtle
import turtleModules

# * Change color mode for RGB support and adjust default pensize
turtle.colormode(255)

# * Rafael Setup (spelled with a 'f' (in Spanish) in honor my son Rafael (Rafi))
rafi = turtle.Turtle()
rafi.shape("turtle")
rafi.color(210, 43, 43)


# * Leonardo Setup
leo = turtle.Turtle()
leo.shape("turtle")
leo.color(0, 0, 128)

# * Donatello Setup
don = turtle.Turtle()
don.shape("turtle")
don.color(75, 0, 130)

# * Michelangelo's Setup
mike = turtle.Turtle()
mike.shape("turtle")
mike.color(255, 140, 0)

# * Hide turtles until needed
leo.hideturtle()
don.hideturtle()
mike.hideturtle()

# * Default Pensize
rafi.pensize(2)
leo.pensize(2)
don.pensize(2)
mike.pensize(2)

# * Speed
rafi.speed(0)
leo.speed(0)
don.speed(0)
mike.speed(0)

# * Prevent window from running
input('Press any key and then push Return OR just push Return to start...')

# * Draw Rafael's Twin Sais
turtleModules.rafiTwinSais(rafi)

# * Draw Leo's Sword
turtleModules.leoSword(leo)

# * Draw Don's Bow Staff
turtleModules.donBoStaff(don)

# * Draw Mike's Nunchucks
turtleModules.mikeNunchucks(mike)

# * Prevent window from Closing
input('Press any key and then push Return OR just push Return to close...')