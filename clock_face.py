from datetime import datetime
from dot_boi import dot

c = color(0, 0, 0)

class face:
    bg_color = color(0, 0, 0)
    alarmTime = 0
    last_sec = 0
    timerDoneTime = 0
    
    def draw(self):
        x = width/4
        y = height / 4
        
        fill(self.bg_color)
        rect(x, y, width/2, height/2)
        
        now = datetime.now()
        hour = now.hour

        ampm = "am"
        if hour > 12:
            hour -= 12
            ampm = "pm"

        alarmLine = 'Alarm: %d' % self.alarmTime
        timeLine = '%d:%02d:%02d %s' % (hour, now.minute, now.second, ampm)
        dateLine = "%d/%d/%d" % (now.month, now.day, now.year)
        timerDone = 'Timer Done'
        
        textSize(30)

        text_color = color(255, now.second * 6, now.second * 6)
        fill(text_color)
        textAlign(CENTER, CENTER);

        sec = int(now.second)
        if sec != self.last_sec:
            self.last_sec = sec
            self.alarmTime -= 1
            self.timerDoneTime -= 1
            
        if mousePressed:
            text(timeLine, x*2, y*2 - 20)
            text(dateLine, x*2, y*2 + 20)
        elif self.alarmTime > 0:
            if self.alarmTime < 60:
                text(timeLine, x*2, y*2 - 20)
                text(alarmLine, x*2, y*2 + 20)
                secondCurrent = now.second + 1
            else: 
                alarmMin = int(self.alarmTime / 60)
                alarmSecs = int(self.alarmTime % 60) 
                text(timeLine, x*2, y*2 - 20)
                #where? if the missing parentheses? i dont think it is really missing. If i put self. infront of it it doenst work
                #if i put pareteses arounf random things it doesnt work
                text('%d:%02d' % (alarmMin, alarmSecs), x*2, y*2 + 20) 
                secondCurrent = now.second + 1
       
        else:
            textSize(50)
            text(timeLine, x*2, y*2)
            
        if self.timerDoneTime > 0:
            textSize(50)
            if self.timerDoneTime % 2 == 1:
                fill(color(225, 0, 0))
            else: 
                fill(color(0, 0, 0))

            text(timerDone, width/2, 15)   
               
        if self.alarmTime == 1: 
            self.timerDoneTime = 5
            self.alarmTime = 0
            
        
   
            
