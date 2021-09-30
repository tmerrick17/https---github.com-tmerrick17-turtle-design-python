import math

# * UNIVERSAL FUNCTIONS
# * goto position Function
def goto(turtleName, x, y, degLeft):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.left(degLeft)
    turtleName.pendown()

# * Repetitive Handle Segment
def drawHandleSgmnt(turtleName):
    turtleName.right(90)
    turtleName.forward(15)
    turtleName.right(90)

def drawHandleOutline(turtleName, side1, width, side2):
    turtleName.forward(side1)
    drawHandleSgmnt(turtleName)
    turtleName.forward(width)
    drawHandleSgmnt(turtleName)
    turtleName.forward(side2)

# * Grip Function
def drawGripSgmnt(turtleName):
    turtleName.right(120)
    turtleName.forward(math.hypot(15, 10))
    turtleName.right(60)

# * Handle Function 
def drawHandle(turtleName):
    # * Starting with the grip of the handle
    for i in range(4):
        drawGripSgmnt(turtleName)
        turtleName.forward(10)
        drawGripSgmnt(turtleName)
        turtleName.forward(20)
    # * Handle Outline Part
    drawHandleOutline(turtleName, 10, 80, 30)

# * 1/2 of Left Side of Blade Length
def leftBladeLength(turtleName, bladeLength):
    turtleName.forward(bladeLength)
    turtleName.right(45)
    turtleName.forward(math.hypot(5,5))

# * 1/2 of Right Side of Blade Length
def rightBladeLength(turtleName, bladeLength):
    turtleName.forward(bladeLength)
    turtleName.left(45)
    turtleName.forward(math.hypot(5,5))

# * All Functions involving the Blades of the Twin Sai
# * Left of Twin Sai Blade
def drawLeftBlade(turtleName):
    # * Secondary Blade
    turtleName.forward(30)
    turtleName.right(90)
    leftBladeLength(turtleName, 40)
    turtleName.right(90)
    turtleName.forward(math.hypot(5,5))
    turtleName.right(45)
    turtleName.forward(30)
    turtleName.left(90)
    turtleName.forward(22)
    turtleName.left(90)
    # * Primary Blade (Left Half)
    leftBladeLength(turtleName, 120)

# * Right of Twin Sai Blade
def drawRightBlade(turtleName):
    # * Secondary Blade
    turtleName.forward(30)
    turtleName.left(90)
    rightBladeLength(turtleName, 40)
    turtleName.left(90)
    turtleName.forward(math.hypot(5,5))
    turtleName.left(45)
    turtleName.forward(30)
    turtleName.right(90)
    turtleName.forward(22)
    turtleName.right(90)
    # * Primary Blade (Left Half)
    rightBladeLength(turtleName, 120)

# * All Functions involving the Sword
# * Sword Guard
# ! Any way to have a function and then reverse the order
def swordGuard(turtleName):
    turtleName.forward(20)
    turtleName.right(90)
    turtleName.forward(10)
    turtleName.right(90)
    turtleName.forward(53)
    turtleName.right(90)
    turtleName.forward(10)
    turtleName.right(90)
    turtleName.forward(20)

# * All Functions involving the Bo Staff
# * Bo Staff
def drawBoStaff(turtleName):
    # * Starting with the grip of the Bo Staff
    for i in range(3):
        for i in range(4):
            drawGripSgmnt(turtleName)
            turtleName.forward(10)
            drawGripSgmnt(turtleName)
            turtleName.forward(20)
    # * Bo Staff Outline Part
    drawHandleOutline(turtleName, 80, 320, 120)

# * All Functions involving the Nunchucks
# * Chain Link Side
def chainLinkSide(turtleName):
    turtleName.pensize(4)
    turtleName.forward(20)
    turtleName.pensize(2)

def chainLinkHalf(turtleName, length, width):
    turtleName.pensize(4)
    for i in range(2):
        turtleName.forward(length)
        turtleName.right(90)
        turtleName.forward(width)
        turtleName.right(90)

# * RAFAEL'S TWIN SAIS FUNCTION
def rafiTwinSais(rafi):
    # * Moving Rafi to starting position for Right Twin Sai
    goto(rafi, 70, 15, 0)
    # * Draw Twin Sai Handle
    drawHandle(rafi)

    # * Moving Rafi to draw the left side of the sai
    goto(rafi, 120, 15, 90)
    # * Draw left side of Sai
    drawLeftBlade(rafi)
    # * Moving Rafi to draw the right side of the sai
    goto(rafi, 120, 0, 315)
    # * Draw right side of Sai
    drawRightBlade(rafi)

    # * Moving Rafi to starting position for Left Twin Sai
    goto(rafi, -70, -15, 135)
    # * Draw Left Twin Sai Handle
    drawHandle(rafi)

    # * Moving Rafi to draw the left side of the sai
    goto(rafi, -120, -15, 90)
    # * Draw left side of Sai
    drawLeftBlade(rafi)
    # * Moving Rafi to draw the right side of the sai
    goto(rafi, -120, 0, 315)
    # * Draw right side of Sai
    drawRightBlade(rafi)

    # * Moving Rafi to Final Spot
    goto(rafi, -15, 15, 270)
# * END OF RAFI'S TWIN SAI's

# * LEO'S SWORD FUNCTION
def leoSword(leo):
    # * Moving Leo to starting position for Sword
    goto(leo, -8, 70, 90)
    leo.showturtle()

    # * Draw Sword Handle
    drawHandle(leo)

    # * Moving Leo to draw the left side of the sai
    goto(leo, -8, 120, 90)

    # * Draw sword guard
    swordGuard(leo)

    # * Moving Leo to starting position for the left side of the Sword Blade
    goto(leo, -12, 130, 269)

    # * Draw Sword Blade
    leftBladeLength(leo, 220)
    goto(leo, 11, 130, 48)
    rightBladeLength(leo, 220)

    # * Moving Leo to Final Spot
    goto(leo, 15, 15, 270)
# * END OF LEO'S SWORD

# * DON'S BOW STAFF FUNCTION
def donBoStaff(don):
    # * Moving Don to starting position for bo staff
    goto(don, -7, -230, 90)
    don.showturtle()
    # * Draw Bo Staff
    drawBoStaff(don)
    # * Moving Don to Final Spot
    goto(don, 15, -15, 225)
# * END OF DONATELLO'S BO STAFF

# * MIKE'S NUNCHUCKS FUNCTION
def mikeNunchucks(mike):
    # * Moving Mike to starting position for Nunchucks in Positive Coordinates
    goto(mike, 100, 300, 0)
    mike.showturtle()
    # * Draw nunchuck handle
    drawHandle(mike)

    # * Move Mike to starting position for chain
    goto(mike, 150, 293, 0)
    # * Draw Chains
    chainLinkSide(mike)
    goto(mike, 167, 298, 0)
    chainLinkHalf(mike, 20, 10)
    goto(mike, 187, 293, 0)
    chainLinkSide(mike)
    goto(mike, 204, 298, 0)
    chainLinkHalf(mike, 20, 10)
    mike.right(90)
    goto(mike, 220, 290, 0)
    chainLinkSide(mike)
    goto(mike, 225, 274, 0)
    chainLinkHalf(mike, 20, 10)
    goto(mike, 220, 257, 0)
    chainLinkSide(mike)

    # * Move Mike to starting position for handle
    goto(mike, 228, 205, 0)
    # * Draw nunchuck handle
    drawHandle(mike)

    # * Moving Mike to starting position for Nunchucks in Negative Coordinates
    goto(mike, -100, -300, 270)

    # * Draw nunchuck handle
    drawHandle(mike)

    # * Move Mike to starting position for chain
    goto(mike, -150, -293, 0)
    # * Draw Chains
    chainLinkSide(mike)
    goto(mike, -167, -298, 0)
    chainLinkHalf(mike, 20, 10)
    goto(mike, -187, -293, 0)
    chainLinkSide(mike)
    goto(mike, -204, -298, 0)
    chainLinkHalf(mike, 20, 10)
    mike.right(90)
    goto(mike, -220, -290, 0)
    chainLinkSide(mike)
    goto(mike, -225, -274, 0)
    chainLinkHalf(mike, 20, 10)
    goto(mike, -220, -257, 0)
    chainLinkSide(mike)

    # * Move Mike to starting position for handle
    goto(mike, -228, -205, 0)
    # * Draw nunchuck handle
    drawHandle(mike)

    # * Moving Mike to Final Spot
    goto(mike, -15, -15, 135)
# * END OF MIKE'S NUNCHUCKS