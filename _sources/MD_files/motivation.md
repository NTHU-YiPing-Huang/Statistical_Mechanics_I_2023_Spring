# Motivation: Why learn statistical mechanics?

## The large number of degrees of freedom

The above process, developing a microscopic model, making macroscopic predictions, and comparing with experiments, seems identical for all scientific research areas. What is so special about statistical mechanics? The key feature is: statistical mechanics deals with a **macroscopic number** of degrees of freedom. What we meant by macroscopic number is a number of order $N\approx 10^{23}$. Because this number is *huge*, we are allowed to use statistics and make statistical statements that can help us to make some predictions.

That is, the system we are studying has a *big* parameter, $N\approx 10^{23}$, and we want to analyze it. It seems the problem is getting so complicated that it is hopeless to understand. Let's take classical coins as an example. A classical coin has $2$ possibilities, head or tail. For $N$ coins, we have $2^N\approx 2^{10^{23}}$ possible outcomes to keep track with. How is it possible?
However, if we think the opposite way, our problem has a natural *small* parameter, $N^{-1}$. If we can use this small parameter wisely, we might be able to use it to simplify our analysis.

Basically, that's the spirit of statistical mechanics.

```{admonition} What?
:class: tip
In the coin example, suppose we toss our coin $M$ times. We will get a final result represented by a binary string with $M$ bits. When $M$ gets bigger and bigger, what statistical quantity will become smaller and smaller?
```

## Emergent phenomena

In the previous discussion, we described how statistical mechanics is developed initially. It is developed to complete our understanding of thermodynamics. However, after it was developed, people found this concept very powerful and could be applied to various circumstances. It is useful, in general, when the number of degrees of freedom is huge.

From this point of view, learning statistical mechanics by connecting with thermodynamics is just a tool or a process to rationalize an idea: when the number of degrees of freedom is huge, it is possible that another relative tiny set of observables can describe the macroscopic properties. Those observables are related to each other in certain ways that are not obvious how they are related to microscopic physics. One might be able to find those observables and their relations using approaches that similar to statistical mechanics.

This is the idea of emergent phenomena. However, the detailed definition of emergence is beyond the scope of this course. So I will list some references and use simple examples to describe the idea. [Here is one reference by S. Kivelson](https://www.nature.com/articles/npjquantmats201624)

Let's take a group of people as an example. Suppose we have $10\times M$ people. They interact in some fashion. In system A, we have $M$ basketball games. In system B, we run an election for the president of a fictitious country. Let's assume $M$ is a large number. 

To understand the behavior of our system A. It is quite simple; we know they are playing basketball games. Once we know the rules of a basketball game, system A will be described accurately by the rule of basketball games. We might have different scores and rebound numbers for each player, but we understand it more or less. They are just basketball games. No emergent phenomena.

To understand the behavior of system B. It is much more challenging. The citizens in system B will exchange their opinion with each other.
They could exchange views with their families and colleagues. People could form unions or parties to collaborate or compete on different issues, etc. The collective behavior could be highly non-trivial. This is an example of emergent phenomena.
[Here is a reference for the voters model.](https://physics.aps.org/articles/v7/40?ory/science/science-news/)

The idea of statistical mechanics starts from developing a microscopic understanding of thermodynamics. However, it did not end there, and the developments of effective theory and emergent phenomena took off and got their own life in the scientific research.



