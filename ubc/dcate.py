import pp
import ubc
from ubc.import_gds import import_gds


def dcate():
    """ directional coupler adiabatic 1550 te """
    c = import_gds("ebeam_adiabatic_te1550")
    return c


if __name__ == "__main__":
    c = dcate()
    cc = ubc.add_gc(c, optical_routing_type=1)
    print(c.ports)
    pp.show(cc)
