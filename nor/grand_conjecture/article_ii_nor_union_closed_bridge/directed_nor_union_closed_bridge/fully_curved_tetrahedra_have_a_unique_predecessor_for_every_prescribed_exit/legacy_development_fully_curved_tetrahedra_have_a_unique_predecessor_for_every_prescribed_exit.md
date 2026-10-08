# Fully curved tetrahedra have a unique predecessor for every prescribed exit — preserved pre-item development

## Composition

(none yet)

## Development

Let alpha be a pure alternating triangle orientation, and let Q={a,b,c,d} be fully curved: every pivot link on Q is a directed triangle. Fix an ordered pair (c,d) in Q and any exterior vertex v.

Lemma: unique exit predecessor. Exactly one of the two vertices in Q minus {c,d}, denoted b, satisfies alpha(b,c,d)=alpha(c,d,v). Let a be the other. Then (a,b,c,d,v) has word (1-sigma,sigma,sigma), where sigma=alpha(c,d,v). Proof: in the pivot link at c, the vertex d has one outgoing and one incoming edge to the other two vertices. Thus their two alpha(b,c,d) values are opposite, and precisely one matches sigma. Full curvature of Q then forces alpha(a,b,c)=1-alpha(b,c,d). This proves both uniqueness and the stated word.

Equivalently, for any fixed terminal triple (c,d,v), exactly one of the orders (a,b,c,d,v) and (b,a,c,d,v) avoids a return switch. A fully curved tetrahedron is not merely an unavoidable switch: it is a switch that can be attached in a prescribed direction to any exterior continuation by choosing its first two vertices in the right order.

Monochromatic suffix extension. More generally let P=(c,d,v,... ) be any sigma-monochromatic path, and let a,b be outside its support with {a,b,c,d} fully curved. Choosing their order by the lemma gives a one-change order spanning P union {a,b}, with word (1-sigma),sigma,sigma,... . This is an actual extension mechanism; it does not require P plus {a,b} to be all of V. If it is all of V, NOR follows immediately. If P already has one genuine switch, this operation can add a second switch, so it is not an unrestricted absorption rule.

Refinement of the five-face Sperner label. When a five-face W has no flat tetrahedral facet, Subsection 75 labels it by the unique vertex v opposite its fully curved facet Q. The lemma supplies a compatible exit choice on a refined flag carrying Q, the ordered terminal pair (c,d), and v: label/select the unique predecessor b in Q minus {c,d} matching the outgoing triangle sign. This resolves the return-switch ambiguity for that local packet. It retains the coface and ordered pair, which a support-only label loses.

Transport identity. Write T_v(p,q)=alpha(v,p,q) and let kappa be the tetrahedral coboundary on {v,b,c,d}. The sum of face parities is invariant under a change of vertex ordering, because an adjacent transposition changes exactly two face parities. Therefore alpha(b,c,d)=kappa xor T_v(b,c) xor T_v(b,d) xor T_v(c,d). Matching the exit sign T_v(c,d) is equivalent to T_v(b,c) xor T_v(b,d)=kappa. In a no-flat five-face this coface tetrahedron is singly curved, so kappa=1: the selected predecessor b must compare c and d in opposite directions in the pivot link of v. Thus the curvature bit now determines a specific continuation label, rather than merely marking an obstruction carrier.

Remaining global gap. Compatibility of these predecessor choices across overlapping packets, and incorporation of the original middle-vertex defect field, are not proved. The local labeling and suffix extension are valid without claiming a global Sperner or connector conclusion.
