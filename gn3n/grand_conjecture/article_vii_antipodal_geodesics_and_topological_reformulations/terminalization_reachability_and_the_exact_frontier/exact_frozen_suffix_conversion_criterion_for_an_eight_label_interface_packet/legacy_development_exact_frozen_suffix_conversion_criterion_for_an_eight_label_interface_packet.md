# Exact frozen suffix conversion criterion for an eight label interface packet — preserved pre-item development

## Exact frozen-suffix conversion criterion for an eight-label interface packet

The eight-label conclusion in [[failed_rooted_absorption_two_covers_the_eight_label_interface_packet]] does not guarantee a two-cover attaching both interface vertices to the unchanged suffix.

Let A be a non-Hamiltonian six-vertex boundary tournament, and let x,y,z,q be fresh labels. Put W=A union {x,y}. Prescribe
h(t,x,y)=0 for every t in A,
h(u,v,z)=0 for all distinct u,v in W except h(x,y,z)=1,
and h(w,z,q)=0 for w in W-{y}, with h(y,z,q)=1.
Thus T=(x,y,z,q) is tight, and all six packet labels satisfy the wrong-way hook h(y,x,t)=1.

These prescriptions are consistent: their reversal orbits have different underlying supports, except for identical prescriptions. They impose no condition on the induced tournament on A. Complete every remaining orbit arbitrarily.

The three-hook theorem gives pc(W)<=2. Nevertheless, there is no two-cover of W union {z,q} in which one path is (L,z,q), where L contains at least two labels of W.

Proof. Since |L|>=2, its final ordered pair must be (x,y), since h(u,v,z) is positive only there. If |L|>=3, its preceding triple is (t,x,y) with t in A, which is zero. Hence L=(x,y). The remaining path would have to be Hamiltonian on A, a contradiction.

Consequently the valid unconditional obstruction is:
**pc(W)<=2 does not force a two-cover attaching at least two interface labels to the fixed suffix (z,q).** A cover with singleton y, or with the suffix as a separate path, is a genuinely different route and is not excluded.

In particular, retaining the entire original corridor T as a contiguous final segment is impossible: any nonempty packet prefix ends with a forbidden (t,x,y), while an empty prefix leaves non-Hamiltonian A as the other path.

This is a local obstruction to a proposed rooted inference, not a counterexample to the global two-cover conjecture. It identifies the necessary freedom in a conversion theorem: it must allow a singleton junction, separate the suffix, or change its boundary order; support-level two-cover existence alone does not guarantee attachment of both interface vertices.

More precisely, a two-cover retaining (z,q) as a contiguous final segment exists if and only if at least one of H[W] and H[A union {x}] is Hamiltonian. If its suffix path has no prefix, the other support is W. If its prefix has one label, that label must be y, leaving A union {x}. Prefixes of length at least two were excluded above. Conversely, either Hamilton support gives the cover W | (z,q), or (A union {x}) | (y,z,q), respectively. This equivalence is unconditional for the prescribed family; it does not assert that both Hamilton alternatives can simultaneously fail.

A concrete choice of A is the non-Hamiltonian six-label edge-order tournament verified in [[the_thirteen_label_attachment_certificate_is_not_exhaustive_even_with_non_hamiltonian_complement]]. Its internal prescriptions are disjoint from every new interface prescription.
