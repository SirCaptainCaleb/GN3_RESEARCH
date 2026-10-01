# Opposite endpoint deletion covers of a longest path always expose disagreement

## Statement

Let H be a minimum counterexample and A=(a_0,...,a_{lambda-1}) a globally longest tight path. For arbitrary exact two-covers of H-a_0 and H-a_{lambda-1}, the two endpoint probes necessarily expose explicit support or order disagreement: a surviving A-order reversal, an A-edge-reversing tight triple, a support-partition crossing on the common two-end deletion, a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle. In particular no multiple-crossing endpoint state is a neutral branch, at any deletion slack sigma.

## Body

# Opposite endpoint deletion covers of a longest path always expose disagreement

Let (H) be a minimum-order counterexample to the two-cover conjecture, and let
[
A=(a_0,ldots,a_{lambda-1})
]
be a globally longest tight path. Choose arbitrary exact two-path covers
[
G_0quad	ext{of }H-a_0,qquad
G_1quad	ext{of }H-a_{lambda-1}.
]

We prove that the two endpoint probes necessarily expose support or order disagreement.

If, in either cover, two surviving vertices of (A) lying in one component occur in a different relative order from (A), then the path-intersection calculus already gives the usual reversed common edge, reversing tight triple, or vertex-simple tight cycle. Thus assume that every component of both covers preserves the relative order of its (A)-vertices.

Apply the positional-lag lemma to the component of (G_0) containing (a_{lambda-1}). If the lemma produces a tight triple reversing an ordered edge of (A), we are done. Otherwise (a_{lambda-1}) is the terminal vertex of that component: if the component has order (s), the lemma gives
[
pge (lambda-1)-(lambda-s)=s-1,
]
while necessarily (ple s-1).

Similarly, apply the lemma to the component of (G_1) containing (a_0). Again, a reversing triple finishes the proof; otherwise the position bound gives (ple0), so (a_0) is the initial vertex of its component.

Now use the endpoint-state trichotomy on the deletion state (G_0), with omitted vertex
[
x=a_0
]
and component endpoint
[
y=a_{lambda-1}.
]
For the comparison cover of (H-y), choose (G_1).

The internal-restoration branch is impossible, because (x=a_0) is an endpoint of its component in (G_1).

Suppose the clean omission-swap branch held. Delete (y) from (G_0), obtaining the inherited exact two-cover (T) of (H-{x,y}). Since (y) is terminal in (G_0), restoring (y) recovers (G_0) at the terminal end of its component. A clean swap requires restoring (x) in (G_1) at the same end of the same ordered component of (T). Hence (x) would be terminal in (G_1). But (x=a_0) is initial there. Every component of a one-vertex deletion cover in a minimum counterexample has order at least three, so its initial and terminal vertices are distinct. This is a contradiction.

Therefore the bridge-disagreement branch of the endpoint-state trichotomy is forced. After deleting (a_{lambda-1}) from (G_0) and (a_0) from (G_1), the resulting exact two-covers of
[
H-{a_0,a_{lambda-1}}
]
differ as ordered covers. The exact-cover disagreement theorem consequently yields either a support-partition crossing or, on a common support, a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Thus arbitrary exact covers of the two endpoint deletions of a globally longest path in a minimum counterexample always expose explicit support or order disagreement. No crossing-multiplicity branch can remain neutral.