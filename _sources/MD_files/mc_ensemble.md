# Microcanonical ensemble

What is an ensemble? It is a framework that relate the microscopic configuration with a probability. The micro canonical ensemble might be the simplest one to define. The system we are considering is a system with conserved energy. The microscopic states that satisfy this energy conserving constraints form the phase space of the system. The micro canonical ensemble assign equal weights to all those states in the constrained phase space.

Why this assignment is useful? Because the equilibrium configurations has overwhelming number in the constrained phase space. So we can calculate the equilibrium value using the micro canonical ensemble. *i.e.* For extensive variable $A$, we have its equilibrium value $a^*$ to be

$$
a^*=\langle A \rangle =\frac{1}{|\Gamma|} \int_{\Gamma}d\xi A(\xi)\text{.}
$$

Why it is so? From the variational principle of entropy, the entropy is maximized at equilibrium.

$$
S(X;a)\le S(X;a^*)\text{.}
$$
Here $X$ represent the rest of the extensive variables. Here $a$ is the possible value of the observable $A$ that is not in equilibrium.

The corresponding expression using the Boltzmann's postulate is

$$
S(X;a)=k_B\ln\left[\int d\xi \delta(A(\xi)-a)\right]=k_B\ln(|\Gamma_a|)\\
S(X;a^*)=k_B\ln\left[\int d\xi \delta(A(\xi)-a^*)\right]=k_B\ln(|\Gamma_{a^*}|)\text{.}
$$

We can immediately see

$$
\frac{|\Gamma_a|}{|\Gamma_{a^*}|}=\exp\left[\frac{1}{k_B}\left(S(X;a)-S(X;a^*)\right)\right]\\
\approx \exp\left[\frac{1}{2k_B}\left(\underbrace{\left.\frac{\partial^2 S}{\partial A^2}\right|_{a^*}}_{<0, \sim \mathcal{O}(N^{-1})}\right)\underbrace{(a-a^*)^2}_{\sim\mathcal{O}(N^2)}\right]\sim e^{-N}\text{.}
$$

In the approximation, we expand the entropy around the equilibrium value $a^*$. We can see the phase space corresponds to observable $a\neq a^*$ is exponentially small in system size. At thermodynamic limit, we found the phase space volume is dominated by the equilibrium phase space, $|\Gamma_{a^*}|$.

Therefore,

$$
\langle A \rangle =\frac{1}{|\Gamma|} \int_{\Gamma}d\xi A(\xi)\approx \frac{1}{|\Gamma_{a^*}|} \int_{\Gamma_{a^*}}d\xi A(\xi)=a^*\frac{1}{|\Gamma_{a^*}|} \int_{\Gamma_{a^*}}d\xi=a^*
$$
 which is the statement we started with at the beginning of the section.
 
In principle, $A$ can be any extensive variable. Usually, the most important conserved quantity is the energy. So we consider the micro canonical ensemble to be the ensemble with fixed value of energy if we did not specified the conserved quantity explicitly.

Let's try to use some examples to demonstrate the idea.
 
## Examples

### Ideal gas model

The Hamiltonian of the ideal gas model is

$$
H=\sum_{i=1}^{N}\frac{\textbf{P}_i^2}{2m} +U(\textbf{R}_i)\text{.}
$$
Here, we assume $U(\textbf{R}_i)$ is 0 in the box and $\infty$ outside the box.

The accessible phase space by the Hamilton equation is

$$
|\Gamma_E|=\underbrace{\frac{1}{N!}}_{\substack{\text{indistinguishable}\\\text{particles}}}\times \underbrace{\frac{1}{h^{3N}}}_{\substack{\text{the unit of}\\ \text{phase space volume}}} \times
\int\prod_{i=1}^{N} d\textbf{R}_i d\textbf{P}_i \underbrace{\delta(E-\sum_{j=1}^N\frac{\textbf{P}_j^2}{2m})}_{\substack{\text{restrict to the configurations}\\ \text{with energy } E}}\text{.}
$$

```{admonition} What?
:class: tip
We are studying the classical ideal gas model. Why indistinguishable is important? (Indistinguishiability is a subtle concept in quantum mechanics. How can "identical" particles to be "distniguishable" or "un-distinguishable"? Here, a good reference is {cite:p}`shankar2012principles`. The question is whether the concept of path is still applicable. For quantum particles, the wave function interpretation will ruin the concept of path.) If we consider a lattice system with quantum spins, do we have the $(N!)^{-1}$ factor in the partition function?
```

The integration over $\textbf{R}_i$ is simple, it just gives the volume $V$. We can use the property of delta function $\delta( Ax)=A^{-1}\delta(x)$ to proceed. We will have

$$
|\Gamma_E|=\frac{V^{N}}{N!h^{3N}}\frac{\pi^{3N/2}(2mE)^{(3N-1)/2}}{\underbrace{\Gamma_E\left(\frac{3N}{2}\right)}_{\text{Euler's gamma function}}}\text{.}
$$

So we have

$$
S=k_B\ln(|\Gamma_E|)\approx Nk_B\ln\left\{\frac{eV}{N} \left[\frac{2\pi m e}{h^2}\left(\frac{2E}{3N}\right)\right]^{3/2}\right\}\text{.}
$$

From the expression of entropy, we can take derivative with respect to $E$ and $V$ to get the expression for internal energy and the state equation.
At this point, we can see that statistical mechanics can let us calculate the thermodynamic quantities explicitly. However, we have thermodynamics already. Can statistical mechanics provide something new? As we mentioned, once we have the probability, we can calculate the expectation value of any physical observables, $O$, by

$$
\langle O \rangle=\left\{
\begin{array}{c}
\sum_{\xi} P(\xi)O(\xi); \text{discrete }\xi\\
\int d\xi P(\xi)O(\xi); \text{continuous }\xi
\end{array}
\right.
$$

For microcanonical ensemble, $P(\xi)=\frac{1}{|\Gamma_E|}$.

### Paramagnetic phase

Paramagnetic phase is a phase where the behavior of the magnetic moments (spins) are dominated by entropy. So it is almost like the spins are not interacting with each other. In that case, the spins can only interact with the external field. We choose the direction of the field to be the $z$ direction, $\vec{h}=h\hat{e}^z$. Consider we have a lattice where the magnetic moments sitting on site $i$ to be $\vec{\mu}_i=\mu\sigma_i\hat{e}^z$. Here we make a bold assumption that the magnetic moment under field can only be parallel or anti-parallel with the external field. Since the spins are effectively decoupled with each other in the paramagnetic phase, this assumption is not a bad assumption to start with.

The energy of the system is 

$$
H=-\vec{h}\cdot \underbrace{\left(\sum_{i=1}^N \vec{\mu}_i\right)}_{M}=-h\mu\sum_{i=1}^{N}\sigma_i\text{.}
$$

From this expression, we found the energy is closely related to $\sum_{i=1}^{N}\sigma_i$. When $h$ and $\mu$ are considered to be fixed, the energy is just a function of $\sum_{i=1}^{N}\sigma_i$. For micro canonical ensemble, we care about the configuration with fixed energy, that corresponds to the configuration where $\sum_{i=1}^{N}\sigma_i$ (or $M$) is a fixed value.

We know $N=N_{\uparrow}+N_{\downarrow}$ where $N_{\uparrow}(N_{\downarrow})$ is the number of spins parallel(anti-parallel) with the external magnetic field. Also, we can see 
$\sum_{i=1}^{N}\sigma_i=\frac{M}{\mu}$. So we have $N_{\uparrow}=(N+M/\mu)/2$ and $N_{\downarrow}=(N-M/\mu)/2$


The number of microscopic configurations with fixed $M$ is

$$
|\Gamma_E|=\frac{N!}{N_{\uparrow}!N_{\downarrow}!}=\frac{N!}{\left(N+\frac{M}{\mu}\right)!\left(N-\frac{M}{\mu}\right)!}\text{.}
$$

Using $S=k_B\ln(|\Gamma_E|)$, we can get the expression of entropy as a function of $M$.

$$
S=k_B\ln(|\Gamma_E|)\xrightarrow{\text{Stirling's approximation}} S(M) \text{.}
$$

$$
\frac{h}{T}=-\frac{d S}{d M}\xrightarrow{\frac{1}{2}\ln\frac{1+x}{1-x}=\tanh^{-1}x} \frac{k_B}{\mu} \tanh^{-1}\frac{M}{\mu N}\text{.}
$$

Here we use the condition $dE=0=TdS+hdM$ since we are considering the micro canonical ensemble where energy is conserved.
