# Compatible full outward carriers after endpoint enlargement

## Composition

(none yet)

## Development

## Compatible full outward carriers after endpoint enlargement

Combine [[one_exception_endpoint_enlargements_have_contractible_outward_loci]] with [[face_monotone_positional_coarsening_gives_compatible_enlarged_protected_carriers]].

Let Q be a finite reversal-invariant poset of proper protected faces. For F in Q choose a positional cut set I(F) such that
G subset F implies I(G) subset I(F),
and I(tau F)=tau I(F).
Write H(F)=M_{I(F)}(F).

Assume H(F) is protected and has a distinguished free block T(F)=B(F) union {z(F)}, with B(F) nonempty. In that block choose either its first or its last position. Require every chamber whose label at that position belongs to B(F) to be outward. Choose first versus last compatibly under reversal. Other factors are unrestricted, so this is a uniform condition across every chamber in those factors.

**Theorem.** The full loci D_F=H(F) intersect X_{r+1} are nonempty contractible equivariant nested carriers. There is consequently an equivariant continuous map Delta Q -> X_{r+1} carried by D_F.

**Proof.** The endpoint-enlargement theorem, or its order-reversed form, proves each D_F contractible. Positional monotonicity gives H(G) subset H(F), hence D_G subset D_F. Reversal commutes with the prescribed enlargements and preserves the target, giving equivariance. Induct on antipodal pairs of simplices of Delta Q. A chain with largest face F has boundary already mapped into D_F; contractibility extends the map. Proper permutahedral face chains have no reversal-fixed simplices, so the paired construction is consistent. QED.

### Why this improves the earlier gluing criterion

The local contraction may use a different distinguished label z(F), endpoint position, and endpoint-subset target for each F. Those particular contraction targets need not be nested. The carriers are the full D_F, whose nesting follows from the ambient enlargements. Thus compatibility of local endpoint-subset targets is not an additional obligation in this sector.

The actual hypotheses still needed globally are monotone, reversal-compatible protected enlargements with the displayed uniform endpoint condition. Choosing a useful enlargement independently on every face does not establish monotonicity.

### A sharp limit of the elementary merging construction

Return to the concrete separated-window model, but allow arbitrary exit values
delta(w)=h(w,z_1,z_2) for w in B union {z},
with delta(z)=1 and all later suffix statuses zero.

The merged face H remains protected for every such exit assignment: strictly inward words have forms alpha,delta,0; delta,0,0; or longer words ending in two zeros. Thus protection alone does not force delta(u)=0 on reservoir labels.

Let u,v in B be a mutual admissible pair before z:
h(u,v,z)=h(v,u,z)=1.
The face G with terminal blocks {u,v}|{z} in the old B|{z} face is outward. Its elementary enlargement merges those blocks to {u,v,z}.

If delta(u)=1, this enlargement contains a chamber with final three distinguished-block labels z,v,u. Boundary antisymmetry gives
h(z,v,u)=1-h(u,v,z)=0.
Its selected determining word is therefore
0, h(v,u,z_1), 1,
which is either 001 or 011. This chamber is not outward. The same argument applies with u and v interchanged.

Consequently, if all outward mutual-pair faces are to be sent to whole outward faces by this merge operation, every vertex incident with a mutual edge must have zero exit status. For a chordless four-cycle this requires all four reservoir labels to have zero exit status.

These exit values concern separate boundary-reversal orbits from the old pair prescriptions and fixed suffix conditions; either value is consistent with the original protected four-cycle construction. The exit condition therefore cannot be inferred from that local construction alone.

This last statement obstructs this particular whole-face merging proof, not every possible filling in the enlarged locus. Other fillings, further positional enlargements, or a genuinely global hypothesis remain possible.
