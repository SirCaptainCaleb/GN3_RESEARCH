# Pair-defect labels repair the proper-face orientation gap — preserved pre-item development

## Pair-defect labels repair the proper-face orientation gap

Root §150 correctly audits the actual-10-root boundary argument: minimum counterexamplehood does not let one orient every proper block as 0^*1^*. The older canonical pair-defect D repairs exactly this issue because it vanishes on BOTH directions of one-change word.

Work in ternary arity r=3 in a minimum-coordinate counterexample. For an order

pi=(v_1,...,v_n)

with status-change indicators d_i, recall

D(pi)
=
sum_{i<j, d_i=d_j=1}
(e_{v_i}-e_{v_{j+3}}).

It is odd under reversal and D(pi)=0 iff pi has at most one status change.

### A strictly crossing witness on every proper face

Let

F=B_1|...|B_s

be any proper ordered-partition face, s>=2.

For each proper block B_j, minimum-counterexamplehood supplies a spanning NOR-good order of B_j. Its restricted ternary word has at most one change; its direction may be either 0->1 or 1->0.

Concatenate these chosen block orders in the fixed face order, obtaining a full order pi_F refining F.

The ambient instance is a counterexample, so pi_F has at least two changes and therefore D(pi_F) is nonzero.

Claim: EVERY summand of D(pi_F) has endpoints in distinct F-blocks.

Suppose a summand associated to changes i<j had both endpoints

v_i, v_{j+3}

in the same block B.

Because every F-block occupies a contiguous interval of positions in pi_F, every coordinate position from i through j+3 also lies in B. In particular the two change positions i and j are both changes of the restricted word on B.

That contradicts the fact that the chosen B-order has at most one change.

Hence every pair-defect root in D(pi_F) crosses at least one block boundary.

### Strict face coorientation

Let beta_F(e_v)=q for v in B_q.

For every pair-defect summand of ANY refinement of F,

beta_F(e_{v_i}-e_{v_{j+3}})<=0,

because i<j+3 and block order is fixed.

For the special witness pi_F just constructed, every summand crosses blocks, so every term is strictly negative and

beta_F(D(pi_F))<0.

Thus every proper face has one explicit, genuinely witnessed pair-defect vector in the strict inward face cone.

### Antipodal choice

Proper faces occur in free reversal pairs: reversing B_1|...|B_s gives B_s|...|B_1, and no proper ordered partition with s>=2 is fixed by this reversal.

Choose pi_F arbitrarily for one face in each antipodal pair and define the opposite choice by reversal. Then

D(pi_{-F})=-D(pi_F).

So the face labels are exactly antipodal.

### Barycentric Sperner carrier

Label the barycenter of each proper face F by D(pi_F) and extend affinely over the barycentric subdivision of the permutahedron boundary.

Consider a boundary flag simplex

F_0<...<F_k=G.

Every pi_{F_i} refines F_i and therefore also refines G. Hence every summand of D(pi_{F_i}) is weakly G-forward and

beta_G(D(pi_{F_i}))<=0.

The largest-face label is the special strict crossing witness, so

beta_G(D(pi_G))<0.

At a point whose minimal supporting flag ends in G, the coefficient of the G-barycenter is positive. Therefore the affine carrier has

beta_G(R(x))<0

and cannot vanish.

Thus R is a continuous odd zero-free boundary carrier built from ONE concrete NOR-good-block concatenation per proper face.

### Degree

The same strict face-normal sign gives a zero-free straight homotopy to the appropriate radial normal boundary map, exactly as in the standard barycentric face-normal argument. Hence the normalized pair-defect boundary carrier has nonzero radial degree.

### What this repairs—and what it does not

This repairs the orientation flaw identified in §150:

- no common 0->1 orientation of the proper blocks is needed;
- every proper block may use either one-change direction;
- the entire proper permutahedron boundary again has a witnessed antipodal zero-free nonzero-degree carrier.

However the labels are PAIR-DEFECT macro roots e_{v_i}-e_{v_{j+3}}, not necessarily actual adjacent-window 10 slide roots. Therefore roots §§144-147 cannot simply be reinstated verbatim: their actual-root flow/path interpretation must be replaced by a pair-defect extraction theorem.

The topological question has shifted to a more faithful form: replace the top-face center label by one bad chamber pair-defect and extract a compatible cycle/path of witnessed two-change intervals.
