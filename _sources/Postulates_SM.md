# Postulates of statistical mechanics

*Reference: {cite:p}`peliti2011statistical` Chap. 3, {cite:p}`ma1985statistical` Chap. 26*

```{admonition} Summary
:class: tip

* The Boltzmann's postulate of entropy
	* $$ S=k_B\ln(|\Gamma|)$$
	* $S\sim \mathcal{O}(N)$ and $|\Gamma|\sim\mathcal{O}(e^{N})$ $\to$ Implicit assumption of statistical independence.
	* Connecting the microscopic physics with the macroscopic physics.
	* Reproduce the key properties of thermodynamic entropy
* What is (Why) phase space?
	* A high-dimensional space 
	* Observables and the extensive quantities
	* Canonical evolution and Livioulle theorem $\to$ Possible to have statistical description $\to$ Turning time average into  the ensemble average!
* The ensemble theory
	* micro canonical ensemble
	* canonical ensemble
	* generalized ensemble
	* grand canonical ensemble


```

After we have introduce the simple example of ideal gas and review the structure of thermodynamics in the last chapter. It is tempting to develop the microscopic interpretation for macroscopic observables based on statistical description. The idea however is not so straight forward. The challenge is: how to go from the time evolution to statistics?

Or, one can ask: what is the general structure behind the time evolution? The question is interesting. However, it is too broad for us to explore. We will try to narrow the scope in the following course and ask a simpler question: what is the general structure for the time evolution without dissipation?

Even for this more specific question, it is still quite challenging. It is because the microscopic components in a generic system interacts with each other. Therefore, it is not clear how one can make a general conclusion since the microscopic components can interact with each other in various different ways.

Boltzmann's postulate suggests an interesting way to think about the problem: the microscopic components might interact with each other in various fashion; however, it is possible to have a phase that even though the microscopic components interacts with each other, the microscopic components can be considered to be statistical independent within the observation space and time scale. When the system reaches such phase, its correlation in space and time are lost. We might have a simpler system to understand.

For such a system, the microscopic configurations can be considered statistically independent. Boltzmann postulates to encapsulate the information neatly in the expression $S=k_B\ln (|\Gamma|)$ where the possible configurations can be considered as the product of configurations in the subsystems and the corresponding information is related to the thermodynamic entropy. Here $S$ is the thermodynamic entropy and $|\Gamma|$ is the accessible phase space volume.

We are going to introduce this idea in this chapter. After we went though the related concept, the related probability description, ensemble theory, is introduced. We will use some simplest non-trivial examples to demonstrate related ideas.
