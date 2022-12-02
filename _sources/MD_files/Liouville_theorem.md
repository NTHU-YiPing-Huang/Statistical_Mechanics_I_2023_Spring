# Liouville's theorem

The Liouville's theorem tells us why phase space is special and how it helps us to develop a statistical description from the time-evolution of many-body systems.

The Liouville's theorem is a theorem based on canonical time-evolution. The time-evolution satisfies the Hamilton's equation

$$
\frac{d \textbf{R}}{dt}= \frac{\partial H}{\partial \textbf{P}}\\
\frac{d \textbf{P}}{dt}= -\frac{\partial H}{\partial \textbf{R}}\text{.}
$$

We want to understand the evolution of the probability density in phase space. The probability density in phase space is defined as

$$
dP(\xi(t))=\rho(\xi(t)) d\xi(t)\text{.}
$$
Here $dP(\xi(t))$ is the probability of the system to be near $\xi(t)$.

There are three conclusions we can derived from Liouville's theorem

1. The local probability density $\rho(\xi(t),t)$ is invariant under the time-evolution.
   
   The idea of the proof is the local conservation of probability. The probability in phase space is conserved. The continuity equation combined with Hamiltonian evolution proves the statement. One can check the details from {cite:p}`sethna2021statistical`.
   
2. The phase space volume is invariant under the time-evolution.
   
   One can follow the proof from {cite:p}`peliti2011statistical`. The idea is simple. We can express the area element of a pair of conjugate variables. Then we try to express the area element after a infinite small time evolution $dt$. We will find the area is invariant up to higher order correction. 
   
3. Let's define $\xi_0=\xi(t=0)$. If $\rho(\xi_0)$ depends only on the extensive variables $\{X_i(\xi_0)\}$, *i.e.*
   
   $$
   \rho(\xi_0)=\Phi(X_1(\xi_0),X_2(\xi_0),\cdots, X_r(\xi_0))\text{,}
   $$
   then $\frac{\partial \rho}{\partial t}=0$. The detail of the derivation can be found in {cite:p}`peliti2011statistical`.

* 1 and 2 are equivalent statement with each other because the conservation of phase space volume and the point in phase space will not disappear suggest the density is invariant.
* Since we postulate the macroscopic system can be specified by the extensive variables. 3 implies that we can have a probability density distribution that has no dependence on time. If it is so, the remaining question is: how to describe the probability density as a function of $\xi$.



