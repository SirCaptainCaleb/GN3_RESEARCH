# S9020 — Non-Hamiltonian K4 Structure and Overlap Amplification

## Theorem A — minimum-edge mate

Let X={x,y,a,b} induce an edge-ordered K4 with no increasing Hamilton path. If xy is the smallest of the six edges of X, then the opposite edge ab is smaller than each of xa,xb,ya,yb. Hence xy and ab are the two locally smallest edges of X. In the standard transitive matching-height boundary orientation induced by the edge order, the opposite pair {xy,ab} is the top matching level M_R (because a turn is tight when its first edge is earlier).

### Proof

Assume xy is the minimum edge of X. If ya<ab, then (x,y,a,b) has edge-label sequence xy<ya<ab and is an increasing Hamilton path, contradiction. If yb<ab, then (x,y,b,a) is increasing. If xa<ab, then (y,x,a,b) is increasing. If xb<ab, then (y,x,b,a) is increasing. Therefore ab is smaller than all four cross edges xa,xb,ya,yb. Since xy is already the minimum edge, ab is the second-smallest edge of the induced K4.

## Theorem B — shared-triangle amplification

Let G be an edge-ordered complete graph and let T={u0,u1,u2} be a three-vertex set. Let x,y be distinct vertices outside T. If both induced edge orders on T∪{x} and T∪{y} have no increasing Hamilton path, then G[T∪{x,y}] has an increasing Hamilton path.

### Proof

First note the elementary K4 classification. Let the six edges of an edge-ordered K4 be e1<e2<...<e6. If e1 and e2 shared a vertex, say e1=ab and e2=bc, then with d the fourth vertex the edge cd occurs after e2, so a-b-c-d would be an increasing Hamilton path. Hence e1,e2 are disjoint. Dually e5,e6 are disjoint. Therefore {e1,e2} and {e5,e6} are two opposite perfect matchings, and the remaining {e3,e4} is the third opposite perfect matching. Thus every non-Hamiltonian edge-ordered K4 has its three opposite matchings in strict height blocks.

Now suppose T={u0,u1,u2} and both T+x and T+y are non-Hamiltonian. Relabel T so u1u2<u0u2<u0u1. In the K4 T+r, r∈{x,y}, the opposite matching containing u1u2 is {u1u2,ru0}, the one containing u0u2 is {u0u2,ru1}, and the one containing u0u1 is {u0u1,ru2}. Since the three internal T edges occur in the displayed low/middle/high order, the matching-height classification forces ru0<ru1<ru2 for r=x,y. Compare xu1 and yu1. If xu1<yu1, then the path u0,x,u1,y,u2 has edge labels u0x<xu1<yu1<yu2 and is increasing. If yu1<xu1, then u0,y,u1,x,u2 is increasing. Thus T∪{x,y} has an increasing Hamilton path.

## Why this is reusable

The first theorem normalizes every non-Hamiltonian edge-ordered K4 into matching-height blocks and, when a minimum edge is named, identifies its opposite mate. The second shows that two such P4-free cells sharing a triangle cannot coexist without creating an increasing Hamilton P5 on their union.

## Scope and nonclaims

These are purely local edge-order theorems. They do not assert that a Hamilton P5 extends to a global path cover.

## Provenance

Rescued from accepted archived results `R1008`, `R963`.
