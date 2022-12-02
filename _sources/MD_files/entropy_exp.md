# The fundamental postulate

The fundamental postulate is

$$
S=k_B\ln(|\Gamma|)\text{.}
$$

After we know what is the meaning of accessible phase space, we would like to discuss the meaning of the equality sign. Because the equality should be interpreted at the thermodynamic limit where $N\to\infty$, we have to some flexibility to define entropy using different expressions.

## Accessible phase space is specified by the extensive variables

The system's microscopic configuration leads to different extensive thermodynamics properties. Therefore, the extensive variables actually restrict the accessible region in the phase space.

Since we assume the thermodynamic state of the system can be specified by extensive variables $X_1,X_2,\cdots, X_r$. Suppose we have uncertainties $\Delta X_i$ for each extensive variable. The accessible phase space of the system and entropy can be expressed as

$$
| \Gamma_1 |=\int d\xi \prod_{i=1}^{r}\theta(X_i(\xi)-(X_i-\Delta X_i))\theta(X_i-X_i(\xi))
$$
and

$$
S_1(\left\{X_i\right\})=k_B\ln\left[\int d\xi \prod_{i=1}^{r}\theta(X_i(\xi)-(X_i-\Delta X_i))\theta(X_i-X_i(\xi))
\right]\text{.}
$$

Here, the $\theta$ function is used to express the idea that we want to include all possible $\xi$ such that the corresponding extensive variable $X_i(\xi)$ is in the range $\left[X_i-\Delta X_i,X_i\right]$.

Let's use a simple example to understand the expression. Consider the case that entropy is a function of energy only. We would focus on $X_0=E$ only. In this case we have

$$
S_1(E)=k_B\ln\left[\int d\xi \theta(H(\xi)-(E-\Delta E))\theta(E-H(\xi))
\right]\text{.}
$$

## Different expressions of entropy

To understand the behavior of $S(\left\{X_i\right\})$, we need to understand the behavior of the phase space volume with this expression. One of the key property of this expression is due to the high dimensionality of phase space. $\xi$ is a vector in the $6N$ dimensional space with $N\sim \mathcal{O}(10^{23})$. In the homework 2, we observe **the volume integral of high-dimensional space has the property that the volume is dominated by the outermost shell**. That is, if we define the phase space volume differently as

$$
| \Gamma_2 |=\int d\xi \prod_{i=1}^{r}\theta(X_i(\xi))\theta(X_i-X_i(\xi))$$

and

$$
| \Gamma_3 |=\int d\xi \prod_{i=1}^{r}\delta(X_i-X_i(\xi))\text{,}
$$
the corresponding entropy, $S_2(\left\{X_i\right\})$, $S_3(\left\{X_i\right\})$, actually will be equivalent to $S_1(\left\{X_i\right\})$ up to subleading terms in $N$. 
$|\Gamma_2|$ is the phase space where the extensive variable has a lower bound $X_{i,l}=0$. $|\Gamma_3|$ represent the phase space with only the configuration with extensive variable value $X_i$. Since Boltzmann's postulate is to a system at thermodynamic limit where $N\to\infty$, the different definitions $S_2(\left\{X_i\right\})$ and $S_3(\left\{X_i\right\})$ are equivalent and are valid expressions for entropy!

**We can use $S_2(E)$ to see that it is a monotonic increasing function with $E$**. Can we see $S(E)$ is also extensive?


## The variation principle of entropy

Consider system $A$ and system $B$ are both isolated systems. (Energies of system $A$ and $B$ are independently conserved) The microscopic confiugration for system $A$ and $B$ are represented by $\xi_A$ and $\xi_B$. Now if we consider the two system as a whole, the microscopic configuration of the composite system is $\xi=\left\{\xi_A,\xi_B\right\}$. Since the two system are isolated from each other, the microscopic configuration $\xi_A$ is completely independent of $\xi_B$. That means the phase space volume is simiply the product of the two, *i.e.*

$$
|\Gamma_{(A\cup B)}|=|\Gamma_A||\Gamma_B|\text{.}
$$

Now, if we put system $A$ and $B$ in thermal contact and are isolated from the environment. The constraint is relexed from the energes are indepenently conserved to the total energy of the composite system is conserved. The possible microscopic configurations are formally expressed as

$$
|\Gamma_{(A|B)}|=\sum_{E^{(A)}}|\Gamma_A(E^{(A)})||\Gamma_B(E_{total}-E^{(A)})|\text{.}
$$

Because the constraint is more relaxed, there are more possible configurations comparing with the case before the thermal contact. So we have $|\Gamma_{(A|B)}|>|\Gamma_{(A\cup B)}|$. This observation seems to suggest the entropy will increase when the system reaches equilibrium. However, when the system reaches equilibrium, the energy of the two system is $E^{(A)}_{eq}$ and $E^{(B)}_{eq}=E_{total}-E^{(A)}_{eq}$. The phase space volume at equilibrium is $|\Gamma_{eq}|=|\Gamma_A(E^{(A)}_{eq})||\Gamma_B(E^{(B)}_{eq})|\le |\Gamma_{(A|B)}$! Shouldn't the entropy (also the accessible phase space volume) be maximized when reaching equilibrium?

It turns out $|\Gamma_{eq}|\lesssim|\Gamma_{(A|B)}|$! That is, even though it is smaller than $|\Gamma_{(A|B)}|$, it is almost identical with $|\Gamma_{(A|B)}|$! Why? Let's use the Boltzman's postulate to express $|\Gamma_{(A|B)}|$ again. We have

$$
|\Gamma_{(A|B)}|=\sum_{E^{(A)}}|\Gamma_A(E^{(A)})||\Gamma_B(E_{total}-E^{(A)})|=\sum_{E^{(A)}} \exp\left[\frac{1}{k_B}\left(S_A(E^{(A)})+S_B(E_{total}-E^{(A)})\right)\right]\\
\approx \int \frac{d E^{(A)}}{\Delta E} \exp\left\{\frac{1}{k_B}\left[\left(S_A(E^{(A)}_{eq})+S_B(E^{(B)}_{eq})\right)+\underbrace{\left.\frac{\partial (S^{(A)}(E^{(A)})+S^{(B)}(E^{(B)}))}{\partial E^{(A)}}\right|_{E^{(A)}_{eq}}}_{=0, \text{extrema condition}}\left(E^{(A)}-E^{(A)}_{eq}\right)\\
+\frac{1}{2}\left(\left. \frac{\partial^2 S^{(A)}(E^{(A)})}{ \partial E^{(A)} \,^2}\right|_{E^{(A)}_{eq}}+\left. \frac{\partial^2 S^{(B)}(E^{(B)})}{ \partial E^{(B)} \,^2}\right|_{E^{(B)}_{eq}}\right)\left(E^{(A)}-E^{(A)}_{eq}\right)^2 \right]\right\}
$$

In the second line, we approximate the summation as integral to make further approximation. Since we know that entropy is maximized at equilibrium, we can expand the entropy around the equilibrium energy configuration. Here, the linear order correction is zero since we expand around the extrema. We stop the expansion at the quadratic order which is the leading non-trivial order.

We would like to know how the correction scales as we reaches the thermodyanmic limit $N\to\infty$. We find the the scaling behavior of the following quantity is

$$
k\equiv \frac{\partial }{\partial E} \underbrace{\frac{\partial S}{\partial E} }_{\mathcal{O}(1)} \sim \mathcal{O}(N^{-1})<0\text{.}
$$

So the we have the correction of the phase space volume to be of order $\int dE^{(A)} e^{\frac{k}{2}(E^{(A)}-E^{(A)}_{eq})^2}\sim \mathcal{O}(N^{1/2})$. *i.e.*

$$
|\Gamma_{(A|B)}|\approx |\Gamma_{eq}|\times K; \text{ where } K\sim \mathcal{O}(N^{1/2})\text{.}
$$

Since we know $|\Gamma_{(A|B)}|\sim |\Gamma_{eq}|\sim\mathcal{O}(e^N)$, such correction is irrelevant at $N\to\infty$ limit.


This expression also suggests the energy fluctuation, $\sim \sqrt{\left(E^{(A)}-E^{(A)}_{eq}\right)^2}$, is of order $N^{1/2}$. So the relative deviation of energy is $\mathcal{O}(N^{-1/2})$.

**The derivation above also shows the entroy is an extensive quantity** at least when the interaction is short ranged and the system $A$ and $B$ can be well approximated as statistically independent.


```{admonition} What?
:class: tip
How about the entropy should be a concave function of extensive variables?
```

## The fundamental postulate, quantum version

There is no fundamental unit of the phase space in classical mechanics. However, the quantum mechanics provide a natural unit for the phase space according to the uncertainty principle $\Delta x\Delta p\sim h$. A nature generalization of the Boltzman's postulate is

$$
S=k_B\ln\mathcal{N}\text{.}
$$

Here $\mathcal{N}$ is the number of states within the window of extensive variable $[\Delta X_i-X_i,X_i]$.
