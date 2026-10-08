# The pure-orientation size-three curvature tube closes by a five-step weave — preserved pre-item development


## The pure-orientation size-three curvature tube closes by a five-step weave

Work in the pure-orientation sector h=alpha.

Let

P=(f_1,...,f_m)

be a sigma-monochromatic path in a counterexample, and suppose its entire omitted set is

U={a,b,c}.

Assume U is a tau-front circuit at (f_1,f_2), tau=1-sigma, with directed pair cycle

a -> b -> c -> a.

The propagation theorem gives, for every relevant j,

alpha(a,b,f_j)=alpha(b,c,f_j)=alpha(c,a,f_j)=tau,

and

alpha(u,f_j,f_{j+1})=tau

for every u in U.

### Theorem
No such configuration is a counterexample.

### Proof

Consider the spanning order

W=(a,f_1,f_2,b,c,f_3,f_4,...,f_m).

We compute its consecutive ternary statuses.

First,

alpha(a,f_1,f_2)=tau

by singleton blocking at the front.

Second,

alpha(f_1,f_2,b)=tau

because alpha(b,f_1,f_2)=tau and cyclic permutation preserves alpha.

Third,

alpha(f_2,b,c)=tau

because alpha(b,c,f_2)=tau and again cyclic permutation preserves alpha.

Fourth,

alpha(b,c,f_3)=tau

by persistence of the circuit edge b->c at pivot f_3.

Fifth, when f_4 exists,

alpha(c,f_3,f_4)=tau

by singleton persistence along the tube.

Every later status lies wholly in the untouched suffix

(f_3,f_4,...,f_m)

of P and therefore equals sigma.

Hence the status word of W has the form

tau,tau,tau,tau,tau,...,sigma,sigma,...

with at most one change.

For m=3 or m=4 the same displayed order simply truncates before the sigma suffix, so it is monochromatic.

This contradicts counterexamplehood. QED.

### Consequence

A pure alternating ternary counterexample cannot have a maximal monochromatic path whose entire omitted set is a three-element front circuit.

Equivalently, the rigid full-curvature tube

U union {f_1}, U union {f_2}, ..., U union {f_m}

with flat cross walls is not an obstruction: it has an explicit spanning one-change weave.

### Conceptual interpretation

The weave uses the tube geometry exactly once.

- The first two path vertices absorb a;
- the persistent cycle edge b->c is read at the second and third pivots;
- c then hands back to the monochromatic path through the flat wall at (f_3,f_4).

So the tube is not merely topologically connected; it has a canonical connector path through its state flags that yields the required Hamilton chamber explicitly.

This closes the pure-orientation whole-front circuit-size-three branch and turns the next target into either:
1. the size-two whole-front branch;
2. larger circuits and their contraction to size two or three;
3. the defect-bearing general h case, where the same weave must be audited against the marked-vertex defect field.
