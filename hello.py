import py_wake
import os
import numpy as np
import matplotlib.pyplot as plt

from py_wake.wind_turbines import WindTurbine, WindTurbines
from py_wake.examples.data.hornsrev1 import V80
from py_wake.examples.data.iea37 import IEA37_WindTurbines, IEA37Site
from py_wake.examples.data.dtu10mw import DTU10MW
from py_wake.wind_turbines.power_ct_functions import PowerCtTabular

v80 = V80()
iea37 = IEA37_WindTurbines()
dtu10mw = DTU10MW()

from py_wake.examples.data import wtg_path

wtg_file = os.path.join(wtg_path, 'NEG-Micon-2750.wtg')
neg2750 = WindTurbine.from_WAsP_wtg(wtg_file=wtg_file)

class DummyWT(WindTurbine):
    def __init__(self, ct=0.8, d=80., zh=70., name='dummyWT'):
        WindTurbine.__init__(
            self,
            name=name,
            diameter=d,
            hub_height=zh,
            powerCtFunction=PowerCtTabular(
                ws=[-100,100],
                power=[0,0],
                power_unit="kW",
                ct=[ct,ct]
            )
        )

