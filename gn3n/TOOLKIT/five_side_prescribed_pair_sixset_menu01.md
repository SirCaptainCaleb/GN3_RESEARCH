# A prescribed-pair six-set has a Hamiltonian, singleton-extension, overlap, or fixed-pair matching outcome

**Summary:** Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put A=X-{x} and S=A union {p,q}. Then at least one of the following holds: (1) S is Hamiltonian, with H-S non-Hamiltonian of path-cover number two; (2) at least one of A union {p}, A union {q} is Hamiltonian, hence one of p,q is a Hamiltonian-deletion label of S; (3) S is non-Hamiltonian, both A union {p} and A union {q} are non-Hamiltonian, and the Hamiltonian two-deletion graph J on A has adjacent edges, yielding the overlap-amplification conclusion of ad81548d4f9f; (4) S is non-Hamiltonian, both singleton extensions are non-Hamiltonian, and J is a perfect matching. In outcome (4), the two matching edges are exactly the two fixed-pair orientation classes of A relative to p,q, every cross pair gives a non-Hamiltonian four-set, and every cross cell carries the complete opposite-orientation hook rectangle of fixedpair_perfect_matching_hooks01.
In outcome (3), the union of the two overlapping Hamiltonian four-sets is itself Hamiltonian. In outcome (4), A is a non-Hamiltonian matching-block K4, and all eight four-sets (A-{a}) union {p} and (A-{a}) union {q}, a in A, are Hamiltonian. In particular, if A is Hamiltonian, outcome (4) is impossible.

## Statement

Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put A=X-{x} and S=A union {p,q}. Then at least one of the following holds: (1) S is Hamiltonian, with H-S non-Hamiltonian of path-cover number two; (2) at least one of A union {p}, A union {q} is Hamiltonian, hence one of p,q is a Hamiltonian-deletion label of S; (3) S is non-Hamiltonian, both A union {p} and A union {q} are non-Hamiltonian, and the Hamiltonian two-deletion graph J on A has adjacent edges, yielding the overlap-amplification conclusion of ad81548d4f9f; (4) S is non-Hamiltonian, both singleton extensions are non-Hamiltonian, and J is a perfect matching. In outcome (4), the two matching edges are exactly the two fixed-pair orientation classes of A relative to p,q, every cross pair gives a non-Hamiltonian four-set, and every cross cell carries the complete opposite-orientation hook rectangle of fixedpair_perfect_matching_hooks01.
In outcome (3), the union of the two overlapping Hamiltonian four-sets is itself Hamiltonian. In outcome (4), A is a non-Hamiltonian matching-block K4, and all eight four-sets (A-{a}) union {p} and (A-{a}) union {q}, a in A, are Hamiltonian. In particular, if A is Hamiltonian, outcome (4) is impossible.

## Body

If S is Hamiltonian, (1) holds and minimum-counterexample calculus gives the complement conclusion. Assume S is non-Hamiltonian. If A union {p}=S-{q} or A union {q}=S-{p} is Hamiltonian, then (2) holds. Hence assume both are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to the four-set A and exterior labels p,q. It gives that (A-{a}) union {p,q}=S-{a} is Hamiltonian for every a in A. Since S-{p}=A union {q} and S-{q}=A union {p} are non-Hamiltonian by assumption, the Hamiltonian-deletion set D of S is exactly A. Apply ad81548d4f9f to S. Its good two-deletion graph J on D=A either has adjacent edges, giving (3), or is a perfect matching. In the perfect-matching case apply fixedpair_perfect_matching_orientation01 and fixedpair_perfect_matching_hooks01 with fixed pair p,q and four-set A. They identify the matching edges with the two 2-vertex fixed-pair orientation classes and give the complete hook rectangle on every cross cell, proving (4).

Strengthening and earlier use. Apply bad_six_deletion_matching_fourcore01 to the six-set S in outcomes (3) and (4), where D=A. Adjacent edges de,df in the deletion graph give four-sets S-{d,e}, S-{d,f} with union S-{d}; this union is Hamiltonian because d belongs to D. If the graph is a perfect matching, the same theorem forces A to be a non-Hamiltonian matching-block K4 and makes all eight four-sets (A-{a})+{p}, (A-{a})+{q} Hamiltonian. Thus a Hamiltonian core A eliminates the matching outcome immediately, without deriving the orientation partition or hook rectangle. These conclusions use only the six-set and its deletion graph; the original five-support and its complement do not enter this local step.

## Metadata

- ID: five_side_prescribed_pair_sixset_menu01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
