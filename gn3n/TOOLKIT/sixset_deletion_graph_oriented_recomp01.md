# Every six-set has adjacent good-deletion overlap or a canonically oriented matching-block exception

**Summary:** Every six-set has adjacent good-deletion overlap or a canonically oriented matching-block exception.

## Statement

Let H be any boundary tournament and let U be any six-vertex set. Put D={d in U:H[U-{d}] is Hamiltonian}, and join d,e in D in a graph J exactly when H[U-{d,e}] is Hamiltonian. Then |D|>=4 and delta(J)>=max{1,|D|-4}. Exactly one of the following structural alternatives holds. (1) J has adjacent edges de,df; then U-{d,e} and U-{d,f} are Hamiltonian four-sets meeting in three vertices, and their union U-{d} is a Hamiltonian five-set. (2) J has no adjacent edges; then |D|=4, J is a perfect matching, H[D] is a non-Hamiltonian matching-block K4, and writing U-D={a,b}, both D+{a} and D+{b} are non-Hamiltonian while every (D-{d})+{a} and (D-{d})+{b} is Hamiltonian. Moreover the fixed-pair Hamiltonian-extension graph on D relative to {a,b} is exactly J. Hence D=C_+ disjoint-union C_- with |C_+|=|C_-|=2, where C_+={y:(a,y,b) is tight} and C_-={z:(b,z,a) is tight}; the two matching edges are C_+ and C_-, and every cross pair y in C_+, z in C_- gives a non-Hamiltonian four-set {a,b,y,z} carrying the four tight hooks (a,y,b), (b,z,a), (y,a,z), (z,b,y). If H is a minimum counterexample, then in alternative (1) the two Hamiltonian four-sets and their Hamiltonian five-set union all have non-Hamiltonian path-cover-two complements.

## Body

# Six-set deletion graph

All assertions are local to U. The four-of-six theorem in smallset01 gives |D|>=4. Fix d in D and consider the Hamiltonian five-set F=U-{d}. It has at least two Hamiltonian four-subsets, by deleting the endpoints of any Hamilton order. Among the |D|-1 four-subsets F-{e} with e in D-{d}, at most three are non-Hamiltonian. Therefore deg_J(d)>=|D|-4.

For the remaining case |D|=4, suppose d has no neighbor. Write D-{d}={e1,e2,e3} and U-D={a,b}. Then each of {a,b,e1,e2}, {a,b,e1,e3}, {a,b,e2,e3} is non-Hamiltonian. Partition {e1,e2,e3} according to whether (a,ei,b) or (b,ei,a) is tight. Two labels belong to the same class. The parallel-middle four-path lemma in localextend01 makes their four-set with a,b Hamiltonian, a contradiction. Thus delta(J)>=1 in this case as well. This is also the prescribed-overlap argument of extremal01, now without its unnecessary non-Hamiltonicity assumption on U.

If J has no adjacent edges, every degree is one, so J is a perfect matching. Its vertex number is even. Since 4<=|D|<=6, only 4 or 6 remain. The bound deg_J(d)>=|D|-4 excludes 6, so |D|=4.

Write U-D={a,b}. By definition of D, U-{a}=D+{b} and U-{b}=D+{a} are non-Hamiltonian. Suppose H[D] were Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 to D and exterior vertices a,b. Its graph K on D joins y,z when {a,b,y,z} is Hamiltonian. On four vertices, complementation sends the two disjoint edges of a perfect matching to each other. Since {a,b,y,z}=U-(D-{y,z}), the edge family of K is exactly the complement-pair image of the edge family of J. Hence K is also a perfect matching, contrary to that lemma's adjacent-edge conclusion. Therefore H[D] is non-Hamiltonian.

The non-Hamiltonian five-set D+{a} is edge-orderable by smallset01. Its restriction represents H[D], and the four-vertex classification makes D a matching-block K4. Moreover a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. In D+{a} that exceptional four-subset is D itself, so (D-{d})+{a} is Hamiltonian for every d in D. The same argument applies to b. This proves all conclusions.

The proof uses neither minimum-counterexample calculus, ambient order, path positions, extremality, nor Hamiltonicity or non-Hamiltonicity of U. The matching exception is a necessary structural alternative; its realizability is not asserted.

# Orientation of the matching exception

By sixset_deletion_graph_strengthened01, absence of adjacent edges forces |D|=4, the good two-deletion graph J to be a perfect matching, and H[D] to be a non-Hamiltonian matching-block K4. Write U-D={a,b}. For y,z in D, the fixed-pair four-set {a,b,y,z} equals U-(D-{y,z}). Hence yz is an edge of its fixed-pair Hamiltonian extension graph K exactly when the complementary pair D-{y,z} is an edge of J. On a four-element vertex set, complementation interchanges the two edges of a perfect matching, so K has exactly the same perfect-matching edge set as J. Apply fixedpair_perfect_matching_orientation01 to a,b,D. It partitions D into two orientation classes C_+,C_- of size two and identifies those classes with the matching edges. Apply fixedpair_perfect_matching_hooks01 to obtain, for every cross pair y,z, non-Hamiltonicity of {a,b,y,z} and the four displayed tight triples. No ambient minimality is used.

# Combined form

The preceding deletion-graph argument gives the positive-degree bound and reduces the no-adjacent-edge case to a four-label perfect matching. The orientation argument identifies that matching with the two fixed-pair orientation classes and supplies the complete cross-hook rectangle. Together they prove the stated dichotomy. In a minimum counterexample, the complement conclusion for the Hamiltonian supports follows from minimum-counterexample calculus.

## Metadata

- ID: sixset_deletion_graph_oriented_recomp01
- Kind: toolkit
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
