# Ergodicity

Here we will introduce an abstract concept-- ergodicity. The idea provides a connection between time-evolution and the statistical description of the system. However, prove a system is ergodic or not is in general difficult. (That's why I skip the discussion during the lecture. For those who are interested in this concept, please check {cite:p}`sethna2021statistical` and the related references.) Therefore, the approach is usually we assume our system is ergodic. Then, we argue the **time average** equals **micro canonical averages**. We will discuss the concept of ergodicity here and the concept of **micro canonical ensemble** later.

In the study of statistical mechanics, we are trying to describe the observables of many-body system under time-evolution using statistical description. The bottleneck that we are trying to pass is how to go from time-evolution to statistics? The Liouville's theorem suggest that understanding the time-evolution in phase space is a good approach as it has the nice properties 3 that we discussed in the last section, *i.e.* it is possible to have a probability density function $\rho$ does not depends on $t$ explicitly. But it does not tell us how to derive the probability density function.

The time average starting at initial condition $\xi(t=0)$ is

$$
\overline{O(t=0)}\equiv \lim_{T\to\infty} \frac{1}{T}\int_{0}^{T} dt O(\xi(t))\text{.}
$$

If $O$ is well behaved, we expect $\overline{O(t=0)}=\overline{O(t=t')}$. That is, the long time average should not depends on the value of $O$ during the time interval $(0,t')$.

$$
\overline{O(t=0)}\equiv \lim_{T\to\infty} \frac{1}{T}\int_{0}^{T} dt O(\xi(t))\\
\overline{O(t=t')}\equiv \lim_{T\to\infty} \frac{1}{T}\int_{t'}^{T} dt O(\xi(t))\text{.}
$$

Therefore, we found the long time averages are constant on trajectories.

Since $\overline{O}$ is constant on trajectories. The microcanonical ensemble average of a constant is still a constant. *i.e.*

$$
\underbrace{\overline{O}=a^*=\langle \overline{O} \rangle}_{\text{long time average is constant}}=\langle  \lim_{T\to\infty} \frac{1}{T}\int_{0}^{T} dt O(\xi(t))\rangle=\lim_{T\to\infty} \frac{1}{T}\int_{0}^{T} dt \langle  O(\xi(t))\rangle=\langle  O \rangle
$$

Because of the nice properties 3 from Liouville's theorem, the micro canonical ensemble  was time independent and the ensemble average equals to the time average.

```{admonition} Note 
:class: tip
The microcanonical ensemble that we are going to discuss later means we average over all apossible phase space configuration with equal weight.

$$
\langle O\rangle\equiv \frac{1}{|\Gamma|}\sum_{\xi\in\Gamma} O(\xi)\text{.}
$$
```

The ergodicity support that

$$
\overline{O}=\langle O\rangle\text{.}
$$

We will discuss the idea of micro canonical ensemble in the next section such that we will establish

$$
\langle O\rangle=O_{eq}\text{.}
$$
