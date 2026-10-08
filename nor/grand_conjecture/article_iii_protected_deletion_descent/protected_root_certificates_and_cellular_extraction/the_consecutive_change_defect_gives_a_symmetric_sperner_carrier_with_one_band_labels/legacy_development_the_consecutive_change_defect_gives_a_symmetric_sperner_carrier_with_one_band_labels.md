# The consecutive-change defect gives a symmetric Sperner carrier with one-band labels — preserved pre-item development

## Development

## The consecutive-change defect gives a symmetric Sperner carrier with one-band labels

The all-pairs defect repairs the proper-face orientation issue, but its individual macro roots may span many intervening changes. There is a sharper variant.

Let an order

pi=(v_1,...,v_n)

have ternary window-status word c_1,...,c_m and change positions

p_1<...<p_k,

where c_{p_j} != c_{p_j+1}.

Define the consecutive-change defect

C(pi)
=
sum_{j=1}^{k-1}
(e_{v_{p_j}}-e_{v_{p_{j+1}+3}}).

For k<=1 the sum is empty.

### 1. Chamber zeros are exactly NOR-good words

If k<=1 then C(pi)=0.

If k>=2, use the order-rank functional lambda_pi(e_{v_t})=t. Every summand satisfies

lambda_pi(e_{v_{p_j}}-e_{v_{p_{j+1}+3}})
=
p_j-(p_{j+1}+3)<0.

Hence lambda_pi(C(pi))<0 and C(pi) is nonzero.

Therefore

C(pi)=0 iff the word has at most one change.

### 2. Reversal oddness

Under reversal-complement, the ordered list of change positions reverses. A consecutive pair p_j<p_{j+1} becomes the corresponding consecutive reversed pair in the opposite order, and

e_{v_{p_j}}-e_{v_{p_{j+1}+3}}

becomes its negative.

Thus

C(pi^rev)=-C(pi).

### 3. Every summand is an isolated-band certificate

Between consecutive change positions p_j and p_{j+1} there are no other changes.

Hence the status subword from rank p_j through p_{j+1}+1 is exactly one of

0,1,1,...,1,0

or

1,0,0,...,0,1.

So each individual macro root in C(pi) canonically certifies one isolated monochromatic band bounded by the opposite color.

This is strictly more local combinatorial provenance than an arbitrary pair from the all-pairs defect.

### 4. Proper-face localization

Let F=B_1|...|B_s be an ordered-partition face and take a positive relation

sum_pi alpha_pi C(pi)=0

over refinements of F.

With beta_F(e_v)=q for v in B_q, every consecutive-change macro root is weakly forward in the face order:

beta_F(e_{v_{p_j}}-e_{v_{p_{j+1}+3}})<=0.

Therefore every occurring summand in a positive zero must have beta_F=0, so its endpoints lie in one F-block.

Because blocks are contiguous, the entire coordinate interval from p_j through p_{j+1}+3 lies in that block. In particular both consecutive changes lie inside that block.

For any bad chamber with k>=2, this holds for every adjacent pair of changes. Consecutive pairs overlap in the change list, so by induction ALL changes of that chamber lie in one common face block.

Thus the same minimum-counterexample descent as for the all-pairs defect applies: a positive zero on a proper face forces all changes into one proper block, and connectivity of the refinement product then yields a smaller counterexample.

### 5. Strict witnessed label on every proper face

Now let F be proper. Choose an arbitrary NOR-good spanning order inside each block B_q and concatenate them.

Each block order has at most one internal change, in either direction.

The full concatenation is bad, so it has at least two changes and C(pi_F) is nonzero.

No consecutive-change summand can have both endpoints in one F-block: if it did, contiguity would place its two consecutive changes inside that block, contradicting the one-change property of the chosen block order.

Hence EVERY summand of C(pi_F) strictly crosses blocks and

beta_F(C(pi_F))<0.

Choosing these witnesses antipodally and labeling proper-face barycenters by C(pi_F) therefore gives the same zero-free nonzero-degree barycentric boundary carrier as the repaired pair-defect construction, but with isolated-band labels.

### Why this is better for Article III

A center-replacement zero of this carrier expands into positive combinations of macro roots whose witnesses are isolated one-band configurations.

Those are exactly the states controlled by:
- flat endpoint transport;
- threshold-band enlargement;
- fully-curved terminal barriers;
- the realized repair-square / Tucker machinery.

So the one-dimensional topological label and the local repair state now describe the SAME combinatorial object.

The remaining theorem is extraction: show that a positive closing relation among witnessed isolated-band macro roots can be converted into a compatible sequence of band transports, or else one terminal fully-curved exchange realizes a strict witness improvement.

This consecutive-change defect is a candidate replacement for the orientation-sensitive actual-10-root boundary carrier in the Sperner program.
