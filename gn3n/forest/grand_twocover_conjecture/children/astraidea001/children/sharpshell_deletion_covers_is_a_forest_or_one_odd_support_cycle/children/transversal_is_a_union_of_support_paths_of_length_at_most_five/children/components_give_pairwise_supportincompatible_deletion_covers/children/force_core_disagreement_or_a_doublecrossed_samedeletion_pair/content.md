# Support-switch triples in the sharp half-order shell force core disagreement or a double-crossed same-deletion pair

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1. Let F_a,F_b,F_c be lambda|lambda deletion covers of H-a,H-b,H-c that are pairwise support-incompatible. Put W=V(H)-{a,b,c}. Then either two of the three covers induce different support partitions on W, or one of H-a,H-b,H-c admits two lambda|lambda covers with different support partitions and hence, by d9ef8e3fe739, at least two ordinary path edges of either cover cross the support cut of the other. In the common-core branch specifically, the core classes have orders lambda-1,lambda-1 and all six supports R union {x}, S union {x} for x in {a,b,c} are Hamiltonian.

## Body

Apply compattriplesupport14. If two restrictions already induce different support partitions on W, we are in the first alternative.

Assume instead that all three induce one common partition W=R disjoint-union S, with each special label switching core class between the two covers in which it appears. By compatsupportparity15, up to relabeling there are two parity types: all three covers split the two surviving special labels, or exactly one cover is split.

The exactly-one-split type is impossible under the lambda|lambda size constraint. In its canonical form,

F_a has supports (R union {b,c}) | S,

while F_b has supports R | (S union {a,c}).

Since every component has order lambda, F_a would force

|R|=lambda-2, |S|=lambda,

whereas F_b would force

|R|=lambda, |S|=lambda-2,

a contradiction.

Hence the all-three-split type holds. Every cover places one surviving special label with R and the other with S, so the lambda|lambda sizes give

|R|=|S|=lambda-1.

By compatsupportham22, each of

R union {a}, R union {b}, R union {c},
S union {a}, S union {b}, S union {c}

is Hamiltonian.

Consider, for example, deletion H-a. The original split cover F_a uses one of

(R union {b}) | (S union {c})

and

(R union {c}) | (S union {b}).

Because all four displayed supports are Hamiltonian, the other pairing is also a lambda|lambda cover of H-a. The two unordered support partitions are different.

Apply the certified same-deletion crossing-gap theorem d9ef8e3fe739. Two covers of one deletion in the sharp half-order shell with different support partitions have at least two ordinary path edges crossing the other support cut. This yields the second alternative. The same conclusion is available symmetrically at each of the three deletions. ∎