import turtle as t

def drawSquare(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.seth(0)
    t.forward(width)
    t.seth(90)
    t.forward(height)
    t.seth(180)
    t.forward(width)
    t.seth(270)
    t.forward(height)
    t.end_fill()
    
def drawCurveUp(size, direction = 'right'):
    radius = size / ((3 * 2 ** (1 / 2) + 2) / 8)
    if direction.lower() in ['l', 'left']:
        t.seth(90)     
        t.circle(radius, 45)    
        t.circle(radius/4, 45)
    elif direction.lower() in ['r', 'right']:
        t.seth(90)     
        t.circle(-radius, 45)    
        t.circle(-radius/4, 45)
        
def drawCurveDown(size, direction = 'right'):
    radius = size / ((3 * 2 ** (1 / 2) + 2) / 8)
    if direction.lower() in ['l', 'left']:
        t.seth(0) 
        t.circle(-radius/4, 45)
        t.circle(-radius, 45)    
    elif direction.lower() in ['r', 'right']:
        t.seth(180)     
        t.circle(radius/4, 45)
        t.circle(radius, 45)    
         
def drawSky(startColor, endColor):
    t.seth(0)
    for i in range(643):
        red = int((endColor[0] - startColor[0]) / 643 * i + startColor[0])
        green = int((endColor[1] - startColor[1]) / 643 * i + startColor[1])
        blue = int(((endColor[2] - startColor[2]) / 643) * i + startColor[2])
        print(red, green, blue)
        t.color(red, green, blue)
        
        tp(-480, i -282)
        t.pendown()
        t.forward(960)
        t.penup()
        

def tp(xPos, yPos):
    t.setpos(xPos, yPos)
    
#Setup
t.colormode(255)
t.penup()
t.speed(0)
colors = {'ground': (211, 227, 195), 'lightBase': (126, 85, 26), 'mediumBase': (102, 64, 18), 'darkBase': (78, 42, 10), 'shadow': (23, 23, 22), 'glass': (138, 170, 212)}
    
#Debug
t.pendown()
tp(-480, -360)
drawSquare(960, 720, 'white')
t.penup()

#Ground
drawSquare(960, 77, colors['ground'])

#Sky //그리는데 오래 걸리므로 실행시 적절히 주석처리 할 것
#drawSky((65, 125, 234), (155, 247, 215))

#집게리아 그리기

#왼쪽곡선 
tp(100, -167)
t.color(colors['darkBase'])
t.begin_fill()
drawCurveUp(177, 'left')
t.seth(270)
t.forward(35)
drawCurveDown(142, 'left')
t.seth(0)
t.forward(12)
t.end_fill()

#지붕
tp(-8, -167)
drawSquare(330, 142, colors['mediumBase'])
tp(0, -167)
t.seth(180)
t.begin_fill()
t.forward(100)
drawCurveUp(156, 'right')
t.end_fill()

tp(-110, -167)
t.color(colors['darkBase'])
t.begin_fill()
drawCurveUp(177, 'right')
t.seth(270)
t.forward(35)
drawCurveDown(142, 'right')
t.seth(180)
t.forward(12)
t.end_fill()

tp(-145, -167)
t.color(colors['lightBase'])
t.begin_fill()
drawCurveUp(177, 'right')
t.seth(0)
t.forward(35)
drawCurveDown(177, 'right')
t.seth(180)
t.forward(35)
t.end_fill()

tp(-145, -247)
drawSquare(35, 80, colors['lightBase'])
tp(-110, -247)
drawSquare(22, 80, colors['darkBase'])

#오른쪽곡선
tp(420, -167)
t.color(colors['darkBase'])
t.begin_fill()
drawCurveUp(177, 'left')
drawCurveDown(177, 'right')
t.seth(0)
t.forward(22)
drawCurveUp(142, 'right')
drawCurveDown(142, 'left')
t.end_fill()

t.color(colors['darkBase'])
t.begin_fill()
drawCurveUp(142,'left')
drawCurveDown(142, 'left')
t.end_fill()

t.color(colors['mediumBase'])
t.begin_fill()
drawCurveUp(142, 'left')
drawCurveDown(142, 'right')
t.end_fill()

tp(172, -167)
t.color(colors['lightBase'])
t.begin_fill()
drawCurveUp(177, 'right')
t.seth(0)
t.forward(35)
drawCurveDown(177, 'right')
t.end_fill()

tp(390, -167)
t.color(colors['shadow'])
t.begin_fill()
drawCurveUp(142, 'left')
t.seth(0)
t.forward(10)
drawCurveDown(142, 'left')
t.end_fill()

tp(172, -247)
drawSquare(35, 80, colors['lightBase'])
tp(207, -247)
drawSquare(22, 80, colors['darkBase'])

tp(390, -247)
drawSquare(10, 80, colors['shadow'])
tp(400, -247)
drawSquare(20, 80, colors['darkBase'])

#왼쪽기반
tp(-165, -283)
drawSquare(130, 36, colors['mediumBase'])
tp(-35, -283)
drawSquare(42, 36, colors['darkBase'])

#왼쪽창문
tp(-88, -247)
drawSquare(90, 80, colors['glass'])

#출입문
tp(2, -283)
drawSquare(81, 116, colors['glass'])

#오른쪽기반
tp(82, -283)
drawSquare(130, 36, colors['mediumBase'])
tp(212, -283)
drawSquare(222, 36, colors['darkBase'])

#오른쪽창문
tp(83, -247)
drawSquare(90, 80, colors['glass'])

#오른쪽측면창문
tp(229, -247)
drawSquare(162, 80, colors['glass'])
