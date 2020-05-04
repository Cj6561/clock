from clock_face import face
from dot_boi import dot


face = face()
alarmTime = ""
letter = ''
def setup():
    global mydot
    size(800, 400)
    mydot = dot(width/2, height/2)

def draw():
    background(225, 225, 225)
    face.draw()
    mydot.draw()
    textSize(20)
    fill(color(0,0,0))
    textAlign(BOTTOM, LEFT);
    text("Alarm Input: " + alarmTime+ letter,4,height - 4)


        
    
    
def keyPressed():
    global alarmTime
    global letter
    print keyCode
    if keyCode == 10:
        if alarmTime != "":
            face.alarmTime = int(alarmTime)
            alarmTime = ""
        
    elif 47 < keyCode < 58: 
        alarmTime += key
        
    if 100 > keyCode > 57:
        letter = '   - whoa, thats not a number'
    elif keyCode == 8:
        alarmTime = ''
    else:
        letter = ''

            
         
    
    
