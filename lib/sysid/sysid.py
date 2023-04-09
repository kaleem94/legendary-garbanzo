import control
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sysidentpy.model_structure_selection import FROLS
from sysidentpy.basis_function._basis_function import Polynomial
from sysidentpy.metrics import root_relative_squared_error
from sysidentpy.utils.generate_data import get_siso_data
from sysidentpy.utils.display_results import results
from sysidentpy.utils.plotting import plot_residues_correlation, plot_results
from sysidentpy.residues.residues_correlation import compute_residues_autocorrelation, compute_cross_correlation

import lib.sysid.simulate_static as sim_static


class sysid():
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    # generate data for a 2nd order siso system
    A = np.array([[0.8, 0.2], [-0.2, 0.8]])
    B = np.array([0.1, 0.2]).reshape(-1, 1)
    C = np.array([0.1, 0.2])
    D = np.array([0.0])
    u = np.random.rand(1000, 1)
    