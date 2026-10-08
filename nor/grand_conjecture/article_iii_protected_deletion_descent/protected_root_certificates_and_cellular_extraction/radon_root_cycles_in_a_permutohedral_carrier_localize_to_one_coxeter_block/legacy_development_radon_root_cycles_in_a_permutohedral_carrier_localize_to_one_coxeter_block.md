# Radon root cycles in a permutohedral carrier localize to one Coxeter block — preserved pre-item development

## Development

## Radon root cycles in a permutohedral carrier localize to one Coxeter block

Let
[
F=B_1|cdots|B_s
]
be an ordered-partition face of the type-(A) permutohedron. Every chamber refining (F) orders the blocks (B_1,ldots,B_s) in that fixed order, while permuting coordinates only inside each block.

Suppose a collection of protected descent roots from chambers refining (F),
[
ho_j=e_{a_j}-e_{c_j},
]
has a positive dependence
[
sum_jlambda_jho_j=0,
qquad
lambda_j>0.
	ag{1}
]

Each root comes from sliding one bad (r)-window to the next. Thus in its chamber the dropped coordinate (a_j) occurs earlier than the entering coordinate (c_j).

### Theorem

Every directed physical-coordinate cycle in the circulation decomposition of (1) is contained in a single block (B_t).

### Proof

Let
[
eta(v)in{1,ldots,s}
]
be the block index of coordinate (v).

Since every chamber refining (F) places all of (B_t) before all of (B_{t+1}), the fact that (a_j) occurs earlier than (c_j) implies
[
eta(a_j)le eta(c_j).
	ag{2}
]

As in the Radon-cycle theorem, orient the physical edge associated to (ho_j) as
[
c_jlongrightarrow a_j.
]
Along this directed edge, (2) says the block index is nonincreasing:
[
eta(c_j)geeta(a_j).
]

Now take any directed cycle in the circulation decomposition:
[
x_1	o x_2	ocdots	o x_k	o x_1.
]
Its block indices satisfy
[
eta(x_1)geeta(x_2)gecdotsgeeta(x_k)geeta(x_1).
]
Hence every inequality is equality. All vertices of the cycle lie in one common block (B_t). QED.

### Window-support strengthening

A protected root from consecutive (r)-windows connects the dropped coordinate and entering coordinate at positions differing by exactly (r) in the chamber. If both endpoints (a,c) belong to the same contiguous Coxeter block (B_t), then every coordinate lying between them in that chamber also belongs to (B_t).

Therefore (B_t) contains the entire support of the two adjacent windows producing that root: an interval of
[
r+1
]
consecutive chamber coordinates.

### Consequence

Any Radon zero of protected roots inside a genuine permutohedral carrier automatically localizes to one unordered Coxeter block. All coordinates outside that block retain one fixed relative order.

This repairs an important compatibility gap in the global carrier program. The topological extraction problem can be separated into two stages:

1. use cellular antipodality/Radon labeling to force a positive root dependence in some product cell;
2. work only inside the single Coxeter block containing a root cycle, treating the outside order and threshold data as protected boundary conditions.

The remaining local theorem is now blockwise:

> A Coxeter block containing a directed cycle of protected (r)-window roots admits either a monotone replacement bridge or a smaller protected root cycle.

For ternary arity, the minimal nontrivial blockwise cycle is the (A_2) three-coordinate exchange already exposed by the corrected flat dynamics.
