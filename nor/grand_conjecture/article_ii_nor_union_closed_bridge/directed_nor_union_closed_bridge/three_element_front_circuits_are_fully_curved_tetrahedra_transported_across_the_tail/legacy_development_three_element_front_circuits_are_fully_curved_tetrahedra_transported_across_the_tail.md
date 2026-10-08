# Three-element front circuits are fully curved tetrahedra transported across the tail — preserved pre-item development

## Composition

(none yet)

## Development


## Three-element front circuits are fully curved tetrahedra transported across the tail

Work in the pure-orientation sector h=alpha.

Let F=(f_1,f_2) be a fixed tail of color tau, and suppose U={a,b,c} is a three-element front circuit. Orient its pair-feasibility cycle as

a -> b -> c -> a,

meaning

alpha(a,b,f_1)=alpha(b,c,f_1)=alpha(c,a,f_1)=tau,

while

alpha(a,f_1,f_2)
=alpha(b,f_1,f_2)
=alpha(c,f_1,f_2)
=tau.

The established circuit rigidity also gives

alpha(a,b,c)=sigma=1-tau

in the cyclic orientation.

### Proposition 1
The tetrahedron

Q_1={a,b,c,f_1}

is fully curved.

### Proof
Read its four increasing-face signs in the local order a,b,c,f_1. They are

alpha(a,b,c)=sigma,
alpha(a,b,f_1)=tau,
alpha(a,c,f_1)=sigma,
alpha(b,c,f_1)=tau,

because alpha(c,a,f_1)=tau implies alpha(a,c,f_1)=sigma.

Thus the face pattern is

sigma, tau, sigma, tau,

which is exactly the fully-curved pattern A=C != B=D. QED.

Hence a three-element front circuit is not merely analogous to a directed triangle: together with the first tail coordinate it is an actual universal-switch tetrahedron.

### Transport from f_1 to f_2

For each cycle edge, compare its sign at the two pivots. Put

epsilon_ab = 1 iff alpha(a,b,f_2) != alpha(a,b,f_1),

and similarly epsilon_bc, epsilon_ca.

The cross tetrahedron {a,b,f_1,f_2} has the face pattern

tau, alpha(a,b,f_2), tau, tau

in the corresponding local orientation. Therefore it is

- flat exactly when epsilon_ab=0;
- singly curved exactly when epsilon_ab=1.

The same holds for the other two cycle edges.

Thus the three cross tetrahedra are precisely the edge-flip record for transporting the directed cycle from pivot f_1 to pivot f_2.

Let

k=epsilon_ab+epsilon_bc+epsilon_ca.

Then the link tournament at f_2 is obtained from the directed 3-cycle at f_1 by reversing exactly these k edges.

Consequently:

- k=0: the same directed cycle persists at f_2, and Q_2={a,b,c,f_2} is fully curved;
- k=1: the f_2 link is transitive and Q_2 is singly curved;
- k=2: the f_2 link is transitive and Q_2 is flat;
- k=3: the reversed directed cycle occurs at f_2 and Q_2 is singly curved.

The curvature parity identity on the five-set {a,b,c,f_1,f_2} gives the same parity statement:

(delta f)(Q_2) = k mod 2,

since Q_1 is fully curved and hence has zero coboundary parity.

### Interpretation

A size-three front circuit is a fully-curved tetrahedron at the first tail coordinate. Moving one step down the tail transports its three cycle edges across the three cross tetrahedra; singly-curved cross tetrahedra are exactly the flipped edges.

This identifies the insertion/circuit frontier with a discrete curvature-transport problem on one five-face. In particular:

- persistence of the circuit corresponds to k=0;
- complete polarity reversal corresponds to k=3;
- partial transport creates flat/singly-curved escape facets.

This is a concrete local packet on which a Connector argument can act: instead of tracking three unrelated deletion witnesses, track the transport of one fully-curved tetrahedron through successive tail coordinates.
