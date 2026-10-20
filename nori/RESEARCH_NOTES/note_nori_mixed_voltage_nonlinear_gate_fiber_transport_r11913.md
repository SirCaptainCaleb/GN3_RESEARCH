# Mixed-voltage whole-gate implication transport through nonlinear fibers

- Stable ID: note_nori_mixed_voltage_nonlinear_gate_fiber_transport_r11913
- Author: NORI1 independent researcher session_nori_r11913_3
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: nori1, whole-gate, implication, nonlinear-fiber, voltage-transport, conditional-forcing
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_3
- Updated session: session_nori_r11913_3
- Disposition: none
- Successor: none

## Related references

- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- note:note_nori_whole_gate_two_root_nonhelly_all_dimensions_20261019_r11913

## Research note

## Mixed-voltage implication transport

**Definitions.** Fix legal paired-flat gates f_j for j≥1 on Q_(2m), leaving gate f_0 on the pair (a,b)=(0,1) free. A witness (r,w) is a starting vertex and a permutation of all original directions such that every edge outside pair zero is red. Its two free-pair edges require gate values X_s=ε and X_t=δ, where X_s indexes complementary orbits of the outside-pair bits. Avoiding this full red path gives the two-variable clause ¬[(X_s=ε)∧(X_t=δ)] and its two directed implications. Attach the label h(r,w)=r_a⊕[a occurs before b in w]∈F₂ to both implications.

**Theorem (arbitrary nonlinear gate-fiber transfer).** Suppose a finite collection W of witnesses based at R produces a 2-CNF whose implication digraph has a strongly connected component C containing both signs of some variable X_s and at least one directed edge with label 0 and one with label 1. Append a new pair (u,v); extend all previously fixed gates independently of the new bits and set f_m(x)=x_a. For every legal antipodally odd enlarged free gate F_0, allowing arbitrary nonlinear dependence on all outside-pair bits, a red full direction-simple antipodal geodesic starts at some vertex of R×F₂². Furthermore the lifted witnessed implication digraph retains such a mixed-label contradictory component. The construction therefore iterates over any number of controlled added pairs.

**Proof.** Fix a witness (r,w), put β=r_a, d=u+β and d'=u+(1−β), identifying u,v with successive direction numbers. Since f_m=x_a, inserting d anywhere before a and d' anywhere after a gives red added edges; older fixed edges retain their colors. When a occurs before b, insert d before a and d' either after b or between a and b. When b occurs before a, insert d' after a and d either before b or between b and a. The two free gate evaluations then see equal new-bit sheets in the first choice, and sheets differing by e_(d') or e_d respectively in the second choice. The differing direction is e_(h(r,w)). Every inserted word is a permutation of all enlarged directions. Four choices of initial new bits are allowed above each old root.

Choose an old outside-bit representative z_s of each complementary orbit, and use variables Y_(s,η)=F_0(z_s,η), η∈F₂². Oddness gives F_0(bar z_s,η)=1⊕Y_(s,η⊕11). Therefore both inserted words retain each original implication's variable signs, and each old directed edge L→L' has from every source sheet two lifted directed edges. Their target-sheet displacements differ by e_h, with the same baseline displacement arising from the old orbit representatives.

Every directed edge inside C lies on a directed cycle. For an edge of label h, lifting its cycle twice with one different insertion choice produces two closed-base directed walks whose sheet displacements differ by e_h. Concatenating them yields a directed closed-base walk translating the sheet by e_h (as 2v=0 in F₂²). Strong connectivity of C transports these sheet shifts throughout C. Edges with both labels generate all F₂², hence all four sheets above C belong to one strongly connected component. The opposite signs of Y_(s,η) lie in that component, contradicting 2-SAT satisfiability. All implications are supplied by the displayed full red-compatible rooted orders. The lifted orders preserve the order of a,b and their roots' a-bit, so both labels occur in the lifted contradictory component. Repeat for further added pairs. ∎

**Explicit three-root base and uniform nonlinear family.** For Q6 number the pairs (0,1),(2,3),(4,5). Gate j is represented by an eight-bit table M_j on complementary orbits of four outside bits y (read in increasing direction order), with k(y)=min(y,15−y), σ(y)=[y≥8], and f_j(y)=((M_j>>k(y))&1)⊕σ(y). Direction 2j+d is red when f_j=d. Fix M_1=0x4E and M_2=0xAA. The following five rooted full orders have every edge outside pair zero red; the final entry gives the prohibited simultaneous assignment and label:
(1; 1,5,0,3,4,2; X_0=1,X_7=1; h=1);
(0; 2,1,3,4,0,5; X_1=1,X_7=0; h=0);
(1; 5,0,3,4,2,1; X_0=0,X_7=1; h=0);
(2; 3,4,1,2,0,5; X_6=1,X_7=0; h=0);
(2; 3,4,0,5,1,2; X_1=0,X_6=0; h=1).

Avoiding the first and third paths forces X_7=0; the fourth forces X_6=0; the fifth forces X_1=1; the second then forces X_7=1. The directed implication cycle includes both labels. The transfer theorem now proves: for every m≥3, extend the two fixed Q6 gates independently of new bits and define f_j(x)=x_0 for j=3,...,m−1. Then **every** legal free gate f_0, with unrestricted nonlinear dependence on all 2m−2 outside bits, produces a red full antipodal geodesic from some root in {0,1,2}×F₂^(2m−6). The forcing root set has cardinality 3·4^(m−3).

**Verification and scope.** Direct evaluation checks all five Q6 rooted orders and their fixed red edges. The two insertion choices from four added-bit starting sheets yield 40 Q8 full direction-simple rooted orders and a contradictory 2-CNF on 32 free-gate variables, with 16 conflicting sites. The proof handles arbitrary nonlinear values of the free gate and retains shared-edge consistency. It requires controlled added gates x_a and independence of older fixed gates from new bits. There is no established mechanism that produces these hypotheses at an arbitrary strict critical-square boundary; unrestricted NORI1 remains open.

### Sharp limitation: root-fiber forcing need not survive without both labels

Fix the Q6 gates M_1=0xFB, M_2=0x3E in the eight-bit complementary-orbit convention defined above, and use the two starting vertices R={5,6}. For every one of the 256 possible legal M_0 tables, some full red geodesic starts at 5 or 6. Independent 64-subset red-path dynamic programming classifies all 256 tables: 180 permit a full red geodesic from both roots, 60 only from 6, and 16 only from 5. The Q6 whole-gate implication digraph for these roots has a contradictory strongly connected component on six signed-variable nodes; **every directed edge internal to that component has label h=1**.

Now append pair (6,7), retain M_1,M_2 independently of the two new bits, and set f_3(x)=x_0. Let y be the four-bit outside-pair-zero string formed from bits 2,3,4,5, put s=min(y,15−y), σ=[y≥8], and η=x_6+2x_7. Define the enlarged legal gate F_0 by the 32-bit mask M=0x50500050 as
F_0(x)=σ⊕((M>>(4s+(η⊕(3σ))))&1).
This rule is independent of the free pair (0,1), changes value under the global antipode, and is nonlinear: its second Boolean derivative in directions 2 and 3 at the zero vertex is 1.

For each r∈{5,6} and η∈F₂², direct subset dynamic programming on Q8 finds no full red antipodal geodesic from root r+64η. Equivalently, the entire geometric Q8 whole-gate clause system for these eight roots is satisfiable; its 132 distinct clauses admit the displayed mask M. The coloring has full red geodesics from 204 other roots, so this is a rooted transport obstruction and not a counterexample to NORI1.

Consequently, **unsatisfiability of the base rooted whole-gate 2-CNF alone does not guarantee unsatisfiability on the four-sheet root fiber after a controlled x_0 dummy-pair extension**. The mixed-label premise in the preceding sufficient theorem cannot simply be deleted. This also distinguishes transporting an old clause family from the harder problem of generating new clauses during transport. Independently checked by full rooted-path enumeration and all-vertex legality tests.

### Necessary and sufficient mixed-label criterion for a nonlinear four-sheet lift

Retain the finite witness family W, its two signed implications per clause, and the witness label h(r,w)=r_0 xor [direction 0 precedes direction 1]. A directed implication edge may have several witnessed labels; retain each occurrence. Append a new pair (u,v), extend the old fixed gates independently of the new bits, and set f_m=x_0. Let W+ consist of all rooted full orders obtained from W by adding two new red steps in permitted positions and using all new starting sheets.

**Theorem.** The witnessed 2-CNF from W+ is unsatisfiable **if and only if** the implication digraph of W has a strongly connected component C containing both signs of some old gate variable and containing internally witnessed implication edges of both labels 0 and 1.

**Sufficiency.** The preceding mixed-voltage theorem applies. Every witnessed implication of label h admits two red-compatible insertions whose target-sheet displacements differ by e_h. Directed cycles in C carrying both labels generate e_0 and e_1, so every sheet above C lies in one strongly connected component containing opposite signs of one lifted variable.

**Necessity.** Any strongly connected component C+ upstairs projects into a strongly connected component C downstairs. If C+ contains opposite signs of a lifted gate bit, C contains opposite signs of the associated old gate bit. Suppose all internal witnessed edges of C have common label h. Choose F_0(x)=x_(u+1−h), with u,v consecutive direction indices. This is a legal gate, independent of its own pair and odd under antipodality. In every red-compatible lift of a witness of label h, the only newly introduced direction that can occur strictly between the two visits to pair zero is u+h. Hence F_0 has equal values at those visits. They use directions 0 and 1, requiring opposite gate values for a red full path. Therefore F_0 avoids every lifted path represented by an internal witnessed edge of C. The implication subgraph over C+ is satisfiable, contradicting C+ containing opposite signs. Thus C must contain both labels.

The theorem permits repeated clauses, coincident variable sites, and arbitrary root sets. It concerns the lifted family W+; admitting additional older direction orders or starting vertices may introduce additional clauses.

**Tests.** Independent Q6-to-Q8 programs constructed directed implications from rooted full orders, all four added sheets, and both canonical insertions. In 600 sampled nonlinear fixed-gate systems with 1–5 selected roots, the criterion matched the lifted 2-CNF in all instances (481 contradictory, 119 satisfiable). For Q6 fixed tables M_1=0x4E,M_2=0xAA and roots 0,1,2, the closed-walk displacement subgroup is F₂²; the lift is contradictory. With M_1=0xFB,M_2=0x3E and roots 5,6, a contradictory old component gives displacement subgroup {0,2}, while opposite signed lifts are separated by displacement 1; the lift is satisfiable.

**Closure limitation.** This result supplies an if-and-only-if transfer criterion, but no theorem yet produces its contradictory base component in an arbitrary strict good/bad square boundary. The bad-side free-gate formula is satisfiable; obtaining a new witnessed clause or a root-and-order exchange remains essential for unrestricted NORI1.
