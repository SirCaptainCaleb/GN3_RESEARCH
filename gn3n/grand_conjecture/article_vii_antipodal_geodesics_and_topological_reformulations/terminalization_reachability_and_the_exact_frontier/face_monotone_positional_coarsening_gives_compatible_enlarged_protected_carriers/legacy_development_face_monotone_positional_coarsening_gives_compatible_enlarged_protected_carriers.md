# Face-monotone positional coarsening gives compatible enlarged protected carriers — preserved pre-item development

## Composition

(none yet)

## Development

## Positional coarsening supplies nested enlarged carriers

For an ordered-partition face F on n labels, its cuts occur at the cumulative block orders, a subset Cut(F) of {1,...,n-1}. For I subset {1,...,n-1}, define M_I(F) by deleting the cuts belonging to I, thereby merging the adjacent blocks separated by them.

**Lemma.**
1. F subset M_I(F).
2. If G subset F and I subset J, then M_I(G) subset M_J(F).
3. M_I is idempotent and M_I M_J=M_{I union J}.
4. Reversal sends M_I(F) to M_{tau I}(tau F), where tau I={n-i:i in I}.

**Proof.** A subface G refines the ordered blocks of F, hence its cut set contains Cut(F), and its block orders are consistent with those of F. Every cut surviving in M_J(F) lies outside J, hence outside I, and therefore survives in M_I(G). The resulting blocks refine those of M_J(F), proving (2); (1) is the same observation with no refinement. Repeating cut deletion proves (3). Reversal exchanges the cut after i positions with the cut after n-i positions, proving (4). ∎

**Carrier theorem.** Let Q be an invariant poset of proper protected faces. Choose cut sets I(F) such that
\[
G\subset F\Longrightarrow I(G)\subset I(F),\qquad
I(\tau F)=\tau I(F).
\]
Suppose each enlarged outward locus
\[
C(F)=M_{I(F)}(F)\cap X_{r+1}
\]
is nonempty and contractible. Then there is an equivariant continuous map Delta Q to X_{r+1} carried by C.

**Proof.** The lemma gives nested ambient faces; intersection with X_{r+1} preserves their inclusions. Reversal preserves the carrier assignment. Extend inductively over antipodal pairs of chain simplices using contractibility of the largest-face carrier. ∎

The same statement applies when C(F) is the intersection of M_{I(F)}(F) with a fixed protected target subcomplex Z, provided the intersections are nonempty and contractible and the target subcomplex is chosen compatibly under reversal.

## Application to moving the following vertex

In [[moving_the_fixed_following_vertex_fills_a_protected_terminal_pair_locus]], all subfaces retaining the singleton following vertex z use the same cut position immediately before z. Its deletion merges the last old block A with z. The enlarged convex faces are therefore nested automatically.

Intersecting them with the fixed endpoint-subset subcomplex C produces the nonempty contractible carriers used in that proof. Their compatibility comes from this actual coarsening operator, rather than choosing Hamilton orders separately on each source face.

For arbitrary neighboring ambient faces, selecting an exterior vertex independently does not imply the required monotonicity of I(F). This theorem isolates a sufficient global gluing condition: a fixed positional enlargement, or a face-monotone family of enlargements, together with protected contractible target loci.

Neither positional coarsening nor equivariance establishes protection. The positive-word boundary tests must still be verified on each enlarged carrier. The operator supplies the missing nesting once those tests hold.
