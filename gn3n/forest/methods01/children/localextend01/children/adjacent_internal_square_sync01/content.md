# Three sparse bypasses synchronize to an internal deletion square or order disagreement

## Statement


Let G be a boundary tournament and let x,y be distinct vertices such that all four states
G, G-x, G-y, G-{x,y}
are non-Hamiltonian with path-cover number two. Suppose x and y are internal in every two-cover of G.

Fix a displayed two-cover
P|Q
of G with
P=(A,x,y,B),
where A and B are nonempty tight paths.

Assume each of the three lower states G-x, G-y, and G-{x,y} has a two-cover attaining the one-crossing equality case of the local bypass ladder relative to P|Q. Then at least one of the following holds:

(1) one of those lower Hamilton paths and the top path P exhibit relative-order disagreement on their common vertices;

(2) all three lower equality covers synchronize with the inherited top order, and the four displayed path orders
P=(A,x,y,B),
P-x=(A,y,B),
P-y=(A,x,B),
P-{x,y}=(A,B)
are all tight. Consequently
P|Q, (P-x)|Q, (P-y)|Q, (P-{x,y})|Q
form a coherent internal-deletion square of two-covers on one fixed support partition, even though x and y are internal and adjacent in the top cover.

Thus a universally-internal adjacent square pair has the following sharpened sparse residue: either some lower state has crossing multiplicity at least two, or a sparse lower cover already creates order disagreement, or the adjacent pair is simultaneously deletion-stable in both singleton directions and in the double deletion.


## Body


By the adjacent-internal-square bypass ladder, a one-crossing equality cover of G-x has support partition
V(A union {y} union B) | V(Q),
a one-crossing equality cover of G-y has
V(A union {x} union B) | V(Q),
and a one-crossing equality cover of G-{x,y} has
V(A union B) | V(Q).
In each case replace the Q-component by the inherited displayed Hamilton path Q; this does not change its support and preserves a valid two-cover.

Let R_x be the resulting Hamilton path on V(P)-{x}, R_y the path on V(P)-{y}, and R_{xy} the path on V(P)-{x,y}.

Compare R_x with the top Hamilton path P on their common vertex set V(P)-{x}. If they order some common pair differently, outcome (1) holds. Otherwise every common pair has the same relative order in R_x and P. A linear order is determined by its pairwise comparisons, so R_x is exactly the restriction of the displayed P-order obtained by deleting x. Hence
R_x=(A,y,B),
and P-x is tight.

The same argument with R_y gives either order disagreement or
R_y=(A,x,B),
so P-y is tight.

Finally compare R_{xy} with P on V(P)-{x,y}. Either they disagree on a common pair or
R_{xy}=(A,B),
so P-{x,y} is tight.

If none of the three comparisons gives order disagreement, all three inherited deletion orders are therefore tight. Since the unchanged path Q is disjoint from each, the four displayed covers
P|Q,
(P-x)|Q,
(P-y)|Q,
(P-{x,y})|Q
are valid two-covers of the corresponding square states. The top cover still has x,y as consecutive internal vertices by hypothesis, so this is an internal-deletion square rather than the endpoint-deletion square supplied by the usual top-cover normal form.

The final trichotomy follows by combining this with the bypass ladder: failure of a one-crossing equality cover in any lower state means every cover of that state has at least two cross-class edges; otherwise the present argument applies.
