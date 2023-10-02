class Rectangle :
    Width = 0
    Height = 0 

    def __init__(self,width ,height):
        self.Width = width
        self.Height = height 

    def set_width (self,w):
        self.Width = w

    def set_height(self , h) :
        self.Height = h

    def get_area (self) :
        return(self.Height*self.Width)
    
    def get_perimeter(self) :
        return (2*(self.Height + self.Width))
    
    def get_diagonal(self): 
        return((self.Width**2 + self.Height**2)**.5)
    
    def get_picture(self) : 
        if (self.Width >50 or self.Height>50) : 
            return ("Too big for picture.")
        size = self.Height
        ans = ""
        while size >0: 
            ans += "*"*self.Width
            ans = ans + "\n"
            size -= 1
        return ans 
    
    def get_amount_inside(self,shape):
        return(self.get_area()//shape.get_area())
    
    
class Square(Rectangle) :
     

    def __init__(self, side):
        self.Width= side 
        self.Height= side 
    def set_side (self,side) :
        self.Width= side
        self.Height= side
        
    def set_width (self,w):
        self.side = w

    def set_height(self , h) :
        self.side = h
        


