## Transmon Qubit: An Artificial Atom

A **transmon** is essentially an artificial atom. It is made up of two parts:

There is a **large main capacitor**. These are usually made up of aluminum or niobium, and they are printed on a silicon chip. In between those, there is a **Josephson junction**. You can see it on the bridge between the two large capacitors.

It is made by overlapping two tiny strips of aluminum and a thin layer of aluminum oxide between them. The Josephson junction has an $E_J$ and a $C_J$ in the picture: the $C_J$ is because it is a capacitor, which is obvious.

### Hamiltonian Derivation

The Hamiltonian of this transmon qubit can be derived as follows. We know that the Hamiltonian is:

$$
H = \text{Kinetic} + \text{Potential}
$$

In a superconducting circuit, "kinetic energy" is the electrical energy stored in the capacitor. We can write it as:

$$
K = -4E_C \frac{d^2}{d\phi^2}
$$

The potential energy comes from the Josephson junction. That can be denoted as:

$$
P = -E_J \cos(\phi)
$$

Together we get the Hamiltonian:

$$
\hat{H} = -4E_C \frac{d^2}{d\phi^2} - E_J \cos(\phi)
$$

Our full **Time-Independent Schrödinger Equation** for our transmon becomes:

$$
\left( -4E_C \frac{d^2}{d\phi^2} - E_J \cos(\phi) \right) \psi_n(\phi) = E_n \psi_n(\phi)
$$
