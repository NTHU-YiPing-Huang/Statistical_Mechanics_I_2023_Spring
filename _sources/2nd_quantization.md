# Second quantization

## Qualitative difference between non-interacting quantum many-particle system and the interacting many-body system

To deal with quantum many-body systems, it is important to keep the structure of its quantum statistics. *i.e.* whether the system is formed by fermions or bosons. In the previous section, we work in the basis that forming the partition function and related calculations are almost trivial. 

The reason that the related calculation is trivial is because we work in the eigen basis of the system. However, it is usually very challenging to get the eigen basis for the many-body quantum systems. Let's try to understand the qualitative difference between the non-interacting many-particle systems and the interacting many-body systems.

We can start from the simplest quantum system: a system formed by quantum bits (two-level system). The dimension of the Hilbert space for a quantum bit is 2. This is the simplest non-trivial case where we can have the non-trivial structure due to the superposition principle. (If there is only one basis in the space, we cannot show the superposition structure). Let's use $\mathcal{H}_b$ to represent the Hilbert space of the quantum bit. To be more specific, we can assign the two basis in the Hilbert space to be $\left\{ |\uparrow\rangle,|\downarrow\rangle \right\}$. The most general state in this space is given by $c_{\uparrow}|\uparrow\rangle+c_{\downarrow}|\downarrow\rangle$.

Now, let's consider the non-interacting quantum many-particle system. In our simple example above, we have lots of quantum bits that does not talk with each other. So to understand the system, essentially all we need to do is to understand what a single quantum bit is doing. So even though we have many particles (in this case, many quantum bits), the problem is essentially a one-body problem. So the eigen specturm of the system is simple, all we need to do is to diagonalize the $2\times2$ matrix. The full spectrum will simple accumulation of the 2 eigne energies for the $2\times2$ Hamiltonian.

Next, we can try to see what happened if we start to couple the quantum bits. When the quantum bits start to talk with each other, the system will be described by a state in the Hilbert space formed by the tensor product of individual Hilbert space for each quantum bit. That is, $\mathcal{H}=\otimes_{j=1}^{N_s}\mathcal{H}_{b,j}$. This is a space that the dimensionality grows exponentially as a function of the system size (in this case, the number of quantum bits, $N_s$).

Now we can see the qualitative difference. In the non-interacting case, we need to diagonalize a $2\times 2$ matrix. We know how to do that. For the interacting case, we need to diagonalize a $2^{N_s}\times 2^{N_s}$ matrix. Which you can try to run that on your computer by choosing $N_s=10,20,40$. Usual desktop can get the full spectrum of the $N_s=10$ case easily, $N_s=20$ and $N_s=40$ case is beyond the ability for the usual desktop. That's why we call such problem a *many-body* problem, because we need to consider the system as a whole and cannot factorize our system and reduce the problem to a one-body problem.

Of course, we are not going to stop there. We will try to see if we can still make some progress to understand the many-body problem. Now we have several choices:

* Start from the non-interacting limit and try to develop some kind of perturbation theory.
* Using some non-perturbative methods, such as mean-field theory or variational method to get the relevant states of our problem. We will introduce the idea of mean field theory which is a versatile method for interacting problem. 
 
Here, we will introduce a notation, *second quantization*, which is convenient to develop a perturbation analysis for the quantum many-body system. We have learned the single particle perturbation theory in quantum mechanics. The challenge here is how to develop the corresponding theory when we consider the quantum statistics(fermions or bosons) of our problem. To do that, we need to find a convenient representation for the many-body wave function and the many-body Hamiltonian. That representation is the *second quantization* formulation that we are going to introduce.

## The many-body states and operators in the second quantization representation

