"""Este proyecto esta basado en el documento Modelamiento y simulacion de circuitos sinapticos
 de david ramirez y julian hurtado """
import numpy as np
import matplotlib.pyplot as plt
"""
-----------------------------------------------------------------------------------------------------------------------
Declacracion de los valores
-----------------------------------------------------------------------------------------------------------------------
"""
# pesos sinapticos
a = 1
b = 0.9
c = 1
# matriz de estados de tiempo
E = np.zeros((5, 1000), dtype="int")
# Pasos de integracion
dt = 1
# Constante de tiempo
tau = 10
T1 = 100.0
T2 = 600.0
N = 300
S = 30
t = range(1000)


# señal de activacion
def ns(y):
    return 0 * (y < T1) + 400 * (y >= T1) * (y <= T2) + 0 * (y > T2)


# Funcion Naka-Rushton
def naka(x):
    return (N * max(0, x) ** 2) / (S ** 2 + max(0, x) ** 2)


"""
------------------------------------------------------------------------------------------------------------------------
Ejecucion de las neuronas
------------------------------------------------------------------------------------------------------------------------
"""
for i in range(999):
    E[0, i + 1] = E[0, i] + (dt / tau) * (-E[0, i] + ns(i))
    E[1, i + 1] = E[1, i] + (dt / tau) * (-E[1, i] + a * E[0, i])
    # Neurona cambio positivo
    E[2, i + 1] = E[2, i] + (dt / tau) * (-E[2, i] + naka(b * E[0, i] - c * E[1, i]))
    E[3, i + 1] = E[3, i] + (dt / tau) * (-E[3, i] + a * E[0, i])
    # Neurona cambio negativo
    E[4, i + 1] = E[4, i] + (dt / tau) * (-E[4, i] + naka(b * E[3, i] - c * E[0, i]))


# plot de la figura
plt.figure(1)
plt.plot(t, E[0, :], label="Señal")
plt.plot(t, E[2, :], label="neurona de cambio positivo")
plt.plot(t, E[4, :], label="neurona de cambio negativo")
plt.legend()
plt.show()