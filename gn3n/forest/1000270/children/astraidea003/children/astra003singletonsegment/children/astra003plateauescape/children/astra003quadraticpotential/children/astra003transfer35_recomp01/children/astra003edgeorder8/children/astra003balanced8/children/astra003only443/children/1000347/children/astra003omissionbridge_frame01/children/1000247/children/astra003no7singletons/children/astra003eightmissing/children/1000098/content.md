# A missing eight-label omission edge forces order disagreement on both local deletion cliques

## Statement

Assume the eight-label missing-edge shell astra003eightmissing for a missing omission edge xy, and fix an x-state P|Q|(x). On each six-set P∪{x} and Q∪{x}, the four good deletion labels are exactly x together with the three labels from S-{x,y} on that side. For arbitrary Hamilton paths chosen on the four corresponding five-deletions, some pair must disagree in relative order on common vertices. Equivalently, each side carries a reversed common edge, reversing tight triple, or vertex-simple tight-cycle witness.

## Body

# Missing omission edges force ordered disagreement

Assume astra003eightmissing for a missing omission edge xy and fix a reachable state P|Q|(x). On the P-side six-set R=P∪{x}, astra003eightmissing identifies the good deletion set exactly as

G(R)={x,a,b,c},

where a,b,c are the three S-{x,y} labels lying on P. The remaining two labels on P are bad deletions.

For each d∈G(R), choose an arbitrary Hamilton path P_d on R-d and combine it with the untouched Hamilton path Q. The certified order-eleven support-compatible deletion-clique theorem says these four exact deletion covers agree on component membership on every common vertex set; any incompatibility is purely relative path order inside R.

Suppose, for contradiction, that no pair has relative-order disagreement. Then the four covers are pairwise fully compatible. Hence every triple of them is a pairwise-compatible deletion triangle. The certified order-eleven triangle theorem says the precedence tournament of the three deleted labels of every such triple is cyclic.

Thus every three-subset of the four-label set {x,a,b,c} would induce a cyclic triangle in one tournament. This is impossible: in any tournament on four vertices, at any fixed vertex at least two of its three incident arcs point the same way, and together with their other endpoints form a transitive triangle.

Therefore some pair among the four deletion paths disagrees in relative order on common vertices. By the certified ordered-path intersection consequence recorded for bad six-sets, this yields at least one of a reversed common ordered edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle inside R.

The same argument applies symmetrically to Q∪{x}. Hence every x-state witnessing a missing omission edge carries an explicit ordered-disagreement witness on both sides. This is the valid residue of the failed astra003eightcomplete argument: support compatibility does not force omission-graph completeness, but failure of order compatibility is unavoidable.
