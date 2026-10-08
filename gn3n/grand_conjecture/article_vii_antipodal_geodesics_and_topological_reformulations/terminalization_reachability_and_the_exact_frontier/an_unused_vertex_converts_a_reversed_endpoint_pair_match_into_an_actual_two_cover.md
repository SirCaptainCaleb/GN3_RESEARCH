# An unused vertex converts a reversed endpoint-pair match into an actual two-cover

## Composition

(none yet)

## Development

## Reversed endpoint pairs give an actual augmentation through an unused vertex

Let P and Q be actual tight paths in a boundary 3-tournament. Suppose
P=(a,b,p_3,...,p_s),
Q=(q_1,...,q_{t-2},b,a),
with a!=b and s,t>=2. Let x be outside V(P) union V(Q).

Exactly one of (x,a,b) and (b,a,x) is tight. In the first case (x,P) is a tight path of order s+1. In the second case (Q,x) is a tight path of order t+1.

Proof. The two tested triples are boundary reverses. Prepending x to P adds just (x,a,b); appending x to Q adds just (b,a,x). Every other triple is inherited from the corresponding actual word, and x is not repeated. QED.

No agreement of the interior orders is assumed. In particular P and Q may come from dissimilar deletion covers and may share many additional vertices.

## Maximum paths exclude reversed endpoint-pair matching at an ambient majority threshold

Suppose the global maximum tight-path order is r>=2 and |V(H)|>=2r-1. An ordered pair (a,b) cannot occur as the initial pair of one maximum path while (b,a) occurs as the terminal pair of another.

Indeed the two r-supports share a and b, so their union has size at most 2r-2. An unused vertex x therefore exists, and the previous lemma constructs an (r+1)-path, a contradiction.

The vertex threshold comes from the union of two actual maximum supports, not a small-order cutoff. It does not use minimum-counterexample analysis.

Equivalently the set of ordered initial pairs of maximum paths is disjoint from the set obtained by reversing every ordered terminal pair of maximum paths. This is a consequence of the explicit augmentation above, not a replacement for it.

## Application to the odd uniform residue

For n=2r+1 with every r-set Hamiltonian and every (r+1)-set non-Hamiltonian, a single reversed endpoint-pair match between ANY two displayed maximum words gives an actual spanning two-cover: take the augmented (r+1)-path and a Hamilton order on its r-vertex complement.

There are at least three unused vertices in this case, since the matched supports share two vertices. Any one suffices.

This supplies a second test on the endpoint data beyond 286's common-root same-role test. It permits overlapping supports and does not require that an exterior neighbor be preserved by an order exchange.

## Relation to the anchored prefixes of 295

Fix a maximum word P beginning (a,b), and consider actual tight words ending (b,a). At least one such word has order three by 295, for some choice of P. Under the ambient threshold, none can have order r, by the matching theorem above; none can be longer than r by global maximality.

Thus increasing such a prefix to order r would terminate in an actual augmentation immediately, without synchronizing any disjoint maximum tail order. This identifies a legitimate possible endpoint for a prefix-growth argument.

It does NOT prove that a prefix can always be increased, that an arbitrary restriction remains tight, or that order r is reachable. The missing growth step is retained as missing. The matching theorem closes its stated branch, while the unrestricted odd residue remains open.
