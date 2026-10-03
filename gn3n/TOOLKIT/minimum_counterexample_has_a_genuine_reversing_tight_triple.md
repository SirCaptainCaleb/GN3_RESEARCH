# Every minimum counterexample has a genuine reversing tight triple

**Summary:** Every minimum counterexample has a genuine reversing tight triple.

## Statement

Every minimum counterexample H contains a tight path P of order at least three and a tight triple T such that T reverses an ordered edge of P.

## Body

Take the two disagreeing tight paths R,S of order at least three supplied by 4cf010e3e5b3 and apply Section 4 of the certified path-intersection calculus pathcalc01.

If pathcalc01 directly returns a tight triple reversing an ordered edge of R or S, the conclusion holds.

If it returns a common ordinary edge traversed oppositely, say (u,v) is an ordered edge of R and (v,u) an ordered edge of S, choose a consecutive tight triple of R containing (u,v). Such a triple exists because R has order at least three; every ordinary edge of a path of order at least three belongs to at least one consecutive triple. That triple contains (u,v), hence reverses the ordered edge (v,u) of S. Thus the conclusion again holds.

It remains that pathcalc01 returns a vertex-simple tight cycle C. Opening C at any cyclic cut gives a Hamilton tight path on V(C). The cycle cannot span H, because then H would be Hamiltonian. Put K=H-V(C). Minimum-counterexample calculus gives pc(K)<=2. The subtournament K cannot be Hamiltonian, because an opened Hamilton path on C together with a Hamilton path on K would two-cover H. Hence K is non-Hamiltonian with pc(K)=2. Since every boundary tournament of order at most three is Hamiltonian, |K|>=4.

Choose a displayed two-cover A|B of K. Some component, say A=(a_0,...,a_m), has order at least two, so m>=1. Open the cycle at an arbitrary cut c_{i-1}|c_i:
C_i=(c_i,c_{i+1},...,c_{i-1}).
If both cross-boundary triples
(a_{m-1},a_m,c_i) and (a_m,c_i,c_{i+1})
were tight, the concatenation A,C_i would be a tight path and together with B would two-cover H. Therefore at least one is non-tight. Boundary reversal antisymmetry gives respectively
(c_i,a_m,a_{m-1})
or
(c_{i+1},c_i,a_m)
tight. The first reverses the displayed edge (a_{m-1},a_m) of A; the second reverses the displayed cycle edge (c_i,c_{i+1}) of C. Thus the cycle branch also supplies a genuine reversing tight triple.

All three outputs of pathcalc01 therefore yield the asserted nonvacuous local reversal.

## Metadata

- ID: minimum_counterexample_has_a_genuine_reversing_tight_triple
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
