# Fernando Lavarreda
# Test for basic implementation of program

from obj.beam import Beam
from obj.planck import Planck
from obj.material import Material
from results import transform_inertia, centroid, trasnform_planck, stress_beam_planck


steel = Material("steel", 200, 150, 150)
alumunium = Material("Al", 70, 40, 10)

b_al = Beam("test", "W", (30*40**3)/12, 30*40, 40, 430, alumunium)
p_steel = Planck(20, 30, steel)

I = transform_inertia(b_al, p_steel)
C = centroid(b_al, trasnform_planck(b_al, p_steel))
beam_vals, planck_vals = stress_beam_planck(b_al, p_steel, 1500000)
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
if abs(beam_vals[0][0]-66)>1:
    failed+=1
    print("Error in beam stress: ", beam_vals[0][0])
else:
    passed+=1
if abs(planck_vals[0][1]+111.97)>1:
    failed+=1
    print("Error in planck stress: ", planck_vals[0][1])
else:
    passed+=1

print("Failed: ", failed)
print("Passed: ", passed)
