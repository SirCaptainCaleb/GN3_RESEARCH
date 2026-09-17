# A universal one-extension four-set forces a dense pair-core cycle of donor or crossing-portal states

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-four-set-pair-core-cycle`

**Summary:** Let H be a hypothetical smallest counterexample and S a four-set such that S+d is Hamiltonian for every d outside S, without assuming S itself Hamiltonian. Put Y=V(H)-S. Then Y, every Y-d, and every Y+s are non-Hamiltonian, and |Y|>=7. For every pair d,e in Y, R195 applied to S+d+e implies at least two core labels s in S for which (S-s)+{d,e} is Hamiltonian. Defining G_s on Y by these s-good pairs gives total edge multiplicity at least 2*C(|Y|,2), so some G_s has more than |Y|-1 edges and therefore contains a cycle. On a shortest such cycle, with T=S-s, every consecutive five-support T+{v_i,v_{i+1}} is Hamiltonian and every nonconsecutive chord support is non-Hamiltonian. For each cycle edge, its complement Y-{v_i,v_{i+1}} has path-cover number at most two by minimality: if Hamiltonian it gives an exact two-cover of H-s; otherwise any exact two-cover of H-s must select a crossing between the Hamilton five-core and/or the two complement rails. Thus every universal one-extension four-set yields an arbitrary-order closed support-exchange cycle whose edges are exact donor rows or current crossing portals, and adjacent active supports differ by one exterior label. This strictly generalizes the order-eleven donor-circuit entrance and does not use Hamiltonicity of S.

### 1. Universal one-extension setup without Hamiltonicity of the core
Let H be a hypothetical smallest Strong Level-(1) counterexample and let S be a four-vertex set such that

  S+{d} is Hamiltonian for every d in Y:=V(H)-S.             (UE.1)

No Hamiltonicity of S is assumed. The case Y empty is impossible because every four-vertex boundary tournament is trivially coverable by two dimers, so assume Y nonempty.

For every d in Y, Y-d is non-Hamiltonian. Indeed, if Y-d were Hamiltonian, its Hamilton path together with a Hamilton path on S+d from (UE.1) would be a spanning two-cover of H.                                      (UE.2)

Y itself is non-Hamiltonian. If a Hamilton path on Y existed, delete one physical endpoint d. The remaining contiguous path Hamiltonizes Y-d and contradicts (UE.2); when |Y|=1, (UE.1) would Hamiltonize H directly.                           (UE.3)

For every s in S, Y+s is also non-Hamiltonian. The three-set S-s has a Hamilton tight order by boundary antisymmetry R3. Thus a Hamilton path on Y+s together with that Hamilton trimer would two-cover H.                                      (UE.4)

Likewise H-s itself is non-Hamiltonian, because a Hamilton H-s together with singleton {s} would two-cover H. By smallest-counterexample minimality R4, every proper non-Hamiltonian support just displayed has exact path-cover number two whenever nonempty.

### 2. Every exterior vertex yields a one-for-one active exchange
Fix d in Y and choose ANY Hamilton path P_d on S+d. At least one physical endpoint of P_d lies in S, because there is only one exterior label d. Delete such an endpoint s. The remaining contiguous four-word is a Hamilton path on

  (S-s)+d.                                                   (UE.5)

Call the cell (s,d) active. Thus every exterior d has at least one active core label s. If the reciprocal support Y-d+s were Hamiltonian, then its Hamilton path together with (UE.5) would two-cover H. Hence every active cell satisfies

  Y-d+s is non-Hamiltonian.                                  (UE.6)

This is the basic one-for-one exchange obstruction and uses no near-end placement theorem.

### 3. The complement has order at least seven
The universal-extension hypothesis forces

  |Y|>=7.                                                     (UE.7)

For |Y|<=4, choose d in Y. Apart from the already-impossible |Y|=1 case, Y-d has order at most three and therefore is Hamiltonian, contradicting (UE.2).

If |Y|=6, accepted R195 applied to the six-set Y says at least four punctures Y-d are Hamiltonian, again contradicting (UE.2).

Suppose |Y|=5. For each d choose one active s(d) supplied by Section 2. Fix any s in S and apply R195 to the six-set Y+s. At least four of its six five-punctures are Hamiltonian. Deleting s leaves Y, which is non-Hamiltonian by (UE.3), so at least four of the five supports

  Y-d+s,   d in Y,                                          (UE.8)

are Hamiltonian. Hence for each fixed s at most one d makes (UE.8) non-Hamiltonian. Across the four values of s there are at most four reciprocal-bad cells. But the five labels d supply at least five active cells (s(d),d), and every active cell is reciprocal-bad by (UE.6). Contradiction. This proves (UE.7).

### 4. Every exterior pair has at least two good core colors
Fix distinct d,e in Y and apply accepted R195 to the six-set

  E=S+{d,e}.                                                  (UE.9)

Deleting d leaves S+e, Hamiltonian by (UE.1), and deleting e leaves S+d. Since R195 supplies at least four Hamilton five-punctures of E, at least two DISTINCT labels s in S satisfy

  (S-s)+{d,e} is Hamiltonian.                                (UE.10)

For each s in S define a simple graph G_s on vertex set Y by

  de in E(G_s)  iff  (S-s)+{d,e} is Hamiltonian.             (UE.11)

Equation (UE.10) says every edge de of the complete graph on Y belongs to at least two of the four graphs G_s. Therefore, writing m=|Y|,

  sum_{s in S} |E(G_s)| >= 2*C(m,2).                         (UE.12)

Some s satisfies

  |E(G_s)| >= C(m,2)/2 = m(m-1)/4.                           (UE.13)

Because m>=7, the right side is strictly greater than m-1. Thus G_s contains a cycle. Choose a shortest cycle

  C=(v_0,v_1,...,v_{r-1},v_0).                              (UE.14)

Put T=S-s, a fixed three-vertex core. For every cycle edge v_i v_{i+1}, choose and retain an actual Hamilton path

  K_i on T+{v_i,v_{i+1}}.                                   (UE.15)

Shortestness makes C chordless in G_s: for nonconsecutive cycle labels v_i,v_j,

  T+{v_i,v_j} is non-Hamiltonian.                            (UE.16)

Thus (UE.14)-(UE.16) are a literal closed one-for-one support-exchange circuit on a common physical trimer T. Consecutive active supports share T+{v_{i+1}} and exchange exactly v_i for v_{i+2}.

### 5. Every circuit edge is a donor row or a crossing portal
Fix a cycle edge de. Its Hamilton five-core is

  K=T+{d,e}.                                                 (UE.17)

The disjoint complement inside H-s is

  Z=Y-{d,e}.                                                 (UE.18)

By R4, pc(Z)<=2.

If Z is Hamiltonian, retain a Hamilton path R on Z. Then

  K | R                                                       (UE.19)

is an exact two-cover of H-s. Call de a DONOR edge at color s. Exactness follows because H-s is non-Hamiltonian.

If Z is non-Hamiltonian, R4 gives an exact two-cover

  A | B                                                       (UE.20)

of Z. Then

  K | A | B                                                   (UE.21)

is a literal three-path cover of H-s. Since H-s itself has exact path-cover number two, retain any exact two-cover U|V of H-s. That exact cover must select at least one physical adjacency joining two distinct atoms among V(K),V(A),V(B). Otherwise each U/V rail would remain inside one atom, and two rails could not cover all three nonempty atoms. Call such a selected adjacency a CROSSING PORTAL for de.

Hence every edge of the closed support circuit (UE.14) carries one of two current objects on the same singleton residue H-s:

  DONOR: an exact two-cover K_i | R_i;
  PORTAL: a literal three-atom cover K_i | A_i | B_i together with an actual exact H-s two-cover selecting a cross-atom state.                (UE.22)

No synchronization of the complement orders for different i is asserted.

### 6. Neighboring-support holonomy interface
Adjacent K_i,K_{i+1} are Hamilton paths on one-for-one neighboring five-supports. Their common support is the four-set T+{v_{i+1}}. Thus accepted R435 may be applied directly to the actual retained orders. Any nonquiet ear is localized to the single exchanged foreign label on the relevant side; equivalently this circuit lies exactly in the one-foreign neighboring-support regime isolated in SV24806. A quiet comparison retains one common literal order on the four shared vertices.

Therefore a universal one-extension four-set does not merely yield isolated five-vertex extensions. At arbitrary exterior order it yields a closed, current, one-for-one support-exchange circuit on one fixed trimer, with every edge already coupled to either an exact donor row or a physical crossing portal. This strictly generalizes the support-circuit entrance of SV17264, whose |Y|=7 Hamilton-core construction is the donor-only specialization.

This section does not prove that the circuit escapes to a two-cover and does not assume the complement residues Z are Hamiltonian. The next target is to consume the shortest circuit using the donor/portal distinction and neighboring-support R435 holonomy, or to show that persistent portal edges generate a terminal closed exchange class in the G9 sense.

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
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
