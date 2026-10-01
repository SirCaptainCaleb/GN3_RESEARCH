# Defect-window distance recovers minimum deletion side; local sign regularity needs extra input

## Statement

For a deletion cover H-x=P|Q with canonical spanning order P,x,Q, the number of vertices lying outside the three-center defect window on the nearer side is min{|P|,|Q|}-1 (up to an additive constant under equivalent endpoint-distance conventions). Thus minimizing this primary defect-window distance over deletion states is equivalent to the already certified minimum-deletion-side normalization. The local failed-insertion signs themselves have no forced interval or no-ABAB structure: certified constructions realize arbitrary sign alternation. This does not rule out every potential defined on sign words, but any monotonicity theorem for such a potential must use additional move-specific or nonlocal support/order information rather than failed insertion alone.

## Body

# Proof

Write the deletion cover as

H-x=P|Q,

with

P=(p_0,...,p_m),  Q=(q_0,...,q_s),

and consider the canonical spanning order

p_0,...,p_m,x,q_0,...,q_s.

Its possible defects are confined to the three consecutive centers

p_m, x, q_0.

The vertices lying strictly to the left of this three-center window are

p_0,...,p_{m-1},

so their number is |P|-1. Similarly the vertices strictly to the right are

q_1,...,q_s,

so their number is |Q|-1. Therefore the nearer-side count is

min{|P|-1,|Q|-1}=min{|P|,|Q|}-1.

Equivalent conventions measuring edge-distance from the window to the nearer endpoint alter this only by an additive constant. Consequently minimizing the primary defect-window distance over all deletion covers is exactly equivalent to minimizing the smaller path order among deletion covers.

That normalization is already the minimum-deletion-side parameter used by the certified minimum-side state machinery. Thus the proposed primary coordinate does not introduce a new well-founded descent.

For the suggested secondary local orientation code, the certified local insertion fence 7f28428bc739 shows that boundary antisymmetry plus failure of insertion into one displayed path imposes no interval or no-ABAB condition on the relevant left/right side signs: arbitrarily long alternation can occur.

This observation does not by itself rule out every numerical potential whose input is a sign word, because monotonicity also depends on which transformations between sign words are actually available. What it does rule out is obtaining monotonicity merely from an intrinsic regularity of failed-insertion signs. Any successful secondary descent proof must therefore use additional information about the allowed move, global maximality, support changes, relative orders across deletion states, endpoint data, or another nonlocal state variable.

Thus the well-founded defect-window brainstorm has genuinely new content only if it supplies such an additional transformation-sensitive invariant on moves preserving the already-minimized smaller path order.