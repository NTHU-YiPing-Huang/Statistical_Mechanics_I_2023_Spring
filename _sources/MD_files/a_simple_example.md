# A simple example

Let's start from the ideal gas model and comparing the deterministic approach and the statistical approach explicitly.

## Deterministic approach

To describe the system in a deterministic fashion, we need to specify the initial condition and the equation of motion.

To specify the initial configuration of the system of $N$ particles. We need to specify the case with one particle first. We know we need a three component position vector, $\textbf{R}$, and a three component velocity vector, $\textbf{V}$, to describe the initial condition for a single particle. When we have $N$ particles, we will need $N$ such vectors for the position and $N$ such vectors for the velocity. That is, the initial condition of the system is specified by $\{\textbf{r},\textbf{v}\}\equiv\{\textbf{R}_1,\cdots,\textbf{R}_N;\textbf{V}_1,\cdots,\textbf{V}_N\}$. Here $\textbf{r}$ and $\textbf{v}$ are vectors of length $3N$.

With the initial condition specified by $\{\textbf{r},\textbf{v}\}$, we still need to construct the equation of motion. In general, they are described by

$$
\sum_{i\neq j}\textbf{F}_{ij}=m_j \frac{\partial^2}{\partial t^2} \textbf{R}_j\text{ for the $j$-th particle.}
$$

In practice, we usually do not have the detailed information of the system with $N\sim \mathcal{O}(10^{23})$. Also, the coupled equation of motion is very complicated. Even if we manage to have the solution, it is impossible to make sense out of this complicated deterministic result.

## Statistical description

Now we understand the challenge from the deterministic approach. We known we have a huge space that describes the possible initial condition of our macroscopic system. Are all the initial condition equivalent? Suppose we have a $1m^3$ box, it is possible that we have a "homogeneous" distribution of or particle as our initial condition. The initial condition that all the particles are concentrated at the top left corner of $1cm^3$ volume of our box is also valid. However, from the intuition, we know it is more likely that the gas molecules will distribute evenly, instead of choosing to sit at one corner. 

This intuition motivates us to make some postulation about the initial conditions. Following is the Maxwell's postulates:

1. $\{\textbf{R}_i,\textbf{V}_i\}$ and $\{\textbf{R}_j,\textbf{V}_j\}$ are independent variables for different $i,j$. Let's use $f(\textbf{r},\textbf{v})$ to denote the density of particles in the space at $\textbf{r},\textbf{v}$. The number of particles in this volume is $dN=f(\textbf{r},\textbf{v})d\textbf{r}d\textbf{v}$.
2. $\textbf{r}$ and $\textbf{v}$ are independent variables. So we expect $f(\textbf{r},\textbf{v})=f_r(\textbf{r})f_v(\textbf{v})$.
3. The density is unifor in the space. So we know $f_r(\textbf{r})=N/V$.
4. The velocity components, the $x,y,z$ components, are mutually independent. So we have $f_v(\textbf{v}=f_x(v_x)f_y(v_y)f_z(v_z)$
5. The distribution of the velocity only depends on the magnitude of the velocity. That is, $f_v(\textbf{v})=f_v(|\textbf{v}|)=f_v((v_x^2+v_y^2+v_z^2)^{\frac{1}{2}})$.

From 4 and 5, we have

$$
\ln f_v(\textbf{v})=\ln f_v((v_x^2+v_y^2+v_z^2)^{\frac{1}{2}})= \ln f_x(v_x)+\ln f_y(v_y)+\ln f_z(v_z)\text{.}
$$

Since the system is isotropic, there is no reason that $f_x(u), f_y(u), f_z(u)$ has different expression, we can simply assume $f_x(u), f_y(u), f_z(u)=g(u)$. Similar argument suggests $f_v(u)=g(u)$ also. So we are looking for a functional from of $g(u)$ such that 

$$
\ln\left[ g(v_x)g(v_y)g(v_z)\right]=\ln\left[ g\left( (v_x^2+v_y^2+v_z^2)^{\frac{1}{2}}\right)\right]\text{.}
$$

We can try some form of the $g(u)$. Say $g(u)\propto u^m$, $g(u)\propto e^{B u}$, ... After some trial functions, we can convince ourselves that the function $g(u)\propto e^{-\lambda u^2}$ with $\lambda>0$. ($\lambda>0$ since it should be a distribution function that is normalizable).

Once we figure out the form of the density function, we know the normalization condition is

$$
N=\int f(\textbf{r},\textbf{v})d\textbf{r}d\textbf{v}=\int f_r(\textbf{r})d\textbf{r}\int f_x(v_x)f_y(v_y)f_z(v_z) dv_xdv_ydv_z\text{.}
$$

So we have the normalization condition

$$
\int du g(u)=1\text{.}
$$

Performing the Gaussian integral, we have $g(u)=\sqrt{\frac{\lambda}{\pi}}\exp[-\lambda u^2]$.

At this point, we don't know what is $\lambda$. But we can already evaluate the expectation value, $\langle v^2\rangle=\langle v_x^2+v_y^2+v_z^2\rangle=3\int v_x^2 g(v_x)dv_x=\frac{3}{2\lambda}$.

To figure out the expression of $\lambda$ using the microscopic modeling, we can consider the ideal gas equation $PV=Nk_BT$ and the microscopic expression of the concept of pressure, $P$.

Consider the surface expand in the $y-z$ plan, the particles collide with the container without energy lost, so we have the momentum transfer to be

$$
\Delta P=\underbrace{\int_0^\infty dv_x f_x(v_x)}_{v_x>0 \text{ particles collide with the right wall} }\underbrace{\rho S v_x\Delta t}_{\text{number of collision in time }\Delta t} \underbrace{(-2mv_x)}_{\text{momentum transfer per particle}}\\ \times \int_{-\infty}^{\infty} dv_y\int_{-\infty}^{\infty} dv_z f_y(v_y)f_z(v_z)
$$

We also know the magnitude of pressure is defined as

$$
P=\frac{|F|}{S}=\frac{|\Delta P|}{S\Delta t}=\rho m \langle v_x^2 \rangle=\frac{\rho m}{2\lambda}=\rho k_BT\text{.}
$$

So we have $\lambda=\frac{m}{2k_BT}$.

## What do we achieve?

Let's review what we have done here.

1. We assume the initial condition satisfy some statistical properties. Here, it is the statistical independence between particles, statistical independence between $\textbf{r},\textbf{v}$ and the statistical independence of the projection of $\textbf{r},\textbf{v}$  on the $x,y,z$ axes.
2. We then can argue the form of the distribution function with $\lambda$ undetermined.
3. We use the microscopic picture and the ideal gas equation $PV=Nk_BT$ to derive the expression of $\lambda$.
4. Then we find the corresponding distribution function.

However, it is not clear that this distribution function is compatible with the deterministic approach. That is, even if we assume the initial condition satisfied this distribution function, it does not mean the distribution function will be satisfied for arbitrary time after we evolve the particles using the deterministic equation of motion! 

To rationalize this picture, we postulate that the statistical independence assumption captures the most relevant initial conditions. Even if the deterministic evolution of the system might drive the system outside of this statistical independence assumption, the chance that the system evolved into such status is small and measure zero when the system is at the macroscopic scale.

So one can imagine that if we start from this particular distribution function as our initial condition. As the system evolved in a deterministic way, we expect the distribution function to fluctuates in time. The statistical independence picture we derived previously suggest the fluctuation to be estimated by the relative standard deviation we discussed in the random walk section. At the limit $N\to\infty$, our distribution function will play dominant role and will be a very good approximation for our system. This is the spirit of the statistical description.
