# Generalized ensemble and grand canonical ensemble

We can dial back to the derivation of canonical ensemble from micro canonical ensemble. We follow the logical structure below.
1. We start by consider the system and the reservoir as a composite system. And we assume this composite system is isolated from the rest of the world. So we can use the micro canonical ensemble to describe this composite system.
2. We consider the two sub-systems can exchange an extensive quantity, energy, between the system we are interested in and the reservoir that is in contact with our system. When the extensive quantity, energy, is exchanged within the system and the reservoir, the total extensive quantity is conserved because the composite system is assumed to be isolated. This allows us to write down the expectation value of any observable defined on the system to be restricted by the conservation of the extensive quantity, energy. We should consider the microscopic configuration of the system and the reservoir.
3. We convert the phase space of the reservoir that is restricted by the conservation of energy to the expression of entropy of the reservoir using the Boltzmann's postulate. With this trick, we get rid of the integration over the microscopic configurations of the reservoir.
4. By definition, the reservoir is huge comparing with the system such that the intensive variable, temperature, can be considered to be fixed. Because of that, we can expand the exponent, which is the entropy of the reservoir, as a function of the extensive quantity, energy, near the total energy using the ratio of the extensive quantity between the system and the reservoir as the small parameter.
5. Then, we got the probability of the microscopic configuration $\xi_s$ is proportional with the exponential function. The argument of the exponential function is related to the first derivative of the entropy of the reservoir with respect to the extensive quantity and the corresponding extensive quantity, energy, for the microscopic configuration $\xi_s$. This is the Boltzmann factor. The derivative is related to a fix quantity, temperature.
6. So we can argue the probability of the microscopic configurations is proportional with Boltzmann factor and the rest of the calculation just follows.

At this point, we found we can generalize this procedure easily by substitute the extensive quantity, energy, by any possible extensive quantity $X_i$. The reservoir can be defined to be a reservoir such that the corresponding first derivative of the entropy of the reservoir with respect to the extensive quantity $X_i$ to be fixed. Just like the temperature in the canonical ensemble. Then we can run through identical arguments we used in canonical ensemble to derive the corresponding ensemble theory. This is the idea of the *generalized ensemble*.

To be more specific, the reservoir has the property that $f_i$ is fixed. Where we define $f_i$ via

$$
\left.\frac{\partial S^{(R)}}{\partial X_i^{(R)}}\right|_E=-\frac{f_i}{T}
$$

The additional factor we need to include in the probability description is simply $\exp\left[\beta \sum_i f_i X_i^{(s)}(\xi_s)\right]$. Here, sum over $i$ indicates all the possible extensive quantities that is allowed to exchange when the system and the reservoir is in contact and the corresponding intensive variables that is kept fixed during the process of reaching equilibrium.

From thermodynamics, we know the pairs of $(X_i,f_i)$ includes $(E,-1),(V,-p),(N,\mu),...$

The corresponding thermodynamic potential is 

$$
-(TS+\sum_i f_i \langle X_i\rangle)\text{.}
$$

The generalized fluctuation-dissipation theorem is

$$
\langle X_i^2\rangle-\langle X_i\rangle^2=\frac{\partial \langle X_i\rangle}{\partial (\beta f_i)}\text{.}
$$

## The grand canonical ensemble

The system is allowed to exchange particle with the reservoir. That also implicitly suggest the system can exchange energy with the system.

Therefore, we have the probability of microscopic state, 

$$
P(\xi_s)\propto \exp\left[\beta((-1)H^{(s)}(\xi_s)+\mu N_s)\right]
$$

$$
Z_{GC}=\sum_{N_s=0}^{\infty}\int d\xi_s\exp\left[\beta((-1)H^{(s)}(\xi_s)+\mu N_s)\right] \approx \exp\left[-\beta(\langle H^{(s)}\rangle -TS-\mu\langle N\rangle)\right]=\exp\left[-\beta \Omega\right]\text{.}
$$

$$
\langle H\rangle=E=-\frac{\partial \ln Z_{GC}}{\partial \beta}\\
\langle \hat{N}\rangle=N=\frac{\partial \ln Z_{GC}}{\partial \beta \mu}\text{.}
$$
Here, we use $\hat{N}$ to represent the observable of number of particle and distinguish this observable with the average of the number of particle which is represented by $N$.

### The ideal gas model (Grand canonical ensemble)

For the ideal gas model, we usually have fixed $N$. If we want to use the grand canonical formalism to describe the system, we can use the following steps to get reid of the chemical potential.
1. Construct $Z_{GC}(T,\mu,V)$.
2. Calculate the average number of particles by $\langle N\rangle=N=\frac{\partial \ln Z_{GC}}{\partial \beta \mu}$ and invert this relation to get $\mu(N,T,V)$.
3. Insert $\mu(N,T,V)$ into $\ln Z_{GC}$ so we can calculate all the thermodynamic quantity and express them using $N,T,V$.

$$
Z_{GC}=\sum_{N=0}^{\infty} e^{\beta\mu N}\left\{\frac{1}{N!}\int \left(\prod_{i=1}^{N}\frac{d \textbf{R}d\textbf{P}}{h^3}\right) \exp\left[-\beta \sum_{j=1}^N\frac{\textbf{P}_j^2}{2m}\right]\right\}=\sum_{N=0}^{\infty} z^NZ_N=\sum_{N=0}^{\infty}\frac{1}{N!}\left(\frac{zV}{\lambda^3}\right)^N=\exp[\frac{zV}{\lambda^3}]
$$

$$
\langle \hat{N}\rangle=N=\frac{\partial \ln Z_{GC}}{\partial (\beta \mu)}=e^{\beta \mu}\frac{V}{\lambda^3}=\frac{zV}{\lambda^3}
$$

Using this relation, we can have the state equation

$$
\Omega=-k_BT \ln Z_{GC}=-Nk_BT=-PV\text{.}
$$


