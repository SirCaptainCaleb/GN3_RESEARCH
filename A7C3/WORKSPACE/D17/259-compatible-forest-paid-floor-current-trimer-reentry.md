# Every paid floor re-enters current maximum-forest space through a proper trimer after at most one aligned return

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-paid-floor-current-trimer-reentry`

**Summary:** Let H be a smallest counterexample of order n>=7 and suppose an ancestry-bearing both-singleton balanced floor is active. Choose any distinct physical pair {x,z}. Accepted R429 supplies an exact two-cover U|V of H-{x,z} with both rails nontrivial; it has exactly n-6 internal rail vertices, so choose one b. Boundary antisymmetry orients {x,b,z} into a proper tight turn J=(a,b,c) with {a,c}={x,z}. R432 aligns the floor to {a,c}. Fully reconstructible R445 applies because b is internal. It yields a two-cover, an explicit geometric interaction, or one protected return to the aligned floor with a completed singleton anchor a. Reapply R445 in the same fixed U|V frame after such a return: its first predecessor birth at a now touches the completed protected anchor, so the second run cannot take the protected-return branch and must close or emit explicit geometry. Every nonclosing R445 geometric output contains an explicit proper tight trimer: growth/fusion/+2/BB outputs contain a consecutive trimer; reversal/contact outputs are or contain one; a tight cycle contains one; and the only possible order-two anchor-growth output is an R434 signed dimer together with its retained sign witness, which itself forms a tight trimer. Accepted R4 currentizes that proper trimer with an exact two-covered complement, producing an actual maximum spanning three-forest containing it literally. Thus every paid floor has a finite certificate-retaining route to closure or current maximum-forest reentry through a named proper trimer. This does not yet prove the reentered forest has lower largest-rail height, so full phased-rank descent across reentry remains open.

### 1. Start from any genuine paid floor
Let H be a hypothetical smallest Strong Level-(1) counterexample of order n>=7 and suppose an ancestry-bearing both-singleton balanced opposite-sign floor is active.

Choose any distinct physical vertices x,z. Accepted Pair-Deletion Rigidity R429 supplies an exact two-cover

  H-{x,z}=U|V                                             (FR.1)

with both rails nontrivial. Across two nontrivial paths there are exactly four rail endpoints, so among the n-2 vertices of the residue exactly

  (n-2)-4=n-6                                            (FR.2)

are internal rail vertices. Since n>=7, choose one such internal vertex b.

Boundary antisymmetry R3 says exactly one of

  (x,b,z), (z,b,x)                                       (FR.3)

is tight. Rename the outer pair as a,c so that

  J=(a,b,c)                                               (FR.4)

is a proper graph-intrinsic tight turn and {a,c}={x,z}.

### 2. Align the floor and use the internal-middle compiler
Apply accepted Complete Floor Pair Steering R432 to the active paid floor with target {a,c}. Unless H already acquires a spanning two-cover, this gives an ancestry-bearing aligned floor

  (a) | (c)                                               (FR.5)

while retaining its payment ledger.

The literal exact cover U|V from (FR.1) is unchanged graph-intrinsic data, and b is still internal on one of its rails with a selected predecessor and successor. Therefore fully reconstructible accepted R445 applies to the aligned internal-middle frame.

R445 has exactly three parent outcomes:

1. a spanning two-cover;
2. explicit non-descent geometry: historical anchor/witness contact, strict path growth or fusion, strict signed +2 extension, reverse-contact/reversal geometry, signed-BB reverse P4, or a vertex-simple tight cycle;
3. a completed protected return to an ancestry-bearing aligned floor (a),(c), with a reached as the protected singleton coordinate.   (FR.6)

### 3. The protected-return branch can occur at most once in this same frame
Suppose R445 returns through branch 3. Then the returned aligned floor retains a as a completed protected singleton anchor in the fixed-J lineage.

Apply R445 again using the SAME physical turn J and the SAME exact pair-deletion frame U|V. The predecessor selected-incidence channel is still present because b is still internal. Its R434 birth produces, unless closure occurs immediately, a nontrivial endpoint-anchored signed dimer containing a.

But a is now already a completed historical singleton anchor. By R434(iii), proved through accepted R436, this new nontrivial support is immediate at-anchor contact/strict-growth geometry. Hence the second application cannot enter another quiet protected-return branch. It yields

  TWO-COVER or explicit R445 geometry.                    (FR.7)

Thus at most one aligned return occurs before an explicit geometric output.

### 4. Every R445 geometric output contains a proper tight trimer
Normalize the explicit branch proof-aware.

- A strict growth, fusion, strict +2 extension, or signed-BB reverse P4 of order at least three contains a consecutive tight trimer.
- A reverse-contact/reversal output is itself a tight trimer or contains the displayed reverse trimer cell.
- A vertex-simple tight cycle contains a consecutive tight trimer.
- A bounded witness/contact output in the R440 part of R445 is already a trimer/reversal cell.

The only apparent exception is the smallest at-anchor growth: an old completed singleton (a) is met by a new R434 endpoint-anchored support of order two. But that support is not a bare dimer. R434 retains it as a SIGNED dimer with a named sign witness. By definition of that signed-dimer certificate, the witness together with the oriented dimer is a literal tight three-vertex path. Hence this order-two growth also supplies an explicit proper tight trimer K.             (FR.8)

Because n>=7, every such trimer is proper.

### 5. Currentize the trimer
Apply accepted smallest-counterexample minimality R4 to the proper graph-intrinsic tight path K. Its complement H-K has an exact two-cover

  P|Q.                                                    (FR.9)

Restoring K gives the literal maximum spanning three-forest

  K|P|Q.                                                  (FR.10)

The trimer K, its R445/R434/R436 source certificate, the fixed turn J, and the floor-payment ancestry are all retained as historical data. No claim is made that U|V or the old aligned floor remain current in (FR.10).

### 6. Paid-floor reentry theorem
Therefore every ancestry-bearing both-singleton floor in order n>=7 admits a finite chosen certificate-retaining continuation to exactly one of

  a spanning two-cover,
  OR an actual maximum spanning three-forest containing a named proper tight trimer.   (FR.11)

The route uses only the fully reconstructible contracts R429, R432, R445/R434/R436, boundary antisymmetry, and R4. In the live large-order A7C3 regime the order hypothesis is automatic.

This removes the paid floor as a terminal noncurrent object in the phased Morse program SV41376. It does NOT yet prove that the reentered forest has a strictly smaller largest-rail deficit than the forest which originally generated the floor. Thus the remaining global obstruction is narrower:

  compare the reentered trimer forest (FR.10) with the pre-floor largest-rail checkpoint strongly enough to obtain strict phased-rank descent, or use the retained cross-epoch trimer/floor ancestry to force one of the bounded monodromy nuclei.   (FR.12)


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
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R445"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R436"
    }
]
```