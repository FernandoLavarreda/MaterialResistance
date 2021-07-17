# Fernando Lavarreda
# Test for basic implementation of program

from obj.beam import Beam
from obj.planck import Planck
from obj.material import Material
from results import transform_inertia, centroid, trasnform_planck

steel = Material("steel", 200, 150, 150)
alumunium = Material("Al", 70, 40, 10)

b_al = Beam("test", "W", (30*40**3)/12, 30*40, 40, 430, alumunium)
p_steel = Planck(20, 30, steel)

I = transform_inertia(b_al, p_steel)
C = centroid(b_al, trasnform_planck(b_al, p_steel))

failed = 0
passed = 0
if abs(C-22.3)>0.06:
    failed+=1
    print("Error in centroid: ", C)
else:
    passed+=1
if abs(I-852436)>1:
    failed+=1
    print("Error in inertia: ", I)
else:
    passed+=1

print("Failed: ", failed)
print("Passed: ", passed)
