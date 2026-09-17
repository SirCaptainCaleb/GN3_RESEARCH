# Order-eleven Hall closure and the pure-PORT meta-bicycle

**Workspace:** D17
**State:** working
**Key:** `middle-layer-k5-hall-closure`

**Summary:** Finite k=5 closure: global switch-freeness compresses to small rigid circuits, exact C4/C5/C6 certificates eliminate the rigid branch, the four-way fan eliminates clean pair-switch, and the remaining pure-PORT structure is organized as a meta-bicycle with explicit local shortcut fences.

### 21. At order eleven global switch-freeness forces a six-edge rigid circuit

Specialize to k=5, n=11, and impose the stronger GLOBAL hypothesis that the complete all-endpoint incidence graph has no PORT-SWITCH at any incident four-core and no PAIR-SWITCH on any five-support. By section 20 every nontrivial component is then a simple rigid graph around one common trimer and has at most eight core vertices. Include all C(11,4)=330 possible four-cores as graph vertices, allowing isolated ones. Every one of the C(11,5)=462 five-supports contributes exactly one graph edge. Thus globally

  V_tot=330,   E_tot=462,   E_tot/V_tot=7/5.

Let m be the minimum number of edges in a bicircular circuit among these rigid components. Such a circuit exists because E_tot>V_tot.

First m<=7. Suppose m>=8. Any graph on at most six vertices then has e<=v, since otherwise it contains a bicircular circuit with at most seven edges. On seven vertices e<=8: if e>=9, a minimal dependent set is an eight-edge circuit spanning all seven vertices and an extra edge is a chord; the bicircular chord lemma of section 14 produces a smaller circuit (the K4-e exception is impossible on seven circuit vertices). On eight vertices every seven-vertex deletion has at most eight edges, so double counting gives

  6e <= 8*8,

hence e<=10. Therefore every component has edge/core ratio at most 10/8=5/4, contradicting the global ratio 7/5. Hence m<=7.

Now suppose m=7. The same argument one level lower gives the following bounds for a component with v cores:

  v<=5: e<=v,
  v=6: e<=7,
  v=7: e<=9,
  v=8: e<=12.

For v=7, every six-vertex deletion has at most seven edges and 5e<=7*7. For v=8, every seven-vertex deletion has at most nine edges and 6e<=8*9. Thus every component with fewer than eight cores has ratio at most 9/7, while an eight-core component has ratio at most 3/2.

Let V_8 be the number of four-cores lying in eight-core components. Then

  462 <= (3/2)V_8 + (9/7)(330-V_8),

so V_8>=176. Hence at least 22 eight-core components are required.

But an eight-core component around a trimer C is full: its cores are C+u for all eight vertices u outside C. Two distinct full trimer bases cannot share a physical pair, because two triples sharing two vertices have a common four-set C union C', which would lie in both graph components. Thus the full trimer bases form a 3-uniform pair-packing on 11 vertices. There are at most

  floor(C(11,2)/C(3,2)) = 18

such triples, so at most 18*8=144 cores can lie in full components. Contradiction. Therefore m is not seven.

A simple bicircular circuit has at least five edges. The m=5 circuit is K4-e and contains a rigid triangle, already excluded in the k=5 uniform residue by the exact seven-vertex rigid-triangle theorem of section 15 / accepted R929. Hence

  m=6.                                               (21.1)

A six-edge bicircular circuit has five vertices and minimum degree at least two. Since sum(deg-2)=2, either one vertex has degree four and the rest degree two, giving a bowtie of two triangles, or two vertices have degree three and the rest degree two, giving a theta graph. The theta path lengths sum to six. Simplicity leaves either lengths 1,2,3, which contains a triangle, or lengths 2,2,2, which is K_{2,3}. The rigid-triangle theorem eliminates every case containing a triangle. Therefore under global switch-freeness the ONLY possible minimum order-eleven rigid circuit is

  K_{2,3}.                                           (21.2)

### 22. Exact rigid-C4 theorem eliminates the final globally switch-free order-eleven residue

The K_{2,3} residue contains a four-cycle, so the previously optional rigid-C4 diagnostic now has a direct downstream consumer. The required finite statement is exact.

**Rigid-C4 seven-vertex theorem.** Let M={0,1,2} and let 3,4,5,6 be four further vertices. Suppose each of the four five-supports

  M+{3,4},  M+{4,5},  M+{5,6},  M+{6,3}

is Hamiltonian and EVERY Hamilton P5 on each support has exactly its displayed exterior pair as endpoints. Then the seven vertices contain a tight P6.

Exact finite verification. Encode boundary antisymmetry by 105 Boolean turn variables, one for each complete-reversal pair of ordered triples on seven vertices, using the lexicographically smaller ordered representative as the positive literal. For each of the four rigid supports exactly 12 of its 120 vertex orders have the prescribed endpoint pair. Introduce one witness variable for each such allowed order, 48 witnesses total. Impose:

* all 7P6=5040 ordered six-tuples are forbidden as tight P6s;
* the 108 disallowed P5 orders on each of the four supports are forbidden, 432 clauses;
* each witness implies its three consecutive tight turns, 144 clauses;
* at least one allowed witness exists on each rigid support, 4 clauses.

The CNF therefore has

  105+48=153 variables,
  5040+432+144+4=5620 clauses.

A standalone deterministic DPLL verification is UNSAT. After unit propagation, choose a variable of maximum occurrence among the currently shortest unresolved clauses, breaking ties by smallest variable index, and branch False before True. Number turn variables by lexicographic reversal representative and witness variables support-by-support in cyclic order 34,45,56,63, with allowed Hamilton orders lexicographic. The exhaustive search closes after 16,971 DPLL nodes, maximum branch depth 38. An independent binary MILP translation was also infeasible under SciPy/HiGHS. Hence the rigid C4 cannot occur in a no-P6 system.

Combining (21.2) with the rigid-C4 theorem gives the exact structural consequence:

  at k=5, the COMPLETE all-endpoint system cannot be globally free of both PORT-SWITCH and PAIR-SWITCH.

This does NOT yet close the order-eleven uniform residue. The forced switch may lie outside the chosen minimum Hall circuit, and the six-vertex switch fences show that an isolated switch is locally feasible. The remaining rooted-circuit theorem must therefore currentize a real global switch back into a Hall-deficient replacement satisfying the ledger (18.2), or consume it directly into P6 / an R561 fixed-support reversed-boundary absorber.

Status: sections 18-21 are complete symbolic internal arguments. Section 22 is an exact finite theorem with deterministic exhaustive verification plus independent MILP infeasibility, but no standalone canonical claim/review status is asserted by this development write.


### 23. Exact rigid-C5 and rigid-C6 theorems eliminate the entire k=5 rigid Hall branch

The rigid-C4 theorem of section 22 suggests testing the only remaining cycle lengths that can occur in a rigid order-eleven Hall circuit. Both admit exact finite elimination.

**Rigid-C5 theorem.** Let M={0,1,2} and let 3,4,5,6,7 be five exterior vertices in cyclic order. Suppose each support

  M+{3,4}, M+{4,5}, M+{5,6}, M+{6,7}, M+{7,3}

is Hamiltonian and EVERY Hamilton P5 on each support has exactly its displayed exterior pair as endpoints. Then these eight vertices contain a tight P6.

For an exact SAT certificate one symmetry normalization is available. Choose any Hamilton order of M+{3,4}; rigidity gives exterior endpoints 3,4. By permuting M and, if necessary, reflecting the exterior 5-cycle across edge 34, we may assume the actual tight order

  (3,0,1,2,4).

Encode boundary antisymmetry by 168 turn variables. The normalized path contributes three unit clauses. On the remaining four rigid supports use 48 Hamilton-order witness variables. The exact CNF then contains:

* 8P6=20160 no-P6 clauses;
* 5*108=540 clauses forbidding Hamilton P5 orders with the wrong endpoint pair;
* 4*12*3=144 witness-implies-turn clauses;
* 4 witness-existence clauses;
* 3 normalization units.

Thus there are 216 variables and 20851 clauses. A watched-literal deterministic DPLL solver proves UNSAT in 429 search nodes, maximum decision depth 36. A second independent full-scan DPLL implementation also proves UNSAT, in 859 nodes and depth 37. Independently, the symmetry-normalized binary MILP translation is infeasible under SciPy/HiGHS.

**Rigid-C6 theorem.** Let M={0,1,2} and exterior vertices 3,4,5,6,7,8 form a rigid six-cycle, with rigid supports M+{3,4}, M+{4,5}, ..., M+{8,3}. Then the nine vertices contain a tight P6. Normalize one actual Hamilton order on M+{3,4} to (3,0,1,2,4) by the same M-permutation and cycle-reflection symmetry. There are 252 turn variables and 60 witnesses for the remaining five rigid supports, hence 312 variables. The CNF has

  9P6 + 6*108 + 5*12*3 + 5 + 3
  = 60480 + 648 + 180 + 5 + 3
  = 61316

clauses. The watched-literal deterministic DPLL solver proves UNSAT in 630 search nodes, maximum decision depth 39. For independent certification, the solver emits its complete branch/propagation proof tree; a separate raw-clause verifier checks every unit reason, every conflict clause, and both branches at every decision, and validates the UNSAT proof. A HiGHS run did not settle this larger MILP within its time cap, so no MILP conclusion is claimed for C6.

Now return to a minimum-cardinality Hall obstruction F in the k=5 uniform residue and suppose R928 places it in the RIGID branch. Its common core M has three vertices, so its simple bicircular circuit G has at most eight exterior/core vertices. If G had no cycle of length at most six, then its girth would be at least seven. This is impossible for any bicircular circuit on at most eight vertices. In the theta topology, write the three internally disjoint branch-to-branch path lengths as a,b,c. Girth at least seven gives a+b,a+c,b+c >=7, hence 2(a+b+c)>=21 and therefore a+b+c>=11; the theta has a+b+c-1>=10 vertices. A figure-eight with both cycles of length at least seven has at least 13 vertices, and two cycles joined by a path need still more.

Hence G contains a cycle of length l in {3,4,5,6}. Every edge of that cycle is one of the rigid Hall supports around the SAME common trimer M. The l=3 case is excluded by the exact rigid-triangle theorem of section 15 / accepted R929 (H has spare vertices beyond the six-vertex triangle packet); l=4 is excluded by section 22; and l=5,6 are excluded by the two exact finite theorems above. Contradiction.

Therefore, at k=5, the RIGID alternative of R928 is impossible for the MINIMUM HALL OBSTRUCTION ITSELF. Every minimum-cardinality Hall obstruction in the order-eleven uniform residue lies in PORT-SWITCH or PAIR-SWITCH. In particular the switched core/support belongs to the deficient family, so every switched endpoint incidence is currentizable into a near-perfect matching by section 7. The off-circuit rooted-distance problem of sections 18-22 is no longer needed for the k=5 branch.

This does not yet absorb the switch: the exact six-vertex port/pair-switch fences remain valid. The new frontier is an IN-CIRCUIT SWITCH EXCHANGE theorem using two near-perfect matchings that currentize competing endpoint realizations and their alternating symmetric-difference structure.

Status: the C5/C6 finite statements have exact exhaustive certificates as described. The graph deduction is symbolic. No standalone canonical review status is asserted by this development write.


### 24. The four-way root fan exactly eliminates an internal clean pair-switch at k=5

Work in the order-eleven uniform residue, so every Hamilton path has order at most five and a tight P6 is forbidden. Let F be an inclusion-minimal Hall-deficient family in the COMPLETE all-endpoint incidence graph, and suppose F is in the R939/R928 PAIR-SWITCH branch: every right core has a unique physical port, while one support S has two distinct endpoint pairs. Since |S|=5 and distinct endpoint pairs are disjoint under unique ports, relabel

  S={a,b,c,d,e}

so that actual Hamilton P5s on S realize endpoint pairs {a,b} and {c,d}. No third endpoint pair can occur: any further two-set among five vertices meets at least one of these two pairs in exactly one vertex, which would create a port switch.

Root the factor-critical Hall circuit at S. By R939/R928 there is a perfect matching M of F-{S} onto N(F). Let

  R_a=S-{a}, R_b=S-{b}, R_c=S-{c}, R_d=S-{d}.

These are four distinct Hall cores. Let T_a,T_b,T_c,T_d be their four matched supports. They are distinct because M is a matching and none equals the omitted root S. Write the matched completion labels as

  x_a=T_a-R_a, ..., x_d=T_d-R_d.

Each x_u lies outside S: the only completion of R_u lying in S is u itself, which would recover S. Unique ports at the four switched cores force actual Hamilton paths on the matched supports with endpoint pairs

  T_a: {x_a,b},   T_b: {x_b,a},
  T_c: {x_c,d},   T_d: {x_d,c}.

Moreover EVERY endpoint-pair graph of every T_u is itself a matching. Indeed, if one support T_u had two Hamilton endpoint pairs sharing a physical endpoint y, then at the endpoint-deletion core T_u-{y} the completion y would be paired with two distinct ports, contradicting the global no-PORT hypothesis of the PAIR-SWITCH branch. Thus each T_u has one endpoint pair or two disjoint endpoint pairs.

**Exact finite four-way-fan theorem.** The five supports S,T_a,T_b,T_c,T_d with the preceding endpoint-pair conditions cannot occur in any P6-free boundary tournament, for ANY equality pattern among x_a,x_b,x_c,x_d. No Hamiltonicity assumption is required for any unrelated five-set.

Finite certificate. Up to relabeling distinct exterior completion vertices, the equality pattern of the ordered four-tuple (x_a,x_b,x_c,x_d) is one of the 15 restricted-growth strings

  0000, 0001, 0010, 0011, 0012,
  0100, 0101, 0102, 0110, 0111,
  0112, 0120, 0121, 0122, 0123.

For each pattern use only the physical vertices in S plus the distinct exterior labels occurring in that pattern, so the instance has n between 6 and 9 vertices. Encode boundary antisymmetry by one Boolean turn variable for each reversal pair (a,b,c)/(c,b,a). For every ordered six-tuple forbid simultaneous tightness of its four consecutive turns. For each of the five displayed supports introduce one Boolean indicator for every possible unordered endpoint pair. Every Hamilton order on that support implies its endpoint-pair indicator. Pairwise forbid two endpoint-pair indicators sharing exactly one vertex; this is exactly the no-PORT cleanliness condition. On S require existence of Hamilton orders with endpoint pairs {a,b} and {c,d}; on each T_u require existence of the matched endpoint pair displayed above. No other five-support is required Hamiltonian.

All 15 CNFs are UNSAT. A deterministic watched-literal DPLL implementation closes them in 13,371 to 26,343 search nodes, with maximum decision depth at most 31. For every one of the 15 instances the solver emitted the complete binary branch tree. A separate verifier using raw clause occurrence counts rather than watched literals replayed unit propagation, both branches at every decision, and every terminal conflict; all 15 proof trees verified. Thus the conclusion is an exact finite theorem, not a solver-timeout inference.

Consequently an inclusion-minimal endpoint-Hall circuit in the k=5 uniform residue cannot lie in the clean PAIR-SWITCH branch. Conditional on the working DR17.42 elimination of the RIGID branch being promoted, the only surviving in-circuit R939/R928 alternative at order eleven is PORT-SWITCH. Until that promotion is accepted, retain accepted R943 as fallback: a clean pair-switch located only at distance one from a different rigid Hall circuit is not covered by this root-at-S theorem.

This theorem uses the whole four-way common matching fan requested by Director v12. It does not synchronize the five Hamilton orders, does not assume the exterior labels are distinct, and does not use generic R435 output.


### 25. Pure core-switches split a Hall bicycle into a meta-bicycle of trimer trees

Specialize to k=5 and retain the accepted R944 minimum-CARDINALITY Hall obstruction F. Assume the PORT-SWITCH branch, and first isolate the PURE CORE-SWITCH subbranch in which every support S in F has exactly one Hamilton endpoint pair, while one or more endpoint cores realize more than one physical port. Because every support has exactly two endpoint-deletion neighbors, contracting support vertices gives a connected simple bicircular circuit G on the physical four-cores N(F): |E(G)|=|N(F)|+1, every vertex has degree at least two, and the usual support-subfamily Hall minimality makes every proper edge family pseudoforest.

For a physical core R let Pi(R) be its set of realized ports, and put

  P = sum_R (|Pi(R)|-1) >= 1.

Split R into one copy (R,p) for every p in Pi(R). If a support S has its unique endpoint pair {u,v}, join the copies (S-u,v) and (S-v,u). Both copies carry the same trimer base

  M=S-{u,v}.

Hence the split graph is a disjoint union of ordinary simple graphs indexed by fixed trimers M. It has

  E_split=|F|,
  V_split=|N(F)|+P,
  E_split-V_split=1-P.                              (25.1)

Every connected split trimer component is a tree or a unicyclic graph. Indeed, a bicircular edge subfamily inside one split component would correspond to a proper support subfamily whose COMPLETE endpoint neighborhood has at most the split vertices used by that subgraph; supports have unique endpoint pairs in the present subbranch, so no unselected endpoint core exists. Such a subfamily would be Hall-deficient, contradicting minimum cardinality of F.

Let t be the number of tree split components and u the number of unicyclic split components. Summing e-v over the split components and using (25.1) gives

  t=P-1.                                             (25.2)

Now form the meta-incidence graph B whose left nodes are the connected split trimer components and whose right nodes are the physical switched cores R with |Pi(R)|>=2; connect R to every split component containing one of its port copies. Gluing along these right nodes recovers G, so B is connected. If s is the number of switched physical cores, then

  |E(B)|=sum_R |Pi(R)|=s+P,
  |V(B)|=(t+u)+s=(P-1+u)+s,

therefore

  beta(B)=|E(B)|-|V(B)|+1=2-u.                     (25.3)

The next finite theorem eliminates u.

**Rigid long-cycle plus pure-port attachment theorem.** Let M be a trimer. Suppose a split trimer component is unicyclic. Its cycle has length at most eight because only eight physical cores M+x exist. Lengths 3,4,5,6 are already excluded by the accepted rigid-cycle theorems used in R944. If the cycle has length 7 or 8, connectedness of the original Hall circuit forces some cycle core R=M+c0 to be a physical port switch. In the pure-core subbranch the support from the other base has a unique endpoint pair {x,q} with q in M, while the two cycle supports at R have port c0. A cycle-neighbor x would duplicate one of those rigid supports with a different unique endpoint pair, so x is either a nonneighbor cycle label or, only for C7, the unique eleventh spare vertex. Up to cycle reflection, the complete list is:

  C7: distance 2, distance 3, or the spare vertex;
  C8: distance 2, distance 3, or distance 4.

All six packets are exact SAT-UNSAT. Normalize one rigid cycle edge to the actual Hamilton order (c0,0,1,2,c1). For each rigid support forbid all 108 Hamilton orders with the wrong endpoint pair and witness one of the 12 allowed orders; impose the same uniqueness requirement on the port-attachment support, and forbid every ordered P6 on the physical vertex union. No unrelated five-set is assumed Hamiltonian.

For C7 with an internal cycle attachment the union has 10 vertices, 444 Boolean variables, and 152326 clauses; the distance-2 and distance-3 proof trees close in 19 and 44 DPLL nodes. The C7-spare packet has 11 vertices, 579 variables, and 333766 clauses, closing in 64 nodes. Each C8 packet has 11 vertices, 591 variables, and 333911 clauses; distances 2,3,4 close in 19,44,46 nodes. A deterministic watched-literal solver emitted the full binary branch tree in every case, and the independent raw-clause occurrence verifier replayed every unit propagation, both decision branches, and every terminal conflict. Independently, all six binary MILP translations are infeasible under SciPy/HiGHS. Thus no unicyclic split component survives.

Consequently u=0. Equations (25.2)-(25.3) become

  number of split trimer components = P-1,
  beta(B)=2.                                         (25.4)

Every switch node of B has degree at least two by definition. Every trimer-component node also has degree at least two: a split tree has at least two leaves, and any leaf core that were not physically switched would have degree one in the original graph G, contradicting minimum Hall degree at least two. Hence B is connected, has minimum degree at least two, and has cyclomatic number two. Equivalently sum(deg_B-2)=2, so B is itself a bicircular circuit of theta / figure-eight / two-cycles-joined-by-a-path topology.

Moreover every degree-two trimer-component node is literally a rigid path: its tree contains exactly two switched physical cores, every leaf must be one of them, and no branch vertex can occur without creating a third leaf. Every degree-two switch node is a physical core with exactly two ports. Thus all but at most two branching meta-nodes are alternating rigid paths and two-port physical switches.

This is a structural reduction only. It does not yet consume the resulting PORT meta-bicycle into P6 or R561. It applies only while every support of F has a unique endpoint pair. Supports with multiple endpoint pairs remain a separate PORT subbranch.

### 26. Two exact fences for PORT local shortcuts

PORT-SWITCH itself forces a genuine same-core order conflict. If R+x and R+y realize endpoint pairs {x,p} and {y,q} with p!=q, delete x,y from the two actual Hamilton P5s to obtain Hamilton P4 orders Q_x,Q_y on R. If Q_x=Q_y as a literal order, then p and q are the two opposite endpoints of that common order and x,y attach on opposite sides, making x,Q_x,y a tight P6. Hence no-P6 implies Q_x!=Q_y. This is stronger localization than a generic Hall conflict, but generic R435 output remains insufficient by the standing fence.

Two tempting stronger local shortcuts are false. First, exact six-vertex MILP finds a P6-free boundary tournament in which all six five-sets are Hamiltonian, one prescribed four-core realizes ports 0 and 1 from its two completions, and EVERY other four-core has a unique port. Thus PORT need not proliferate locally. Second, a support-local port switch with endpoint pairs {a,b},{a,c} can coexist with the three matched-neighbor incidences supplied by the root fan; equality patterns using one or two exterior completion labels are exactly feasible. Hence neither local propagation nor a three-way root fan consumes PORT without using more of the Hall circuit.

A common-complement R44 test gives only partial pruning. For a normalized PORT packet P_x=(x,0,1,2,3) and P_y=(y,Q) with different port, there are 16 no-P6 feasible literal core-order conflicts Q even after all six local five-sets are required Hamiltonian. Applying R44 to the same disjoint Hamilton complement kills two of those 16 patterns directly, but 14 survive. Therefore the next PORT theorem should consume the meta-bicycle or a support-multiplicity analogue, not another isolated same-core conflict.




## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
