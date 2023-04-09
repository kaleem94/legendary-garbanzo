import numpy as np


def sim_static(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Simulate a static system.

    Args:
        A (np.ndarray): State matrix.
        B (np.ndarray): Input matrix.
        C (np.ndarray): Output matrix.
        D (np.ndarray): Feedthrough matrix.
        u (np.ndarray): Input signal.

    Returns:
        np.ndarray: Output signal.
    """
    y = np.zeros((u.shape[0], C.shape[0]))
    x = np.zeros((A.shape[0], 1))
    for k in range(u.shape[0]):
        x = A @ x + B @ u[k, :]
        y[k, :] = C @ x + D @ u[k, :]
    return y

if __name__ == "__main__":
    #sample arguments to test the function above
    A = np.array([[0.8, 0.2], [-0.2, 0.8]])
    B = np.array([0.1, 0.2]).reshape(-1, 1)
    C = np.array([0.1, 0.2])
    D = np.array([0.0])
    u = np.random.rand(1000, 1)
    y = sim_static(A, B, C, D, u)
    print(y)
    print(y.shape)
    print(y.size)
    print(y.ndim)

