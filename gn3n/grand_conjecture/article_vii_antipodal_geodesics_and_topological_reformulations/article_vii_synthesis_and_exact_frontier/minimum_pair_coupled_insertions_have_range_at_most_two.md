# Minimum-pair coupled insertions have range at most two

## Composition

(none yet)

## Development

Let B=(b_1,...,b_m) be a tight path and let x,y be vertices outside B. Assume neither B+x nor B+y is Hamiltonian in the inherited order: inserting either vertex alone into any slot of B fails. Suppose nevertheless that there is a tight order R on V(B) union {x,y} whose restriction to V(B) is exactly the displayed order B. Then x and y occur at positional distance at most two in R. Equivalently, they are adjacent in R or exactly one vertex of B lies between them.

Proof. Consider x. In the order obtained by inserting x alone into its R-slot in B, every consecutive triple not containing x is inherited from B and is tight. The only triples that require checking are the consecutive triples containing x; there are at most three. If y were at positional distance at least three from x in R, none of those x-containing triples would contain y. They would therefore occur unchanged in R and hence be tight. Thus the inherited-order insertion of x into B would succeed, contrary to hypothesis. Hence dist_R(x,y)<=2. The same conclusion follows symmetrically from y. ∎

In a genuine minimum deletion pair {x,y} with H-{x,y}=P|Q, minimum-pair nonaugmentability makes both holes individually noninsertable into each inherited path. Consequently any coupled absorption of both holes into P while retaining the order of P has only two local forms: adjacent holes, or holes separated by one P-vertex. The same holds for Q. Long-range two-hole insertion is impossible.

More generally, for a local rule of uniformity r, the identical argument shows that if each of two labels is individually noninsertable into a fixed geodesic order, then any successful simultaneous insertion preserving that order must place the two new labels in a common r-window, hence at positional distance at most r-1. This is a uniformity-portable locality principle.
