class Orange:
    def __init__(self, size, taste ):
        self.size = size 
        self.taste = taste 
    def __str__(self):
      return self.size + '-' + self.taste 
    def grow(self):      
         if (self.size == 'small'):
             self.size = 'medium'
             #self.size = 'large'
         elif (self.size == 'medium'):
              self.size = 'large'
    def corrupt(self):
        if (self.taste == 'good'):
            self.taste = 'bad'
x1 = Orange("small",  "good") 
x2 = Orange("small",  "bad") 
x3 = Orange("large",  "good") 
x4 = Orange("large",  "bad") 
x5 = Orange("medium",  "good") 
x6 = Orange("medium",  "bad") 
x1.grow()
x1.corrupt()
x2.grow()
x2.corrupt() 
x3.grow()
x3.corrupt() 
x4.grow()
x4.corrupt() 
x5.grow()
x5.corrupt() 
x6.grow()
x6.corrupt() 
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)