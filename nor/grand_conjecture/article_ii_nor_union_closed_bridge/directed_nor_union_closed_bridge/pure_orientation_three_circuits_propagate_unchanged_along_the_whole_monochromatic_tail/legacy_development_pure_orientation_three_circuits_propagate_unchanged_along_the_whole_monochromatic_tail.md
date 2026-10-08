# Pure-orientation three-circuits propagate unchanged along the whole monochromatic tail — preserved pre-item development

## Development


## Pure-orientation three-circuits propagate unchanged along the whole monochromatic tail

Work in the pure-orientation sector h=alpha.

Let

P=(f_1,...,f_m)

be a sigma-monochromatic path in a counterexample, and assume its entire omitted set is

U={a,b,c}.

Suppose U is a tau-front circuit at (f_1,f_2), tau=1-sigma, with directed pair cycle

a -> b -> c -> a,

so

alpha(a,b,f_1)=alpha(b,c,f_1)=alpha(c,a,f_1)=tau,

and

alpha(u,f_1,f_2)=tau

for every u in U.

### Step 1: all three vertices remain blocked at the shifted tail

Fix z in U and let x->y->z be the two preceding vertices in the circuit cycle.

Consider the spanning order

(x,y,f_1,z,f_2,f_3,...,f_m).

Its first three statuses are

alpha(x,y,f_1)=tau,

alpha(y,f_1,z)=sigma,

alpha(f_1,z,f_2)=sigma.

Indeed y->z gives alpha(y,z,f_1)=tau, so swapping z with f_1 gives alpha(y,f_1,z)=sigma; and alpha(z,f_1,f_2)=tau similarly gives alpha(f_1,z,f_2)=sigma.

If

alpha(z,f_2,f_3)=sigma,

then every later status is sigma because P is sigma-monochromatic. The displayed spanning order would have word

tau, sigma, sigma, sigma, ...,

with one change, contradiction.

Hence

alpha(z,f_2,f_3)=tau

for every z in U.

So every singleton remains tau-feasible at the shifted tail (f_2,f_3).

### Step 2: any cycle-edge flip closes the counterexample

Take a cycle edge y->z at pivot f_1, so alpha(y,z,f_1)=tau.

Suppose this edge flips at the next pivot:

alpha(y,z,f_2)=sigma.

Then by reversal on the first two coordinates,

alpha(z,y,f_2)=tau.

Let x be the third circuit vertex. Since (x,z,y) is a reverse cyclic ordering of U,

alpha(x,z,y)=tau.

Together with Step 1,

alpha(y,f_2,f_3)=tau.

Therefore

(x,z,y,f_2,f_3,...,f_m)

is a tau-tight prefix followed by the sigma-monochromatic suffix of P. It is spanning and has at most one change, contradiction.

Thus no cycle edge may flip.

Hence

alpha(a,b,f_2)=alpha(b,c,f_2)=alpha(c,a,f_2)=tau.

The same directed 3-cycle is present at pivot f_2, and the reverse edges have color sigma.

### Step 3: the full circuit shifts

At the shifted tail (f_2,f_3):

- all three singletons are tau-feasible by Step 1;
- the three cycle-oriented pairs are tau-feasible by Step 2;
- no ordering of all three vertices is tau-tight.

For the last point, an internal triple on U has color tau exactly in a reverse-cyclic ordering. Its final ordered pair is then a reverse edge of the circuit, which has color sigma at pivot f_2. Hence every three-vertex ordering fails.

So U is again a tau-front circuit at (f_2,f_3), with the same directed pair cycle.

### Induction

Repeat the argument along the sigma-monochromatic path.

For every j=1,...,m-1, U is a tau-front circuit at the consecutive tail pair

(f_j,f_{j+1}),

and the pair-feasibility tournament on U is the same directed cycle

a -> b -> c -> a.

Equivalently, the fully-curved tetrahedron carried by U and the current first tail coordinate propagates unchanged along the entire monochromatic carrier.

### Interpretation

A pure-orientation size-three whole-front obstruction is therefore a curvature tube, not a local accident. Partial transport is impossible: any edge flip gives a spanning one-change order.

This is exactly the kind of rigid connected object suggested by the Connector viewpoint. The remaining task is to collide this forward tube with the rear/reversed-pole circuit structure; if those impose incompatible cycle orientation, the size-three bipolar branch closes.

The hypothesis that U is the entire omitted set is essential in Steps 1 and 2, because the constructed witness must be spanning to contradict counterexamplehood.
