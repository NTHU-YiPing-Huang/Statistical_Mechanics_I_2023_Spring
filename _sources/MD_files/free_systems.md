# Interacting free systems

*Reference: {cite:p}`peliti2011statistical` Chap. 4*

```{admonition} Summary
:class: tip
* Partition functions of interacting free systems are factorizable.
* Sometimes, interacting free models can provide valuable insights for our system.
	* $T^3$ dependence of specific heat $\to$ linear dispersive bosonic mode?
	* $T$ dependence of specific heat $\to$ existence of fermi surface?
* We will discuss the following interacting free systems
	* Oscillators (classical and quantum) : The equipartition theorem and Einstein's phonon.
	* Phonon and photon: statistical behavior of the linear dispersive bosonic mode. Generic feature, $C\propto T^3$
	* Fermi gas: the existence of fermi sea and the thermodynamics due to the fermi surface. Generic feature, $C\propto \frac{D(E_F)\delta T k_BT}{\delta T}\propto T$
	* Bose gas: the Bose-Einstein condensate, finite capacity to host bosons at excited states$\to$ bosons accumulate at ground state if needed.

```

## What we have learned so far...

We spend half of our semester discussing about the fundamentals of statistical mechanics. Starting from the Boltzmann's postulate, we bridge the microscopic phase space volume and macroscopic thermodynamics function entropy. The postulate encapsulate key information for the theoretical framework such that we can build ensemble theory on top of that. The ensemble theory teaches us how to construct probability description of our system. On the one hand, the probability description bridges to the old thermodynamics description. On the other hand, the probability description provides a microscopic statistical picture and allows us to make finer predictions of the microscopic behavior of the system.

The above framework is constructed from a sequence of formal discussion. The two examples that we rely on is the ideal gas model and the paramagnetic phase of Ising spin model. In the following lectures, we will apply  the idea of statistical mechanics on various systems. Before we start the discussion of individual models, we will first describe the logic flow of how to use statistical mechanics to study a physical system.

## How to apply statistical mechanics...

Here, we made a table to demonstrate the rough idea of how statistical mechanics is applied to a physical system.


### The flow chart

<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 30%;
}
table th:nth-of-type(3) {
    width: 60%;
}
</style>

| Stage  | Statistical mechanics idea                                                                                                                                                                                                                                                                                                        | Example using physical system                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :----: | :-----------------:                                                                                                                                                                                                                                                                                                               | :---------------:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1      | Pick a system                                                                                                                                                                                                                                                                                                                     | A piece of magnetic material                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2      | Identify the relevant microscopic degrees of freedom, $\xi$                                                                                                                                                                                                                                                                       | We need to ask: where does the magnetic behavior of the system came from? Usually, this relies on the input from various experiments. Experimentalists could ask various cleaver questions to identify that. For example, will the magnetic behavior change if we change the chemistry of the material by substitute one of the element with another one? If most of the condition is kept fixed, however magnetism disappears when we change the element A of the material into element B. It is very likely that the magnetism is related to element A. So it is reasonable to guess that A atom has an magnetic moment tied with it. So we can postulate the relevant microscopic degrees of freedom is represent by a little vector sitting on atom A. To simplify our discussion, let's assume the vector is a binary vector that points along or opposite to the $z$ direction. So the microscopic degrees of freedom is $\{\mu_i=\mu \sigma_i\}$, $i=1\sim N$, for a $N$ spin system. $\mu_i$ is the moment on atom A, $\mu$ is the size of the magnetic moment. |
| 3      | Construct the possible energy for the microscopic degree of freedom. We need to propose a Hamiltonian $H(\xi)$ based on physical arguments. (Symmetries of the system, experiments, *e.t.c.*)                                                                                                                                     | We ask: how the little spins interact with each other? Again, we usually need the help from experiments and make some educated guess. Maybe when we lower the temperature, the magnetic system developed ferromagnetic property spontaneously. From the free energy expression, $F=E-TS$, the low temperature physics is dominated by the energy $E$ (If we send $T\to0$, $TS$ becomes irrelevant.) Therefore, we need to guess a form of energy such that the little spins prefer to align with each other (Ferromagnetic order). *i.e.*, the energy is minimized when the spins are paralleled. We can guess $H(\{\mu_i\})=\sum_{i=1,j=1}^N (-J)\mu_i\mu_j$. This is the **Ising model**.                                                                                                                                                                                             |
| 4      | Now we can pick an ensemble that satisfied the constraint of our system. We can construct the corresponding partition function which lead to (1) the thermodynamic potential (macroscopic connection with thermodynamics) (2) the probability for the microscopic configuration $P(\xi)$ (microscopic statistical descriptions).  | Most of the time, the experiments study the equilibrium system with fixed temperature. Therefore, we usually pick the canonical ensemble. Then, according to our previous knowledge of statistical mechanics. We know how to construct the partition function. In our magnetic system case, $Z=\sum_{ \{\mu_i\} } e^{-\beta H(\{\mu_i\})}$. We can have the thermodynamic potential or calculate the expectation value of observable $\langle O(\{\mu_i\}) \rangle= \sum_{ \{\mu_i\} } P( \{\mu_i\} ) O(\{\mu_i\})$. Especially, we want to calculate those quantities that can be compared with experimental measurements such that we can compare our theory with experiments.                                                                                                                                                                                                        |
| 5      | We can improved our guess of $\xi$ and $H(\xi)$ by comparing with experiments. (Going back to stage 2.)                                                                                                                                                                                                                           | Usually, the agreement between the theory and experiments is not 100%. Then, one need to ask whether the disagreement is **qualitatively** or **quantitatively**. Usually, we modify the guess of $\xi$ and $H(\xi)$ such that we can reproduce the qualitative behavior of the system. ( For example, if our model predict there is no ferromagnetic physics which contradicts with experimental facts, we had better ask did we pick the wrong microscopic degrees of freedom, or they did not interact as the way we proposed.)                                                                                                                                                                                                                                                                                                                                                      |

### Potential obstacles

There are several potential obstacles:

1. Modeling (stage 2 and stage 3) : There is no standard protocol to identify the relevant degrees of freedom or construct the model.
2. Solution (stage 4) : In general, the partition function has no close form. Especially, for a generic system, the microscopic degrees of freedom interacts with each other and we don't have the nice factorizable structure of the partition function. (We will know better about what it means later.)

The obstacle 1 usually is a subject for individual research field. So we will not address the issue here. The obstacle 2 is a problem that is intrinsic when we apply statistical mechanics to various systems.

Therefore, we will focus our discussion on how to deal with the obstacle 2. We will frequently see two types of approaches. 

* Start from the interacting free limit and gently turn on the interaction-- perturbative approach
* Non-perturbative approach-- variational method, mean-field theory, *e.t.c.*

The idea of perturbative approach is to find an interacting free approximation of our real system. The interacting free limit, of course, is not equivalent with our physical system. However, the difference is just quantitative. One can argue that the discrepancy can be resolved by including more details. In that sense, understanding of the interacting free limit provides valuable insights to our target system. For example, the non-interacting limit of the fermi liquid theory is the fermi gas. In real materials, the electrons interact via Coulomb interaction. However, understanding of the fermi gas model provides qualitative correct picture for our real system. (Why it is so is an interesting question. A classic reference for this problem is {cite:p}`shankar1994renormalization`.)

The perturbative approach might not work as always. For example, the BCS theory of superconductivity is not a theory that can be constructed from the fermi gas theory using perturbative approach. We will discuss the simplest non-perturbative approach, the mean field theory, later in this semester.

For now, we will focus on the interacting free models and study the corresponding behaviors.
