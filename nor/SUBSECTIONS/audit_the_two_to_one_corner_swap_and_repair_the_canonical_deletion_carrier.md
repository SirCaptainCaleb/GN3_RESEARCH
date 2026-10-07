# Audit the two-to-one corner swap and repair the canonical deletion carrier

## Metadata

- ID: audit_the_two_to_one_corner_swap_and_repair_the_canonical_deletion_carrier
- Parent Section: directed_nor_union_closed_bridge
- Position: 176
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The proposed 2|1 corner collapse in §164 omits the changed outer window alpha(x,u,a)->alpha(x,u,b); a specified globally flat tournament leaves four changes after the swap. The r=1 wrap word in §166 also has four changes, not two. Nevertheless reversing the deletion witness repairs the canonical profile to 1,p,q,2. In a minimum flat alternating counterexample p,q>=3 by §171, and the 1|p and q|2 barriers are fully curved. The remaining 2|1 corner is not proved flat, so §169's packet surgery remains conditional. Canonical profile existence and global convex-run maximality have not been proved simultaneous.

## Development

This audits §§164,166,169. Work with an alternating ternary orientation.

Missing outer window in §164. For the order
...,x,u,a,b,c,d,e,...,
swapping a,b changes FOUR windows:
alpha(x,u,a) -> alpha(x,u,b),
alpha(u,a,b) -> alpha(u,b,a),
alpha(a,b,c) -> alpha(b,a,c),
alpha(b,c,d) -> alpha(a,c,d).
The first is not controlled by full curvature of {a,b,c,d}. It is omitted from §164's closing argument.

Symbolic globally coboundary-flat counterexample to the local closing claim. On vertices 0=x,1=u,2=a,3=b,4=c,5=d,6=e,7=f, define a tournament by t(i,j)=1 for i<j precisely on
01,12,23,34,45,56,67,02,35,03,25,
and t(i,j)=0 on every other increasing pair. Set t(j,i)=1-t(i,j), and alpha=1 xor the three cyclic edge bits. This construction has zero tetrahedral coboundary everywhere.

The cyclic order (x,u,a,b,c,d,e,f) has word
1,0,0,1,0,0,1,1,
hence four changes and profile 1,2,3,2 up to rotation.
The tetrahedron {a,b,c,d} is fully curved:
alpha(a,b,c)=0, alpha(b,c,d)=1,
alpha(a,b,d)=1, alpha(a,c,d)=0.
After swapping a,b the word is
0,1,1,0,0,0,1,1,
still with four changes. In particular alpha(x,u,a)=1 but alpha(x,u,b)=0. This refutes the advertised immediate collapse, not NOR.

Wrap counting in §166. From a deletion carrier O of word 0^p1^q and its perfect blocker x, the prepended linear word is 1,0^p,1^q. The first wrap bit is 0. If the second wrap bit r is 1, the cyclic word
1,0^p,1^q,0,1
has FOUR changes, not two. Its run lengths are 2,p,q,1 up to rotation. If r=0, the profile is 1,p,q,2.

Useful repair. When r=1, instead prepend x to the REVERSED deletion order. Reversal oddness gives the linear word 1,0^q,1^p; its wrap bits are now 0,0. Therefore a minimum counterexample in the flat alternating sector still admits a canonical cyclic profile 1,p,q,2 after exchanging p,q if necessary. The existing singleton-insertion lemma gives p,q>=2; the newly read §171 strengthens this to p,q>=3 by an explicit endpoint reorder valid for every opposite run length. That proof does not rely on the invalid wrap-flatness claim.

Two valid forced full barriers. The transition 1|p is fully curved by the endpoint perfect-blocker calculation in §163. The transition q|2 is also fully curved: on the ordered tetrahedron
(v_{m-2},v_{m-1},v_m,x)
the consecutive colors are 1,0 and the off-face alpha(v_{m-2},v_{m-1},x)=s_{m-2}=0, because q>=2. Zero coboundary then forces the other off-face to be 1, giving the full pattern.

The opposite 2|1 transition is NOT proved flat by §164. Consequently §169's endpoint surgery is conditional on that flatness; its downstream packet calculation may be retained under an explicit flat-corner assumption.

Extremality caution. Existence of a canonical 1,p,q,2 witness does not show that a GLOBAL maximum of sum r_i^2 among all four-change orders retains this profile. Conversely, maximizing only within the canonical subclass does not permit a contradiction using a repair that leaves that subclass. The conditional extremal lemmas §§120-122 must not be stacked with deletion minimality without a preservation or selection theorem.
