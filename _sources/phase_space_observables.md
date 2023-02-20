# Phase space and Observables

The right hand side of the Boltzmann's postulate is related to the concept of accessible phase space. So we will start our discussion from what is a phase space and how it could related to the thermodynamic extensive variables. After that, we can ask: why choosing the phase space? What's so special about phase space? The answer is related to the Liouville's theorem.

## Phase space

As we mentioned, we care about the canonical evolution of a Hamiltonian system where the energy is conserved. For one particle, we need to specify its position, $\textbf{R}_1$, and momentum, $\textbf{P}_1$, to uniquely define its status. For $N$ particles, we will need $N$ position vectors and $N$ momentum vectors to describe them.

We can use $\xi\equiv\{\textbf{R}_1,\textbf{R}_2,...,\textbf{R}_N;\textbf{P}_1,\textbf{P}_2,...,\textbf{P}_N\}$ to describe the status of the $N$ particle system. The space spanned by $\xi$ is the phase space.

The phase space is a space with $6N$ degrees of freedom if we consider a three-dimensional system. Since $N\sim 10^{23}$, we actually have a high-dimensional system! 

When we consider the evolution where energy is conserved, we therefore has $6N-1$ independent degrees of freedom. The evolution of the system therefore is described by a path parameterized by the evolution time $t$ in the $6N$ dimensional phase space.

### Examples

1. Single free particle in one-dimensional space:
The phase space trajectory for a single free particle is easy. We know the momentum is a fixed value $p_0$ and the position just grows linearly with time $t$. That trajectory is a straight line in the phase space.
2. Single mode simple harmonic oscillator in one-dimensional space:
The momentum of the oscillator will change as we expected. The energy conserving condition suggest the trajectory form an eclipse in the phase space.
3. Two free particles in one-dimensional space:
In this case, we have a 4 dimensional phase space. Even this simplest non-trivial example takes some imagination to realize it in our brain. So we further simplify the case by assuming the momentum of particle one and particle 2 are identical, $\textbf{P}_1=\textbf{P}_2=P\hat{i}$. The trajectory for this simplified case can be visualized in a three-dimensional space where the $z$ coordinate represent the momentum and the $x,y$ coordinates represent the position $\textbf{R}_1,\textbf{R}_2$. The trajectory will be a straight line with fixed $z$ coordinates that bisect the angle between $xz$ and $yz$ plane.


## Observables (Definition of "accessible")

The path $\xi(t)$ can be quite complicated in the high dimensional space. However, as we know the thermodynamic extensive variables such as energy and volume can fluctuates at the microscopic level, but they are relative smooth functions of the microscopic coordinates at the macroscopic scale. 

Therefore it is reasonable to define a family of function that take the rather complicated microscopic configurations $\xi(t)$ as input, but output a relative smooth value as a function of time. We call such functions observables. 

It is quite reasonable to postulate that the extensive variables in thermodynamics are all observables. (We can measure them!) The accessible volume of the phase space is therefore specified by the thermodynamics extensive variables.

### Examples

* Observable: 
	* The total kinetic energy:
$
E_{k}=\sum_{i=1}^N \frac{\textbf{P}_i^2}{2m}
$
	* The total particle number:
$
N=\int d\textbf{r}\sum_{i=1}^N\delta(\textbf{r}-\textbf{r}_i)
$
	* Another example for the microscopic state and the macroscopic observable is the coin flipping game. Consider we have $N$ coins with labels. And we flip them all. The microscopic state for the system is the outcome of each coins ( The outcome will be one of the $2^N$ configurations) One can define the "sum" of the coins by using $\sigma_i=\pm1$ to represent the heads and tails of each coin.  $\sum_{i=1}^N \sigma_i$ will be an observable that is relative smooth function of the microscopic state. Since we know the law of large number suggest this function will have a smooth distribution described by a Gaussian function.
* Not an observable: $\prod_{i=1}^N \theta(a-|\textbf{r}_i|)$.
Here

$$
\theta(x)=\left\{
\begin{array}{c}
x>0, 1\\
x<0, 0
\end{array}
\right.
$$

### Example of "accessible" phase space

* The piston: The volume of the chamber for a piston is a variable. When we discuss the accessible phase space for the gas inside the chamber, we need to discuss the real space part and the momentum part. We will discuss the space part first since it is relative straight forward. The gas in the chamber cannot escape. Therefore, the volume of the chamber is the accessible volume for the gas inside the chamber.




