# Fernando Lavarreda
# Description of beams over which a planck is placed

from .material import Material

class Beam:
    def __init__(self, name:str, type_:str, inertia:int, area:int, height:int, weight:int, material:Material) -> None:
        self.name = name
        self.type = type_
        self.intertia = inertia
        self.area = area
        self.height = height
        self.weight = weight
        self.material = material

    def get_centroid(self) -> int:
        """Defualt centroid assumption to be center of figure"""
        return self.height/2
    
    def get_weight(self)->int:
        return self.weight
    
    def get_height(self)->int:
        return self.height
    
    def get_material(self)->Material:
        return self.material

    def get_name(self)->str:
        return self.name
    
    def get_type(self)->str:
        return self.type
    
    def get_inertia(self)->int:
        return self.intertia
    
    def get_area(self)->int:
        return self.area