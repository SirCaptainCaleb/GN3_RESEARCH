# Double-persistent faces have bounded block width and bounded boundary footprints

## Composition

(none yet)

## Development

## Double-persistent faces have bounded block width and bounded boundary footprints

Let (Fsubset X_r) be a protected face at a reflected positive span-two depth (r). Assume the left and right depth-(r) occurrences are present in **every** chamber of (F). Write their five-vertex determining windows as
[
I_L=[a,a+4],qquad I_R=[b,b+4],qquad a<b.
]

The statements below concern face-block positions, not the order of the full determining span.

**Lemma 1 (persistent-window footprint bound).** Every ordered-partition block of (F) meets (I_L) in at most two positions, and meets (I_R) in at most two positions.

**Proof.** A face block occupies consecutive positions. If one block met (I_L) in at least three positions, it would contain three consecutive positions of (I_L). Every ordering of the vertices in those block positions is available in chambers of (F). Fix all other block orders and reverse the first and third vertices of those three consecutive positions. This reverses the corresponding ordered triple, so boundary antisymmetry flips its tight/non-tight status.

But the left depth-(r) occurrence is persistent, so its word—one of (001,011)—has all three relevant consecutive statuses fixed in every chamber of (F). Contradiction. The right window is identical. (square)

This is stronger than the exclusive footprint argument: persistence fixes the actual word, so no support-preserving constancy theorem is needed.

**Lemma 2 (inward five-position bound).** Any five consecutive positions lying strictly between the two selected reflected starts cannot belong to one face block.

**Proof.** Their three internal status starts are strictly inward of the selected reflected depth. Protection excludes (001) and (011) at all three starts in every chamber of (F). The five-position obstruction [[verified_five_position_obstruction_and_ordered_tuple_compression]] gives a contradiction. (square)

Consequently every face block wholly contained in the strictly inward corridor has order at most four.

There is also a boundary version. A block meeting the final two positions of (I_L) and continuing inward has order at most four: if it had order at least five, five consecutive positions beginning at (a+3) would have all three internal status starts strictly inward. The same holds for a block meeting the first two positions of (I_R) and extending inward.

### What is and is not bounded at the ends

A face block straddling the **outer boundary** of the full determining span
[
J=[a,b+4]
]
can be arbitrarily large outside (J). Lemma 1 says only that its footprint **inside the determining window** has order at most two. Thus it is incorrect to regard the whole boundary block as a rank-one Coxeter factor.

What is true is positional:

- at most two consecutive slots of a left boundary block lie in (I_L);
- at most two consecutive slots of a right boundary block lie in (I_R);
- a single adjacent generator crossing an endpoint of (J) exchanges only one label across that endpoint.

Over the full boundary-block permutahedron, however, many different labels can occupy the one or two determining slots. This label multiplicity is genuine and must be handled by subset-locus topology or by uniform forcing, not by a bounded-rank quotient.

All face blocks wholly inside the long inward corridor still have order at most four. Hence the unbounded face geometry consists of a long product of bounded-width interior factors together with possibly large **endpoint label reservoirs** whose footprints in the determining windows are of size at most two.

### Strategic consequence

A frozen-window carrier may collapse every block meeting (J), so arbitrarily many bounded-width interior factors cause no separate target-side coherence problem. If one deliberately retains endpoint variation, it must be treated as a permutahedral choice of which labels occupy one or two boundary slots.

The useful dichotomy is therefore not “rank-one endpoint interface versus interior.” It is:

1. **bounded positional footprint** at each endpoint;
2. possibly **unbounded label reservoir** in the source boundary block;
3. a one-vertex boundary test whenever only the outermost determining slot is left variable.

The one-variable sector is exactly where [[prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci]] applies. If all allowed labels fail that one-vertex test, the large reservoir becomes algebraically useful: every label satisfies the same reversed boundary triple, producing the uniformly blocked common-hook structure used in the packet lemmas.

This correction leaves the persistent-window and inward block-width lemmas unchanged, but withdraws the earlier claim that the full boundary interaction has Coxeter rank one.
