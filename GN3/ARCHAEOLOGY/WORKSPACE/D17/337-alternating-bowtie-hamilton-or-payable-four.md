# The full five-vertex alternating bowtie is Hamiltonian or PAYABLE-FOUR before payment

**Workspace:** D17
**State:** established
**Key:** `alternating-bowtie-hamilton-or-payable-four`

**Summary:** Retain the five-vertex hard-run packet on a,b,c,d,e with tight turns (a,b,c),(d,c,b),(c,d,a),(e,a,d),(a,e,c). The central bilateral R542/skip-middle mechanism forces one of the two bypass P4s (a,b,c,e) or (a,e,c,b). If the five-set is Hamiltonian, any four consecutive vertices give a P4 and SV78086 consumes it as a PAYABLE-FOUR portal. If it is non-Hamiltonian, R902/R887 edge-orders the five-set. In the first bypass case ab<bc<ce together with the source inequalities forces de<ce and de<ad: ce<de would give the increasing Hamilton path a-b-c-e-d; if ad<de, then ad<ab gives d-a-b-c-e while ab<ad gives b-a-d-e-c. Hence (d,e,c) and (e,d,a) are tight; together with the old (e,a,d), the physical dimer {a,d} is signed in both tested orientations with common head witness e, an R407 packet, so SV79137 supplies PAYABLE-FOUR. In the second bypass case ae<ce<bc. Non-Hamiltonicity forces bd<bc, since bc<bd gives a-e-c-b-d, and then bd<ad, since ad<bd gives e-a-d-b-c. Thus (d,b,c) and (b,d,a) are tight. The old (a,b,c) and new (d,b,c) give a same-oriented two-witness collision on (b,c); SV76748 compiles that packet to P4/P5, direct mass-four pair, or R407, each PAYABLE-FOUR via SV78086/SV79137. Therefore the exact bowtie survivor is fully classified and cannot be a silent phase-zero species: it yields TWO-COVER, strict old-E Psi descent, or an explicit nonquiet portal.

### 1. The full five-vertex hard cell
Retain five distinct physical vertices a,b,c,d,e in one growth-free alternating fixed-endpoint hard-run cell. The source packet contains the five tight turns

  (a,b,c),
  (d,c,b),
  (c,d,a),
  (e,a,d),
  (a,e,c).                                                (AB.1)

At the central turn (c,d,a), the two neighboring middles are b,e. The bilateral R542/skip-middle mechanism of SV73346 together with its source-visible P4 refinement forces, before any payment is chosen, one of the two literal bypass P4s

  K_1=(a,b,c,e),
  K_2=(a,e,c,b).                                          (AB.2)

Thus in the K_1 branch (b,c,e) is tight, while in the K_2 branch (e,c,b) is tight.

We classify the induced five-set X={a,b,c,d,e}. If X is Hamiltonian, choose any Hamilton P5 on X. Its first four vertices form a literal P4, hence a PAYABLE-FOUR portal by SV78086. The only interesting case is therefore that X is non-Hamiltonian.

### 2. R902 edge-order coordinates
Assume X is non-Hamiltonian. Accepted R902, through the R887 comparison-order mechanism, supplies a strict total order < on the ten ordinary edges of K_5 such that every tight turn (u,v,w) is represented by

  uv < vw.                                                 (AB.3)

The five source turns (AB.1) therefore give

  ab < bc,
  cd < bc,
  cd < ad,
  ae < ad,
  ae < ce.                                                 (AB.4)

We now add the appropriate bypass inequality from (AB.2).

### 3. First bypass: K_1=(a,b,c,e)
Here

  bc < ce.                                                 (AB.5)

We first claim

  de < ce.                                                 (AB.6)

Indeed, if ce<de then

  ab < bc < ce < de,

so the edge-order mechanism makes

  (a,b,c,e,d)

a Hamilton tight P5 on X, contradiction.

Next claim

  de < ad.                                                 (AB.7)

Suppose instead ad<de. Since the edge order is strict, compare ad and ab.

- If ad<ab, then

    ad < ab < bc < ce,

  and (d,a,b,c,e) is a Hamilton P5.

- If ab<ad, then using (AB.6),

    ab < ad < de < ce,

  and (b,a,d,e,c) is a Hamilton P5.

Both are impossible. Hence (AB.7) holds.

By (AB.6)-(AB.7), the turns

  (d,e,c),
  (e,d,a)                                                  (AB.8)

are tight. The source packet already contains (e,a,d). Therefore the two tested orientations

  (a,d),  (d,a)

of the same physical dimer {a,d} are both HEAD-signed by the same witness e:

  (e,a,d),  (e,d,a) tight.                                (AB.9)

This is exactly an R407 bidirectional same-witness packet. Current unit SV79137 reads the accepted R407 proof one step earlier and shows that such a packet already contains a direct PAYABLE-FOUR birth. Hence the non-Hamiltonian K_1 branch is PAYABLE-FOUR before any generic interaction/payment continuation.

### 4. Second bypass: K_2=(a,e,c,b)
Here

  ce < bc.                                                 (AB.10)

We claim

  bd < bc.                                                 (AB.11)

If bc<bd, then

  ae < ce < bc < bd,

so (a,e,c,b,d) is a Hamilton P5, contradiction.

We also claim

  bd < ad.                                                 (AB.12)

If ad<bd, then by (AB.4) and (AB.11),

  ae < ad < bd < bc,

so (e,a,d,b,c) is a Hamilton P5, contradiction. Thus (AB.12) holds.

Consequently

  (d,b,c),
  (b,d,a)                                                  (AB.13)

are tight. In particular the old source turn (a,b,c) and the new turn (d,b,c) make the same tested oriented dimer

  D=(b,c)

HEAD-signed by two distinct witnesses a,d. This is a raw same-oriented R523 collision packet.

SV76748 consumes every such collision above order ten, before payment, into one of

  literal P4,
  literal P5,
  direct opposite-sign mass-four pair,
  R407 bidirectional same-witness packet.                  (AB.14)

Every output in (AB.14) is PAYABLE-FOUR in the fixed-E phase-zero calculus: P4 directly by SV78086, P5 by taking any four consecutive vertices and then SV78086, a direct mass-four pair by definition/SV78086, and R407 by SV79137 followed by SV78086.

Hence the non-Hamiltonian K_2 branch is likewise PAYABLE-FOUR.

### 5. Bowtie cancellation theorem
Combining Sections 1-4 gives the exact local theorem:

> The full five-vertex alternating bowtie generated by three consecutive hard/reversed middles cannot support an untyped rank-flat survivor. Before any unrelated reset it contains either a Hamilton P5 or source-visible signed geometry that compiles to PAYABLE-FOUR.

Therefore, relative to the old fixed endpoint pair E of the hard-run lineage, SV78086 sends the entire bowtie packet to exactly one of

  TWO-COVER,
  strict decrease of the old fixed-E clock Psi_E,
  explicit nonquiet portal.                               (AB.15)

The original five turns alone do not force Hamiltonicity; the bypass P4 from the full bilateral packet is essential. This is why the earlier raw bowtie edge-order test had surviving linear extensions.

### 6. Scope fence
This theorem does not consume the explicit nonquiet portal in (AB.15), and it does not claim alternative paid descendants coexist. Its point is sharper: the five-vertex alternating hard cell itself is no longer an independent bottom-family species. Hamiltonian and non-Hamiltonian realizations both cross the PAYABLE-FOUR boundary before reset.

R24 and R5 are unused.

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