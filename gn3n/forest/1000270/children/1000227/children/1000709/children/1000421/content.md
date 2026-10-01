# Three-label producers collapse to a four-core, while opposite endpoint exchanges force a longest-path and support-triangle package

## Statement

In the order-thirteen mu=6 shell, let Q be a Hamiltonian six-set with deficient seven-complement X, and D={t in X:X-t is Hamiltonian}. If |D|>=3, then either two canonical covers (X-t)|Q have relative-order disagreement, yielding the standard reversed-edge/reversing-triple/tight-cycle witness, or |D|=3 and the three covers are pairwise compatible on one four-vertex core P=X-D with one common insertion gap; the transitive precedence case is exactly a 2+2 gap, and a cyclic endpoint gap enters the certified four-kernel frontier. Separately, if distinct a,c in X give order-preserving singleton replacements at the two endpoints q_0,q_5 of Q=(q_0,...,q_5), then those replacements splice to a second globally longest six-path on (Q-{q_0,q_5}) union {a,c}; the associated deficient supports N_a=(X-{a}) union {q_0} and N_c=(X-{c}) union {q_5} satisfy d_J(X,N_a)=d_J(X,N_c)=1 and d_J(N_a,N_c)=2, so X,N_a,N_c form a Gamma-triangle with the two corresponding hybrid single-transfer triangles.

## Body

# Three-label producers collapse to a four-core, while opposite endpoint exchanges force a longest-path and support-triangle package

Work in the order-thirteen mu=6 shell. Let Q be a Hamiltonian six-set and X=V(H)-Q its non-Hamiltonian seven-complement.

## Three-label producer compression

Put
D={t in X : X-{t} is Hamiltonian}.
For each t in D choose the canonical exact deletion cover
F_t=(X-{t})|Q,
and normalize the Q-component to one fixed Hamilton order.

Suppose first that some pair F_t,F_u orders two common vertices of X-{t,u} differently. Path restriction/intersection calculus then gives the standard explicit witness: a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Assume no such pairwise order disagreement. The family is already support-compatible because every F_t has supports X-{t} and Q; after normalizing Q, the absence of order disagreement makes every pair fully compatible on its common domain.

If |D|>=4, choose four distinct labels. The four-cover compatibility theorem with q=2 glues the four pairwise-compatible deletion covers to a spanning two-cover of H, contradicting minimal counterexample status. Hence in the no-disagreement branch
|D|=3.

Write D={a,b,c}. The three canonical covers are pairwise compatible. Compatible-triangle gap geometry gives a common ordered support class
P=X-{a,b,c}
together with the fixed Hamilton path Q, and all three labels occupy one identical insertion gap of P. Since |X|=7,
|P|=4.

If the precedence tournament on {a,b,c} is transitive, the two-deep-gap theorem puts at least two vertices of P on each side of the common gap. Because |P|=4, the split is exactly 2+2.

If the precedence tournament is cyclic and the common gap is an endpoint of P, the endpoint compatible-triangle theorem applies: the four-set consisting of the three labels and the first common-core vertex is either Hamiltonian with non-Hamiltonian path-cover-two complement or the exceptional cyclic K4, and the certified four-kernel frontier applies.

Thus every degree-at-least-three canonical producer family either exposes explicit order disagreement or collapses to one highly constrained four-core.

## Opposite endpoint replacements splice

Now write
Q=(q_0,...,q_5)
and let a,c be distinct vertices outside Q. Suppose
(Q-{q_0}) union {a}
and
(Q-{q_5}) union {c}
have Hamilton paths L,R, respectively, and that each preserves the relative order of its common Q-vertices.

Because Q union {a} and Q union {c} are non-Hamiltonian, the endpoint-replacement argument localizes the inserted labels. On the left,
L is either
(a,q_1,...,q_5)
or
(q_1,a,q_2,...,q_5).
On the right,
R is either
(q_0,...,q_4,c)
or
(q_0,...,q_3,c,q_4).

Splice the certified left initial segment to the certified right terminal segment through the unchanged middle pair q_2,q_3. In the four cases the sequences
(a,q_1,q_2,q_3,q_4,c),
(a,q_1,q_2,q_3,c,q_4),
(q_1,a,q_2,q_3,q_4,c),
(q_1,a,q_2,q_3,c,q_4)
are tight: every consecutive triple is inherited from L, R, or Q.

Each path uses exactly
(Q-{q_0,q_5}) union {a,c}
and has order six, so it is globally longest. Thus opposite minimal endpoint exchanges by distinct labels commute into a second longest path.

## The endpoint exchanges force a radius-three triangle

Assume the corresponding exact endpoint deletion covers have singleton-exchange supports
H-q_0=(Q-{q_0}+{a}) | (X-{a})
and
H-q_5=(Q-{q_5}+{c}) | (X-{c}).

Restoring q_0 to either component of the first cover gives a D=1 state. Restoring it to X-{a} gives the deficient support
N_a=(X-{a}) union {q_0};
restoring it to the opposite component gives Q union {a}.
Similarly the right endpoint cover gives
N_c=(X-{c}) union {q_5}
and Q union {c}.

The Johnson distances are immediate:
d_J(X,N_a)=1,
d_J(X,N_c)=1.
Since a,c,q_0,q_5 are distinct and
N_a intersect N_c=X-{a,c}
has order five,
d_J(N_a,N_c)=2.

Hence X,N_a,N_c are pairwise adjacent in the radius-three deficient-support graph Gamma and span a triangle.

There is also transfer structure attached to this triangle. The two D=1 states arising from H-q_0 differ by transferring q_0, so N_a and Q union {a} are joined by the legal single-transfer move labelled q_0. Independently, the canonical exact cover H-a=(X-{a})|Q shows that X and Q union {a} are joined by the legal transfer labelled a. Thus
X, N_a, Q union {a}
form a hybrid triangle with one Gamma edge and two single-transfer edges. The q_5,c side is symmetric.

So the producer route reduces to a compact package: canonical three-label families collapse to one four-core unless they already give order disagreement, while opposite singleton endpoint exchanges yield both a second longest path and a short radius-three/transfer configuration ready for the expansion machinery.
