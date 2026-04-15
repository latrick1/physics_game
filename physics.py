import time
from graphics import *


class object_physic():
    def __init__(self,velo_x,velo_y, objcet, friction) -> None:
        self.grav = 0.3
        self.friction = friction
        self.velo_x = velo_x
        self.velo_y = velo_y
        self.objcet = objcet
        
    
    def update(self):
        if self.velo_y >= 25:
            self.velo_y = 25
        else:
            self.velo_y += self.grav
        
        self.velo_x *= self.friction
        self.objcet.move(self.velo_x, self.velo_y)
        
    def set_y(self,amount):
        self.objcet.move(0,-1 * amount)
    
    def bounce(self, amount):
        self.objcet.move(0, -1 * amount)
    
    def get_y(self):
        return self.objcet.getP2().getY()

    
    def get_x(self):
        return self.objcet.getP2().getX()


def win():
    win = GraphWin("physics", 1200, 780)
    rec = Rectangle(Point(0,0), Point(100,100))
    rec.setFill("red")
    rec.draw(win)
    arrow = Line(rec.getCenter(), Point(win.getWidth()/6 , 0))
    arrow.setArrow("last")
    return win, rec, arrow

def phyisic(win:GraphWin, rec:Rectangle, arrow:Line):
    rectan = object_physic(0,0, rec, 0.99)
    arow = object_physic(0,0, arrow, 0.9)
    phyisic_object_list = []
    phyisic_object_list.append(rectan)
    phyisic_object_list.append(arow)
    engin(phyisic_object_list, win)

def engin(phyisic_object_list:list, win:GraphWin):
    rectan  = phyisic_object_list[0]
    arrow = phyisic_object_list[1]
    timer = 0
    while True:
        timer += 1
        mouse = win.checkMouse()
        
        if rectan.get_x() - 99 <= 0:
            rectan.velo_x = -1 * rectan.velo_x
            rectan.update()
        elif rectan.get_x()  >= win.getWidth() + 1:
            rectan.velo_x = -1 * rectan.velo_x
            rectan.update()
        
        if rectan.get_y() >= win.getHeight():
            if rectan.velo_y >= 0:
                # print(rectan.velo_y)
                pass
            if rectan.get_y() <= 779:
                rectan.update()
            else:
                rectan.set_y(rectan.get_y() - win.getHeight())
                if rectan.velo_y >= 2:
                    rectan.velo_y = (rectan.velo_y * -1) + 2
                    if rectan.velo_x > 0.5:
                        rectan.velo_x -= 0.5
                    elif rectan.velo_x == 0:
                        pass
                    elif rectan.velo_x < -0.5:
                        rectan.velo_x += 0.5
                    rectan.update()
                print(rectan.get_y())
            if mouse != None:
                if mouse.getX() <= rectan.get_x():
                    # print(rectan.get_x())
                    flip = -1
                else:
                    flip = 1
                print(mouse.getX()- win.getWidth())
                rectan.velo_x = ((mouse.getX()-rectan.get_x())/25)
                rectan.velo_y = (-1 * (mouse.getY()-rectan.get_y())/50 - 25)
                # print(-1 * mouse.getY()/100)
                rectan.update()
        else:
            if mouse != None:
                if mouse.getX() <= rectan.get_x():
                    # print(rectan.get_x())
                    flip = -1
                else:
                    flip = 1
                print(mouse.getX()- win.getWidth())
                rectan.velo_x = ((mouse.getX()-rectan.get_x())/25)
                rectan.velo_y = (-1 * (mouse.getY()-rectan.get_y())/75 - 20)
                # print(-1 * mouse.getY()/100)
            rectan.update()
        time.sleep(0.01)
        
        if timer == 100000:
            break
    win.close()

if __name__ == "__main__":
    window,rec,arrow = win()
    phyisic(window,rec,arrow)