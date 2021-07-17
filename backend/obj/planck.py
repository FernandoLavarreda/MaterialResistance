# Fernando Lavarreda
# Planck placed over beam to create structure

from .material import Material

class Planck:
    def __init__(self, height:int, width:int, material:Material) -> None:
        self.height = height
        self.width = width
        self.material = material
    
    def get_inertia(self)->float:
        """Default assumption of a rectangle bh**3/12"""
        return (self.width*self.height**3)/12
    
    def get_centroid(self)->float:
        """Assumption of a rectangle"""
        return self.height/2

    def get_area(self)->float:
        """Assumption of a rectangle as base case"""
        return self.height*self.width

    def get_height(self)->int:
        return self.height
    
    def get_width(self)->int:
        return self.width

    def get_material(self)->Material:
        return self.material