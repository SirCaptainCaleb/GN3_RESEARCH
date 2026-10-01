# Mixed incompatible triples have only a one-switch or paired-switch normal form

## Statement

Let F_a,F_b,F_c be three pairwise-incompatible deletion covers with nonempty common core W. Color a pair blue when it is support-compatible and red when it is support-incompatible. If the triangle is not monochromatic, then, up to relabeling, exactly one of the following two normal forms holds.

(A) Blue path: ab and bc are blue, ac is red. All three covers induce one common partition R|S on W, and the sole surviving special label b on the red common domain switches core class between F_a and F_c. Thus the red incompatibility is carried exactly by b, while the two blue pairs are order-incompatible.

(B) One blue edge: ab is blue and ac,bc are red. Either F_c induces a different support partition on W from the common partition induced by F_a,F_b, or all three induce one common R|S and both a and b switch class when compared with F_c: b switches between F_a and F_c, and a switches between F_b and F_c.

## Body

# Proof

Put W=V(H)-{a,b,c}.

## Case A: two blue edges

Assume ab and bc are support-compatible while ac is support-incompatible.

Restrict to W. Support compatibility of F_a,F_b gives one partition of W, and support compatibility of F_b,F_c gives the same partition. Hence all three induce one common partition R|S on W.

The common domain of F_a and F_c is W union {b}. Their support relations agree on W. Since they are support-incompatible, their only possible disagreement is the class of b. Therefore b belongs to opposite core classes in F_a and F_c.

This proves (A). Because the covers are pairwise incompatible, the two blue support-compatible pairs ab and bc are necessarily order-incompatible.

## Case B: one blue edge

Assume ab is support-compatible while ac and bc are support-incompatible.

The pair F_a,F_b induces one common partition R|S on W.

If F_c induces a different partition on W, the first alternative of (B) holds.

Assume instead F_c induces the same core partition.

Compare F_a and F_c. Their common domain is W union {b}. Since their core partitions agree but the pair is support-incompatible, b must switch class between F_a and F_c.

Compare F_b and F_c. Their common domain is W union {a}. The same argument shows that a switches class between F_b and F_c.

Thus both surviving labels of the blue pair switch when the third cover is introduced, proving the paired-switch alternative.

These exhaust all non-monochromatic two-colorings of a triangle up to relabeling.
