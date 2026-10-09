# Devine–Milans snake mechanism: exact NORI dual terminal fan, forced two-step cap, and false naive multiplicity

# Snake digraph transfer to active NORI: exact dual terminal fan, forced 2-step cap, and linearity/multiplicity no-go

Source: user-attached Richard C. Devine and Kevin G. Milans, **Linear Hypergraph Turan Numbers of Paths**, file main.tex, especially Def. snake digraph (lines 52–58), terminal incidence/indegree lemma (60–69), density proof (71–83), special edge and cograph lemmas (109–153). NO outside literature or web search. The paper considers LINEAR LOOSE hypergraph paths: edge intersections of size 1, nonconsecutive edges disjoint. NORI instead concerns ordered three-coordinate windows of paths on Q_n with two-direction overlap and genuine physical-face coloring; do not conflate the structures.

**Mechanism in the paper.** For an r-uniform linear graph, maximize path length φ(e,v) for paths ending at hyperedge e and vertex v. Select incidence (e,v) when φ(e,v)=φ(e). Every edge supplies at least r−1 such incidences since the final r−1 vertices of a loose path can be reordered without changing its hyperedges. At a terminal vertex v, distinct incident hyperedges are disjoint away from v, so a forbidden extension must charge a distinct vertex of the chosen maximal path. This gives d^-(v) <= (φ(v)−1)(r−1)+1. Both the r−1 multiplicity AND pairwise-disjointness are essential and are NOT automatic in the overlapping THREE-window NORI complex.

**Definition (actual endpoint fan).** Let a,b,d be distinct cube directions and y∈Q_n. Write F_y(a,b,d) for the actual 3-face through y with those three free directions and all other cube coordinates fixed as at y. Define
   C^out(y;a,b;d)=c(F_y(a,b,d),(a,b,d)),
   C^in(y;b,a;d)=c(F_y(a,b,d),(d,b,a)).
These are face colors, not artificial coordinate-only triples. The active NORI law is EXACTLY the local equality
   C^out(y;a,b;d)=1−C^in(bar y;b,a;d).
Thus outdegree in color q at (y;a,b) equals indegree in opposite color 1−q at (bar y;b,a), termwise for each candidate d.

**THEOREM (MAXIMAL MONOCHROMATIC SNAKE FAN).** Let P be a genuine monochromatic k-edge direction-distinct cube geodesic from x to y, k>=3, of color q. Let S be its used coordinate set (|S|=k), let (a,b) be the LAST TWO ordered directions of P, and suppose P is unextendable as a monochromatic q-geodesic by any unused direction (e.g. P is globally longest among q-mono geodesics). Then for EVERY d∈[n]\S,
   C^out(y;a,b;d)=1−q,
   C^in(bar y;b,a;d)=q.
Put h=bar y xor e_a xor e_b. For each such d, there is an ACTUAL monochromatic q 3-edge geodesic
   h xor e_d  --d--> h --b--> h xor e_b --a--> bar y.
In particular there are n−k distinct q-colored INCOMING 3-geodesic branches with a COMMON PHYSICAL 2-edge tail, terminal vertex bar y and ordered terminal directions (b,a). Their distinct starting cube roots h xor e_d are all distance 2 from each other; exactly the star of unused directions at hub h. This is the rigorous NORI analogue of maximal-path terminal fan information from the Devine–Milans snake method, with a reversal-odd opposite-corner transfer. It does NOT create complementary support at one starting root and therefore does not alone close NORI.

PROOF: Appending unused d creates exactly one new ordered 3-face window, c(F_y(a,b,d),(a,b,d)); mono-q unextendability forces it to be 1−q. Antipodal reversal swaps F_y and F_bar_y and reverses (a,b,d) to (d,b,a), complementing the color, so the latter window is q. The 3-step path from h⊕d through h and h⊕b to bar y traverses precisely the face F_bar_y(a,b,d) in orientation (d,b,a). Different d are different directions and yield distinct roots at Hamming distance two. QED.

**THEOREM (N−2 MAXIMAL PATH TWO-STEP CAP FOR A HYPOTHETICAL COUNTEREXAMPLE).** Assume the NORI grand closure FAILS, so no full antipodal geodesic has at most one ordered-three-face color switch. Let P be ANY monochromatic (n−2)-edge cube geodesic, n>=5, of color q ending at y with final directions a,b and missing exactly two directions d,e. Then the two genuine full n-edge completions of P have the forced window-color patterns
  P followed by (d,e): q repeated n−4 times, then (1−q), then q;
  P followed by (e,d): q repeated n−4 times, then (1−q), then q.
Equivalently,
 c(F_y(a,b,d),(a,b,d))=c(F_y(a,b,e),(a,b,e))=1−q,
 c(F_(y xor e_d)(b,d,e),(b,d,e))=q,
 c(F_(y xor e_e)(b,e,d),(b,e,d))=q.
PROOF: If either first appended face were q then the prefix of length n−1 would remain mono, and appending the last direction produces a full path with at most one switch, contradiction. So both are 1−q. If either final appended face were 1−q, the corresponding FULL geodesic would have exactly one switch, also contradiction; therefore both are q. Note this is only a conditional pattern (there may be no q-mono n−2 paths under counterexample). The four windows are genuine physical faces, and the local condition is not itself inconsistent: assign colors on the corresponding reversal-orbits accordingly.

**NO-GO (ARBITRARY TERM-FAN DEGREES).** For FIXED y,a,b, the n−2 ordered physical windows (F_y(a,b,d),(a,b,d)), d distinct outside {a,b}, belong to n−2 DIFFERENT antipodal-reversal orbits: the free-coordinate sets differ with d, so neither two can be related by the involution. Thus ANY prescribed vector of n−2 binary colors on those terminal extensions extends to a globally valid active NORI coloring by assigning their antipodal-reversal partners the complementary colors and coloring all remaining involution-orbits arbitrarily. In particular the local color-q outdegree may be ANY integer from 0 to n−2. No unconditional lower bound corresponding to the paper's r−1 selected terminal incidences is available at a single physical terminal state.

**FAILURE OF LOOSE HYPERGRAPH LAST-EDGE PERMUTATION.** Two successive NORI ordered three-face windows overlap in TWO directions, unlike linear loose hypergraph edges overlapping in one VERTEX. Swapping the last two cube directions changes the last TWO ordered-three-face windows, and their colors are arbitrary except for coupling to different antipodal faces. Furthermore distinct incident physical 3-faces may share an entire 2-dimensional square rather than one vertex. Thus neither the 'reorder r−1 final vertices for free' nor the 'each blocked incident edge consumes a distinct path vertex' step of the paper transfers to the physical window graph. A replacement must track ordered TWO-TAIL memory and exterior cube face bits. This agrees with the existing NORI exact reversal-tail complementary-support criterion, Item nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008.

**Research proposal.** Build a two-color, opposite-corner SNAKE of actual terminal states (y,(a,b),q,used-support S), with out-fan and in-fan paired by tau. Take lexicographically maximal monochromatic witnesses, derive opposite-corner equal-color fans and study how *two or more such branches with common terminal 2-edge tail* generate literal root-slide packets and link them to complementary supports from a SINGLE ROOT. Beware the naive positive-degree and simple-cycle traps demonstrated above. No unrestricted grand closure is claimed.
