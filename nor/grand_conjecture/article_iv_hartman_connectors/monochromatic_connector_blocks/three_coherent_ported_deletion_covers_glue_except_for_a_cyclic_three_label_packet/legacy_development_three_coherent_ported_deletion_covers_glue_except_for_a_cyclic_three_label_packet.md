# Three coherent ported deletion covers glue except for a cyclic three-label packet — preserved pre-item development

## Development

# Three coherent deletion covers: gluing except for one cyclic three-label packet

Work in the normalized flat split B -> z -> A -> x, with alpha the tournament-derived reversal-odd ternary label. A fully ported zero path is an ordered shore path with alpha=0 on every consecutive triple and both defined terminal ordered pairs forward. A cover is a partition of the shore into at most two such paths.

**Theorem (three-deletion gluing with a classified exception).** Let D={a,b,c} be three distinct labels of A, with |A|>=4. For each d in D choose a cover F_d of A\{d} into at most two fully ported zero paths. Assume that for each distinct d,e in D, the induced same-path equivalence relation and the relative order of coordinates within common paths agree on A\{d,e}. Then exactly one of the following constructive conclusions applies:

(i) The three covers reconstruct at most two fully ported zero paths on all of A. Consequently there is a spanning compatible connector on A union {x,z}, and the full homogeneous-cut NOR instance closes.

(ii) The reconstructed same-path relation has at most two classes, but a,b,c all lie in one class and their three pairwise order comparisons form a directed 3-cycle. All vertices of that class outside D precede all three labels or follow all three labels. The cyclic packet has alpha=1 in each of its three cyclic comparison orders, while the corresponding pairwise adjacent insertion collars inherited from the deletion covers have alpha=0. The theorem makes no closure assertion in (ii).

In particular (i) holds if the deleted labels are not all in one reconstructed class, or if their three comparisons are acyclic. Four coherent deletion covers are therefore unnecessary outside the cyclic-packet exception.

**Proof.** For any unordered pair {u,v} of shore labels, choose d in D\{u,v} and define u~v if they lie in the same path of F_d. At least one such d exists, and pairwise agreement makes the definition independent of the choice. Every triple other than D survives one of the three deletions; hence on each such triple ~ is an equivalence relation with at most two classes.

These properties also hold on D. Indeed, if a~b, b~c, a!~c, pick u in A\D. In F_b, a and c occupy two different classes, so u joins one, say a. By the common-support agreements and transitivity of F_c, u~b. Transitivity in F_a then gives u~c, contradicting F_b. If a,b,c are pairwise inequivalent, then in F_c the vertex u joins one of a,b, say a. The relation u~a remains in F_b, forcing u!~c there; u!~b follows from F_c. Thus F_a has the three distinct classes {u},{b},{c}, impossible. Therefore ~ partitions A into at most two classes.

For two labels in one class, define their comparison by any deletion cover retaining both. This is well-defined by agreement. It is a total pairwise comparison, transitive on every triple other than D. A nontransitive comparison therefore is precisely a directed cycle on D, which requires all three labels in the same class.

First suppose all comparisons are transitive. They define a linear order on each global class, and restricting either order to A\{d} recovers its corresponding path order in F_d. Every consecutive triple in a global path other than exactly {a,b,c} remains consecutive in a deletion cover avoiding it, and so has alpha=0. Its first and last ordered pairs are forward by the same argument, choosing a deleted label outside the pair. If {a,b,c} forms a consecutive block a,b,c in a global class, take an immediately adjacent class vertex L before the block, if one exists. The three deletion paths give alpha(L,a,b)=alpha(L,a,c)=alpha(L,b,c)=0. The tournament cocycle identity
alpha(a,b,c) = alpha(L,a,b) xor alpha(L,a,c) xor alpha(L,b,c)
gives alpha(a,b,c)=0. If the block begins the class but has a right neighbor R, use instead
alpha(a,b,c) = alpha(a,b,R) xor alpha(a,c,R) xor alpha(b,c,R).
If the class consists precisely of a,b,c, each of its pairwise comparisons is the forward terminal edge of a 2-vertex fully ported path in a deletion cover. Thus t(a,b)=t(a,c)=t(b,c)=1, and the tournament formula
alpha(a,b,c) = 1 xor t(a,b) xor t(b,c) xor t(a,c)
again gives zero. Consequently both reconstructed paths are fully ported and have zero word.

The already proved ported-gluing theorem yields the spanning connector P,x,z,Q for two nonempty classes, or z,P,x for one nonempty class, and the homogeneous-cut insertion theorem closes the full instance.

Now suppose the comparisons on D form the cycle a<b, b<c, c<a. Every class vertex u outside D must lie entirely before or entirely after D: if, for example, a<u<b, then c<a<u forces c<u while u<b<c forces u<c, a contradiction, using transitivity of every comparison triple involving u. The other possible interleavings are cyclic relabelings. Thus all three labels occupy a single comparison gap in the rest of their class. With a left neighbor L, the deletion collars say alpha(L,a,b)=alpha(L,b,c)=alpha(L,c,a)=0. Reversal oddness and the first displayed cocycle identity yield alpha(a,b,c)=1. With a right neighbor R, use the analogous right-hand identity. If D constitutes the whole class, all three pairwise cyclic comparisons are forward in the deletion paths, so t(a,b)=t(b,c)=t(c,a)=1; the same tournament formula yields alpha(a,b,c)=1. Cyclic rotation preserves alpha, hence all three cyclic comparison orders have alpha=1. This proves (ii).

**Boundary of the result.** The hypothesis concerns actual ordered fully ported zero-path covers and their common-support agreement. It is stronger than the existence of arbitrary deletion connectors or independently chosen two-path covers. The cyclic packet is an obstruction to this specific coherent three-cover reconstruction, not a counterexample to spanning NOR. A promising next step is an ambient, collar-preserving resolution of this isolated full-curvature packet, possibly using independent x,z movement or a second path.
