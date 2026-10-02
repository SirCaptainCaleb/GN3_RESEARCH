# Opposite crosswise endpoint covers force order disagreement, radius-two transport, or reciprocal double crossing

## Statement


Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, let A=(a_0,...,a_{lambda-1}) be globally longest, and let U=V(H)-V(A). Suppose exact endpoint covers of H-a_0 and H-a_{lambda-1} each have exactly two crossings across the corresponding A|U cut and lie in the crosswise four-block case. Then at some stage one obtains inherited relative-order disagreement, an explicit endpoint reversal, or a restored D=1 state at Johnson distance two; otherwise the two endpoint covers have their forced neutral orientations, their induced covers of H-{a_0,a_{lambda-1}} exhibit bridge disagreement, and—if that disagreement is in support partition rather than common-support order—each induced cover crosses the other's support partition at least twice. In particular a singleton support exchange cannot remain order-neutral.


## Body


# Opposite crosswise endpoint covers force order disagreement, radius-two transport, or reciprocal double crossing

Let H be a minimum counterexample in the sharp half-order shell
|V(H)|=2lambda+1. Fix a globally longest tight path
A=(a_0,...,a_{lambda-1})
and put U=V(H)-V(A).

Assume first that T is an exact two-cover of H-a_0 with exactly two crossings across
(A-{a_0})|U, in the crosswise four-block case. Cutting the two crossings gives two nonempty A-blocks B_1,B_2 and two nonempty U-blocks C_1,C_2, with each component consisting of one B-block and one C-block.

If a B-block is not ordered as the restriction of A, we already have inherited relative-order disagreement. Otherwise a_1 and a_2 must lie in different B-blocks. Indeed, if both lie in one inherited-order block B_1, then they are the first two vertices of B_1. If the mixed component is (B_1,C_1), prefixing a_0 gives the tight path (a_0,B_1,C_1) of order lambda+1. If it is (C_1,B_1), then the other B-block is nonempty, so |B_1|<=lambda-2 and |C_1|>=2; then
(C_1,a_1,a_2,...,a_{lambda-1})
is tight of order at least lambda+1. Both contradict maximality.

Now consider a mixed component oriented B_i followed by C_i. If |B_i|=1, the exact crosswise-restoration formula gives a restored D=1 support at Johnson distance two from U. If |B_i|>=2 and b_0,b_1 are the first two vertices of B_i in inherited A-order, then (a_0,b_0,b_1) cannot be tight, since otherwise (a_0,B_i,C_i) would have order lambda+1. Boundary antisymmetry therefore gives the explicit tight reversal
(b_1,b_0,a_0).

Consequently, if there is no inherited-order disagreement, explicit endpoint reversal, or radius-two restoration, both components of the left endpoint cover are forced into the neutral orientation
C_i followed by B_i.
The right endpoint statement is symmetric: in a neutral crosswise cover of H-a_{lambda-1}, the last two surviving A-vertices lie in different A-blocks and both mixed components have orientation
B_i followed by C_i.

## Comparing the two neutral endpoint states

Let T_L and T_R be neutral crosswise covers of H-a_0 and H-a_{lambda-1}. In T_L, the component containing y=a_{lambda-1} ends at y. In T_R, the component containing x=a_0 begins at x.

Apply the endpoint-state trichotomy to T_L, endpoint y, and the cover T_R of H-y. Internal restoration is impossible because x is an endpoint of T_R. The clean omission-swap branch is also impossible: deleting y from T_L and x from T_R would give the same ordered two-deletion cover, and clean swap would force x to be restored at the same terminal end at which y is restored. But neutrality of T_R makes x the initial endpoint of its component. Since every component has order lambda>=3, initial and terminal endpoints are distinct.

Hence the only remaining branch is bridge disagreement between the two induced exact covers of
H-{a_0,a_{lambda-1}}.
This disagreement is either support-partition crossing or, on a common support, relative-order disagreement such as a reversed common edge, reversing tight triple, or vertex-simple tight cycle.

## A singleton support exchange is endpoint-localized

Write the two induced covers as
C=P|Q and C'=P'|Q',
with |P|=|P'|=lambda and |Q|=|Q'|=lambda-1.
Suppose the support partitions differ and C' has exactly one ordinary crossing edge relative to V(P)|V(Q).

Cutting that edge yields three monochromatic blocks. The P-side cannot form one block, because then all lambda vertices of P together with a nonempty Q-block would lie in one component of C', producing a path longer than lambda. Thus the P-side has two blocks and the Q-side one. The unique Q-block contains all lambda-1 vertices of Q, so the attached P-block must be a singleton {p}. Therefore
V(P')=V(Q) union {p},
V(Q')=V(P)-{p}.

Assume now that the common-support orders are preserved. Write
P=(p_0,...,p_{lambda-1}).
Neutrality at the right endpoint restores x=a_0 initially to Q'=P-{p}, so (x,P-{p}) is tight. If p=p_j with j>=2, then (x,p_0,p_1) is tight and (x,P) would be a path of order lambda+1. Hence p is one of p_0,p_1.

This yields explicit reversal data. If p=p_0, then (x,p_1,p_2) is tight, while tightness of (p_0,x,p_1) would Hamiltonize P union {x}; hence (p_1,x,p_0) is tight. If p=p_1, the same argument gives (p_0,x,p_1) tight. Thus, if s is the other of p_0,p_1,
(s,x,p)
is tight.

At the opposite end, neutrality at the left endpoint restores y=a_{lambda-1} terminally to Q, so (Q,y) is tight. Since P'=Q union {p} preserves the relative order of Q, maximality forces p to occupy one of the last two positions of P'. If p is last, the failure of (Q,p,y) forces the reverse triple (y,p,q_m); if p is penultimate, appending y can fail only at (p,q_m,y), forcing (y,q_m,p). Thus a singleton bridge exchange is localized simultaneously to the first two positions of P and the last two positions of P', with explicit reversal triples at both omitted endpoints.

## Neutral endpoint orders exclude singleton exchange

The singleton exchange cannot in fact survive in the neutral order branch. In T_L, the component containing y has form
C_U followed by B_A,
where C_U is a nonempty U-block and B_A an inherited A-block ending at y. The radius-two branch is absent, so B_A is not a singleton. After deleting y, the common component Q therefore contains some u in U preceding some a in A.

But P'=Q union {p} is a full component of the neutral right endpoint cover, and every such component has an inherited A-block followed by a U-block. Hence the same a precedes the same u in P'. The common pair {u,a} is ordered oppositely in Q and P', giving relative-order disagreement.

Therefore, absent inherited/common-support order disagreement and absent radius-two restoration, an exactly-one-crossing support exchange is impossible. Applying the same argument with the two induced covers interchanged shows that each cover crosses the other's support partition at least twice.

Thus opposite crosswise endpoint covers yield one of the bridge's bounded outputs:
relative-order disagreement, an explicit endpoint reversal, radius-two D=1 transport, or reciprocal double crossing of the common two-deletion covers.
