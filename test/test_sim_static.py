import unittest

import numpy as np

import lib.sysid.simulate_static as sim_static


class test_sysid(unittest.TestCase):
    def test_sim_static(self) -> None:
        A = np.array([[0.8, 0.2], [-0.2, 0.8]])
        B = np.array([0.1, 0.2]).reshape(-1, 1)
        C = np.array([0.1, 0.2])
        D = np.array([0.0])
        u = np.random.rand(1000, 1)
        y = sim_static.sim_static(A, B, C, D, u)
        self.assertEqual(y.shape, (1000, 2))
        self.assertEqual(y.size, 2000)
        self.assertEqual(y.ndim, 2)


# if __name__ == "__main__":
#     unittest.main()

# implement hte test in robot framework