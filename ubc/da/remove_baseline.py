import numpy as np
from ubc.da.read_mat import read_mat


def remove_baseline(wavelength: np.ndarray, power: np.ndarray, deg: int = 4):
    """
    Fit a polynomial ``p(x) = p[0] * x**deg + ... + p[deg]`` of degree `deg`
    returns power corrected without baseline
    """
    pfit = np.polyfit(wavelength - np.mean(wavelength), power, deg)
    power_baseline = np.polyval(pfit, wavelength - np.mean(wavelength))

    power_corrected = power - power_baseline
    power_corrected = power_corrected + max(power_baseline) - max(power)
    return power_corrected


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import ubc

    w, p = read_mat(ubc.path.mzi1)
    pc = remove_baseline(w, p)
    plt.plot(w, pc)
    plt.show()
