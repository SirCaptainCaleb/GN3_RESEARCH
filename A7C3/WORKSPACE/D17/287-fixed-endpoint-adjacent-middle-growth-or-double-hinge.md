# Adjacent hard middle cells force literal turn growth or a double-hinged adjacent floor

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-adjacent-middle-growth-or-double-hinge`

**Summary:** Fix an E={a,c}-aligned exact pair-deletion frame H-E=U|V and two consecutive internal vertices b,d on one displayed rail. For each middle x in {b,d}, orient E+x as its tight proper turn J_x and apply the literal predecessor/successor R3 split underlying R434. Any non-reverse choice already extends J_x to a literal P4 or P5. Thus the only hard cell is DOUBLE-REVERSE. If b,d have the same outer orientation and both cells are DOUBLE-REVERSE, R584 on the two common-pole reverse turns forces a strict P4 extension of one endpoint turn. If their outer orientations are opposite, the shared reverse seam d-c-b (after normalization J_b=(a,b,c), J_d=(c,d,a)) makes two opposite-sign hinged-dimer pairs: (b,a) with (a,d) hinged at a, and (c,b) with (d,c) hinged at c. Accepted R547 collapses each independently to an ancestry-bearing mass-two floor on the SAME singleton pair {b,d}. Therefore every adjacent internal-middle pair is either literal turn-growth at one cell or a bounded DOUBLE-HINGE atom consisting of two distinct floor births on {b,d}, one through each old endpoint a,c. No rank descent is claimed for the double-hinge atom.

### 1. One internal middle has only one hard R3 pattern
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix a physical endpoint pair

  E={a,c}

and one literal exact pair-deletion cover

  H-E=U|V.

Let b be internal in one displayed rail, with selected predecessor and successor

  r -> b -> s.

Orient the three-set E+{b} so that the proper tight turn is

  J_b=(a,b,c).                                            (AM.1)

Apply the exact R3 calculations underlying accepted R434 to the selected predecessor and successor. At the a-side exactly one of

  F_a=(r,a,b),
  R_a=(b,a,r)                                             (AM.2)

is tight. At the c-side exactly one of

  F_c=(b,c,s),
  R_c=(s,c,b)                                             (AM.3)

is tight.

Three of the four patterns already give literal strict growth of the old turn J_b:

- F_a+F_c gives the tight P5 (r,a,b,c,s);
- F_a+R_c still gives the tight P4 (r,a,b,c);
- R_a+F_c still gives the tight P4 (a,b,c,s).

Hence the only local cell that does not literally extend J_b is

  DOUBLE-REVERSE: R_a and R_c are both tight.             (AM.4)

In that cell the dimer (b,a) is tail-signed by r, while the dimer (c,b) is head-signed by s. These are opposite-polarity dimers meeting only at b, so accepted R547 already collapses them to a mass-two opposite-sign singleton pair on {a,c}. Thus even one hard cell carries a same-E floor-remint ancestry, but this alone is not called progress because it may return to the old aligned checkpoint.

### 2. Two adjacent internal middles
Now let b,d be consecutive internal vertices of the same displayed rail, with local rail segment

  r -> b -> d -> s.                                      (AM.5)

For each of b,d orient its E-triple by R3. Suppose neither cell gives the literal P4/P5 growth of Section 1. Then both are DOUBLE-REVERSE. We distinguish whether their outer orientations agree.

### 3. Same outer orientation forces strict turn growth
Assume after one common naming of E that

  J_b=(a,b,c),
  J_d=(a,d,c)                                             (AM.6)

are both tight. DOUBLE-REVERSE at b gives, from its successor d,

  (d,c,b) tight.                                         (AM.7)

DOUBLE-REVERSE at d gives, from its predecessor b,

  (d,a,b) tight.                                         (AM.8)

Apply accepted R584 with common poles A=d and C=b and probes c,a. Since both (d,c,b) and (d,a,b) are tight, one of

  (d,c,b,a),
  (d,a,b,c)                                              (AM.9)

is a literal tight P4.

The first possibility would require the turn (c,b,a) tight, but this is the complete reversal of J_b=(a,b,c) and is therefore bad by R3. Hence necessarily

  (d,a,b,c)                                              (AM.10)

is tight. This is a strict one-vertex extension of J_b.

The exact dual handles the common orientation (c,*,a). Therefore two adjacent DOUBLE-REVERSE cells with the same outer orientation cannot both remain rank-flat floor-remint cells: they force literal path growth.

### 4. Opposite outer orientation gives two independent hinge births on one adjacent pair
Assume instead, after normalization,

  J_b=(a,b,c),
  J_d=(c,d,a)                                             (AM.11)

are tight. DOUBLE-REVERSE at b gives

  (b,a,r) tight,
  (d,c,b) tight.                                         (AM.12)

Thus (b,a) is tail-signed by r and (c,b) is head-signed by d.

DOUBLE-REVERSE at d, whose predecessor is b and successor is s, gives

  (d,c,b) tight,
  (s,a,d) tight.                                         (AM.13)

Thus (d,c) is tail-signed by b and (a,d) is head-signed by s.

Now pair the dimers across the two cells rather than within them.

**HINGE a.** The tail-signed dimer (b,a) and head-signed dimer (a,d) have opposite polarity and meet in exactly the one physical hinge a. Accepted R547 deletes the hinge and produces an ancestry-bearing mass-two opposite-sign singleton pair on

  {b,d}.                                                  (AM.14)

**HINGE c.** The head-signed dimer (c,b) and tail-signed dimer (d,c) likewise have opposite polarity and meet exactly in hinge c. R547 again produces a mass-two singleton pair on the SAME physical pair

  {b,d}.                                                  (AM.15)

The two floor births are distinct historical certificates: one passes through the old endpoint a, the other through the old endpoint c. They need not be treated as simultaneously current descendants, but all four source dimers and both hinge-cut ancestries are graph-intrinsic and coexist in the common parent frame.

Call this the DOUBLE-HINGED ADJACENT FLOOR packet.

### 5. Adjacent-middle compiler
Combining Sections 1-4, every two consecutive internal middle vertices b,d in one E-aligned exact pair-deletion rail satisfy at least one of:

1. one of the two local middle cells literally extends its proper E-turn to a P4 or P5;
2. the two cells have the same outer orientation and R584 forces a strict P4 extension;
3. the two cells have opposite outer orientations and the physical adjacent pair {b,d} carries two independent R547 mass-two floor ancestries, one hinged through a and one through c.

Thus the fully anchored fixed-E portal cannot remain an anonymous sequence of R436 events. Outside literal turn growth, every adjacent hard pair is compressed to one bounded four-dimer/two-hinge certificate.

### 6. Scope fence
The DOUBLE-HINGE output is a structural compression, not by itself a decrease of Psi_E. Steering either {b,d} floor back to E may be rank-flat at a fully aligned source checkpoint. No simultaneous currentness of the two paid descendants is asserted. The durable datum is the common-parent coexistence of the four signed dimers, the two old endpoint hinges a,c, the selected adjacency b-d, and the two alternative R547 floor-birth ancestries. Consuming that double-hinge packet is the remaining alternating-orientation problem.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R547"
    },
    {
        "relation": "dependency",
        "revision_id": "R584"
    }
]
```