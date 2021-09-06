d= 0
s= 0
b= 0
def setup(): 
    size(600, 300)
def draw(): 
    global d
    global s
    global b
    background(234, 234, 24)
    fill(49, 49, 38)
    square(d, 45, 30)
    if d > width:
       d= 0
    else:
       d= map(second(), 0, 59, 0, height)
    fill(170, 53, 14)
    square(s, 100, 60)
    if s > width:
       s= 0
    else:
       s= map(minute(), 0, 59, 0, height)
    fill(12, 245, 223)
    square(b, 200, 90)
    if b > width:
       b= 0
    else:
       b= map(hour(), 0, 59, 0, height)
       
       
    
