# Fernando Lavarreda
# Program to determine stress and momentum for a beam-planck system

from gui import window
from backend.dbm import manage
from backend.obj.beam import Beam
from backend.obj.planck import Planck
from backend.obj.material import Material
from backend.results import stress_beams_planck, momentum_beams_planck


ACTIONS = {
    'load_profiles':manage.call_beam,
    'load_material':manage.call_material,
    'create_material':Material,
    'create_planck':Planck,
    'create_beam':Beam,
    'main':stress_beams_planck,
    'secondary':momentum_beams_planck,
}

if __name__ == "__main__":
    app = window.Main(ACTIONS, "gui/media/metal.ico", ("lol", "ood"), "info/data.db")
    app.mainloop()