# Fernando Lavarreda
# Obtain values for a given beam & planck combination

from .obj.beam import Beam
from .obj.planck import Planck
from .plot import plot_many

def n_factor(beam_:Beam, planck_:Planck)->float:
    """Relation factor to transform upper planck to same material as beam"""
    return planck_.get_material().get_y_modulus() / beam_.get_material().get_y_modulus()


def trasnform_planck(beam_:Beam, planck_:Planck)->Planck:
    n = n_factor(beam_, planck_)
    tplanck = Planck(planck_.get_height(), planck_.get_width()*n, beam_.get_material())
    return tplanck


def centroid(beam_:Beam, planck_:Planck)->float:
    centroid_ = (planck_.get_centroid()*planck_.get_area()+beam_.get_area()*(beam_.get_centroid()+planck_.get_height()))\
                / (planck_.get_area()+beam_.get_area())
    return centroid_


def transform_inertia(beam_:Beam, planck_:Planck)->float:
    """Inertia for the given combination of data"""
    nplanck = trasnform_planck(beam_, planck_)
    c = centroid(beam_, nplanck)
    inertia = nplanck.get_inertia()+beam_.get_inertia()+nplanck.get_area()*(c-nplanck.get_centroid())**2\
                + beam_.get_area()*((c-nplanck.get_height()-beam_.get_centroid())**2)
    return inertia


def stress(momentum_:float, inertia:float, height:float, n_factor_=1)->float:
    return -momentum_*height*n_factor_/inertia


def momentum(stress_, inertia, height, n_factor=1)->float:
    return -stress_*inertia/(height*n_factor)


def stress_beam_planck(beam_:Beam, planck_:Planck, momentum_:float)->list:
    n_f = n_factor(beam_, planck_)
    zero = centroid(beam_, trasnform_planck(beam_, planck_))
    inertia = transform_inertia(beam_, planck_)
    bottom_t = (stress(momentum_, inertia, zero-planck_.get_height()-beam_.get_height()), zero-planck_.get_height()-beam_.get_height())
    upper_stress_beam = (stress(momentum_, inertia, zero-planck_.get_height()), zero-planck_.get_height())
    bottom_stress_planck = (stress(momentum_, inertia, zero-planck_.get_height(), n_f), zero-planck_.get_height())
    upper_c = (stress(momentum_, inertia, zero, n_f), zero)
    return [(bottom_t[0], upper_stress_beam[0]), (bottom_t[1], upper_stress_beam[1])]\
           ,[(bottom_stress_planck[0], upper_c[0]), (bottom_stress_planck[1], upper_c[1])]


def stress_beams_planck(beams_:list, planck_:Planck, momentum_:float):
    all_beams = []
    all_plancks = []
    labels = []
    for beam_ in beams_:
        beam_points, planck_points = stress_beam_planck(beam_, planck_, momentum_)
        all_beams.append(beam_points)
        all_plancks.append(planck_points)
        labels.append(beam_.get_name())
    plot_many(all_beams, all_plancks, labels, \
        [-beams_[0].get_material().get_s_comp(), beams_[0].get_material().get_s_ten(), -planck_.get_material().get_s_comp(), planck_.get_material().get_s_ten()],\
        [beams_[0].get_material().get_name()+"compression", beams_[0].get_material().get_name()+"tension", planck_.get_material().get_name()+"compression", planck_.get_material().get_name()+"tension"])
