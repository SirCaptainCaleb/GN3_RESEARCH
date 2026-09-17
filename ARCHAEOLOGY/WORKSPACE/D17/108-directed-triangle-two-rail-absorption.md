# A five-Hamiltonian directed triangle has a two-rail seam normal form

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-two-rail-absorption`

**Summary:** Let Y be a tight directed triangle and A|B an exact cover of H-Y. Both rails have order at least three. Every exterior four-set Y+x that is P4-free is the exact cyclic 00 R516 cell. Cyclic sandwich tests reduce any ordered endpoint pair to a tight a-Y-b P5, a reverse bridge with exactly two ancestral restoration holes, or a uniform one-sided whole-Y P4/shield fan. P4-free anti-aligned endpoints force a two-witness R542 packet on an actual ancestral rail boundary. Role-trapping all four rail endpoints gives a literal 2x2 head/tail rectangle on each reverse Y-dimer; accepted R846 then yields HIGH/SEAM/CLOSE, or a WEAVE whose third Y-vertex is internal. Puncturing that vertex currentizes the WEAVE back to H-Y as a three-cover versus ancestral A|B, forcing an actual ancestral A/B selected edge to cross WEAVE components and hence an R176 cross-state with exact provenance. This remains a finite absorption interface, not universal closure.

### 1. Setup and the triple-deletion rail floor
Let H be a hypothetical smallest counterexample with pc(H)>2. Let

  Y={y_0,y_1,y_2}

be a tight directed triangle, indexed cyclically so that

  (y_0,y_1,y_2), (y_1,y_2,y_0), (y_2,y_0,y_1)

are tight. Retain the five-Hamiltonicity established in `same-support-r435-cycle-reduction`: every set Y+{d,e} with distinct exterior d,e is Hamiltonian, by accepted R887+R902.

By smallest-counterexample minimality, H-Y has path-cover number at most two. It is not Hamiltonian, since a Hamilton path on H-Y together with the tight trimer Y would two-cover H. Hence choose an ACTUAL exact two-cover

  A|B

of H-Y and orient its literal orders as

  A=(a_0,a_1,...,a_p),   B=(b_0,b_1,...,b_q).

Both rails have order at least three. If A has order one, choose an endpoint b of B. A Hamilton P5 on Y+{a_0,b}, together with B-b (possibly empty), gives a spanning cover by at most two paths. If A has order two, the Hamilton P5 on Y+V(A) together with B gives a spanning two-cover. Both contradict pc(H)>2. Hence |A|>=3, and symmetrically |B|>=3. In particular a_1,a_{p-1},b_1,b_{q-1} all exist.

### 2. A P4-free one-vertex extension is exactly the cyclic 00 cell
Fix x outside Y and suppose Y+x has no Hamilton P4. Apply accepted R516 to the tight base trimer (y_0,y_1,y_2).

First, at least one of (y_0,y_1,x),(y_1,y_0,x) is tight. If both were bad, R3 would give (x,y_1,y_0) and (x,y_0,y_1) tight, and then (x,y_0,y_1,y_2) would be a Hamilton P4. Dually, at least one of (x,y_1,y_2),(x,y_2,y_1) is tight, since otherwise R3 gives (y_2,y_1,x) and (y_1,y_2,x), making (y_0,y_1,y_2,x) a Hamilton P4.

Thus the same-polarity hypotheses of R516 hold. Among its four exact no-P4 signatures, the directed-triangle requirements (y_1,y_2,y_0) and (y_2,y_0,y_1) leave only the 00 signature. Therefore every P4-free four-set Y+x is exactly the cyclic 00 cell of R516. Accepted R593 is consequently available for any fifth vertex, although the seam arguments below do not need to invoke it.

### 3. Three cyclic sandwiches have an exact R3 trichotomy
Fix any ordered exterior pair a,b. For i modulo 3 define

  L_i=(a,y_i,y_{i+1}),
  R_i=(y_{i+1},y_{i+2},b).                                (TA.1)

If L_i and R_i are both tight for some i, then

  P_i=(a,y_i,y_{i+1},y_{i+2},b)                           (TA.2)

is a literal Hamilton P5 on Y+{a,b}. Call this the CYCLIC SANDWICH branch.

Assume no index has both L_i,R_i tight. If for some i both L_i and R_{i-1} are bad, R3 gives

  (b,y_{i+1},y_i),   (y_{i+1},y_i,a)

and hence the tight reverse bridge

  K_i=(b,y_{i+1},y_i,a).                                  (TA.3)

Call this REVERSE-BRIDGE.

Suppose neither (TA.2) nor (TA.3) occurs. Then whenever L_i is bad, R_{i-1} must be tight. Since no sandwich occurs, R_{i-1} tight forces L_{i-1} bad. Therefore one bad L_i propagates around the 3-cycle, making all three L_i bad and all three R_i tight. If no L_i is bad, all three L_i are tight, and the no-sandwich assumption makes all three R_i bad.

Thus the only remaining possibilities are the two UNIFORM branches:

  all L_i bad and all R_i tight,                            (TA.4a)
  all L_i tight and all R_i bad.                            (TA.4b)

In (TA.4a), every order (y_i,y_{i+1},y_{i+2},b) is a Hamilton P4 on Y+b, while R3 turns the three bad L_i into the full reverse shield

  (y_{i+1},y_i,a) tight for all i.                          (TA.5a)

In (TA.4b), every order (a,y_i,y_{i+1},y_{i+2}) is a Hamilton P4 on Y+a, while the three bad R_i give

  (b,y_{i+2},y_{i+1}) tight for all i.                      (TA.5b)

### 4. Anti-aligned endpoint specialization: reverse bridges have only two restoration holes
Apply Section 3 to the ancestral source/terminal pair a=a_0, b=b_q.

If a cyclic sandwich (TA.2) occurs, then P_i | A[1,p] | B[0,q-1] is a literal spanning three-cover of exactly the anti-aligned bridge form in accepted R485. Its bridge has three internal Y-vertices, so the required bridge-length floor holds. The same displayed configuration also satisfies the strengthened R494/R495 contract, and R501 is a legal downstream compiler once the R495 fork is reached. Thus the branch enters the historical anti-aligned bridge machinery with all ancestral rails and witness identities retained; no R501 conclusion is asserted without following its exact predecessor branch.

Suppose instead that a reverse bridge K_i=(b_q,y_{i+1},y_i,a_0) occurs. Let h=y_{i+2} be the unused triangle vertex. The candidate long order

  (b_0,...,b_{q-1},b_q,y_{i+1},y_i,a_0,a_1,...,a_p)         (TA.6)

contains every vertex of H except h. Every turn in (TA.6) is inherited from A, B, or K_i except exactly

  s_B(i)=(b_{q-1},b_q,y_{i+1}),
  s_A(i)=(y_i,a_0,a_1).                                     (TA.7)

If both are tight, (TA.6) together with the singleton h is a spanning two-cover, impossible. Hence at least one hole in (TA.7) is bad. R3 gives the exact labelled shields

  s_B(i) bad => (y_{i+1},b_q,b_{q-1}) tight,                (TA.8B)
  s_A(i) bad => (a_1,a_0,y_i) tight.                        (TA.8A)

Thus REVERSE-BRIDGE is already a two-hole spanning proposal whose failure is attached to the actual ancestral terminal or source dimer. The exact dual applies to the other anti-aligned pair b_0,a_p.

### 5. If both endpoint four-sets are P4-free, an ancestral R542 packet is forced
Assume Y+a_0 and Y+b_q are both P4-free. Then for every i, L_i=(a_0,y_i,y_{i+1}) is bad, since otherwise (a_0,y_i,y_{i+1},y_{i+2}) would be a Hamilton P4. Likewise every R_i=(y_{i+1},y_{i+2},b_q) is bad. Hence all three reverse bridges K_i of (TA.3) are tight.

For each i, the two restoration holes (TA.7) cannot both be tight. Across i=0,1,2 there are therefore three failure clauses. Pigeonhole gives at least two failures on one side.

If s_A(i),s_A(j) are bad for distinct i,j, then (TA.8A) gives two distinct same-tail witnesses y_i,y_j on D_A=(a_1,a_0). Since K_A=(a_0,a_1,a_2) is a literal tight trimer, D_A is exactly its reverse initial boundary dimer. This is a genuine accepted R542-ready packet on the ACTUAL A-rail boundary.

If instead two B-side holes fail, (TA.8B) gives two distinct same-head witnesses from Y on D_B=(b_q,b_{q-1}), the reverse terminal boundary dimer of K_B=(b_{q-2},b_{q-1},b_q).

Thus

  Y+a_0 and Y+b_q both P4-free
  => an R542 packet on D_A or D_B, with two named witnesses in Y.   (TA.9)

No reminting or tested-orientation ambiguity occurs. The dual anti-aligned pair b_0,a_p gives the corresponding packet on B's reverse initial dimer or A's reverse terminal dimer.

### 6. Role-correct endpoint exposure has one restoration hole
For the source a_0, a Hamilton P4 on Y+a_0 is role-correct exactly when it ends at a_0. Such a path has the form F=(y_i,y_{i+1},y_{i+2},a_0). Concatenating F with A[1,p] has exactly one new seam

  (y_{i+2},a_0,a_1).                                       (TA.10)

If it is tight, the resulting path on Y+V(A), together with B, spans H in two paths. Hence in a counterexample every role-correct source-end P4 forces

  (a_1,a_0,y_{i+2}) tight.                                  (TA.11)

If no Hamilton P4 on Y+a_0 ends at a_0, then every candidate (y_i,y_{i+1},y_{i+2},a_0) is bad at its final mixed turn. Therefore

  (a_0,y_{i+2},y_{i+1}) tight for every i.                  (TA.12)

Equivalently the source endpoint a_0 head-signs all three reverse Y-dimers.

Dually, for the terminal a_p, a role-correct P4 starts at a_p. Failure of its sole restoration seam gives a reverse terminal-boundary shield; complete absence of a source-exposing P4 forces

  (y_{i+1},y_i,a_p) tight for every i,                      (TA.13)

so a_p tail-signs every reverse Y-dimer. The same statements hold for b_0 and b_q.

Consequently, if ALL FOUR rail endpoints are role-trapped, then for every reverse triangle dimer D_i=(y_{i+1},y_i) the two sources a_0,b_0 are head witnesses and the two terminals a_p,b_q are tail witnesses on the identical tested orientation. Accepted R523 therefore gives the synchronized literal P4 fan

  (h,y_{i+1},y_i,t) tight

for every h in {a_0,b_0}, every t in {a_p,b_q}, and every i. This is a 2-by-2 endpoint fan on each of the three physical reverse Y-dimers.

### 7. The all-role-trapped rectangle enters R846 and currentizes WEAVE back to H-Y
Fix one reverse Y-dimer

  D_i=(y_{i+1},y_i)

in the all-role-trapped branch. Section 6 gives exactly the 2x2 signed-dimer rectangle required by accepted R846: head set {a_0,b_0} and tail set {a_p,b_q}, all on the same tested orientation D_i.

By smallest-counterexample minimality H-D_i has path-cover number at most two, and it cannot be Hamiltonian because a Hamilton path on H-D_i together with the vacuous dimer D_i would two-cover H. Hence H-D_i has an exact two-cover T. Both T-rails are nontrivial: if one were a singleton {x}, the other would be Hamiltonian on H-(D_i union {x}); boundary antisymmetry supplies some tight Hamilton trimer on the three vertices V(D_i) union {x}, and that trimer together with the other rail would two-cover H.

Therefore accepted R846 applies to D_i and T. It yields HIGH, SEAM, CLOSE, or WEAVE. Retain the exact R846 output rather than replacing it by a generic P4/R542 label.

In the WEAVE branch, the two T-rail starts are exactly a_0,b_0 and the two ends exactly a_p,b_q. Let y_k be the third vertex of Y, so Y=V(D_i) union {y_k}. Since y_k is none of the four T endpoints, it is internal on one T rail. Deleting y_k splits that rail into two nonempty tight paths while leaving the other T rail nonempty. Thus

  R=T-y_k

is a literal three-cover of the ORIGINAL residue

  W=H-Y.

The ancestral A|B is an exact two-cover of the same W. Because two paths cover three R-components, some selected adjacency xy of A|B must have endpoints in two distinct components of R. This selected state is not anonymous: it is a literal ancestral adjacency of A or B. Since W is proper, accepted R176 applies to xy, with any chosen Y-vertex available as a spare ambient coordinate.

Retain simultaneously:
- the tested dimer D_i and its 2x2 head/tail rectangle;
- the fixed R846 WEAVE cover T;
- the internal split vertex y_k;
- the three literal components of R=T-y_k;
- the actual ancestral A/B selected adjacency xy crossing two of those components;
- the chosen spare Y-label if R176 is invoked.

Thus the all-role-trapped branch is sharpened to

  R846 HIGH / SEAM / CLOSE,
  or a WEAVE carrying an ancestry-current component-drop cross-state on H-Y.       (TA.14)

This does not make the R176 balanced-pair descendant current in T or A|B. The valuable output is the exact ancestral crossing and the fixed WEAVE reconstruction that produced it.

### 8. Two-probe fallback on one rail
Accepted R700 supplies a compatible downstream fence. Apply it to a chosen cyclic orientation of the trimer Y and the two actual endpoints of A. If either four-set Y+a_0 or Y+a_p has a Hamilton P4, retain that literal P4 together with the actual position of the A-endpoint in it. If that position is role-correct, Section 6 gives the one-hole restoration shield; otherwise no endpoint-role conclusion is inferred. If both four-sets are P4-free, R700 makes both reverse boundary dimers of the chosen orientation of Y simultaneous R542-ready packets with witnesses a_0,a_p. The same applies to B.

This is a fallback, not a substitute for the direct seam analysis above. In the especially rigid branch of Section 5, the stronger packet (TA.9) lies on an ancestral RAIL boundary with witnesses in Y, whereas R700's generic packet lies on a boundary of Y with rail-endpoint witnesses.

### Scope
This section does not prove universal triangle absorption. It proves a finite role- and seam-preserving normal form for the Director's two-rail target. The remaining hard branch is now a fixed-boundary reconstruction consumer: combine the one-hole boundary shields, the three reverse-bridge proposals, or the R846 WEAVE ancestry-current cross-state to force a spanning two-cover, a genuine full-support reversal/R561 support, or a strict exact complement-representative improvement. Generic payment may be used only after the stronger reconstruction ancestry displayed above has been exhausted.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R485"
    },
    {
        "relation": "dependency",
        "revision_id": "R495"
    },
    {
        "relation": "dependency",
        "revision_id": "R501"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R593"
    },
    {
        "relation": "dependency",
        "revision_id": "R700"
    },
    {
        "relation": "dependency",
        "revision_id": "R846"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
