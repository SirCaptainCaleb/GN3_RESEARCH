# A four-cycle five-support has a thirteen-label attachment certificate — preserved pre-item development

## Development

## A four-cycle five-support has a thirteen-label attachment certificate

Let S={a,b,c,d,z} have the mutual four-cycle a-b-c-d-a before z. Suppose its complement has a displayed two-cover P|Q, where P and Q are nonempty tight paths. Write R_u for the explicit tight four-path on S-u from [[a_mutual_terminal_pair_star_gives_rooted_four_paths_and_four_hamiltonian_deletions]], for each u in {a,b,c,d}.

The following sufficient tests give a spanning two-cover without prescribing any unproved Hamilton-path endpoint.

### Joining the complementary paths through a cycle label

For u in {a,b,c,d}, the sequence (P,u,Q) is tight if and only if all defined seam triples below are tight:
h(p_{m-1},p_m,u)=1 when |P|=m>=2,
h(p_m,u,q_1)=1,
h(u,q_1,q_2)=1 when |Q|>=2.

If this holds, R_u | (P,u,Q) is a spanning two-cover. The order (Q,u,P) gives a second test with the same actual path orientations.

Consequently, in a tournament with no spanning two-cover, no cycle label can join P to Q in either direction. This holds for every two-cover of the complement, including every valid repartition of P|Q. It is stronger than merely saying that a particular joining test has too few candidates: all four guaranteed Hamiltonian deletions are usable.

### Assigning a rooted four-path and its deleted singleton to the two tails

For any tight path A=(a_1,...,a_l), say that a displayed tight path T can attach to A if either (A,T) or (T,A) is tight. This definition keeps the actual order of both paths. For the singleton {u}, attachment means ordinary prepending or appending.

If T=R_u=(v,r,z,s), its attachment tests are:
- (A,R_u): h(a_{l-1},a_l,v)=1 when l>=2, and h(a_l,v,r)=1.
- (R_u,A): h(z,s,a_1)=1, and h(s,a_1,a_2)=1 when l>=2.

For the singleton u:
- (A,u): h(a_{l-1},a_l,u)=1 when l>=2.
- (u,A): h(u,a_1,a_2)=1 when l>=2.
If A has order one, both singleton attachments are vacuously tight.

For each u form a bipartite graph with left vertices the two displayed paths R_u and {u}, and right vertices P,Q. Include an edge exactly when the corresponding attachment succeeds in at least one of these actual orders.

**Attachment theorem.** A matching covering both left vertices gives a spanning two-cover of H. The two new paths are the successful concatenations of the matched pairs.

**Proof.** R_u and {u} partition S, while P and Q partition its complement. A matching assigns the two disjoint parts of S to different complementary paths. The seam tests guarantee tightness of both concatenations. Their supports are disjoint and span H. QED.

By the two-by-two case of Hall's theorem, absence of such a matching is equivalent to an empty left row or an empty right column. Thus for each cycle deletion a no-two-cover tournament must have either:
- one of R_u and {u} unable to attach to either complementary path; or
- one of P and Q unable to accept either R_u or {u}.
This describes failure of these attachment tests, not failure of every possible repartition.

### The attachment conditions couple opposite cycle deletions

R_a and R_c share their terminal pair (z,s), with s=d if t=1 and s=b otherwise. Therefore the tests for (R_a,P) and (R_c,P) coincide:
h(z,s,p_1)=1,
h(s,p_1,p_2)=1 when |P|>=2.

If those tests hold and either a or c attaches as a singleton to Q, the matching gives a two-cover. Hence a no-two-cover state satisfying the shared terminal test must forbid singleton attachment of both a and c to Q. The same statement holds after exchanging P,Q.

The other opposite pair b,d has the corresponding shared terminal pair determined by e=h(a,z,c). Thus one cannot treat the four rooted deletions as unrelated arbitrary Hamilton orders.

### Finite support of the certificate

Every test uses only S and the first two or last two vertices of P and Q. Their union has at most
5+4+4=13
labels, regardless of the lengths of the inherited paths. Each individual test uses at most nine labels.

This is a finite attachment certificate, not an upper bound on the order of a counterexample and not a proof that some test must succeed. It makes the surviving global carrier-loop interface a Hamiltonian five-support with four explicitly rooted deletions facing two specified path boundaries. A closure argument still must rule out simultaneous failure or provide a different repartition.

### Placement in the Article VII frontier

[[a_mutual_four_cycle_with_hamiltonian_complement_already_gives_a_spanning_two_cover]] excludes the Hamiltonian-complement case outright. When the complement is non-Hamiltonian but has a two-cover, the present tests apply directly. If no complement two-cover is available, that hypothesis requires a separate proof before these tests can be used.

The rooted paths here are derived solely from boundary antisymmetry, so they avoid the cyclic-rotation gap recorded in [[audit_cyclic_rotation_invalidates_the_new_descent_and_second_layer_claims]].
