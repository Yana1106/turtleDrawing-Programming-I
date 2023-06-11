import turtle as t

def drawSquare(width, height):
    t.seth(0)
    t.forward(width)
    t.seth(90)
    t.forward(height)
    t.seth(180)
    t.forward(width)
    t.seth(270)
    t.forward(height)
    
def drawCurve(size, direction = 'right'):
    radius = size / ((3 * 2 ** (1 / 2) + 2) / 8)
    if direction.lower() in ['l', 'left']:
        t.seth(90)     
        t.circle(radius, 45)    
        t.circle(radius/4, 45)
    elif direction.lower() in ['r', 'right']:
        t.seth(90)     
        t.circle(-radius, 45)    
        t.circle(-radius/4, 45)
        
#drawSky함수 만드는 중이므로 건들지 말 
def drawSky(startColor, endColor): 
    t.colormode(255)
    for i in range(200):
        tp(0, i)
        # 16진수로 표현한 색상 값
        hex_color = str((endColor - startColor) // 200 * i + startColor)
        print(hex_color)

        # 16진수를 RGB 값으로 변환
        red = int(hex_color[2:4], 16)
        green = int(hex_color[4:6], 16)
        blue = int(hex_color[6:8], 16)
        t.color(red, green, blue)
        t.forward(100)

def tp(xPos, yPos):
    t.penup()
    t.setpos(xPos, yPos)
    t.pendown()
    
drawSky(0x417DEA, 0x9BF7D7)


