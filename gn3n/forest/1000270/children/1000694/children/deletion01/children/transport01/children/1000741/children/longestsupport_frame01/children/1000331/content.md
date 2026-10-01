# Longest-path complements force synchronized crossing, pervasive mixing, and a rigid two-crossing geometry

## Statement


Let H be a minimum counterexample, let A be a globally longest tight path of order lambda, and put U=V(H)-V(A). Define D={u in U: H[U-u] is Hamiltonian}. Then for u in D the cover A|(U-u) is exact, and any exact cover of H-a with a in A is support-compatible with at most one such fixed-A cover. Hence |D|>=3 forces one fixed-A deletion state to be support-crossed by chosen deletion covers at both ends of A, while |D|<=2 forces every exact cover of H-u to mix the cut A|(U-u) for every u in U-D. More generally, whenever C=U-u is non-Hamiltonian, every exact cover of H-u has at least two ordinary crossing edges across A|C. If exactly two crossings occur, cutting them yields two A-blocks and two C-blocks; either the cover is crosswise, or its unique non-crosswise shape is C_1-A_1-C_2 together with the remaining A-block, with |A_1|<=2lambda-|V(H)|+1. Thus in the sharp half-order shell |V(H)|=2lambda+1 only the crosswise shape occurs.


## Body


# Longest-path complements force synchronized crossing, pervasive mixing, and a rigid two-crossing geometry

Let H be a minimum counterexample, let
A=(a_0,...,a_{lambda-1})
be a globally longest tight path, and put
U=V(H)-V(A).
Minimum-counterexample calculus gives that U is non-Hamiltonian and pc(H[U])=2; in particular |U|>=4.

Define
D={u in U : H[U-u] is Hamiltonian}.

## Fixed-A deletion states and the global dichotomy

For u in D, choose a Hamilton path on U-u. Together with A it gives the two-path cover
F_u=A|(U-u)
of H-u. This cover is exact: if H-u were Hamiltonian, that Hamilton path together with the singleton u would two-cover H.

Fix a in A and any exact two-cover G_a of H-a. Suppose G_a is support-compatible with F_u on H-{a,u}. The common support classes of F_u are U-u and A-a. In G_a, the omitted label u belongs to one of its two path supports. It cannot be adjoined to U-u, because that would Hamiltonize all of U. Therefore it must be adjoined to the other class, and the support partition of G_a is
(U-u) | ((A-a) union {u}),
up to exchanging the two components.

A fixed G_a cannot have this form for two distinct u,v in D: the supports U-u and U-v differ, and U-u cannot equal (A-a) union {v}, since the former lies in U while the latter contains vertices of A. Thus each exact deletion cover H-a is support-compatible with at most one F_u.

If |D|>=3, choose exact covers at the two endpoints a_0 and a_{lambda-1} of A. Each excludes at most one member of the family {F_u:u in D}, so some u in D gives a canonical fixed-A state F_u that is support-incompatible with both endpoint covers. Hence one fixed deletion state is crossed at the support level from both ends of the longest path.

If |D|<=2, then for every u in U-D, the tournament H[U-u] is non-Hamiltonian. No exact cover of H-u can have support partition A|(U-u), because the second support would have to carry a Hamilton path. Therefore every exact cover of H-u mixes the longest-path cut A|(U-u). Thus all but at most two complement labels force mixed deletion covers.

This is the global longest-path dichotomy:
many Hamiltonian deletions of U force synchronized two-end support crossing, while few Hamiltonian deletions force pervasive mixing.

## Every non-Hamiltonian complement deletion is crossed at least twice

Fix u in U such that C=U-u is non-Hamiltonian, and let T be an exact two-cover of H-u. Since A is Hamiltonian,
pc(H[A])=1.
Since C is a proper induced subtournament of the minimum counterexample and is non-Hamiltonian,
pc(H[C])=2.

Let t be the number of ordinary path edges of T crossing the cut A|C. Cutting all t crossing edges produces b_A monochromatic A-blocks and b_C monochromatic C-blocks. The transition-count identity gives
b_A+b_C=t+2,
while b_A>=1 and b_C>=2.

If t=1, then b_A=1 and b_C=2. All vertices of A form one contiguous block of T, and since there is a crossing edge that A-block is joined to a nonempty C-block. The corresponding component is then a tight path containing all lambda vertices of A plus another vertex, contradicting maximality. Hence
t>=2.

## Equality geometry for exactly two crossings

Assume now that T has exactly two crossing edges. Then b_A+b_C=4. Since b_C>=2 and b_A=1 would again put all of A into one block adjacent to a nonempty C-block, we must have
b_A=b_C=2.

Contract the four monochromatic blocks. Because T has two components and two crossing edges, there are only two possibilities.

First, the crossing edges lie in different components. Then each component consists of one A-block and one C-block: the crosswise four-block shape.

Second, both crossing edges lie in one component, so one component has three alternating blocks and the other is the remaining monochromatic block. The pattern
A_1-C_1-A_2
is impossible because it contains both A-blocks, hence all lambda vertices of A, together with nonempty C_1, producing a path longer than lambda.

The only non-crosswise possibility is therefore
C_1-A_1-C_2,
with the other component equal to the remaining A-block A_2. The three-block component contains every vertex of C together with A_1, so maximality gives
|C|+|A_1|<=lambda.
Since
|C|=|V(H)|-lambda-1,
we obtain
|A_1|<=2lambda-|V(H)|+1.

Thus an exact two-crossing cover has only two possible shapes: crosswise, or the single exceptional C-A-C shape controlled by the longest-path slack.

In the sharp half-order shell
|V(H)|=2lambda+1,
the bound becomes |A_1|<=0, impossible for a nonempty block. Hence only the crosswise shape remains.

So a longest path supplies, in one package, a global support-level dichotomy and a local crossing theorem: non-Hamiltonian complement deletions are crossed at least twice, and equality is rigid except for one quantitatively slack-controlled shape.
