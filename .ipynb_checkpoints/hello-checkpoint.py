import py_wake

from py_wake.examples.data.hornsrev1 import Hornsrev1Site, V80, wt_x, wt_y, wt16_x, wt16_y
from py_wake.literature.noj import Jensen_1983 as NOJ

wind_turbines = V80()
site = Hornsrev1Site()
noj = NOJ(site=site, windTurbines=wind_turbines)

