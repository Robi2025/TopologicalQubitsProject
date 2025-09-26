import numpy as np

class KitaevChain:
    def __init__(self, N=10, mu=0.0, t=1.0, delta=1.0):
        """
        Modelo simplificado de la cadena de Kitaev.
        N: número de sitios
        mu: potencial químico
        t: hopping
        delta: gap superconductor
        """
        self.N = N
        self.mu = mu
        self.t = t
        self.delta = delta

    def hamiltoniano(self):
        # Construye una matriz simplificada del hamiltoniano
        H = np.zeros((self.N, self.N))
        for i in range(self.N-1):
            H[i, i+1] = -self.t
            H[i+1, i] = -self.t
        for i in range(self.N):
            H[i, i] = -self.mu
        return H
