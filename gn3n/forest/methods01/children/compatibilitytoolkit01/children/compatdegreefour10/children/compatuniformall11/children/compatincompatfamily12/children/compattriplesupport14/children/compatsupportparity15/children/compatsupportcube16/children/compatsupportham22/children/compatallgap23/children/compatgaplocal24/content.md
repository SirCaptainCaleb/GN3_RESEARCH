# Adjacent-gap concentration yields a reverse cross triple or a common-gap four-set

## Statement

Continue the no-order-disagreement branch of compatallgap23 on one core K, with common core order L and insertion positions of a,b,c lying in at most two adjacent gaps. Then exactly one of the following holds. (i) All three labels use one common gap. If that gap is internal with consecutive core vertices u,v, then for every pair x,y in {a,b,c}, H[{u,v,x,y}] is Hamiltonian. If the common gap is an endpoint gap, all three chosen Hamilton paths share the corresponding endpoint-extension pattern. (ii) Both adjacent gaps are occupied. Let x,y be labels using the two different gaps and let z be the third label. Then the simultaneous two-label insertion of x,y into L cannot be tight, because otherwise K union {x,y} together with the Hamiltonian opposite-core enlargement by z would two-cover H. Consequently the unique cross triple coupling the two insertions is non-tight, and its reverse is tight. Thus the two-gap branch forces an explicit reverse cross triple through the core vertex between the adjacent gaps.

## Body

# Proof

Let the core be K and let L=(v_1,...,v_k) be the common relative order induced by the three chosen Hamilton paths on K union {a}, K union {b}, K union {c}. Each path is L with its special label inserted into one gap.

By compatallgap23 the three insertion positions lie in either one gap or two adjacent gaps.

## One common gap

Suppose all three labels use the same gap.

If the gap is internal, say between consecutive core vertices u,v in L, then for every special label x the Hamilton path on K union {x} contains the tight triple (u,x,v).

Thus for any two labels x,y, both (u,x,v) and (u,y,v) are tight. The two-parallel-middle lemma from localextend01 gives a Hamilton tight path on {u,v,x,y}.

If the common gap is the left endpoint, every chosen path begins x,v_1,... for x in {a,b,c}; if it is the right endpoint, every chosen path ends ...,v_k,x. This is precisely a common endpoint-extension pattern. No stronger conclusion is asserted here.

## Two adjacent occupied gaps

Suppose both gaps are occupied. They share one core vertex; write the local common order as ...,u,w,v,... with one occupied gap u|w and the other w|v, allowing the evident endpoint versions.

Choose x inserted in u|w and y inserted in w|v, and let z be the remaining special label.

Consider the sequence obtained from L by making both insertions: ...,u,x,w,y,v,...

Every consecutive triple of this sequence is known tight from the Hamilton path with x inserted or from the Hamilton path with y inserted, except possibly the cross triple (x,w,y). Indeed the local triples on the x side occur in the x-path, those on the y side occur in the y-path, and all triples away from the two occupied gaps occur unchanged in both paths.

If (x,w,y) were tight, the simultaneous sequence would be a Hamilton tight path on K union {x,y}. In the all-split support pattern, the remaining label z Hamiltonizes the opposite core K2. Hence (K union {x,y}) | (K2 union {z}) would be a spanning two-cover of H, impossible.

Therefore (x,w,y) is non-tight. Boundary antisymmetry gives the reverse triple (y,w,x) tight.

The endpoint-adjacent cases are identical: the only triple coupling the two insertions is still the cross triple through the shared old core vertex.

Thus absent core-order disagreement, one-gap concentration gives either an internal common-gap Hamiltonian four-set or a common endpoint-extension pattern, while two adjacent occupied gaps force an explicit reverse cross triple.