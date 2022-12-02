# Canonical ensemble

We have introduce the micro canonical ensemble which has fixed total energy. However, we usually did not have control over the energy. Instead, we can control the temperature of the system. One question is: can we form ensemble theory under the fixed temperature constraint instead of the fixed energy constraint? It turns out the corresponding ensemble with fixed temperature is the canonical ensemble. To go from the micro canonical ensemble where the probability of microscopic state $\xi$ is $P(\xi)=\frac{1}{|\Gamma_E|}$, to canonical ensemble, the modification we need to make is to modify the probability such that it is proportional with the Boltzmann factor, *i.e.*, $P(\xi)\propto \exp\left[-\frac{H(\xi)}{k_BT}\right]$.

To derive this conclusion, we put our system into thermal contact with a reservoir at fixed temperature $T$. Now our composite system (contains the system that we are interested in and the reservoir) is considered as an isolated system with fixed total energy, $E_t$, so we can use the micro canonical ensemble to describe the composite system. Let's use $\xi_s$ and $\xi_R$ to represent the microscopic configurations of our system and the reservoir. The expectation value of observable $A$ defined on the system is

$$
\langle A\rangle=\frac{1}{|\Gamma_{E_t}|}\int d\xi_R\int d\xi_s A(\xi_s) \delta(H^{(s)}(\xi_s)+H^{(R)}(\xi_R)-E_t)\\
=\frac{1}{|\Gamma_{E_t}|}\int d\xi_s A(\xi_s) \underbrace{\int d\xi_R\delta(H^{(s)}(\xi_s)+H^{(R)}(\xi_R)-E_t)}_{|\Gamma_R(E_t-H^{(s)}(\xi_s))|=\exp\left[k_B^{-1} S_R(E_t-H^{(s)}(\xi_s))\right]}\\
\approx \frac{1}{|\Gamma_{E_t}|}\int d\xi_s A(\xi_s) \exp\left[k_B^{-1} \left( S_R(E_t)-\underbrace{\left.\frac{\partial S_R}{\partial E}\right|_{E_t}}_{T^{-1}} H^{(s)}(\xi_s)+\cdots \right)\right]
$$
In the last line, we expand the entropy $S_R$ around the total energy $E_t$. Since the reservoir is huge comparing with our target system. So we can expand the expression around $E_t$ By definition, $\langle A \rangle=\int d\xi_s A(\xi_s) P(\xi_s)$. From the above expression, we have shown

$$
P(\xi_s)\propto \exp\left[-\frac{H^{(s)}(\xi_s)}{k_BT}\right]\text{.}
$$


```{admonition} What?
:class: tip
Why can we assume $A$ only depends on $\xi_s$? The derivation above is true when we can have our observable defined on the support of the system's microscopic configurations $\xi_s$. It turns out most of the observable related to the system can be defined in this way. For example, the volume of the system will depends only on the microscopic configurations of the target system. How about the energy of the system?
```

Once we know the probability is proportional with the Boltzmann factor, $\exp\left[-\frac{H^{(s)}(\xi_s)}{k_BT}\right]$. We can normalize the probability $P(\xi_s)$. The normalization factor is the partition function

$$
Z=\left\{
\begin{array}{c}
\sum_{\xi_s}\exp\left[-\frac{H^{(s)}(\xi_s)}{k_BT}\right]\\
\int d\xi_s\exp\left[-\frac{H^{(s)}(\xi_s)}{k_BT}\right]
\end{array}
\right.
\text{.}
$$

When $\xi$ is treated as continuous variable, we can represent the expectation value of observable $A$ as

$$
\langle A\rangle =\int d\xi A(\xi) P(\xi)=\frac{1}{Z}\int dE'\underbrace{\left\{\int d\xi \delta( H(\xi)-E' ) A(\xi)\right\}}_{a^*(E')e^{\frac{S(E')T}{k_BT}}} exp\left[-\frac{E'}{k_BT}\right]\text{.}
$$

Here, the integral in the curly parentheses is the average value of $A$ in the micro canonical ensemble picture. As we have learned, the configuration number in micro canonical ensemble is overwhelmed by the configurations with equilibrium value $a^*$. So this integral can be approximated by the equilibrium value at $E'$ times the phase space volume which can be expressed as the exponential of entropy according to the Boltzmann's postulate.

So we have

$$
\langle A\rangle =\frac{1}{Z}\int dE'a^*(E')exp\left[-\frac{E'-TS(E')}{k_BT}\right]\text{.}
$$
If we stare at this expression, we can realize the degenerate configurations in the energy, $E'$, is captured by the entropy $S(E')$.


Here, if we make a reasonable assumption that $a^*(E')$ varies slowly comparing with the exponential function. We can use the saddle point approximation. The integral is dominated by the contribution that $E'=E^*$ such that

$$
\left.\frac{\partial}{\partial E'}\left( E'-TS(E')\right)\right|_{E'=E^*}=0\text{.}
$$

This equation leads to

$$
\left.\frac{\partial S}{\partial E}\right|_{E^*}=T\text{.}
$$

That is, the integral is dominated by the energy such that the corresponding temperature is the equilibrium temperature $T$. *i.e.* the equilibrium energy $E^*=\langle H\rangle$. Similarly, the partition function will also have similar behavior.

$$
Z\approx \exp\left[-\frac{E^*-TS(E^*)}{k_BT}\right]\equiv \exp\left[-\frac{F}{k_BT}\right]\text{.}
$$

Once we got $Z$, we can easily connect it with the Helmholtz free energy $F$ by

$$
F=-k_BT\ln Z\text{.}
$$

So statistical mechanics can bridge the microscopic picture with thermodynamics! Even more, it provides the probability for each microscopic configuration $P(\xi)$. To some extend, we have finer information so we can make further predictions about our system beyond conventional thermodynamics! Here we use the following calculation to show this point.

## The energy fluctuation

The expectation value of the energy for continuous $\xi$ can be expressed as

$$
\langle H\rangle =\int d\xi H(\xi) P(\xi)=\frac{1}{Z}\int d\xi H(\xi)\exp\left[-\beta H(\xi)\right]\text{.}
$$

Here, we follow the convention to denote $(k_BT)^{-1}$ as $\beta$.

$$
\frac{\partial \ln Z(\beta)}{\partial \beta}=-\int d\xi H(\xi) \frac{e^{-\beta H(\xi)}}{Z} =-\langle H\rangle =-E\propto N\\
\frac{\partial^2 \ln Z(\beta)}{\partial \beta^2}= \langle H^2\rangle-\langle H\rangle^2=\frac{\partial (-E)}{\partial \beta}=k_BT^2\frac{\partial E}{\partial T}=k_BT^2C\propto N\ge0\text{.}
$$

So we have the very important result of the *Fluctuation-dissipation theorem*!

$$
\underbrace{\langle H^2\rangle-\langle H\rangle^2}_{\substack{\text{fluctuation}\\ \text{in energy}}}=k_BT^2\times \underbrace{C}_{\substack{\text{specific heat,}\\ \text{thermodynamic quantity}}}\text{.}
$$

Through statistical mechanics, we found the specific heat(macroscopic quantity) is related to the fluctuation(microscopic picture) in energy! 

## The ideal gas model (canonical ensemble)

The partition function is

$$
Z=\frac{1}{N!}\int \left(\prod_{i=1}^{N}\frac{d \textbf{R}d\textbf{P}}{h^3}\right) \exp\left[-\beta \sum_{j=1}^N\frac{\textbf{P}_j^2}{2m}\right]
=\frac{V^N}{N!}\left\{\int \frac{d P}{h} \exp\left[-\beta \frac{P^2}{2m}\right]\right\}^{3N}=\frac{1}{N!}\left(\frac{V}{\lambda^3}\right)^N\text{.}
$$
In the second equality, we integrate over the space and use the fact that the momentum integral over each component of each particle factorizes. Here, the Gaussian integral over momentum give us the result that can be expressed by the de Broglie wave length, $\lambda=\sqrt{\frac{h^2}{2\pi mk_BT}}$.

The Helmholtz free energy can be calculated by

$$
\frac{-F}{k_BT}=\ln Z\xrightarrow{\text{Stirling's approximation}} N\ln\left[ e \frac{V/N}{\lambda^3}\right]\text{.}
$$

When the average occupied space for each particle is much larger then the unit of volume formed by the de Broglie wave length, the wave function overlap can be ignored, so we don't need to worry about the quantum statistics (*i.e.* the Bose/Fermi statistics). Once we have the Helmholtz free energy, we can derive other thermodynamic quantities easily.
