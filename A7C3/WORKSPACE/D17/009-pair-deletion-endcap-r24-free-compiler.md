# Pair-deletion endcaps have an R24-free floor-or-collision compiler already from order nine

**Workspace:** D17
**State:** established
**Key:** `pair-deletion-endcap-r24-free-compiler`

**Summary:** Clean replacement of the R168-dependent core of historical R402: pair rigidity plus counting supplies a long residual rail, so four-end attachment failure yields either a direct mass-four pair paid by R514 or four explicit same-tested-dimer two-witness collision packets. The proof needs only R3,R429,R514,R523 and works for n>=9.

### Statement
Let H be a hypothetical smallest Strong Level-(1) counterexample of order n>=9. Fix distinct deleted vertices a,c and an arbitrary exact pair-deletion two-cover

  H-{a,c}=U|V,

with actual Hamilton orders U=(u_1,...,u_r), V=(v_1,...,v_s). For t in {a,c}, let G_t be the subset of the four physical end positions U_L,U_R,V_L,V_R at which t directly attaches: for example U_L is good for t when (t,u_1,u_2) is tight and U_R is good when (u_{r-1},u_r,t) is tight, with the dual definitions on V.

Then one of the following holds.

1. TWO-COVER: H has a spanning two-cover.
2. BLOCKED-END FLOOR: for one deleted vertex, say a, G_a is empty. Then one of U,V has order at least four, its two reverse terminal dimers are physically disjoint opposite-polarity signed supports witnessed by a, hence form a direct mass-four balanced pair. Accepted R514 yields either a spanning two-cover or an ancestry-bearing both-singleton mass-two floor.
3. COMMON-END COLLISION WEB: G_a=G_c={e} for one end position e. At every one of the four end positions there are two distinct same-polarity certificates on one literally identical tested oriented terminal dimer, witnessed by a and c. Accepted R523 therefore gives a same-support two-extension collision packet at each end position. When a rail is a dimer, its two end positions may use opposite tested orientations of the same unordered edge; these are kept as two separate R523 packets, exactly as the tested-order convention requires.

This is the R24-free core formerly hidden inside historical R402. It does not use R5, R168, R169, the singleton order-four floor, or the order-greater-than-ten gate.

### Proof
Accepted Pair-Deletion Rigidity R429 applies to the fixed pair {a,c}. Thus the displayed pair-deletion cover is exact and both rails are nontrivial: r,s>=2.

Suppose there exist distinct end positions e in G_a and f in G_c. If e and f lie on different rails, attach a at e and c at f. Each rail gains one endpoint and remains a tight path, so the two augmented rails span H. If e and f are the two opposite ends of one rail, attach a and c at those two ends; the other rail is unchanged. Again the two paths span H. Therefore in a counterexample no such distinct pair of good positions exists.

Consequently either one of G_a,G_c is empty, or both are nonempty and must equal the same singleton {e}. This is purely the four-position set argument and uses no rail-size floor.

Assume first that G_a is empty. At every end the direct a-attachment turn is bad, so R3 gives its exact complete reversal. In particular on U the left failure gives (u_2,u_1,a) and the right failure gives (a,u_r,u_{r-1}); these sign the tested reverse terminal dimers (u_2,u_1) and (u_r,u_{r-1}) in opposite polarities with the same witness a. The V-side is identical.

Now r+s=n-2>=7 and r,s>=2, so max(r,s)>=4. Choose a rail W=(w_1,...,w_m) with m>=4. Its reverse terminal dimers

  D_L=(w_2,w_1),   D_R=(w_m,w_{m-1})

are physically disjoint. The preceding reversal turns certify them with opposite polarities, so D_L,D_R form a graph-intrinsic balanced opposite-sign pair of total support mass four. The proof mechanism of accepted R514 is exactly the needed modern payment: a 2+2 mass-four pair enters R427, producing either a two-cover or a descendant with a singleton support, and R428 then pays the remaining nontrivial support while retaining certificate ancestry. Hence H closes or reaches an ancestry-bearing both-singleton mass-two floor. No R168 rail-three floor is used; order four of the chosen long rail is already enough for disjoint terminal dimers.

Finally assume G_a=G_c={e}. Fix any end position h. If h=e, both direct attachment turns for a and c are tight on the same tested oriented terminal dimer, so they are two same-polarity certificates with distinct witnesses a,c. If h!=e, both direct turns are bad; R3 reverses each, and the two resulting tight turns again test the same oriented reverse terminal dimer with witnesses a,c and the same polarity. The exact mechanism of accepted R523 says that two same-polarity certificates on one fixed tested orientation are precisely the same-support two-extension collision packet. Apply this independently at all four end positions. Tested order is retained; no identification of opposite orientations of a dimer rail is made.

This proves the trichotomy.

### Relation to the quarantined route
Historical R402/P411 invoked R168 to assert r,s>=3 and then used the resulting long rail. That invocation was stronger than necessary. R429 gives r,s>=2 directly from R3+R4, and n>=9 already forces one rail to have order at least four, which is the exact threshold for two disjoint terminal dimers. Modern R514 replaces the old R39/R174 payment wording, while R523 replaces the legacy compressed R38 collision label by its literal tested-order mechanism.

Historical R402 and its R168 ancestry remain preserved as provenance. This section is a new R24-independent proof unit; it does not repair the later historical R447 fixed-turn consumer, whose separate R387 dependency is outside this cut.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R429"},
    {"relation":"dependency","revision_id":"R514"},
    {"relation":"dependency","revision_id":"R523"}
]
```
