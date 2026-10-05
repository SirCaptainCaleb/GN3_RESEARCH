# Two-slot persistent boundary reservoirs are uniformly blocked and rooted

## Metadata

- ID: two_slot_persistent_boundary_reservoirs_are_uniformly_blocked_and_rooted
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 111
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

### Structure of a two-slot blocked reservoir

Let \(B\) be a two-slot reservoir at a persistent left \(011\) window with inward corridor vertex \(c_2\). In the blocked alternative, for all distinct \(u,v\in B\),
\[
h(u,v,c_2)=0,\qquad h(c_2,v,u)=1.
\]
Moreover persistence supplies the fixed inward continuation, so every reservoir label extends into a rooted tight path on the first corridor segment. The right boundary has the reversed symmetric statement. Therefore the remaining two-slot branch is a bounded rooted endpoint problem, not an arbitrary ordered-pair relation.

## Development

## A two-slot persistent boundary reservoir is automatically blocked and supplies rooted four-paths

Let \(F\subset X_r\) be a double-persistent protected face for a mixed reflected span-two occurrence. On the left, every chamber has the persistent word
\[
011
\]
on positions
\[
a,a+1,a+2,a+3,a+4.
\]
Suppose one face block \(B\) meets this determining window in its first two positions \(a,a+1\) and extends outward beyond \(a\). Write
\[
c_2=v_{a+2},\qquad c_3=v_{a+3},\qquad c_4=v_{a+4}
\]
after freezing the other blocks meeting the window. The labels occupying positions \(a,a+1\) may be any ordered pair of distinct vertices of \(B\).

**Lemma 1 (uniform two-slot polarization).**
For every distinct \(u,v\in B\),
\[
h(u,v,c_2)=0,
\qquad\text{hence}\qquad
h(c_2,v,u)=1.
\]

**Proof.**
Choose a chamber of \(F\) in which \(u,v\) occupy positions \(a,a+1\), respectively. Persistence of the left \(011\) occurrence forces its first status
\[
h(u,v,c_2)
\]
to be \(0\). Since every ordered pair of distinct labels of a face block can occupy those two positions, this holds for all ordered pairs. Boundary antisymmetry gives the second identity. \(\square\)

Thus a two-slot reservoir is not an arbitrary ordered-pair locus. It is **automatically a completely blocked buffer reservoir** in every possible ordered pair state.

There is a stronger rooted consequence.

**Lemma 2 (rooted four-path supply).**
For every three-element subset
\[
A=\{x,y,z\}\subseteq B,
\]
the four-set
\[
A\cup\{c_2\}
\]
has a Hamilton tight path with \(c_2\) as a prescribed endpoint.

**Proof.**
Every three-vertex boundary tournament has a tight Hamilton order; choose one, say
\[
(x,y,z).
\]
Lemma 1 gives
\[
h(c_2,x,y)=1.
\]
Together with
\[
h(x,y,z)=1
\]
this makes
\[
(c_2,x,y,z)
\]
a tight Hamilton path. \(\square\)

In fact the conclusion is uniform over the choice of the three reservoir labels: every triple of labels in \(B\) can be converted to a Hamilton four-support rooted at the fixed inner vertex \(c_2\).

The right-hand mirror is identical. If a face block occupies the last two positions of a persistent right \(001\) determining window and extends outward, its ordered-pair freedom is uniformly polarized and every three reservoir labels give a rooted Hamilton four-path at the corresponding fixed inner corridor vertex.

### Strategic consequence

Combine this with [[prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci]] and [[frozen_interiors_make_buffer_success_sectors_contractible]].

At one end of a double-persistent face, an unbounded boundary block has footprint at most two.

1. **Footprint one.** The endpoint choice is a one-vertex reservoir. Its successful-buffer locus is contractible; if that locus is empty, every allowed label is uniformly blocked.
2. **Footprint two.** Persistence itself forces every ordered pair to be blocked, and any three reservoir labels supply a Hamilton four-path with a prescribed inner endpoint by Lemma 2.

Therefore there is no remaining need for a general topology theorem for arbitrary two-slot ordered-pair conditions. The two-slot sector belongs entirely to the blocked combinatorial branch, but with stronger endpoint control than the earlier three-hook packet lemma: the Hamilton order now has the inner corridor vertex \(c_2\) as a specified endpoint.

This does not yet give a two-cover or an outward repair. The rooted four-path points outward from \(c_2\), whereas attaching it to the untouched inward corridor requires an additional junction argument. The next local theorem should exploit the simultaneously fixed tight triples
\[
h(c_1,c_2,c_3)=h(c_2,c_3,c_4)=1
\]
from the persistent \(011\) word together with the connector-free constraints of the genuine deletion-distance-two residue. The remaining question is no longer existence of a rooted Hamilton packet, but whether its orientation can be handed off across the fixed inner edge \(c_2c_3\), or whether failure of every such handoff forces an outward repair/farther witness.
