# Nine deletion labels already force a completely classified incompatibility triple

## Statement

Let H be a minimum counterexample, let D be any set of m>=9 deletion labels, choose one deletion cover F_d of H-d for each d in D, and form the compatibility graph G. Then at least one of the following occurs: (i) the synchronized endpoint conclusion of compatthreeoneside09; (ii) three pairwise-incompatible covers whose three pairwise incompatibilities are uniformly support-incompatible; (iii) three pairwise-incompatible covers whose three pairwise incompatibilities are uniformly support-compatible but order-incompatible; (iv) a mixed blue-path triple with one support-switch label as in compatmixedtri37(A); or (v) a one-blue-edge mixed triple with either common-core support disagreement or a paired two-label support switch as in compatmixedtri37(B).

## Body

# Proof

Apply compatdegreefour10.

If its high-compatibility branch occurs, alternative (i) holds.

Otherwise Delta(G)<=4. By compatfourcolor22, G is 4-colorable. Since m>=9,

ceil(m/4) >= 3,

so one color class contains three labels. The corresponding chosen deletion covers are pairwise incompatible.

Color the three incompatible pairs blue when they are support-compatible and red when they are support-incompatible.

If all three edges are red, alternative (ii) holds.

If all three edges are blue, the three covers are pairwise support-compatible but, since they are pairwise incompatible, every pair is order-incompatible. This is alternative (iii).

If the triangle is not monochromatic, apply compatmixedtri37. Up to relabeling, either the support-compatible pairs form a two-edge path, giving the single-switch normal form in alternative (iv), or there is exactly one support-compatible pair, giving the core-disagreement / paired-switch normal form in alternative (v).

Thus nine chosen deletion labels already force an explicit three-cover structural interface.
