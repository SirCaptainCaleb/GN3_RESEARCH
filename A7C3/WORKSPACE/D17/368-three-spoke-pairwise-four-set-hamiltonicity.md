# Any two spokes of a common three-spoke packet form a Hamilton outer four-set

**Workspace:** D17
**State:** established
**Key:** `three-spoke-pairwise-four-set-hamiltonicity`

**Summary:** If three distinct physical spokes x,y,z satisfy (a,x,c),(a,y,c),(a,z,c), then for every distinct p,q among {x,y,z} the four-set {a,c,p,q} has a literal Hamilton P4. Apply R3 to {p,c,q}: either (p,c,q) is tight, giving (a,p,c,q), or (q,c,p) is tight, giving (a,q,c,p). Consequently any exact deletion cover whose deleted dimer is {a,p} and whose opposite rail is the dimer {c,q} (or the dual arrangement) immediately closes H with the complementary Hamilton rail. In the SV58280 three-spoke lineage this consumes exact whole-marker remints of all three source P4 births B_L,B_R,B_X, not only the outer B_X remint treated in SV88934.

### 1. Pairwise four-set Hamiltonicity inside a three-spoke packet
Let a,c,x,y,z be five distinct physical vertices and assume

  (a,x,c), (a,y,c), (a,z,c)

are tight. Fix any two distinct spokes p,q in {x,y,z}.

Apply boundary antisymmetry R3 to the three-set {p,c,q}, displayed with middle c. Exactly one of

  (p,c,q), (q,c,p)

is tight.

If (p,c,q) is tight, concatenate it with the retained spoke turn (a,p,c). Then

  (a,p,c,q)

is a literal tight Hamilton P4 on {a,c,p,q}.

If (q,c,p) is tight, concatenate it with (a,q,c). Then

  (a,q,c,p)

is a literal tight Hamilton P4 on the same four-set.

Therefore every pair of spokes p,q determines a Hamilton outer four-set

  H[{a,c,p,q}] has a tight Hamilton P4.                 (TS4.1)

No edge-order representation, P5 order, or payment ancestry is needed beyond the three common-orientation spoke turns.

### 2. Exact dimer-rail remints on two spokes close immediately
Suppose, for distinct spokes p,q, an exact deletion representative has the form

  H-{a,p} = (c,q) | Q                                   (TS4.2)

with Q a Hamilton tight path on the complementary vertex set. By (TS4.1), {a,c,p,q} has a Hamilton tight P4 P. The supports of P and Q are disjoint and partition V(H), so

  H = P | Q

is a spanning two-cover.

The exact head/tail dual and rail exchange are identical. Thus any whole-marker remint whose two physical dimers are {a,p} and {c,q} with p,q distinct source spokes is impossible in a counterexample.

### 3. Source-birth consequence
In the SV58280/SV83487 lineage write the three spokes as x,y,z. The three source PAYABLE-FOUR P4 births use the support pairs

  B_L : {x,a} with {y,c},
  B_R : {a,y} with {c,z},
  B_X : {x,a} with {c,z}.

Each pair is of the form covered by Section 2. Therefore exact whole-marker remint of any one of B_L,B_R,B_X closes H immediately. SV88934 is the B_X instance with later notation x=u,y=m,z=v; the present section records the pairwise parent statement.

### 4. G29 use and fence
This widens the forbidden exact-remint surface but does not yet eliminate a non-source rebirth involving a fourth frame vertex t outside {x,y,z}. In the canonical SV81686 rebirth B_new=((a,y),(c,t)), the branch t in {x,z} is now an exact-remint trap; only t outside the three-spoke set can support a genuinely new physical dimer type.

No alternative paid descendants are braided. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```