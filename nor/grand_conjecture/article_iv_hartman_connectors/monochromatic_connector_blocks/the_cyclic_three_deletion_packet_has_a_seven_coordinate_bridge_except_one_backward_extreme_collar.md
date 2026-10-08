# The cyclic three-deletion packet has a seven-coordinate bridge except one backward-extreme collar

## Composition

Three coherent fully ported deletion covers reconstruct a whole-shore ported two-path cover unless their omitted triple forms one cyclic comparison packet (§44). For the cyclic case, six inherited left/right collar zeros imply a constant XOR of incidences to its two shore neighbors. Explicit seven-coordinate orders using independently placed x,z repair every internal collar pattern except R→D→L; the two fixed-neighbor terminal orders and both endpoint ports are retained. A cyclic packet at either endpoint of its class has a direct one-sided zero replacement. Hence three coherent ONE-PATH deletion witnesses yield a compatible spanning connector—and full homogeneous-cut NOR closure—unless the omitted labels form an internal cyclic packet with R dominating all three and all three dominating L. This is a certified local/one-path reduction; two-path witness reconciliation and the backward-extreme internal sandwich remain open.

## Development

# A seven-coordinate bridge repairs every cyclic three-deletion packet except the backward-extreme sandwich

Work in the normalized flat tournament z -> A -> x. Put
h(u,v,w)=1 xor t(u,v) xor t(v,w) xor t(u,w),
where t(u,v)=1 iff u->v. Let D={a,b,c} lie in the cyclic-comparison exception of the three-coherent-deletion-cover theorem, with cyclic comparison a<b, b<c, c<a. Assume this packet has immediate shore neighbors L and R in its reconstructed class. The three coherent deletion covers furnish the six zero collars
h(L,a,b)=h(L,b,c)=h(L,c,a)=0
and
h(a,b,R)=h(b,c,R)=h(c,a,R)=0.
Their next exterior windows are inherited whenever the corresponding neighbor exists.

**Theorem (relative seven-coordinate bridge).** Define l_d=t(L,d), r_d=t(d,R) for d in D. The six collar equations imply l_d xor r_d=k independent of d. Unless l_a=l_b=l_c=k=0, there is a zero order on {L,R,a,b,c,x,z} beginning with L, ending with R, and having a shore vertex immediately after L and immediately before R. The following three explicit templates, up to cyclic relabeling of (a,b,c), cover all the permitted patterns:

I. (L,a,x,z,b,c,R), if l_a=1 and l_b=l_c. 

II. (L,a,b,x,z,c,R), if l_a=l_b and r_c=1.

III. (L,a,z,b,x,c,R), if (l_a,l_b,l_c)=(1,0,1) and k=0.

In the remaining pattern, r_d=l_d=0 for every d, so R dominates D and D dominates L. There is NO zero order of these seven coordinates that begins with L, ends with R, and has shore coordinates immediately inside both endpoints. This is a local, fixed-two-collar impossibility, not a nonexistence claim for a larger connector or a two-sided repair.

**Proof.** For any consecutive cyclic comparison d<e, the two collar equations give
t(d,e)=1 xor l_d xor l_e = 1 xor r_d xor r_e.
Hence l_d xor r_d is independent of d.

For template I, the five successive interior triple statuses are
h(L,a,x)=1 xor l_a,
h(a,x,z)=0,
h(x,z,b)=0,
h(z,b,c)=1 xor t(b,c),
h(b,c,R)=0.
The stated l conditions make the first and fourth zero, since t(b,c)=1 xor l_b xor l_c.

For template II, the statuses are
h(L,a,b)=0,
h(a,b,x)=1 xor t(a,b),
h(b,x,z)=0,
h(x,z,c)=0,
h(z,c,R)=1 xor r_c.
The conditions make both variable bits zero.

For template III, the statuses are
h(L,a,z)=1 xor l_a,
h(a,z,b)=t(a,b),
h(z,b,x)=0,
h(b,x,c)=t(b,c),
h(x,c,R)=1 xor r_c.
For (l_a,l_b,l_c)=(1,0,1), both t(a,b) and t(b,c) equal zero. The equality k=0 gives r_c=l_c=1, so all five statuses vanish.

To prove that the three templates cover every nonexceptional case, classify the binary triple (l_a,l_b,l_c). If it is all ones, template I works. If it has one 1 and two 0s, cyclically place the unique 1 first and use I. If it has two 1s and one 0, put the unique 0 last; template II works for k=1, while for k=0 put that 0 in the middle and use III. If all three are 0, template II works exactly when k=1. This leaves only all l_d=0 and k=0.

For local impossibility in that remaining case, the shore D forms the directed cycle a->b->c->a in the cyclic-comparison orientation, and R->D->L. Consider any proposed zero order L,d,e,...,f,R with d,e,f the three D vertices and x,z elsewhere. Since h(L,d,x)=h(L,d,z)=1, the next coordinate e after d must lie in D. Zero of h(L,d,e) forces d->e. The third D coordinate f then obeys e->f and h(d,e,f)=1, so the next coordinate after e must be x or z. If it is x, the next coordinate must be z (because h(e,x,f)=1), after which h(z,f,R)=1. If it is z, either possible continuation gives h(e,z,x)=1 or h(e,z,f)=1. Thus no zero order with the stated fixed endpoints and shore-inside conditions exists.

**Exterior-collar consequence.** The templates retain the outer shore coordinates L,R and choose their immediate inner neighbors among D. In the three-deletion setup, a preceding ordered collar (K,L,d) and following collar (d,R,S), if present, has zero status for every d in D: each appears as the first or last member of the packet in one deletion witness. Thus each template is a zero replacement across the complete shore exterior collar when x,z are available for relocation, and both far endpoint ports are inherited from the deletion witnesses.

**Closure scope.** If the three deletion covers each consist of a single fully ported shore path, the cyclic packet has both neighbors, and the pattern is not the backward-extreme sandwich, a template produces a whole-shore compatible zero connector directly. The homogeneous-cut theorem then produces a full NOR order. With a second shore path, the templates provide a local zero-packet realization; routing x,z away from their old positions and merging that second path remain separate global obligations. When the packet touches a class endpoint, the one-sided collar and terminal port must be analyzed independently.

**Endpoint packet resolution (elevation).** If the cyclic D packet begins its reconstructed path, each forward comparison d<e among the cyclic pair orders occurs as the initial pair of a ported deletion path. Thus t(a,b)=t(b,c)=t(c,a)=1. If R is the next shore vertex, the zero word
(a,x,z,b,c,R,...)
replaces the cyclic packet and preserves every subsequent shore window: h(a,x,z)=h(x,z,b)=h(z,b,c)=0, while h(b,c,R) and its following windows come from F_a. Its first edge a->x is forward and its far last port is inherited. If D is the whole class, (a,x,z,b,c) is already a compatible zero connector. Symmetrically, if D ends its class and L precedes it, the zero word
(...,L,a,b,x,z,c)
uses h(L,a,b)=h(a,b,x)=h(b,x,z)=h(x,z,c)=0; its last edge z->c is forward and its initial port is inherited. If the whole class is D, the five-coordinate base applies.

**Single-path three-cover corollary.** Suppose each of the three coherent deletion covers has ONE fully ported zero path (so the reconstructed class is all A). Their compatible global reconstruction closes unless the three labels form a cyclic internal packet whose immediate shore neighbors satisfy R->D->L. An acyclic packet closes by the three-cover theorem; cyclic endpoint packets close by the displayed one-sided replacements; cyclic internal packets close by templates I--III unless the backward-extreme pattern holds. This is a sufficient NOR-closure theorem with a single sharply localized residual configuration; it does not cover two-path deletion witnesses without a separate x,z routing step.
