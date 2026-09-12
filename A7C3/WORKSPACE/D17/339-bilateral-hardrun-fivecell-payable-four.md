# Every bilateral hard-run five-cell is PAYABLE-FOUR; a nonHamilton survivor is double R407

**Workspace:** D17
**State:** established
**Key:** `bilateral-hardrun-fivecell-payable-four`

**Summary:** At one interior node of the SV73346 alternating bilateral hard run, normalize J_b=(a,b,c), J_d=(c,d,a), J_e=(a,e,c). The common parent also contains (d,c,b),(d,c,e),(b,a,d),(e,a,d). Applying the current R542-to-P4 unit SV78488 to the central reverse-initial packet forces one skip-middle bypass: either (b,c,e) or (e,c,b) is tight. If the five-set {a,b,c,d,e} is Hamiltonian, its Hamilton P5 contains a P4 and hence is PAYABLE-FOUR by SV78086. Otherwise R902 supplies an ordinary-edge order. In the (b,c,e) branch, nonHamiltonicity forces de<ce and de<ad, hence (d,e,c),(e,d,a) are tight; together with (d,c,e),(e,a,d) this gives simultaneous R407 packets on {c,e} with witness d and {a,d} with witness e. In the (e,c,b) branch the dual inequalities force db<bc and db<ad, yielding R407 on {b,c} with witness d and on {a,d} with witness b. SV79137 says every R407 packet already contains a PAYABLE-FOUR birth. Thus the full five-cell packet is always PAYABLE-FOUR, so at fixed-E phase zero SV78086 yields TWO-COVER, strict old-E Psi_E descent, or explicit nonquiet portal. The raw five-turn bowtie alone need not be Hamiltonian; the conclusion uses the full bilateral source packet plus its forced bypass.

### 1. Full five-cell source packet
Retain one interior node of the growth-free alternating hard run SV73346. Normalize three consecutive internal middles by

  J_b=(a,b,c),
  J_d=(c,d,a),
  J_e=(a,e,c)                                            (BF.1)

all tight. The same source frame gives the bilateral central certificates

  (d,c,b), (d,c,e),
  (b,a,d), (e,a,d)                                      (BF.2)

all tight. Thus the central carrier J_d=(c,d,a) has reverse initial dimer (d,c) tail-signed by b,e and reverse terminal dimer (a,d) head-signed by b,e. All five physical vertices a,b,c,d,e are distinct.

Apply current unit SV78488 to the reverse-initial R542 packet (d,c) with witnesses b,e. Its two seam tests are (c,b,a) and (c,e,a), which are complete reversals of the already-tight neighbor turns J_b=(a,b,c) and J_e=(a,e,c). Hence both tests are bad. The BOTH-BAD branch is forced, so R584 gives one of the two skip-middle P4s

  (a,b,c,e),
  (a,e,c,b).                                             (BF.3)

Equivalently one of the bypass turns

  (b,c,e),
  (e,c,b)                                                (BF.4)

is tight. No payment choice has been made.

### 2. Hamiltonian branch is already PAYABLE-FOUR
Let X={a,b,c,d,e}. If H[X] has a Hamilton tight P5, choose any consecutive four vertices of that P5. They form a proper tight P4. By SV78086 every proper P4 contains two disjoint opposite-polarity boundary dimers of total support mass four. Therefore the full five-cell packet is PAYABLE-FOUR.

Hence only the nonHamiltonian branch of X needs classification.

### 3. Edge-order classification when (b,c,e) is the bypass
Assume (b,c,e) is tight and X is nonHamiltonian. Accepted R902, via the R887 comparison representation, supplies a strict total order < on the ordinary edges of K_X in which every tight turn (u,v,w) means uv<vw.

From (a,b,c), (b,c,e), (d,c,e), (c,d,a), (b,a,d), and (e,a,d) we retain in particular

  ab < bc < ce,
  cd < ce,
  cd < ad,
  ab < ad,
  ae < ad.                                               (BF.5)

Compare de with ce. If ce<de, then

  ab < bc < ce < ed,

so R887 makes (a,b,c,e,d) a tight Hamilton P5, contradiction. Hence

  de < ce,                                                (BF.6)

which is exactly the tight turn (d,e,c).

Now compare de with ad. If ad<de, then using (BF.6)

  ba=ab < ad < de < ec=ce,

so (b,a,d,e,c) is a tight Hamilton P5, contradiction. Hence

  de < ad,                                                (BF.7)

which is exactly the tight turn (e,d,a).

Together with the source turns (d,c,e) and (e,a,d), equations (BF.6)-(BF.7) give two simultaneous bidirectional same-witness packets:

- on the physical dimer {c,e}, both tested orientations (c,e) and (e,c) are HEAD-signed by the same witness d, via (d,c,e) and (d,e,c);
- on the physical dimer {a,d}, both tested orientations (a,d) and (d,a) are HEAD-signed by the same witness e, via (e,a,d) and (e,d,a).

Thus the nonHamiltonian survivor in this bypass branch contains TWO simultaneous R407 packets.

### 4. Edge-order classification when (e,c,b) is the bypass
Assume instead (e,c,b) is tight and X is nonHamiltonian. R902/R887 now gives

  ae < ce < bc,
  cd < bc,
  cd < ad,
  ab < ad.                                               (BF.8)

Compare db with bc. If bc<db, then

  ae < ec=ce < cb=bc < bd=db,

so (a,e,c,b,d) is a tight Hamilton P5, contradiction. Hence

  db < bc,                                                (BF.9)

which is the tight turn (d,b,c).

Compare db with ad. If ad<db, then

  ea=ae < ad < db < bc,

so (e,a,d,b,c) is a tight Hamilton P5, contradiction. Hence

  db < ad,                                                (BF.10)

which is the tight turn (b,d,a).

Together with the source turns (d,c,b) and (b,a,d), this gives two simultaneous R407 packets:

- on {b,c}, both orientations (c,b),(b,c) are HEAD-signed by common witness d;
- on {a,d}, both orientations (a,d),(d,a) are HEAD-signed by common witness b.

Thus the second nonHamiltonian bypass branch is also double R407.

### 5. PAYABLE-FOUR conclusion and phase-zero consumer
SV79137 reads the accepted R407 proof one step earlier and shows that every R407 packet already contains a direct source-visible mass-four balanced-pair birth before the later interaction label. Therefore in either nonHamiltonian branch above, choose either one of the two R407 packets: the full five-cell packet is PAYABLE-FOUR.

Combining with Section 2 gives the parent conclusion

  BILATERAL HARD-RUN FIVE-CELL -> PAYABLE-FOUR.           (BF.11)

If this packet is born while working relative to an old fixed endpoint pair E in phase zero, apply SV78086. There is a finite ancestry-retaining continuation to exactly

  TWO-COVER,
  STRICT descent of the old fixed-E clock Psi_E,
  or EXPLICIT NONQUIET PORTAL.                            (BF.12)

Thus two neighboring reversed-floor atoms cannot form a silent rank-flat five-cell recurrence. The only surviving continuation is explicit nonquiet geometry, not an unclassified bowtie or an R407 terminal label.

### 6. Scope fence
The original five-turn bowtie displayed in the earlier handoff is not by itself contradictory under R902: its comparison inequalities admit acyclic orders. The theorem uses the FULL SV73346 bilateral source packet (BF.1)-(BF.2) and the forced SV78488/R584 bypass (BF.3).

The two R407 packets coexist as source certificates in the nonHamiltonian branch, but their paid descendants are alternatives. No simultaneous current paid floors are asserted. BF.12 does not call the explicit nonquiet portal progress. R24 and R5 are unused.

## References

```json
[
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