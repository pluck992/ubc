import pp
from ubc.layers import lys


@pp.autoname
def bend_circular(radius=10, width=0.5, layer=lys["WG"], layers_cladding=[], **kwargs):
    c = pp.c.bend_circular(
        radius=radius,
        width=width,
        layer=layer,
        layers_cladding=layers_cladding,
        with_pins=True,
        **kwargs,
    )
    labels = [
        f"Lumerical_INTERCONNECT_library=Design kits/EBeam",
        f"Lumerical_INTERCONNECT_component=ebeam_bend_1550",
        f"Spice_param:radius={radius:.3f}u wg_width={width:.3f}u",
    ]

    for i, text in enumerate(labels):
        c.add(pp.c.label(text=text, position=(c.x, c.y + i * 0.1), layer=lys["DEVREC"]))
    return c


if __name__ == "__main__":
    c = bend_circular()
    pp.show(c)
