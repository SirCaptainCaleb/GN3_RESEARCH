# Endpoint compatible triangles enter the cyclic four-kernel frontier

## Statement

Let H be a minimum-order counterexample. Suppose three pairwise-compatible deletion two-covers have a common insertion gap at the left endpoint of one common path. Relabel their deletion labels a,b,c so the necessarily cyclic precedence is a→b→c→a, and write the common path after the gap as R=(r0,...,rk), with the other common path Q. Thus H-a=(b,c,R)|Q, H-b=(c,a,R)|Q, and H-c=(a,b,R)|Q. Then X={a,b,c,r0} is either Hamiltonian or is exactly the exceptional cyclic non-Hamiltonian four-vertex configuration. In the Hamiltonian case pc(H-X)=2 and H-X is non-Hamiltonian. In the cyclic case every fifth vertex extends X Hamiltonianly, and the cyclic-kernel exterior-forcing conclusions apply.

## Body

# Endpoint cyclic triangles enter the four-kernel frontier

Let H be a minimum-order counterexample. Suppose three pairwise-compatible exact deletion two-covers have a common insertion gap at the left endpoint of one common path. By endpoint-gap compatibility geometry their precedence tournament is cyclic. Relabel the deletion labels so

a -> b -> c -> a,

and write the common path after the gap as

R=(r_0,...,r_k),

with R nonempty, and let Q be the unchanged second path. Then the three deletion covers are

H-a = (b,c,R) | Q,
H-b = (c,a,R) | Q,
H-c = (a,b,R) | Q.

Put X={a,b,c,r_0}.

## Claim

Either H[X] is Hamiltonian, or H[X] is exactly the exceptional cyclic non-Hamiltonian four-vertex configuration.

If H[X] is Hamiltonian, then H-X is non-Hamiltonian and pc(H-X)=2.

If H[X] is non-Hamiltonian, then the cyclic-four-kernel extension and exterior-forcing conclusions apply: every X union {d}, d outside X, is Hamiltonian, and more strongly every (X-{u}) union {d,e} with u in X and distinct d,e outside X is Hamiltonian. The corresponding complements in H are non-Hamiltonian exact-two-coverable proper induced subtournaments.

## Proof

The three displayed deletion covers directly give the tight triples

(b,c,r_0), (c,a,r_0), (a,b,r_0).

Apply endpoint hook forcing to the first component of each cover, using the omitted deletion label. From H-a=(b,c,r_0,...)|Q we obtain

(c,b,a), (r_0,a,b).

Likewise H-b and H-c give

(a,c,b), (r_0,b,c)

and

(b,a,c), (r_0,c,a).

Thus nine of the twelve reversal pairs on X are already fixed:

(b,c,r_0), (c,a,r_0), (a,b,r_0),
(c,b,a), (a,c,b), (b,a,c),
(r_0,a,b), (r_0,b,c), (r_0,c,a).

Assume H[X] is non-Hamiltonian. The remaining three reversal pairs all have middle vertex r_0.

If (a,r_0,b) were tight, then

(c,a,r_0,b)

would be a Hamilton path, because (c,a,r_0) is already tight. Hence (b,r_0,a) is tight.

If (c,r_0,a) were tight, then

(b,c,r_0,a)

would be Hamiltonian, because (b,c,r_0) is tight. Hence (a,r_0,c) is tight.

If (b,r_0,c) were tight, then

(a,b,r_0,c)

would be Hamiltonian, because (a,b,r_0) is tight. Hence (c,r_0,b) is tight.

So in the non-Hamiltonian branch the twelve tight representatives are

(a,c,b), (c,b,a), (b,a,c),
(r_0,c,a), (a,r_0,c), (c,a,r_0),
(a,b,r_0), (b,r_0,a), (r_0,a,b),
(r_0,b,c), (c,r_0,b), (b,c,r_0).

Under the relabelling

(A,B,C,Z)=(a,c,b,r_0),

this is exactly the canonical cyclic non-Hamiltonian four-kernel

ABC, BCA, CAB,
ZBA, AZB, BAZ,
ACZ, CZA, ZAC,
ZCB, BZC, CBZ.

This proves the dichotomy.

If X is Hamiltonian and H-X were Hamiltonian, the two Hamilton paths would two-cover H, impossible. Since H-X is proper, minimality gives pc(H-X)<=2, hence pc(H-X)=2.

If X is the cyclic kernel, the small-set cyclic-kernel extension theorem makes X union {d} Hamiltonian for every exterior d, and the stronger cyclic-kernel exterior-forcing theorem makes every (X-{u}) union {d,e} Hamiltonian. In each case a Hamiltonian complement would two-cover H, while minimality makes the proper complement at most two-coverable; hence each such complement is non-Hamiltonian with path-cover number exactly two. ∎

## Role in the frontier

This identifies the endpoint compatible-triangle residue with the same four-set frontier already produced by first-type insertion obstruction: Hamiltonian four-set with exact-two-cover complement, or the universal cyclic four-kernel. It therefore connects common-gap compatibility geometry directly to the existing endpoint-transport kernel machinery.