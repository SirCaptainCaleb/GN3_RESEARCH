# Directed one-gap graph: affine asymmetry and uniform failure of global connectivity

- Stable ID: note_nori_onegap_directed_obstructions_asym_and_nonconnected_r11913
- Author: NORI1 independent researcher session_nori_r11913_3
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: nori1, one-gap, directed-graph, antipodal-strong-components, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_3
- Updated session: session_nori_r11913_3
- Disposition: none
- Successor: none

## Related references

- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

## Two false strengthenings of one-gap antipodal forcing

Let m≥3 and consider the legal paired-flat model on Q_(2m), with pair (0,1) free and all other gates fixed. A **one-gap witness** is a rooted full direction permutation (P,a,t,1−a,S), with a∈{0,1}, t≥2, whose edges outside pair zero are red. Let u and v=u⊕e_t be its outside-pair states at the two free steps. The witness gives the clause excluding f_0(u)=a,f_0(v)=1−a. Encode avoidance by an arc u→v when a=1 and v→u when a=0. The arc collection is H. Let H^* adjoin v̄→ū for every u→v; bars are complements of all 2m−2 outside bits. An antipodally odd f_0 avoids all one-gap red full geodesics iff it is isotone on H^*. Thus one-gap forcing for every legal f_0 is equivalent to an SCC of H^* containing u and ū for some u.

**Proposition 1 (affine Q8 asymmetry).** With fixed gates
f_1=x_0⊕x_4⊕x_6, f_2=x_0⊕x_2⊕x_6, f_3=x_0⊕x_2⊕x_4,
the directed graph H contains 0→e_2 but does not contain e_2→0.

**Proof and small finite certificate.** Each displayed function omits its own pair and has odd global antipodal parity. Starting at full vertex 96, the word (5,6,1,2,0,3,4,7) uses all eight directions once and has every nonfree edge red. Its two free steps require f_0(0)=1 and f_0(e_2)=0, yielding 0→e_2.

For a reverse arc, a witness can be reversed to place its first free direction 0 at outside state u=0 and its second free direction 1 at v=e_2. Let sh∈{0,1,2,3} represent the two initial free bits and encode the six outside directions (2,...,7) by masks 1,2,4,8,16,32. The intervening direction 2 is red only for sh=1 or sh=3. In both cases, a red prefix ending at u=0 can use only one of the direction masks A∈{0,2,8,10,32,34,40,42}, while a red suffix starting at v=e_2 on the final free sheet sh⊕3 can use only B∈{0,8,32,40}. A complete outside direction order requires A⊕B=62 (the six outside directions other than 2). However {62⊕A:A in the displayed prefix set}={62,60,54,52,30,28,22,20}, disjoint from the suffix set. Hence no reverse witness exists. These reachability sets follow by the recurrence R_sh(r,0)=true and R_sh(r,M)=∨_(t∈M)(R_sh(r,M\{t}) and [the direction-t edge at r⊕(M\{t}) is red]). This proof retains roots, full direction simplicity, and the common fixed gates.

**Proposition 2 (global strong connectivity fails in all dimensions 2m≥10).** For every m≥5, there are legal fixed gates such that H^* has at least 2^(2m−5) isolated outside vertices, despite containing an SCC with an antipodal pair.

**Proof.** In Q10 set
f_1=x_7, f_2=x_9, f_3=1⊕x_3, f_4=x_4.
The frozen coloring on outside directions 2,...,9 is independent of the free pair. Its red graph factors into a four-dimensional block A on directions (2,3,6,7), and a four-dimensional block B on (4,5,8,9). Within A the set x_3=1,x_7=0 is a four-vertex red component: its red edges only flip 2 and 6, retaining the displayed bits. Within B the set x_4=0,x_9=1 is likewise a four-vertex red component: its red edges only flip 5 and 8. Neither component contains an antipodal pair.

Let S consist of the outside vertices satisfying either
(i) (x_3,x_7)=(1,0) and (x_4,x_9)=(1,0), or
(ii) (x_3,x_7)=(0,1) and (x_4,x_9)=(0,1).
There are 32 such vertices. For z in case (i), its A projection lies in the small red component of A; for the antipode z̄, its B projection lies in the small red component of B. The roles reverse in case (ii). Hence neither z nor z̄ belongs to any full red antipodal geodesic of the frozen outside graph. Every one-gap witness projects, after deleting its two free steps, to a full red antipodal geodesic in that graph. Therefore no arc of H touches z or z̄; no arc of H^* touches z. Thus H^* has at least 32 isolated vertices.

For arbitrary m>5, extend the first four fixed gates independently of new bits, and define f_j=x_2 for every 5≤j<m. These gates omit their own pairs and are antipodally odd. If a one-gap witness touched a vertex whose projection to the first eight outside directions belongs to S, deleting all new-pair steps and the two free-pair steps would yield a full red antipodal geodesic in the preceding Q8 outside graph through that projection. This is impossible. Consequently every fiber of S over the 2m−10 new outside bits consists of isolated vertices in H^*: there are 32·2^(2m−10)=2^(2m−5) such vertices. In particular H^* cannot be strongly connected.

For the Q10 base, the frozen outside red graph has the red full geodesic from 0 with direction order (2,7,3,6,8,4,9,5). Extend this word by placing each new even direction before its step in direction 2 and each new odd direction afterward; all steps remain red since f_j=x_2. For any odd free gate f_0, its value differs at the antipodal endpoints of the resulting red outside geodesic, so it changes across at least one edge. Insert directions 0 and 1 immediately before and after such an edge in the order prescribed by f_0. This gives a red full one-gap antipodal geodesic. Thus the construction invalidates global strong connectivity of H^* while retaining the desired antipodal-SCC conclusion.

**Scope.** The graph H can be asymmetric even for affine gates; the antipodal closure H^* need not be globally strongly connected in any dimension at least ten. The remaining full-class target—some SCC of H^* contains an antipodal pair—survives both constructions. The note does not establish that target and does not produce a counterexample to unrestricted NORI1. The finite Q8 witness check also agrees with an independent subset-reachability enumerator.
