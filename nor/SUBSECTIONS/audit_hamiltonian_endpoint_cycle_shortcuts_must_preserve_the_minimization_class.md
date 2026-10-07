# Audit: Hamiltonian endpoint-cycle shortcuts must preserve the minimization class

## Metadata

- ID: audit_hamiltonian_endpoint_cycle_shortcuts_must_preserve_the_minimization_class
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 129
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The recent Hamiltonian endpoint-cycle exclusion is unproved: a stopped-pivot root may lie on a bad deletion word 0,1,0^(p-2),1^q, and a shorter mixed circuit does not contradict endpoint-family minimality. Minimizing only Hamiltonian cycles also cannot exclude proper-support shortcuts. Unrestricted reversal-closed raw transition families already contain trivial two-circuits. Endpoint descent must preserve an explicit admissible witness class; §128 achieves this in the second-splice-zero branch and resolves phase-three pinned stops. Corner lifting and the long-phase double-one stop remain open.

## Development

## Audit: endpoint-cycle minimality must survive every replacement

The local endpoint pivot calculations in roots §§113,119,123-125 produce real coordinate orders and physical roots. However the claimed exclusion of Hamiltonian endpoint cycles in §§121/124 is not yet established, even conditional on corner lifting.

### Exact class change in the first-stop branch

Let O_x=(a,b,c,d,e,...) have word 0^p1^q, p>=3, and let alpha(a,c,d)=1.
Deleting b from the prepended state yields
(x,a,c,d,e,...)
with exact word
0,1,0^(p-2),1^q.
This is not a good deletion witness. Its root x->d therefore need not belong to the family of endpoint roots obtained by prepending an omitted coordinate to a good deletion order.

The directed chord x->d and an old cycle segment do form a shorter positive PHYSICAL root cycle when d lies on the old support. But that cycle may contain a non-endpoint root. Minimum length within the endpoint family cannot exclude it.

The missing premise is either a witness-preserving conversion of that chord into an admissible endpoint root, or an extraction theorem for the mixed family to which the shorter circuit belongs. Root §128 supplies such a conversion in a specific second-splice-bit branch, and resolves phase length three at pinned junctions.

### Two different notions of minimum

A cycle chosen to be shortest among Hamiltonian cycles cannot be contradicted by a proper-support shortcut: the new cycle is outside the minimization class.

A cycle chosen shortest among ALL admissible endpoint cycles can be contradicted by a shorter endpoint cycle, but it need not be Hamiltonian in the first place.

Thus the valid conditional target is to exclude the hypothesis that a globally shortest admissible endpoint cycle is Hamiltonian. Even that exclusion requires retaining the endpoint class at every step. It does not imply that no Hamiltonian endpoint cycle exists in the instance.

### Why unrestricted mixed-root minimality is insufficient

Enlarging the family to all actual transition roots removes the class mismatch but also destroys the intended obstruction.

For any coordinate order pi containing a transition on consecutive windows with packet (a,b,c,d), full reversal gives packet (d,c,b,a). Reversal-oddness makes the status word complement-reverse, so the transition has the SAME direction (01 remains 01, and 10 remains 10). Its physical slide root changes from e_a-e_d to e_d-e_a.

Consequently a reversal-closed family of raw actual transition roots containing any transition already contains a two-edge positive circuit. Such a circuit says nothing about a spanning NOR-good order. The same warning applies to any proposed mixed family unless its retained witness and orientation restrictions exclude these trivial reversed pairs or provide an actual extraction for them.

Therefore global minimum mixed-circuit length is not a substitute for provenance-preserving endpoint surgery. It must be defined within an explicit compatible state class, with a theorem showing each replacement remains in that class.

### Correct live theorem and closure obligation

A realized pinned junction a->x->c offers:
- first splice bit zero: a genuine endpoint pivot b->c;
- first splice bit one: a raw stopped transition x->d, which alone does not justify endpoint minimality;
- additionally, second splice bit zero: root §128 gives a genuine endpoint root c->a;
- phase length three and second splice bit one: root §128 gives strict deletion-phase descent.

The remaining endpoint obligations are the unproved corner lift and the long-phase stopped branch with both splice bits one. The topological route likewise still requires a carrier on compatible realized states and a terminating extraction from its forced zero. Neither formal physical cancellation nor a shorter circuit in a larger class closes r=3 NOR.
