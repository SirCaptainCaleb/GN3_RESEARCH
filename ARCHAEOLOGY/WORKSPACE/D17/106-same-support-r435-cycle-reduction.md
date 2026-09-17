# Same-support R435 reduces to selected reversal or a five-Hamiltonian directed triangle

**Workspace:** D17
**State:** established
**Key:** `same-support-r435-cycle-reduction`

**Summary:** Same-support R435 geometry reduces to an actual full-support selected reversal only in the adjacent-chord branch, or else to local three-support reversal / a tight directed triangle after seam tests and cycle shortening. Local reversal is not silently promoted to a Hamilton-order discrepancy, and a triangle produced after a failed shortening seam need not be contiguous in the reference rail. The directed triangle is nevertheless five-Hamiltonian by R887+R902. R508 forces it to be crossing-active in every relevant pair-deletion cover, with generic finite transition bound 1<=tau_Y<=4; every exterior singleton-deletion cover also crosses Y, and a surviving singleton tau=1 cover has block profile b_Y=1,b_E=2. Endpoint- and seam-controlled absorption remains open.

### 1. Same-support R435 ears are selected chords
Let

  P=(v_0,v_1,...,v_r), \qquad Q

be two Hamilton tight paths on the SAME physical vertex support X. Apply accepted R435/P448 to a pair of consecutive P-contacts along Q that occur in reverse P-order, say v_i then v_j with i>j. Because every vertex of Q lies in X=V(P), an R435 ear having no internal P-contact has no internal vertices at all. It is exactly the single Q-selected state

  v_i v_j.                                                    (CR.1)

Thus if i=j+1, (CR.1) is a full-support selected-edge reversal of the P-state v_j v_i, because both P and Q are Hamilton paths on X.

Assume i>=j+2. The two R435 seam tests specialize exactly to

  A=(v_{i-1},v_i,v_j), \qquad B=(v_i,v_j,v_{j+1}).            (CR.2)

If A is bad, R3 gives the tight reverse trimer

  (v_j,v_i,v_{i-1}).                                         (CR.3L)

This trimer locally selects the reverse state v_i v_{i-1} of the P-edge v_{i-1}v_i. It does NOT by itself construct a Hamilton path on all of X with that reversed state.

If B is bad, R3 gives

  (v_{j+1},v_j,v_i).                                         (CR.3R)

This trimer locally selects the reverse state v_{j+1}v_j of the P-edge v_jv_{j+1}. Again this is only a local three-vertex reversal until a full-support Hamilton realization is separately supplied.

If both A and B are tight, the proper R435 cycle is literally

  v_j,v_{j+1},...,v_i,v_j.                                (CR.4)

At this first R435 stage the cycle support is one contiguous interval of P closed by the selected chord v_i v_j.

### 2. Every reverse trimer reduces to a local reversal or a directed 3-cycle
The following local compiler uses only boundary antisymmetry. Let

  T=(x,u,v)

be any tight trimer on three distinct vertices. Test the reversal-pair mate (x,v,u).

If (x,v,u) is tight, then the two tight trimers T and (x,v,u) select the physical dimer {u,v} in opposite directions on this three-vertex support. Call this a LOCAL DIMER REVERSAL. No Hamilton order on any larger ambient support is asserted.

Suppose instead that (x,v,u) is bad. R3 gives

  (u,v,x) \text{ tight}.                                    (CR.5)

Now test (v,x,u). If it is bad, R3 gives (u,x,v) tight. The trimers (x,u,v) and (u,x,v) then give a LOCAL reversal of the state xu on the same three-set.

The only remaining case is

  (x,u,v),\quad (u,v,x),\quad (v,x,u) \text{ all tight}.      (CR.6)

Call (CR.6) a tight directed 3-cycle. Its three complete reversals are all bad by R3.

Consequently every R435 reverse-trimer output enters exactly one of two local currencies:

  a local three-support dimer reversal,
  or a tight directed 3-cycle.                               (CR.7)

A local reversal may enter `fixed-complement-selected-reversal-normal-form` only after the surrounding construction supplies two Hamilton paths on the FULL common active support carrying the opposite directed state and the same literal complement. The trimer itself is not such a realization.

### 3. Proper cycles shorten to the same local currencies
Let

  C=(c_0,c_1,...,c_{m-1})

be a vertex-simple tight directed cycle of length m>=4, so every cyclic consecutive triple is tight. In the initial same-support R435 application (CR.4), take the displayed cyclic order to agree with the contiguous P interval.

Delete c_0 and test whether

  C'=(c_1,c_2,...,c_{m-1})

is still a tight directed cycle. Every cyclic turn of C' is inherited from C except exactly the two new wrap seams

  (c_{m-2},c_{m-1},c_1), \qquad (c_{m-1},c_1,c_2).            (CR.8)

If both are tight, C' is a tight directed cycle of length m-1. If either seam is bad, R3 supplies its complete reverse as a tight trimer, and Section 2 gives a local dimer reversal or a tight directed 3-cycle.

Iterating successful shortening terminates at length three or at the first failed shortening seam. IMPORTANT: after a failed shortening seam, the resulting trimer, and hence a directed triangle produced by Section 2, need not be a contiguous subinterval of the original Hamilton path P. Therefore the correct common normal form is

  a full-support selected reversal if the original adjacent-chord branch already supplied one,
  a local three-support reversal requiring later currentization,
  or a tight directed 3-cycle.                               (CR.9)

This section does not silently promote local reversal to a Hamilton-order disagreement.

### 4. The irreducible triangle is five-Hamiltonian
Let Y={x,u,v} support the tight directed 3-cycle (CR.6). Under accepted R887, the ordinary edges xu,uv,vx form the directed comparison triangle

  xu -> uv -> vx -> xu.

Hence every induced boundary tournament containing Y is non-edge-orderable: its comparison orientation already contains this directed cycle.

Take any two distinct exterior vertices d,e. The induced five-vertex system on

  Y+{d,e}

is therefore non-edge-orderable. Accepted R902/P973 says every non-Hamiltonian boundary tournament on five vertices is edge-orderable. By contrapositive,

  Y+{d,e} \text{ is Hamiltonian}.                             (CR.10)

Thus the directed-triangle residue is a universal FIVE-SUPPORT absorber: every two-vertex extension of its three-set has a Hamilton tight path. This statement is graph-intrinsic and does not prescribe endpoints, endpoint roles, first/last dimers, or a particular Hamilton order.

In particular, if the original order conflict lives on the pair-deletion residue H-{j,k}, then Y+{j,k} is a literal Hamilton five-support. It does not by itself splice into an untouched complement or restore both sides of an old rail.

### 5. Pair-deletion and singleton currentization of the triangle
Retain a tight directed 3-cycle Y and distinct exterior labels j,k. By (CR.10), Y+{j,k} has a Hamilton tight path Q_5.

Suppose an exact two-cover T of H-{j,k} is supplied and V(H)-{j,k}-Y is nonempty. Apply accepted R508 with deletion block D={j,k}, absorber remainder S=Y, and Hamilton path Q_5 on D union S. Every such T selects a directed state with exactly one endpoint in Y. Thus the triangle is crossing-active in every representative of this pair-deletion fiber.

No contiguity of Y in a retained Hamilton rail should be inferred after the shortening/local-trimer compiler. In any two-path cover, the three physical vertices of Y occupy at most three Y-blocks. Since a class occurring in b_Y blocks contributes at most 2b_Y boundary transitions and the two rails have only four component ends in total, the crude finite currentization bound is

  1 <= tau_Y(T) <= 4.                                       (CR.11)

If in a particular source representative Y is known independently to occur as one contiguous block, then tau_Y is one when that block meets a rail end and two when it is internal. This is a specialization, not the generic compiler output.

There is also a singleton-fiber consequence. Fix d outside Y and let T be any literal two-path cover of H-d. Put E=V(H)-(Y+{d}). Suppose T selected no Y|E state. Then each path component lies wholly on one side. With both sides nonempty, one component is a Hamilton path on Y and the other a Hamilton path R on E. Choose an endpoint e of R. The five-set Y+{d,e} is Hamiltonian by (CR.10), while R-e is a tight path (possibly empty). These paths give a spanning cover of H by at most two paths, contradicting pc(H)>2. Hence every exterior singleton-deletion two-cover crosses Y.

If such a singleton cover has exactly one Y|E transition, let b_Y,b_E be its numbers of maximal Y- and E-blocks. A two-path forest with one class transition has b_Y+b_E=3. If b_E=1, then E itself is Hamiltonian, and the same endpoint-absorption argument closes H. Therefore every surviving singleton tau_Y=1 cover has

  b_Y=1,  b_E=2.                                            (CR.12)

So the durable triangle currency is universal five-Hamiltonicity plus cover-current crossing pressure. The remaining consumer must use actual endpoint roles, selected seams, or a second representative; neither a local reversal nor a static five-support is closure.

### Scope
This section is a compiler and currentization lemma, not a closure theorem. It preserves the distinction between full-support Hamilton-order reversal and a local three-vertex reversal. It does not assert contiguity of the terminal directed triangle, endpoint accessibility on a five-support, R561 from the triangle alone, or automatic restoration of a deletion fiber.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
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
