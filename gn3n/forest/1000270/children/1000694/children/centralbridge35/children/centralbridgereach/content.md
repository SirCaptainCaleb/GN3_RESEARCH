# Every deletion state reaches its canonical central bridge in two Astra moves

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover, with P=(p0,...,pm), Q=(q0,...,qs). Regard P|Q|(x) as a spanning three-cover. The canonical bridge state of centralbridge35 lies in the same Astra-003 component and is reached in exactly two explicit pairwise repartitions. If (pm,x,q0) is tight, first repartition Q|(x) as (x,q0)|Q+ and then repartition P|(x,q0) as P-|(pm,x,q0). If (pm,x,q0) is non-tight, first repartition Q|(x) as (q1,q0,x)|Q++ and then repartition P|(q1,q0,x) as P--|(q1,q0,x,pm,p_{m-1}). In particular the 5-bridge route passes through a spanning three-cover with a three-vertex component after one move.

## Body

Let

H-x=P|Q

be an exact deletion two-cover in a minimum counterexample, with

P=(p_0,...,p_m),
Q=(q_0,...,q_s).

By the minimum-counterexample deletion-cover bound, both components have order at least three, so all tails used below are nonempty.

Start from the spanning three-cover

P | Q | (x).

The two outer join triples

(p_{m-1},p_m,x)
and
(x,q_0,q_1)

are non-tight, since either would absorb x into one deletion-cover component and give a spanning two-cover with the other component. Hence

(x,p_m,p_{m-1})
and
(q_1,q_0,x)

are tight by boundary antisymmetry.

We treat the middle join.

## Case 1: (p_m,x,q_0) is tight

First repartition the pair Q|(x). Its union has the exact two-cover

(x,q_0) | Q^+,

where

Q^+=(q_1,...,q_s).

The two-vertex component is automatically a tight path, and Q^+ is an inherited contiguous subpath. Thus

P | (x,q_0) | Q^+

is reached by one legal Astra move.

Now repartition P|(x,q_0). Their union has the exact two-cover

P^- | C,

where

P^-=(p_0,...,p_{m-1})
and
C=(p_m,x,q_0).

The path P^- is inherited and C is tight by the case assumption. Hence the second legal move reaches

P^- | (p_m,x,q_0) | Q^+,

which is exactly the order-three canonical bridge state of centralbridge35.

## Case 2: (p_m,x,q_0) is non-tight

Boundary antisymmetry gives

(q_0,x,p_m)

tight.

First repartition Q|(x). Since the already forced triple

(q_1,q_0,x)

is tight, their union has the exact two-cover

T_Q | Q^{++},

where

T_Q=(q_1,q_0,x)
and
Q^{++}=(q_2,...,q_s).

Thus one legal move gives

P | T_Q | Q^{++}.

In particular, already after one move the component contains a spanning three-cover with a three-vertex component.

Now repartition P|T_Q. Their union has the exact two-cover

P^{--} | C,

where

P^{--}=(p_0,...,p_{m-2})

and

C=(q_1,q_0,x,p_m,p_{m-1}).

The path P^{--} is inherited. The three consecutive triples of C are

(q_1,q_0,x),
(q_0,x,p_m),
(x,p_m,p_{m-1}),

all of which are tight by the forced outer reversals and the middle-case reversal. Hence C is a tight five-path.

The second legal move therefore reaches

P^{--} | (q_1,q_0,x,p_m,p_{m-1}) | Q^{++},

the canonical order-five bridge state of centralbridge35.

Thus in both middle orientations the canonical bridge is not merely an existential spanning cover: it lies within Astra distance two of the original deletion state.

Equivalently, every exact deletion state and its canonical bounded cross-component bridge belong to the same Astra connected component. Moreover the five-bridge branch factors through an explicit order-three state after its first move.
