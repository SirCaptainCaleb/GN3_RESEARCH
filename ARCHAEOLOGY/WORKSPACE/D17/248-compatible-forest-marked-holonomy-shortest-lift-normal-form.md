# Shortest maximum-forest holonomy must be marked, base-simple, and fiber-compressed

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-marked-holonomy-shortest-lift-normal-form`

**Summary:** Formalizes the global maximum-three-forest holonomy target. A marked transition carries only physical/ancestral data whose transport is explicitly certified by the source transition. A nontrivial holonomy is a closed walk of literal maximum three-forest representatives whose lifted mark does not return. Any shortest such holonomy has no repeated literal base representative before closure: equal lifted marks let one delete the subloop, while unequal marks already give a shorter nontrivial holonomy. Marks determined solely by the current literal forest can never have nontrivial holonomy. For a fixed unordered support partition into three Hamilton supports, arbitrary actual Hamilton words on the three supports may be reused independently, so any two representatives in that support fiber are joined by one exact reversible FIBER-REORDER jump; any mark literally retained in both endpoint representatives is retained by that jump. Hence a shortest marked holonomy may be taken fiber-compressed: every maximal constant-support segment has one edge. In particular a pure CYCLE-ROTATE movable-break orbit is recurrence, not nontrivial physical holonomy, for every state-determined mark such as current break, selected edge, endpoint role, or oriented dimer. The global extinction problem therefore begins with support-changing transitions or genuinely history-bearing ancestry.

### 1. Literal maximum-forest state space
Let H be a hypothetical smallest counterexample, so pc(H)=3. A LITERAL MAXIMUM FOREST state is a spanning three-path cover

  F=P_1|P_2|P_3

with each displayed P_i an actual oriented tight path. The components are unordered as a cover, but the literal path words, selected directed states, support sets, endpoints, and any named ancestry retained by the construction are part of the representative record.

The current D17 development supplies several reversible transitions between such states, including SLIDE, CYCLE-ROTATE, endpoint transfers, and same-support Hamilton-order replacement. Other currentizations may be nonlocal. This section does not enlarge any local theorem silently: whenever a transition is used below, its mark transport must be explicitly certified by the source construction.

### 2. Marked lifts and genuine holonomy
A MARK at a state F is a finite named datum retained from the proof construction, for example a named physical dimer with tested orientation, a selected reversal ancestry, a component ancestry label, a portal crossing ancestry, or another explicitly declared physical role. A marked transition

  (F,mu) -> (F',mu')

is legal only when the underlying representative transition F->F' is legal and the source theorem explicitly licenses the asserted transport mu->mu'. No mark is transported merely because two representatives look similar.

A MARKED HOLONOMY is a marked walk

  (F_0,mu_0),(F_1,mu_1),...,(F_m,mu_m)

with

  F_m=F_0

as the same literal maximum-forest representative, but

  mu_m != mu_0.                                           (MH.1)

Thus a closed orbit of representatives is not automatically nontrivial holonomy. Nontriviality means that certified transported information fails to return when the literal state returns.

### 3. Shortest marked holonomy is base-simple
Choose a marked holonomy with the minimum number m of representative transitions. Then no literal base state F_i with 0<=i<j<m can repeat.

Indeed suppose F_i=F_j. If mu_i=mu_j, delete the closed marked subwalk from i to j; the remaining walk has the same initial and terminal marked discrepancy and is shorter. If mu_i!=mu_j, the subwalk from i to j is itself a shorter marked holonomy. Both contradict minimality.

Therefore

  F_0,F_1,...,F_{m-1} are pairwise distinct.              (MH.2)

This is the basic first-change principle for G13: any proposed rerouting that recreates an earlier literal representative either shortens the holonomy or already isolates a smaller holonomy.

### 4. State-determined data cannot carry holonomy
Call a mark STATE-DETERMINED if its value is a function of the literal current representative alone. Examples include the current selected directed-edge set, the current endpoints of a displayed rail, the current cyclic break of a displayed path word, and the current orientation in which a named physical dimer is selected, whenever those are read only from the current forest rather than from ancestry.

For every state-determined mark,

  F_m=F_0  implies  mu_m=mu_0.                            (MH.3)

Hence no closed representative walk can have nontrivial holonomy in a purely state-determined coordinate. Any genuine holonomy must use ancestry or another transported datum not recoverable solely from the terminal literal forest.

In particular, moving a break all the way around one tight cycle and returning to the original cyclic break is a genuine closed representative orbit but not, by itself, a nontrivial physical holonomy. The movable-break family remains valuable because other transitions may attach to different breaks; the recurrence alone is not the obstruction.

### 5. Exact support-fiber compression
Fix three pairwise disjoint nonempty supports X_1,X_2,X_3 partitioning V(H). Suppose

  F=P_1|P_2|P_3,
  G=Q_1|Q_2|Q_3

are two literal maximum forests with

  V(P_i)=V(Q_i)=X_i

for i=1,2,3 after one fixed matching of the three support sets. Since tightness is internal to each path, the three target Hamilton words Q_i may be installed independently on their disjoint supports. Thus G itself certifies the simultaneous replacement. Declare the exact reversible representative transition

  F <-> G

inside this fixed support fiber to be one FIBER-REORDER jump. This is not an inferred path surgery: both endpoint states are already literal actual maximum forests, and no cross-component turn is used.

If a named mark mu is literally present with the same certified meaning in F and G, the FIBER-REORDER jump may retain mu unchanged. If the mark is not literally retained at both ends, no transport is asserted.

Consequently every marked walk segment whose support partition is constant and whose endpoint mark is literally the same may be replaced by one FIBER-REORDER edge. A shortest marked holonomy may therefore be chosen so that

  every maximal constant-support segment has length one. (MH.4)

There is no legitimate shortest-holonomy complexity hidden in a long chain of same-support word changes.

### 6. Consequence for the global extinction target
Equations (MH.2)-(MH.4) give a precise global normal form.

A shortest nontrivial maximum-forest holonomy must simultaneously satisfy:

1. it is simple in literal representative space before the final return;
2. its nontrivial mark is genuinely history-bearing, not a function of the current selected edges/path words alone;
3. all same-support recurrence is fiber-compressed to a single exact reorder edge;
4. therefore every remaining long portion of the loop contains actual support change, component recompletion, or another transition whose theorem carries nontrivial ancestry across different literal forests.

This removes pure movable-break recurrence and long same-support reorder chains from the list of possible global obstructions. It does not prove that the remaining support-changing marked holonomy is impossible. The next target is first-change extinction for the support-changing edges: show that the first transition which changes the carrier of the marked ancestry either commutes/reroutes to an earlier representative, exports a smaller marked loop, or creates a two-path augmentation.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```