from datetime import datetime

class dot:
    dt_color = color(225, 0, 00)
    width = 800 / 4
    height = 400 / 4
    X = width
    Y = height
    originX = 0
    originY = 0
    last_sec = 0

    
    def __init__(self, width, height):
        self.originX = 202
        self.originY = 102
        self.width = width
        self.height = height
        
    def movment(self):
        now = datetime.now()
        sec = int(now.second)
        
        if sec == self.last_sec:
            return
        else:
            self.last_sec = sec
        
        sec = now.second
        if sec == 0:
            self.X = self.originX + 4
            self.Y = self.originY
        elif 0 < sec <= 15:
            self.X = self.originX + (self.width / 15 * sec) - 16
            self.Y = self.originY
        elif 15 < sec < 30:
            self.X = self.originX + self.width - 16
            self.Y = self.originY + (self.height / 15 * (sec - 15))
        elif 29 < sec < 45:
            self.X = self.originX + ((self.width / 15 * (45 - sec))) -16
            self.Y = self.originY + self.height - 16
        
        else:
            self.X = self.originX + 4
            self.Y = self.originY + (self.height / 15 * (59 - sec))
        


    def draw(self):
        fill(self.dt_color)
        square(self.X, self.Y, 10)
        self.movment()
        #print str(self.X) + " "+str(self.Y)
        
            
        
    
   
        
        
        
        
