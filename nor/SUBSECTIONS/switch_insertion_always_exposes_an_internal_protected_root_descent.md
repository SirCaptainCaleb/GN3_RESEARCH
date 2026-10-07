# Switch insertion always exposes an internal protected root descent

## Metadata

- ID: switch_insertion_always_exposes_an_internal_protected_root_descent
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 4
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Insert x immediately after v_p in a deletion order of word 0^p1^q. Windows outside the x-packet are inherited; its left outside neighbor is zero and right outside neighbor is one whenever they exist. Hence any 10 descent forced by full counterexamplehood lies strictly inside the x-packet. Both windows contain x, giving a nonzero physical root without arbitrary permutohedron-carrier extraction. Compatible surgery remains unproved.

## Development

## Switch insertion always exposes an internal protected root descent

Let (h) be any reversal-odd binary label on ordered (r)-tuples. Let
[
O=(v_1,ldots,v_m)
]
be a genuine one-change deletion order in a minimum coordinate counterexample, with word
[
0^p1^q,
qquad p,q>0,
]
and let (x) be the omitted coordinate.

Form the full order
[
F=(v_1,ldots,v_p,x,v_{p+1},ldots,v_m),
]
i.e. insert (x) immediately after the coordinate (v_p).

### Theorem

The window word of (F) contains an adjacent descent
[
10
]
between two consecutive (r)-windows that both contain (x).

Equivalently, the switch insertion itself canonically exposes a nonzero protected descent root.

### Proof

The full instance is a counterexample, so (F) is not one-change. Hence its binary window word has at least two changes, and therefore contains a (10) descent.

All windows of (F) not containing (x) are unchanged windows of (O). Since the old word is (0^p1^q), no (10) descent can occur between two adjacent windows both avoiding (x).

It remains to exclude a (10) descent across either boundary of the contiguous packet of windows containing (x).

The windows containing (x) have start ranks
[
p-r+2,ldots,p+1
]
after clipping at the global endpoints.

- If the left packet boundary exists, the outside window immediately before the packet is unchanged from an old window whose start rank is at most (p). Its color is therefore (0). A boundary pair beginning with this outside window cannot be (10).

- If the right packet boundary exists, the outside window immediately after the packet is the shifted copy of the old start-((p+1)) window. Its color is (1). A boundary pair ending with this outside window cannot be (10).

Thus no (10) descent can occur outside the packet or across either packet boundary.

Since some (10) descent must exist, it lies strictly inside the packet. Both participating windows therefore contain (x). Sliding from the first to the second drops one old physical coordinate (a) and enters another old physical coordinate (c), producing the nonzero protected root
[
e_a-e_c.
]

### Consequences

1. **The pure-sign-jump exception disappears.**  
   Sections 201 and 203 localized an exceptional adjacent insertion edge where the obstruction could jump from the pre-switch side to the post-switch side without an extracted root. At the canonical switch insertion (F), such a jump is irrelevant: an internal protected (10) root exists unconditionally.

2. **No arbitrary carrier extraction is needed to obtain a root.**  
   Every one-change deletion witness already supplies a root certificate in the fixed order of all nonomitted coordinates.

3. **The remaining general-uniformity problem is strictly sharper.**  
   Starting from this canonical internal root, one must show that the protected root can be converted into a threshold-compatible replacement bridge, or that a finite collection of such canonical roots forces a Radon cycle admitting surgery.

4. Under reversal, a reversal-compatible rule such as choosing the lexicographically first internal descent relative to the ordered packet can be paired with the corresponding reversed rule to obtain opposite physical roots. The topological problem is therefore no longer existence of signed root labels, but extraction of a compatible surgery from their global arrangement.
