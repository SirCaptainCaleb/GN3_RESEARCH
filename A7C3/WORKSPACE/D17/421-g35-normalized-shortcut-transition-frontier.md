# The normalized closing fan loses strict descent only across a two-crossing zipper rectangle

**Workspace:** D17
**State:** established
**Key:** `g35-normalized-shortcut-transition-frontier`

**Summary:** Normalize every delta-zero component to its F-state as in SV112526, and for each proper zipper prefix q with a_q != b_m close the two unmatched copies by g_q=a_q->b_m. The resulting matching Nhat_q has exact two-cover cardinality. Consecutive closures differ by the bipartite 2-switch {f_q,g_{q-1}} <-> {e_q,g_q}. Zipper parity implies the shortcut transition count changes only by 0 or +/-2. More precisely, it rises by 2 exactly when chi(e_q)=1, chi(f_q)=0, chi(g_{q-1})=0 and chi(g_q)=1: the old pairing consists of two same-side edges and the new pairing of two X|B edges. Since the q=0 normalized closure has tau<=2 while the final q=m-1 closure is literally F, the first non-loop index where the closure transition count reaches the old floor tau(F) is, unless interrupted by the unique singleton-defect loop coincidence, an exact two-crossing frontier: the preceding closure has tau(F)-2 and the frontier closure has tau(F). Thus numerical descent cannot evaporate diffusely along the corridor; it dies at one local K2,2 zipper rectangle whose installed F-edge is an old transition. Physical realization remains separate.


### 1. Normalized zipper closures
Retain the G35 unique augmenter in zipper coordinates

  e_i=a_{i-1}->b_i,   f_i=a_i->b_i     (1<=i<m),
  e_m=a_{m-1}->b_m,

and the F-normalized prefix matchings hat M_q of SV112526. Let

  W_0 = sum_D w(D) <= 0

be the total transition weight of all delta-zero symmetric-difference components. Then

  tau(hat M_q)=1+S_q+W_0,                                 (NF.1)

where S_q=sum_{i<=q}(chi(e_i)-chi(f_i)).

Whenever the physical labels a_q and b_m are distinct, both a_q,out and b_m,in are unmatched in hat M_q. Define the NORMALIZED CLOSURE

  hat N_q := hat M_q + g_q,
  g_q := a_q -> b_m.                                      (NF.2)

It has

  |hat N_q|=|M_F|,                                        (NF.3)

so it has the exact matching cardinality of a spanning two-cover. Its transition count is

  T_q := tau(hat N_q)=1+S_q+W_0+gamma_q,
  gamma_q:=chi(g_q).                                      (NF.4)

### 2. Consecutive closures form one exact zipper rectangle
For 1<=q<m, compare the q-1 and q closures. All selected edges agree except on the two OUT copies a_{q-1},a_q and two IN copies b_q,b_m. The old pairing is

  f_q = a_q -> b_q,
  g_{q-1}=a_{q-1} -> b_m,

while the new pairing is

  e_q = a_{q-1} -> b_q,
  g_q = a_q -> b_m.                                      (NF.5)

Thus

  hat N_q = hat N_{q-1} - {f_q,g_{q-1}} + {e_q,g_q}.      (NF.6)

This is a literal K_{2,2} matching switch. Equivalently, defect transport by one step and closure to the far endpoint commute at the bipartite-matching level.

### 3. Closure transition count changes only by an even step
Put

  Delta_q := chi(e_q)-chi(f_q) in {-1,0,1}.               (NF.7)

Zipper parity gives

  gamma_q = (S_q mod 2) xor (w(C_*) mod 2).               (NF.8)

Hence gamma_q toggles exactly when Delta_q is odd. From (NF.4),

  T_q-T_{q-1}=Delta_q+(gamma_q-gamma_{q-1}).               (NF.9)

There are only five possibilities:

- Delta_q=0: gamma_q=gamma_{q-1}, so T_q-T_{q-1}=0.
- Delta_q=+1 and gamma_{q-1}=0: gamma_q=1, so T_q-T_{q-1}=+2.
- Delta_q=+1 and gamma_{q-1}=1: gamma_q=0, so T_q-T_{q-1}=0.
- Delta_q=-1 and gamma_{q-1}=0: gamma_q=1, so T_q-T_{q-1}=0.
- Delta_q=-1 and gamma_{q-1}=1: gamma_q=0, so T_q-T_{q-1}=-2.

Therefore

  T_q-T_{q-1} in {-2,0,2}.                                (NF.10)

In particular all normalized closure transition counts have one common parity.

### 4. Every upward step is exactly a same-side to cross-pair switch
The case T_q-T_{q-1}=2 is characterized by

  Delta_q=+1,
  gamma_{q-1}=0,
  gamma_q=1.                                               (NF.11)

Since Delta_q=+1 with binary transition indicators means

  chi(e_q)=1,
  chi(f_q)=0,                                              (NF.12)

(NF.11) says precisely

  chi(f_q)=chi(g_{q-1})=0,
  chi(e_q)=chi(g_q)=1.                                    (NF.13)

Thus every numerical rise of the closing fan replaces TWO same-side edges by TWO X|B transitions in the single zipper rectangle (NF.5). Numerical descent cannot be lost through a diffuse accumulation of one-edge costs.

The downward case is the exact reverse: two cross edges are replaced by two same-side edges.

### 5. The first loss of strict descent is a canonical local frontier
At q=0, the pre-pivot shortcut fan SV111694 and neutral normalization give

  T_0<=2<tau(F),                                          (NF.14)

provided the closure is not the unique loop coincidence a_0=b_m.

At the terminal proper prefix q=m-1, the closure edge is exactly

  g_{m-1}=a_{m-1}->b_m=e_m.

Since hat M_{m-1}=M_F-{e_m} by SV112526,

  hat N_{m-1}=M_F,
  T_{m-1}=tau(F).                                         (NF.15)

Assume for the moment that no loop coincidence interrupts the closure sequence before the numerical frontier. Let q^dagger be the least index with

  T_{q^dagger}>=tau(F).                                   (NF.16)

All T_q have the same parity as T_{m-1}=tau(F), and each step has size at most two. Hence

  T_{q^dagger-1}=tau(F)-2,
  T_{q^dagger}=tau(F).                                    (NF.17)

By Section 4, the switch from q^dagger-1 to q^dagger is exactly

  {two same-side edges}  ->  {two X|B edges}.              (NF.18)

Moreover the newly installed zipper edge e_{q^dagger} is an actual old F transition, while the displaced J-edge f_{q^dagger} is same-side.

Thus the first numerical disappearance of strict old-source descent is one canonical four-copy rectangle, not an interval of ambiguous transition debt.

### 6. The unique singleton-defect interruption
The physical labels a_q are pairwise distinct along the OUT shore of C_*, so a_q=b_m can occur for at most one q. At that index g_q would be a forbidden loop and the normalized matching hat M_q has both copies of that physical vertex unmatched.

Accordingly the numerical frontier theorem has only one exceptional interruption: one isolated singleton-defect coincidence. On either side of that single index the even-step transition staircase and zipper rectangles remain valid. No second loop obstruction can occur.

### 7. Physical meaning and scope
If a closure hat N_q is a literal tight acyclic selected graph, then it is an exact two-cover; whenever T_q<tau(F) this is strict old-source transition descent. The present theorem does not assert physical realizability of the closures. Its role is to identify the exact local place where a family of matching-level strict descents can cease to be numerically strict.

Consequently, after the forward blocker normalization SV112526, the remaining G35 physical consumer may be localized against one of two bounded events:

1. the unique possible singleton-defect loop coincidence; or
2. the first two-crossing zipper rectangle (NF.18), comparing a strict-descent same-side closure with the first closure at the old transition floor.

No R24, R5, payment, replay, MILP, SAT, or blocker taxonomy is used.

