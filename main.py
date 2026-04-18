
import numpy as np               # For linear algebra and arrays
import matplotlib.pyplot as plt  # For plotting your energy levels and pulses
import qutip as qt               # The core quantum dynamics engine
import scqubits as scq           # Specifically for transmon hardware modeling

transmon.plot_wavefunction(which=[0, 1, 2], mode='real')