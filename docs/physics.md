

!\[\[Pasted image 20260416150138.png|710]]





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

K = -4E\_C \\frac{d^2}{d\\phi^2}



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

$$\\left( -4E\_C \\frac{d^2}{d\\phi^2} - E\_J \\cos(\\phi) \\right) \\psi\_n(\\phi) = E\_n \\psi\_n(\\phi)$$

