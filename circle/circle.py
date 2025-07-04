import math

class Circle():
  def  __init__(self,radius):
    if  radius <= 0 :
         raise ValueError("No se permiten ingresar valores negativos")
    self.radius=radius

  def get_radius(self):
    return self.radius

  def set_radius(self,radius):
    if  radius <= 0 :
         raise ValueError("No se permiten ingresar valores negativos")
    self.radius=radius
  
  def get_area(self):
     return math.pi*(self.radius**2)
  
  def get_perimeter(self):
     return math.pi * self.radius *2
 
  def __mul__(self, n):
    if  n <= 0 :
         raise ValueError("No se permiten ingresar valores negativos")
    return Circle(self.radius * n)
  
  def __str__(self):
    return(f"Circulo \n Radio:{self.radius} \n Area: {self.get_area()} \n Perimetro: {self.get_perimeter()}")
