# Review of thermodynamics

## Thermodynamic systems

A macroscopic system whose behavior is identified by a small and finite number of thermodynamic properties such as energy, $E$, particle number, $N$, volume, $V$, temperature, $T$, chemical potential, $\mu$, pressure, $P$, e.t.c.

Such description misses a lot of the microscopic information. However, we don't care about the full detail of the system. So the thermodynamic description is still very useful. 

There are relations between those thermodynamic properties. Those relations are determined/observed from experiments. If we formally use $R_i$ to represent the relations. We have a set of equations such as

$$
R_1(E,P, ...)=0\\
R_2(E,N, ...)=0\\
\cdots
$$

Those equations might not be independent. Thermodynamic finds the principles behind those relations such that we can reconstruct those relations with minimum assumptions.

## Concept of equilibrium

Feynmann's description of equilibrium : "... when all fast processes have already occurred, while the slow ones have yet to take place."

The distinction between fast and slow depends on the observation time scale $\tau$. Thermodynamics is formulated with the notion of equilibrium. However, usually the observation time scale $\tau$ is implicitly assumed to be well defined. We should keep in mind that in order to define equilibrium, we need to specify the time scale $\tau$.

## Extensive variables

Extensive variable are the thermodynamic variables that adds up when we consider the union of the system and its duplication.

For example, the particle number of system 1 is $N_1$. The particle number of its duplicate is $N_{1'}=N_1$. The particle number of the union of system 1 and its duplicate is $N^{(1\cup 1')}=N_1+N_1=2N_1$. Similar idea suggest the volume of the system is also an extensive variable.

Temperature is not an extensive variable. It is an intensive variable. That is, when we have system 1 with $T_1$ and its duplicate with $T_{1'}=T_1$. The union of them will reach equilibrium and still have temperature $T_1$.

Is energy an extensive variable? The total energy of the system and its duplicate should be expressed as

$$
E^{(1\cup1'}=E_1+E_{1'}+E_{int}(1,1')\text{.}
$$

The first two terms are easy to understand, they are the energy of system 1 and its duplicate 1'. The last term is the interaction between system 1 and its duplicate 1'. If the interaction between the system 1 and its duplicate is sub-extensive, meaning $E_{int}(1,1')$ scales with particle number slower than $N$, then we can claim energy is an extensive variable at the limit $N\to\infty$. Since $\lim_{N\to\infty}E^{(1\cup1'}=E_1+E_{1'}$. This could happen when system 1 and 1' can only interact between the interface of them. That happens when the interaction between them are short-ranged. On the other hand, for long range interactions, the relation will not hold and energy will not be an extensive variable. In most cases, we consider only short-ranged interaction. However, it is still important to keep in mind about this subtlety.

## The central problem of thermodynamics and its solution

Given initial state of several thermodynamic systems. We can put them together and let them interact with each other in some fashion. The central problem of thermodynamics ask the following question: what will be the final equilibrium thermodynamic state of the combined system?

The way that the sub systems interact with each other provides the constraint for the systems. For example, the two systems could interact in a way that it is allowed to exchange energy between the systems but not allowed to exchange particles. Or maybe there is no energy exchange between each other. However, they can still do work on the each other. Different constraints will required different ways to analyze the problem. However there is a postulated solution that can be constructed with different constraints.

### The postulated solution of the central problem of thermodynamics -- entropy

The entropy postulate is: There exist a function $S$ of the extensive variables called entropy that assumes the maximum value for a state of equilibrium.

1. Entropy is a function of extensive variables: Extensive variables are those physical quantities that scales like $N$ when the system size ($\propto N$) increases.
2. Entropy is extensive: Entropy itself scales like $N$.
3. Entropy is a concave function (The idea of a concave function. The different definition of concave and convex functions): Consider two thermodynamic states, specified by two sets of extensive variables $X^{(i)}=\{X^{(i)}_0,X^{(i)}_1,..., X^{(i)}_r\}, X^{(j)}=\{X^{(j)}_0,X^{(j)}_1,..., X^{(j)}_r\}$, describing the **same** system. The definition of a concave function is 
   
   $$
   S\left( (1-\alpha) X^{(i)}+\alpha X^{(j)}\right)\ge (1-\alpha)S(X^{(j)})+\alpha S(X^{(j)})\text{.}
   $$
4. Entropy is a monotonic increasing function of internal energy:
   
   $$
   \frac{\partial S}{\partial E}=\frac{1}{T}>0\text{.}
   $$

**The solution of the central problem of thermodynamics is the state that maximize entropy with the corresponding thermodynamic constraints.**

### Systems in thermal contact (the definition of empirical temperature)

We can discuss systems under thermal contact and leave the other cases for the readers as reading materials.

1. Thermally conductive and mobile wall ( the definition of empirical pressure ):
   Consider two systems in thermal contact that are isolated from the environment. The total energy of the two systems is conserved (This is the thermodynamic constraint of this simple system). The equilibrium state of this system is postulated to be the thermodynamic state such that the entropy is maximized. *i.e.*
   
   $$
   \left.\frac{\partial S^{(A\cup B)}}{\partial E^{(A)}}\right|_{eq}=\left.\frac{\partial }{\partial E^{(A)}}\left[S^{(A)}(E^{(A)},X^{(A)}_1,...,X^{(A)}_r)+S^{(B)}(E^{(B)},X^{(B)}_1,...,X^{(B)}_r)\right]\right|_{eq}\\
   =\left.\frac{\partial S^{(A)}}{\partial E^{(A)}}\right|_{E^{(A)}_{eq}}
   -\left.\frac{\partial S^{(B)}}{\partial E^{(B)}}\right|_{E-E^{(A)}_{eq}}=0\text{.}
   $$
   Therefore, we find the quantity, $\frac{\partial S}{\partial E}=\frac{1}{T}$, for system $A$ and $B$ must be equal with each other at equilibrium. At this moment, we don't know what is this quantity. But according to previous definition, we know $T^{(A)}=T^{(B)}$ at equilibrium. 
   
   How the energy flows during the process of reaching equilibrium? We know the total entropy of the system at equilibrium is larger than the initial total entropy.
   
   $$
   S^{(A)}(E_{eq}^{(A)})+S^{(B)}(E_{eq}^{(B)})\ge S^{(A)}(E_{in}^{(A)})+S^{(B)}(E_{in}^{(B)})\text{.}
   $$
   We also know that entropy is a concave function, so we have
   
   $$
   S^{(i)}(E_{eq}^{(i)})-S^{(i)}(E_{in}^{(i)}) \le \left.\frac{\partial S}{\partial E}\right|_{E_{in}^{(i)}} \left( E_{eq}^{(i)}-E_{in}^{(i)}\right)\text{.}
   $$
   *We can get above expression by differentiate the definition of concave function with respect to $\alpha$ from both side and set $\alpha=0$ afterwards.*
   
   Insert this relation into the previous inequality under the energy conserving condition, we have
   
   $$
   \left( \left.\frac{\partial S^{(A)}}{\partial E^{(A)}}\right|_{E_{in}^{(A)}}-\left.\frac{\partial S^{(B)}}{\partial E^{(B)}}\right|_{E_{in}^{(B)}}\right)\left( E_{eq}^{(A)}-E_{in}^{(A)}\right)\ge 0\text{.}
   $$
   
   This inequality says the energy flows from $A$ to $B$ if $T^{(A)}_{in}>T^{(B)}_{in}$.
   
   The behavior of $T$ seems to be identical with the temperature defined in thermodynamics! In fact, we can proof that $T$ is proportional with the thermodynamic temperature $\Theta$!
   
   
   
   To show $T\equiv \Theta$, we use the following strategy. One can define the thermodynamic temperature $\Theta$ using the maximal efficiency of a thermal engine between $\Theta_1$ and $\Theta_2$ ($\Theta_1>\Theta_2$). The maximal efficiency is $\eta_{Max}=1-\frac{\Theta_2}{\Theta_1}$.
   
   Consider a heat engine that is in contact between two heat bath with temperature $T_1$ and $T_2$ where $T_1>T_2$. We assume the heat engine can only exchange energy with the environment by doing work. The second law of thermal dynamics suggest
   
   $$
   dE= \delta Q-\delta W=-\delta W\text{.}
   $$
   
   The definition of efficiency is the ratio between the work and the energy flow out from the high temperature reservoir after one cycle. After one cycle, the energy of the reservoir changes from $E_1,E_2$ to $E_1', E_2'$.
   So we have
   
   $$
   \eta=\frac{\delta W}{E_1-E_1'}= \frac{(E_1+E_2)-(E_1'+E_2')}{E_1-E_1'}\text{.}
   $$
   We want to find an expression of $\eta$ using the temperature $T$.
   
   The entropy of the reservoirs after a cycle will increase. So we have
   
   $$
   S^{(1)}(E_1)+S^{(2)}(E_2)\le S^{(1)}(E_1')+S^{(2)}(E_2')\text{.}
   $$
   
   The entropy of the reservoir before and after the cycle can be expressed as
   
   $$
   S^{(i)}(E_i')=S^{(i)}(E_i)+\frac{E_i'-E_i}{T_i}\text{.}
   $$
   
   Insert this relation to the entropy expression of the reservoirs, we have
   
   $$
   \frac{E_1-E_1'}{T_1}\le \frac{E_2-E_2'}{T_2}
   $$
   
   and
   
   $$
   \delta W\le (E_1-E_1')\left(1-\frac{T_2}{T_1}\right)\text{.}
   $$
   
   So we have shown
   
   $$
   \eta_{Max}=1-\frac{T_2}{T_1}\text{.}
   $$
   
   This relation suggest $T\propto \Theta$. The proportionality constant can be fixed by the tri-critical point of water. Therefore, we conclude $T\equiv \Theta$.
   
   The definition of empirical pressure and chemical potential can be derived in a similar fashion and will be left as an exercise.
   
2. Thermally conductive and mobile wall ( the definition of empirical pressure ) 
   
3. Semipermeable wall ( the definition of empirical chemical potential ) 

## The fundamental equation ( Entropy scheme and energy scheme)

The fundamental equation can be described according to two different schemes

1. Entropy scheme : The corresponding variation principle is to **maximize** the entropy of the system under the given constraints.
2. Energy scheme : The corresponding variation principle is to **minimze** the energy of the system under the given constraints.

Need a figure for it.

## The Lagendre transform (Expressing the function by its tangent)

Suppose we have a function with two variables $f(x,\xi)$ and we want to express the function using the slope of $f$ along $x$, *i.e.* we want to describe our function using $p=\left.\frac{\partial f}{\partial x}\right|_{\xi}$.

Let's try to imagine how to do that. We can formally express $p$ as

$$
p=\left.\frac{\partial f}{\partial x}\right|_{\xi}\equiv g(x,\xi)\text{.}
$$

Invert this equation, we have $x=\tilde{g}(p,\xi)$. It is tempting that we insert this expression back to the expression $f(x,\xi)$ to have

$$
f(\tilde{g}(x,\xi),\xi)=\phi(p,\xi)\text{.}
$$

The expression is almost right. However, if we think a little bit harder, we will find it is unlikely that we can express a function only via its slope. The reason is simple, we could have two functions with identical first derivative simply by having a constant shift. Therefore, we need a little bit more information other than the slope. If we consider $F(x,\xi)=f(x+\psi(\xi),\xi)$, and follow the previous procedure, we will get identical expression of $\phi(p,\xi)$.

It turns out, the information we need is simply the tangent of the function. 
For the single variable function, we have the expression of the tangent as

$$
y=f(x)-x\frac{\partial f}{\partial x}\text{.}
$$

In analogy, we have

$$
\phi(p,\xi)=f(\tilde{g}(p,\xi),\xi)-\tilde{g}(p,\xi)p\text{.}
$$

This is the meaning of Lagendre transformation.

## Thermodynamic potentials

We are interested to discuss the equilibrium configuration of our system under different circumstances. The first question is: in equilibrium with what? Usually, we have our system interact with a reservoir described by a fixed intensive variable. 

For example, we can have our system to be in thermal contact with a heat bath with fixed temperature $T$ which is the slope of the energy $E$ as a function of entropy. Initially, we might describe our system according to the energy scheme. If we want to use this scheme to discuss our system, we need to deal with the fact that entropy is not really fixed during the process of reaching equilibrium. In this case, it is reasonable to change the description of our system using the temperature $T$ instead of using $S$. From the discussion of the last section, we know we can use Lagendre transformation to achieve our goal. The corresponding description is the Helmholtz free energy.

$$
F(T,X)=E(S(T,X),X)-T S(T,X)\text{.}
$$

One can derive the corresponding variational principle of the Helmholtz free energy.



## Thermodynamic stability

The key idea is simple, we ask how the system response when the intensive variables are not homogeneous. If the system try to even out the inhomogeneity, the system is stable. On the other hand, if the system's response make the inhomogeneity more and more serious, the system will not reach equilibrium and will collapse.
