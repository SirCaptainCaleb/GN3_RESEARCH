# Same-support R435 portals carry edge-generated birth ancestry, not an independent monodromy coordinate

**Workspace:** D17
**State:** established
**Key:** `r435-same-support-portal-edge-generated-ancestry`

**Summary:** Specialize the accepted Reverse Ear proof to two Hamilton paths P,Q on the same support. Any reverse-order consecutive Q contacts form one selected Q chord v_i->v_j. If i=j+1 this is the adjacent selected reversal. If i>j+1, the two R435 seam tests are (v_{i-1},v_i,v_j) and (v_i,v_j,v_{j+1}). A failed left seam gives the tight trimer (v_j,v_i,v_{i-1}), whose two directed states are exactly the reversals of the selected Q chord and the adjacent selected P edge v_{i-1}->v_i; a failed right seam is dual using P edge v_j->v_{j+1}. If both seams pass, the proper tight cycle is exactly the selected Q chord v_i->v_j plus the contiguous selected P interval v_j->...->v_i. Hence every same-support R435 portal has a canonical finite birth certificate made solely from selected-edge ancestry in the two input forests and fixed physical vertices. Proper-cycle CYCLE-ROTATE changes only the state-determined break, while the birth certificate stays fixed. Together with SV39182, square-only support-changing one-edge transport cannot create nontrivial monodromy in these birth certificates. Therefore R435 itself is not an independent global holonomy generator: any surviving history-bearing loop must use a later portal conversion/non-one-edge move that changes how this edge-generated certificate is carried.

### 1. Exact same-support specialization of Reverse Ear
Let

  P=(v_0,...,v_k)

and let `Q` be another Hamilton tight path on the SAME physical support. Choose two consecutive vertices of `Q`, written in their `P` labels as

  v_i -> v_j,

with `i>j`. Because every vertex of `Q` is already a `P`-vertex, the Reverse-Ear subpath `E` between these consecutive contacts is exactly the single selected Q-state

  e_Q=(v_i,v_j).                                        (RA.1)

There is no hidden internal ear vertex in the same-support case.

### 2. Adjacent reversal is already one selected-edge ancestry carrier
If `i=j+1`, accepted R435 is in its first branch: `Q` literally selects

  v_{j+1} -> v_j,

which reverses the selected P-state

  e_P=(v_j,v_{j+1}).                                    (RA.2)

Thus the portal birth certificate is simply the physical selected-edge ancestry pair `(e_P,e_Q)` on one dimer. This is exactly the selected-reversal species already transported by SV36339.

### 3. A reverse-trimer birth uses exactly two selected input edges
Assume `i>j+1`. In the full accepted proof P448 the two tested seams become, because `E` is one state,

  s_L=(v_{i-1},v_i,v_j),
  s_R=(v_i,v_j,v_{j+1}).                                (RA.3)

If `s_L` is bad, R3 gives the literal tight reverse trimer

  T_L=(v_j,v_i,v_{i-1}).                                (RA.4)

Its two directed states are

  v_j -> v_i,
  v_i -> v_{i-1},

which are exactly the reversals of

  e_Q=(v_i,v_j) selected by Q,
  e_P^-=(v_{i-1},v_i) selected by P.                    (RA.5)

Likewise, if `s_R` is bad, R3 gives

  T_R=(v_{j+1},v_j,v_i),                                (RA.6)

whose states reverse exactly

  e_P^+=(v_j,v_{j+1}) selected by P,
  e_Q=(v_i,v_j) selected by Q.                          (RA.7)

Therefore a same-support R435 reverse trimer has no additional hidden ancestry. Its complete birth certificate is one selected Q chord plus one adjacent selected P edge, together with the choice of left or right seam.

### 4. A proper-cycle birth is one Q chord plus one contiguous P interval
If both seams in (RA.3) are tight, the constructive cycle in P448 is

  C=(v_i,v_j,v_{j+1},...,v_{i-1},v_i).                  (RA.8)

Its directed rim consists exactly of

  e_Q=(v_i,v_j)

followed by the contiguous selected P-edge interval

  (v_j,v_{j+1}), (v_{j+1},v_{j+2}), ..., (v_{i-1},v_i). (RA.9)

Hence the proper-cycle birth certificate is the finite ordered tuple

  B_C=( e_Q ; e_j,e_{j+1},...,e_{i-1} ).                (RA.10)

Again there is no extra ancestry coordinate produced by the Reverse-Ear proof.

### 5. Currentization preserves the portal but adds no new birth history
For a reverse trimer, accepted R4 may currentize the graph-intrinsic tight trimer as one rail of a maximum three-forest. The exact R435 birth record (RA.5) or (RA.7) may of course be retained as metadata, but it is already completely determined by the named input selected-edge ancestries and physical vertices.

For a proper cycle, SV25652 chooses one fixed exact two-cover of the complement and currentizes every cyclic break. SV28309 gives explicit reversible CYCLE-ROTATE edges between neighboring breaks. The physical cycle `C` and its birth tuple (RA.10) are unchanged throughout; only the omitted rim edge / current break moves. That break is state-determined in the sense of SV35882.

Thus CYCLE-ROTATE itself contributes no change to the R435 birth certificate.

### 6. Edge-token monodromy extinction kills the square-only transport of R435 birth data
SV39182 proves that canonical selected-edge ancestry has trivial monodromy on every portal-free closed walk of support-changing one-edge transfers: nontrivial edge-token transport forces augmentation, a current trimer, a current cycle, or a genuinely non-one-edge portal.

The R435 birth certificates (RA.2), (RA.5), (RA.7), and (RA.10) are finite tuples of precisely those selected-edge ancestries plus fixed physical vertex labels. Therefore any transport of an R435 birth certificate through the square-only support-changing one-edge sector is also monodromy-trivial, coordinate by coordinate.

In particular, the Hall-to-R435 entrance SV37965 cannot obtain a nonzero global history class merely by declaring the emitted reversal/trimer/cycle to be a new independent mark and then moving through ordinary one-edge exchange squares. The mark already factors through the edge ancestry which SV39182 makes flat.

### 7. Universal-discrepancy consequence
Same-support R435 is therefore a PORTAL CREATOR but not, by itself, an independent MONODROMY GENERATOR.

Any genuinely nontrivial history-bearing loop descending from an R435 discrepancy must include a later operation that changes the carrier model of the edge-generated birth certificate: for example a non-one-edge component recompletion, an R561 support escape, or another explicit portal-conversion theorem which reattaches the ancestry in a new form.

Equivalently, within the transition system generated only by

  same-support R435 birth,
  graph-intrinsic trimer currentization,
  proper-cycle CYCLE-ROTATE,
  portal-free support-changing one-edge squares,

the R435 birth ancestry is flat.

This is a direct restriction on the G15 global-monodromy program: a successful nonzero Hall/Arm-M class must live in portal conversion, not in the already-completed one-edge exchange sector or in the raw R435 birth event itself.
