# Fernando Lavarreda
# Create a material that contains young modulus, name, compression and tension stress


class Material:
    def __init__(self, name:str, young_modulus:int, stress_compression:int, stress_tension:int) -> None:
        self.name = name
        self.y_modulus = young_modulus
        self.s_comp = stress_compression
        self.s_ten = stress_tension
    
    def get_y_modulus(self)->int:
        return self.y_modulus
    
    def get_name(self)->int:
        return self.name
    
    def get_s_comp(self)->int:
        return self.s_comp
    
    def get_s_ten(self)->int:
        return self.s_ten

