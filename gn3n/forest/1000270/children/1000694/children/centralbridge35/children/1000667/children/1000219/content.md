# Every deletion singleton state has a two-move canonical quadratic descent

## Statement

Let H be a minimum counterexample of order n and H-x=P|Q an exact deletion two-cover, with p=|P| and q=|Q|. The singleton lift P|Q|{x} reaches the canonical central-bridge state of centralbridge35 by two legal Astra-003 moves. If the bridge has order 3, Phi decreases by 2n-12. If it has order 5, Phi decreases by 4n-36. Hence for every minimum counterexample (in particular n>10), every deletion singleton state has an explicit strict two-move quadratic descent.

## Body

# Canonical central bridges are explicit two-move quadratic descents

Let H be a minimum counterexample and let

H-x=P|Q,

where P=(p_0,...,p_m), Q=(q_0,...,q_s), and write p=|P|, q=|Q|. Consider the spanning singleton lift

C_0=P|Q|{x}.

We show that the canonical central-bridge state from centralbridge35 is reached from C_0 in two legal pairwise-repartition moves, and compute the quadratic potential drop.

## Case 1: the middle join is tight

Assume (p_m,x,q_0) is tight. Boundary obstruction at the left end of Q gives no special requirement for the first move: the two-set {x,q_0} is itself a tight path, and Q^+=(q_1,...,q_s) is an inherited tight suffix. Therefore the pair Q|{x} may be repartitioned as

(x,q_0) | Q^+.

This gives

C_1=P | (x,q_0) | Q^+.

Now repartition the pair P|(x,q_0). The inherited prefix

P^-=(p_0,...,p_{m-1})

is tight, and by hypothesis

(p_m,x,q_0)

is a tight three-path. These two paths are disjoint and cover V(P) union {x,q_0}. Hence the second legal move gives

C_2=P^- | (p_m,x,q_0) | Q^+,

which is exactly the order-3 canonical bridge state.

The singleton state has

Phi(C_0)=p^2+q^2+1.

The bridge state has component orders p-1, q-1, 3, so

Phi(C_2)=(p-1)^2+(q-1)^2+9.

Since p+q=n-1,

Phi(C_0)-Phi(C_2)
=2(p+q)-10
=2n-12.

Thus the descent is strict for n>6.

## Case 2: the middle join is non-tight

Assume (p_m,x,q_0) is non-tight. The forced outer reversal gives

(q_1,q_0,x)

tight. Hence Q|{x} may first be repartitioned as

(q_1,q_0,x) | Q^{++},

where Q^{++}=(q_2,...,q_s). Thus

C_1'=P | (q_1,q_0,x) | Q^{++}.

By centralbridge35, the five-path

(q_1,q_0,x,p_m,p_{m-1})

is tight. The inherited prefix

P^{--}=(p_0,...,p_{m-2})

is also tight. Therefore the pair P|(q_1,q_0,x) can be repartitioned as

P^{--} | (q_1,q_0,x,p_m,p_{m-1}),

producing exactly the order-5 canonical bridge state

C_2'=P^{--} | (q_1,q_0,x,p_m,p_{m-1}) | Q^{++}.

Its component orders are p-2, q-2, 5, so

Phi(C_2')=(p-2)^2+(q-2)^2+25.

Hence

Phi(C_0)-Phi(C_2')
=4(p+q)-32
=4n-36.

Thus the descent is strict for n>9.

Every minimum counterexample relevant to the current project has order greater than ten, so in either branch the canonical bridge gives a strict quadratic descent from the deletion singleton lift.

Therefore no deletion singleton state can be quadratic-minimal in its trapped Astra component, and the descent is not merely existential: it is realized by a fixed two-move segment whose endpoint is the canonical bounded 3- or 5-bridge state.
