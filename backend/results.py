# Fernando Lavarreda
# Obtain values for a given beam & planck combination

from obj.beam import Beam
from obj.planck import Planck

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


def stress(momentum:float, inertia:float, height:float, n_factor=1)->float:
    return -momentum*height*n_factor/inertia


def momentum(stress_, inertia, height, n_factor=1)->float:
    return -stress_*inertia/(height*n_factor)
