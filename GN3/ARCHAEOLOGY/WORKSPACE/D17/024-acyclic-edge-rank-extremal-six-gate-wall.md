# Edge-rank extrema synchronize all six merge gates in the acyclic branch

**Workspace:** D17
**State:** established
**Key:** `acyclic-edge-rank-extremal-six-gate-wall`

**Summary:** Assume the comparison orientation is acyclic and fix a realizing strict edge order. Global lexicographic extrema of maximum three-covers give an ALL-TERMINAL wall containing the global maximum edge and an ALL-SOURCE wall containing the global minimum edge. Moreover, at the upper pole the rail whose terminal selected edge is largest among the three has every one-cut suffix transfer from either foreign rail blocked; dually the lower pole has a full one-cut prefix barrier at the smallest source edge. Thus the acyclic branch has opposite global extreme-anchored poles carrying complete one-sided transfer barriers, not merely six native blocked gates. No DOUBLE absorption, polarity-transition theorem, or two-cover escape is claimed.

### 1. Acyclic edge-order coordinate
Assume Gamma(H) is acyclic. By accepted R887 choose one strict total order of the ordinary edges realizing every tight turn; write rho(e) for the rank of e in that order. For any spanning compatible three-forest F, put

  W(F)=sum rho(e)

over its selected rail edges.

Retain any class C of maximum three-forests which is closed under every reversible SLIDE move of `compatible-forest-six-seed-slide-double` SV22098. A SLIDE-connected component is enough; any terminal exchange class in the sense of current Guidance G9 has this property because every SLIDE successor is reversible and therefore remains in the same strongly connected class.

Choose F^+ in C maximizing W and F^- in C minimizing W.

### 2. The maximum-weight representative has no singleton rail
Write F^+=X|Y|Z and consider an ordered seed X->Y with terminal t of X and source s of Y. If X were a singleton, the terminal-side seam is absent. If Y were also a singleton, joining t to s would immediately merge two rails and give a spanning two-cover, impossible. Hence Y has first edge s->q. The only merge seam is then beta=(t,s,q). It cannot be tight, again because that would merge X and Y. Therefore beta is bad. In the realizing edge order this means

  rho(sq) < rho(ts).

Replacing the selected edge sq by ts gives the legal source-transfer SLIDE (X,s)|(Y-s)|Z. Its weight is larger by rho(ts)-rho(sq)>0, contradicting maximality of F^+. Thus no rail of F^+ is a singleton.

### 3. Every terminal-side merge turn is bad at the maximum
Now write

  X=(...,p,t),   Y=(s,q,...).

Let alpha=(p,t,s) and beta=(t,s,q). If alpha were tight, beta could not also be tight because then X followed by Y would be a spanning two-rail merge. Hence beta would be bad. The source-transfer SLIDE deletes sq and adds ts. Tightness/badness in the global edge order gives

  rho(pt) < rho(ts),   rho(sq) < rho(ts),

so in particular the SLIDE changes W by

  rho(ts)-rho(sq)>0,

again contradicting maximality. Therefore alpha is bad for EVERY ordered pair of distinct rails. By R3 this equivalently retains the reverse turns

  (s,t,p) tight                                      (ER.1)

for both foreign rail sources s at each terminal dimer (p,t).

Thus F^+ is an ALL-TERMINAL reverse wall: all six terminal-side native merge gates are blocked simultaneously. A seed may still be DOUBLE or a downward SLIDE according to its source-side gate.

### 4. The minimum-weight representative is the exact dual
Choose F^- minimizing W in C. If a target rail Y were a singleton, then for any non-singleton source rail X=(...,p,t), the only seam alpha=(p,t,s) cannot be tight, else the two rails merge. Thus alpha is bad, so rho(ts)<rho(pt), and the terminal-transfer SLIDE deleting pt and adding ts strictly decreases W, contradiction. Two singleton rails would merge directly. Hence every rail of F^- is nontrivial.

For an arbitrary ordered seed X->Y, if beta=(t,s,q) were tight, alpha must be bad. The terminal-transfer SLIDE deletes pt and adds ts; alpha bad means rho(ts)<rho(pt), so W strictly decreases. Contradiction. Therefore beta is bad for every ordered pair. By R3 the reverse turns

  (q,s,t) tight                                      (ER.2)

hold for both foreign terminals t at each source dimer (s,q).

Thus F^- is an ALL-SOURCE reverse wall.

### 5. Terminal-class consequence
Every SLIDE-closed finite class therefore contains two canonical extremal representatives of opposite polarity:

  F^+ : all six terminal-side gates bad;
  F^- : all six source-side gates bad.

For the G9 terminal-exchange-class program, this synchronizes the six merge seeds without comparing six unrelated charged preorders. The remaining obstruction is genuinely global: either consume one of these one-sided walls using DOUBLE recompletions / class closure, or use a path inside the same closed class between the two extrema. No claim is made that the extrema coincide, that all six seeds are DOUBLE, or that the one-sided walls alone force a universal four-set or a spanning two-cover.

### 6. Global lexicographic extreme-edge anchoring in minimum R888 counterexamples
Now specialize to a minimum counterexample to R888. Accepted R982 says that all maximum increasing three-covers are connected by a chain of indecomposable neutral collision exchanges. These exchanges are reversible because both endpoints are literal maximum covers. Thus, if they are admitted as additional proved exchange edges, the entire maximum-cover space is one reversible exchange class; in particular there is no acyclic-branch need to choose among disconnected terminal classes at this enlarged level.

Order the selected-edge rank multisets lexicographically after sorting ranks from largest to smallest, and choose a global lexicographic maximum F^max among ALL maximum three-covers. The proof of Sections 2-3 works verbatim with this lexicographic objective: a source-transfer SLIDE replaces exactly one selected edge sq by the strictly larger edge ts, so it strictly increases the sorted rank multiset. Therefore F^max has no singleton rail and satisfies the ALL-TERMINAL wall (ER.1).

Let e_max be the globally largest ordinary edge. Accepted R999 supplies some maximum three-cover containing e_max literally as a selected dimer edge. Any maximum cover omitting e_max has largest selected rank strictly below rho(e_max), whereas a cover containing it has largest selected rank rho(e_max). Hence F^max itself contains e_max. Since no selected edge can follow the globally largest edge in an increasing rail, e_max is necessarily the terminal edge of one rail of F^max. Consequently one of the three terminal dimers of the synchronized ALL-TERMINAL wall is the physical global maximum edge.

Dually, sort selected ranks from smallest to largest and choose a global lexicographic minimum F^min. A terminal-transfer SLIDE replaces pt by the strictly smaller edge ts, so the Section 4 argument gives the ALL-SOURCE wall and excludes singleton rails. R999 supplies a maximum cover containing the globally smallest edge e_min; lexicographic minimality therefore forces e_min into F^min, and increasingness forces it to be the source edge of one rail.

Thus the acyclic branch has two global canonical poles inside one R982-connected maximum-cover space:

  F^max : ALL-TERMINAL wall + global maximum edge at a rail terminal;
  F^min : ALL-SOURCE wall + global minimum edge at a rail source.     (ER.3)

This does not yet prove that the two poles can be joined by the narrower SLIDE/DOUBLE transition set of G9, nor does it consume the extreme walls. It does identify the next closure interface: any successful acyclic closed-class theorem may work globally between two synchronized representatives already anchored to the absolute edge extremes, rather than six independent merge-seed preorders.

### 7. Full one-cut barrier at the largest terminal edge
In the global lexicographic maximum F^max, choose a rail X=(...,p,t) whose terminal selected edge pt has largest rank among the three terminal selected edges. Let Y=(y_0,...,y_m) be either foreign rail. For any selected cut y_i->y_{i+1}, consider the one-cut suffix transfer obtained by deleting y_i y_{i+1} and adding t y_{i+1}, so the suffix Y[i+1,m] is appended to X and Y[0,i] remains a rail. If this transfer were tight, its first new seam would give rho(pt)<rho(t y_{i+1}). Since every selected edge of Y is at most the terminal edge of Y, and the terminal edge of Y has rank at most rho(pt), we have rho(y_i y_{i+1})<=rho(pt)<rho(t y_{i+1}). Thus the transfer would replace one selected edge by a strictly larger edge and increase the lexicographic selected-rank multiset, contradicting F^max.

Therefore EVERY such one-cut suffix transfer is blocked. Concretely, when i<m-1 at least one of

  (p,t,y_{i+1}),   (t,y_{i+1},y_{i+2})

is bad; at i=m-1 the sole seam (p,t,y_m) is bad. This holds simultaneously on both foreign rails. Hence the rail carrying the largest terminal edge is not merely protected at the two native sources: its terminal supports a complete one-cut suffix barrier against both other rails.

The exact source-dual holds at F^min. Choose a rail whose source selected edge is smallest among the three source edges. Every one-cut prefix transfer from either foreign rail into that source is blocked, because any successful transfer would replace a selected edge no smaller than that source edge by a strictly smaller cross edge and contradict lexicographic minimality.

This strengthens the global poles from six endpoint gates to two full one-cut barrier systems. It does not by itself supply canonical R895 barrier indices, because the moving objects are rail suffixes/prefixes rather than single exterior vertices, and no two-cover conclusion is claimed.
