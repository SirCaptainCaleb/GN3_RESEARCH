# Transition-weighted symmetric difference reduces defect-one exchange to descent or a dominant augmenting component

**Workspace:** D17
**State:** established
**Key:** `g33-transition-weighted-augmenting-component-duality`

**Summary:** Let F be the old exact two-cover and J either defect-one cut three-forest from SV103530. In the bipartite matching symmetric difference, assign each alternating component C its matching-size excess delta(C)=|F∩C|-|J∩C| in {-1,0,1} and transition excess w(C)=tau(F∩C)-tau(J∩C). Their totals are 1 and d=tau(F)-tau(J)>0. Flipping any component subset S into J gives a matching with size |J|+sum delta and transition count tau(J)+sum w. Therefore either some S with sum delta=1 has sum w<d, giving a size-|G|-2 matching candidate with strictly fewer transitions than F, or no such matching-level descent exists. The latter is equivalent to every zero-delta component subfamily having nonpositive total w. In particular every delta=0 component has w<=0, every delta=+1 / delta=-1 pair has combined weight <=0, and because the number of + components exceeds the number of - components by one, EVERY + component has w>=d. Thus in the rigid branch each F-heavy augmenting path alone carries at least the full old-versus-defect transition gap. Physical tightness/acyclicity of the recombined matching remains a separate obligation.

### 1. Weighted alternating components
Retain the normal form SV103530 and fix either of its literal spanning three-path forests J on the top fiber G. Let F be the actual old exact two-cover. Write M_F,M_J for their directed bipartite matchings. Thus

  |M_F|-|M_J|=1,
  d:=tau(F)-tau(J)>=1.                                      (TW.1)

Let C range over the connected components of the ordinary matching symmetric difference M_F triangle M_J. Define

  delta(C)=|M_F intersect C|-|M_J intersect C|,

so delta(C) is -1,0,or 1, and define the transition weight

  w(C)= #(X|B edges of M_F intersect C)
        -#(X|B edges of M_J intersect C).                    (TW.2)

Common matching edges lie outside the symmetric difference and cancel from both comparisons. Therefore

  sum_C delta(C)=1,
  sum_C w(C)=d.                                             (TW.3)

### 2. Every component subset is an exact matching recombination
For any subset S of symmetric-difference components, flip precisely the components in S from M_J to M_F and leave all other components in the J state. Because distinct symmetric-difference components are vertex-disjoint in the bipartite matching graph, the result M_S is again a bipartite matching. Its exact size and transition count are

  |M_S|=|M_J|+sum_{C in S} delta(C),
  tau(M_S)=tau(J)+sum_{C in S} w(C).                        (TW.4)

In particular S has total delta one exactly when M_S has |V(G)|-2 selected directed adjacencies, the correct matching size for a spanning two-path forest. The full set S=all components gives M_F and has total weight d.

### 3. Descent versus zero-excess dual obstruction
There are exactly two alternatives.

**MATCHING DESCENT.** Some component subset S satisfies

  sum_{C in S} delta(C)=1,
  sum_{C in S} w(C)<d.                                     (TW.5)

Then M_S has the two-cover matching size and strictly fewer X|B selected adjacencies than the old source cover F. This is already the correct static transition improvement at the matching level. It becomes an exact cover descent as soon as the corresponding directed matching is physically acyclic and all of its mixed consecutive turns are tight.

**DUAL RIGIDITY.** No subset S satisfies (TW.5). Equivalently, every subset T of symmetric-difference components with

  sum_{C in T} delta(C)=0                                  (TW.6)

has

  sum_{C in T} w(C)<=0.                                    (TW.7)

To see the equivalence, take complements. If T has total delta zero, then S=all\T has total delta one and weight d-w(T). Thus w(T)>0 is exactly a strict matching-descent recombination. Conversely every delta-one S has zero-delta complement T and w(S)=d-w(T).

This is a finite exact duality; no path-turn argument is used.

### 4. Dominant augmenting components in the rigid branch
Assume DUAL RIGIDITY. A singleton delta-zero component is an allowed T in (TW.6), so every such component has w<=0. A pair consisting of one delta=+1 component C_+ and one delta=-1 component C_- also has total delta zero, hence

  w(C_+)+w(C_-)<=0.                                       (TW.8)

Let P be the number of +1 components and N the number of -1 components. Equation (TW.3) gives P=N+1. Fix ANY +1 component C_*. Pair each of the other P-1=N positive components with a distinct negative component. Every such pair has nonpositive total weight by (TW.8), and all delta-zero components have nonpositive weight. Summing (TW.3) therefore yields

  d <= w(C_*).                                            (TW.9)

Because C_* was arbitrary, EVERY F-heavy augmenting component satisfies

  w(C_*)>=d>=1.                                           (TW.10)

Thus if matching-level transition descent is impossible, transition discrepancy cannot be diffusely hidden among neutral exchange components: each augmenting path by itself carries at least the entire old-versus-defect transition gap.

### 5. Physical consumer still required
The matching recombination M_S in the descent branch need not yet be a tight path forest. It may contain a physical directed cycle, or it may create a mixed predecessor-successor turn that is bad. Those are the only physical obstructions after matching compatibility is secured. Likewise (TW.10) is a static concentration statement, not closure.

The next consumer should therefore attack one of two sharply separated objects:

1. a transition-improving size-|G|-2 matching whose only remaining defects are physical cycle/mixed-turn windows; or
2. a single F-heavy alternating path carrying at least the whole transition gap d.

This is strictly smaller than a generic full-H trimer splice and contains no payment generation.

### 6. Scope
This is elementary matching arithmetic applied to the exact F,J coordinates of SV103530. It uses no R24, R5, R508/R509/R540 conclusion, payment, or historical replay. Tightness and acyclicity are deliberately left as explicit downstream obligations.
