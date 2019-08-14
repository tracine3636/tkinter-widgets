#!/usr/bin/env python

# -*- coding: utf-8 -*-

#

#  tkinter_shapes.py

#  

#  Copyright 2018 Scott Thomson <github @scotty3785>

#  

#  This program is free software; you can redistribute it and/or modify

#  it under the terms of the GNU General Public License as published by

#  the Free Software Foundation; either version 2 of the License, or

#  (at your option) any later version.

#  

#  This program is distributed in the hope that it will be useful,

#  but WITHOUT ANY WARRANTY; without even the implied warranty of

#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#  GNU General Public License for more details.

#  

#  You should have received a copy of the GNU General Public License

#  along with this program; if not, write to the Free Software

#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,

#  MA 02110-1301, USA.

#  

#  

import math



class Shape:

    def __init__(self,canvas, x,y,radius,sides,angle=0,**args):

        """Create a shape

        canvas - A tkinter canvas instance

        x - x coordinate of the centre of the shape

        y - y coordinate of the centre of the shape

        radius - radius of the shape

        sides - sets how many sides the shape has

        angle (optional, default 0) - rotate the shape by a number of degrees

        The only additional argument currently supported is 'color'''"""

        self._x = x

        self._y = y

        self._radius = radius

        self._sides = sides

        self.canvas = canvas

        self.rotation_angle = angle

        self._color = args.pop('color','blue')

                

        self.draw()

        

    def draw(self):

        """Draw the shape and set default configuration"""

        coords = self.get_poly_coords(self._x,self._y,self._radius,self._sides,self.rotation_angle)

        self.shape = self.canvas.create_polygon(coords,fill=self._color)

        self.canvas.itemconfig(self.shape,activeoutline='darkblue')

        self.canvas.itemconfig(self.shape,activewidth='2')

        

    def redraw(self):

        """Recalculate shape coordinates and redraw"""

        coords = self.get_poly_coords(self._x,self._y,self._radius,self._sides,self.rotation_angle)

        self.canvas.coords(self.shape,coords)

        

    def get_poly_coords(self,x,y,radius,sides,rotate=0):

        """Calculate position of the vertices of the shape"""

        if (sides < 3):

            sides = 3

            raise Exception('Number of sides must be greater than 2')

        ang_dif = 360//sides

        coords = []

        for angle in range(0,360,ang_dif):

            xc = x + (radius * math.sin(math.radians(angle-(ang_dif/2)+rotate)))

            yc = y + (radius * math.cos(math.radians(angle-(ang_dif/2)+rotate)))

            coords.append(int(xc))

            coords.append(int(yc))

        return coords

        

    def rotate(self,rotate_by):

        """Rotate the shape by the 'rotate_by' degrees''"""

        self.rotation_angle += rotate_by

        self.redraw()

        

    def select(self,state):

        """Select/Unselect by marking the shape with a black outline or clear the outline"""

        bd = ('black',2) if state else (self.color,1)

        self.canvas.itemconfig(self.shape,outline=bd[0],width=bd[1])

        

    @property

    def color(self):

        """Get the color of the shape"""

        return self.canvas.itemcget(self.shape,'fill')



    @color.setter

    def color(self,color):

        """Set the color of the shape"""

        self.canvas.itemconfig(self.shape,fill=color)

    

    @property

    def radius(self):

        """Get the radius of the shape"""

        return self._radius

    

    @radius.setter

    def radius(self,radius):

        """Set the radius of the shape"""

        self._radius = radius

        self.redraw()

        

    @property

    def x(self):

        """Get the x coordinate of the shape"""

        return self._x

        

    @x.setter

    def x(self,x):

        """Set the x coordinate of the shape"""

        self._x = x

        self.redraw()

        

    @property

    def y(self):

        """Get the y coordinate of the shape"""

        return self._y

        

    @y.setter

    def y(self,y):

        """Set the y coordinate of the shape"""

        self._y = y

        self.redraw()    

        

    @property

    def sides(self):

        """Get the number of sides of the shape"""

        return self._sides

        

    @sides.setter

    def sides(self,sides):

        """Set the number of sides of the shape"""

        if (sides < 3):

            sides = 3

            raise Exception('Number of sides must be greater than 2')

        self._sides = sides

        self.redraw()



def with_args( func_name, *args):

    """Helper function to make lambda functions easier

    Thanks to guizero"""

    return lambda: func_name(*args)



def rotate_left():

    """Rotate the shape by +10 degrees"""

    shape.rotate(10)

    

def rotate_right():

    """Rotate the shape by -10 degrees"""

    shape.rotate(-10)

    

def move(x,y):

    """Move the shape by x,y pixels"""

    shape.x += x

    shape.y += y

    

def change_color():

    """Change the color to a random color"""

    cols = ['red','blue','green','yellow','purple']

    shape.color = random.choice(cols)

    

def change_sides(chg):

    """Increase the number of sides by 'chg' sides''"""

    shape.sides += chg

    #shape.redraw()

    

def change_size(chg):

    """Change the side of the shape's radius by 'chg' pixels''''"""

    shape.radius += chg

    

def objectSelect(event):

    """Make the clicked on shape the selected shape, set the outline of 

    the new shape and clear the outline of the new shape"""

    global shape

    element_id = canvas.find_withtag(CURRENT)

    for s in shape_list:

        try:

            if s.shape == element_id[0]:

                shape.select(False)

                shape = s

                shape.select(True)

        except IndexError as err:

            pass
