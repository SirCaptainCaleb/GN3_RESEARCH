# Compatibility triangles concentrate in one insertion gap

## Statement

Let H be a boundary tournament with pc(H)>2. Let a,b,c be distinct vertices, and for each d in {a,b,c} let F_d be a deletion cover of H-d. Suppose F_a,F_b,F_c are pairwise compatible on their common vertices. Then there is a partition V(H)=X disjoint-union Q with {a,b,c} subseteq X, a fixed Hamilton path on H[Q], and a common linear order R on X-{a,b,c} such that each F_d uses the fixed Q-path and a Hamilton path on X-{d} obtained by inserting the other two labels into R. Moreover the three labels a,b,c all occupy the same insertion gap of R. Consequently every compatibility triangle in a counterexample is localized to one common support and one common gap; the only remaining freedom is the three pairwise orders of a,b,c inside that gap and the tightness of the resulting three-label middle triple.

## Body

# Compatibility triangles concentrate in one insertion gap

Let H be a boundary tournament with pc(H)>2, and let a,b,c be distinct vertices. For d in D={a,b,c}, let F_d be a deletion cover of H-d. Assume the three covers are pairwise compatible on their intersections.

By the support-compatible-family theorem in d43a7c9e2f61, there are exactly two support classes X,Q, all labels in D lie in X, every F_d has support partition (X-{d}) | Q, H[Q] is Hamiltonian, and the Q-component may be chosen with one fixed Hamilton order throughout the family. Thus all remaining variation lies in Hamilton paths P_d on X-{d}.

Put R=X-D. Pairwise compatibility implies that the restrictions of P_a,P_b,P_c to R have the same relative order; write this common order as
R=(r_1,...,r_m),
allowing m=0. For x in D, compare the two paths P_d that contain x. Their common domain contains R union {x}, so compatibility forces x to have the same position relative to every vertex of R in both paths. Hence x determines a well-defined insertion gap g(x) of R, with the two endpoint gaps included.

Suppose the three gaps are not all equal. Construct an ordering P of X by starting with R, inserting each label x in its gap g(x), and, when two labels share one gap, ordering that pair as it appears in the unique deletion path containing both. Distinct gaps are separated by a vertex of R, so their relative order is forced by the gap positions. Therefore, for each d in D, deleting d from P gives exactly P_d.

Because the three labels do not all share one gap, no three consecutive vertices of P can contain all of a,b,c. Every consecutive triple of P therefore omits at least one label d, and is a consecutive triple of P_d. It is tight. Hence P is a Hamilton path of H[X]. Together with the fixed Hamilton path on H[Q], this gives a two-cover of H, contradicting pc(H)>2.

Therefore g(a)=g(b)=g(c). This proves the localization.

If the three pairwise precedence relations among a,b,c are transitive, say a<b<c, then the common-gap ordering obtained by inserting the block (a,b,c) into R agrees with every P_d after deleting d; all consecutive triples are inherited from one of the deletion paths except possibly the middle triple (a,b,c). Thus even this branch has only one unconstrained local triple. If the precedence relations are cyclic, the entire incompatibility is the cyclic three-label order at that same gap. In either case the obstruction is bounded and local, while R and the Q-path are inert.

No minimum-counterexample hypothesis is used beyond pc(H)>2.
