# Four-of-six equality endpoints have an oriented matching-block normal form

## Metadata

- ID: four_of_six_equality_endpoints_have_an_oriented_matching_block_normal_form
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 63
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let Y be a Hamiltonian five-set with distinguished labels x,y and ordinary labels r,s,t. Let e be an exterior label such that U=Y union {e} is non-Hamiltonian. Assume the good deletion labels of U are exactly
D={e,x,y,r}.
Equivalently, U-e=Y, U-x, U-y, and U-r are Hamiltonian, while U-s and U-t are non-Hamiltonian.

Apply the six-set deletion-graph theorem to U. Exactly one of the following holds.

(1) Adjacent good-deletion overlap. The good-deletion graph J on D contains adjacent edges ab,ac. Hence U-{a,b} and U-{a,c} are Hamiltonian four-sets meeting in three vertices, and their union U-a is a Hamiltonian five-set. Thus the equality endpoint already carries overlapping bounded Hamiltonian supports.

(2) Oriented matching-block exception. The graph J is a perfect matching, H[D] is a non-Hamiltonian matching-block K4, and relative to the exterior pair {s,t} there is a partition
D=C_+ sqcup C_-, |C_+|=|C_-|=2,
where C_+={z:h(s,z,t)=1} and C_-={z:h(t,z,s)=1}. The two matching edges are C_+ and C_-. Every cross pair p in C_+, q in C_- gives a non-Hamiltonian four-set {s,t,p,q} and the four tight hooks
(s,p,t), (t,q,s), (p,s,q), (q,t,p).

The placement of the two distinguished holes gives a further dichotomy.

(2a) If x,y lie in the same orientation class, then xy is a matching edge of J. Therefore
U-{x,y}={e,r,s,t}
is Hamiltonian.
The other matching edge is {e,r}, so
U-{e,r}=Y-{r}={x,y,s,t}
is Hamiltonian as well. Thus in this subcase the ordinary-deletion core Y-r really is a Hamiltonian four-set containing both holes.

(2b) If x,y lie in opposite orientation classes, then they are not adjacent in J. Consequently
Y-r=U-{e,r}
is non-Hamiltonian exactly when e and r also lie in opposite classes; in the perfect-matching exception this is forced. The matching pairs instead have the form {x,z_x},{y,z_y} with {z_x,z_y}={e,r}. Hence the two Hamiltonian four-sets
U-{x,z_x} and U-{y,z_y}
separate the hole labels and are governed by the complete cross-hook rectangle above.

Thus a four-of-six equality endpoint is not an arbitrary six-label obstruction. It either exposes adjacent overlapping Hamiltonian four-supports or has one canonical edge-ordered matching-block normal form, with the two holes either paired together (yielding a Hamiltonian hole-preserving four-core) or split across the two matching blocks.

This also corrects terminology used in earlier endpoint-core addenda: from (Y-r) union {e} Hamiltonian one may call Y-r a four-vertex core accepted by e, but Y-r itself is Hamiltonian only with additional input such as subcase (2a) above.
