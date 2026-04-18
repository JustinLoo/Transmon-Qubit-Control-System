![[Pasted image 20260416150138.png|710]]

A transmon is kinda a artificial atom. it is made up of two parts

There is a large main capcaitor . these are usually made up of aluminim or niobium and they are prinited on a islicon chip. in etweenn those there is a josephson junction. u can see it on the bedige between the two large cacpaitors.

It is made by overlapping two tiny strips of aluminim and a thin layer of alumim oxided betweeen them,

THe josephson junction has an ej and a cj in the picture above:

the cj is because its a capcaitor thats obvoius

the hamiltonian of this transmon qubit can be derived as following

we know that the hamiltonian is 

$$
H = \text{Kinetic} + \text{Potential}
$$

In a superconducting circuit, "kinetic energy" is the electrical energy stored in the capacitor

we can write it as

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

Note that we use phase and charge instead of position and momentum. these are analoguous to one another.

our goal is to solve this TISE in python. however, we can see that this is a differential equation. In order to simplify the math, we represent this TISE in the charge domain

$$
4E_C(n - n_g)^2 c_n - \frac{E_J}{2} (c_{n-1} + c_{n+1}) = E c_n
$$

Here we can see DISCETE linear algebra. this makes python cmomputation possible