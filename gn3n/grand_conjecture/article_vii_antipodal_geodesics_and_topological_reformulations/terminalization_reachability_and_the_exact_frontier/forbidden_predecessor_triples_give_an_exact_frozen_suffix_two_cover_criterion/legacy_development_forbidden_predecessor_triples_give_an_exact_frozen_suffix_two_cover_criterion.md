# Forbidden predecessor triples give an exact frozen suffix two cover criterion — preserved pre-item development

## Composition

(none yet)

## Development

## Forbidden predecessor triples give an exact frozen-suffix two-cover criterion

Let W be a finite vertex set disjoint from a fixed tight path S=(z,q,s_3,...), with |S|>=2, in a boundary 3-tournament. Define
J={v in W:h(v,z,q)=1}
and
E={(u,v):u,v in W, u!=v, v in J, h(u,v,z)=1}.
Suppose that for every (u,v) in E and every t in W-{u,v},
h(t,u,v)=0.

Then a spanning cover by at most two tight paths, one of which has S as a contiguous final segment, exists if and only if one of the following holds:
(1) H[W] is Hamiltonian;
(2) H[W-{v}] is Hamiltonian for some v in J;
(3) H[W-{u,v}] is Hamiltonian for some (u,v) in E.
Here the empty support is permitted and contributes no path.

Proof. Write the path containing S as (L,S), where L is an ordered subset of W. If |L|>=2, its last pair (u,v) belongs to E: its two junction triples are (u,v,z) and (v,z,q). If |L|>=3, the preceding label t produces the forbidden triple (t,u,v). Thus |L|<=2. The cases |L|=0,1,2 leave exactly the supports in (1),(2),(3), respectively, which must be Hamiltonian because only one other path is available. Conversely each displayed Hamilton support, together with S, (v,S), or (u,v,S), respectively, gives the required cover. No later suffix label affects the criterion.

This elevates [[exact_frozen_suffix_conversion_criterion_for_an_eight_label_interface_packet]] from one prescribed pair and six packet labels to arbitrary packet size, arbitrary tight suffix length, and any collection of allowed interface pairs. The criterion retains the ordered pair: unordered support Hamiltonicity does not replace the junction tests.

The hypothesis is a condition on actual consecutive triples, not cyclic rotations. It need not hold in every failed-absorption state. When it does hold, the remaining rooted problem is exactly a Hamiltonian deletion problem with at most two deleted packet vertices.
