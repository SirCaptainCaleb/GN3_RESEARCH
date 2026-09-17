# Criticality alone permits an exterior vertex with zero Hamilton six-replacements

**Workspace:** D17
**State:** established
**Key:** `critical-six-exterior-zero-replacement-fence`

**Summary:** There exists an explicit seven-vertex boundary tournament with U={0,1,2,3,4,5} non-Hamiltonian and deletion-Hamiltonian, but for the exterior vertex q=6 every one of the six replacement supports U-y+q is non-Hamiltonian. A compact 105-turn certificate is given by seven 15-bit local orientation strings, one for each middle vertex, using the R893 boundary-tournament reversal-pair convention. Explicit Hamilton P5 witnesses are retained for all six punctures U-y; exhaustive enumeration of all 720 orders on U and on each of the six replacement six-sets finds no Hamilton P6. Therefore no positive exterior replacement-density theorem follows from six-vertex criticality alone. In particular, the 2r+1 active-side threshold of the five-rail reciprocal-density theorem cannot be met by applying a per-exterior criticality-only lemma. Any successful density or absorption argument must spend additional geometry linking the exterior vertices, such as short-G1 structure, the fixed Hamilton rail, or anchored common-complement constraints.

### 1. The tempting generic replacement lemma is false
A natural attempt to consume `fixed-complement-six-five-reciprocal-density-threshold` is to hope that a non-Hamiltonian deletion-Hamiltonian six-set U automatically has several Hamilton replacements U-y+q for every exterior vertex q. This fails maximally.

There is a seven-vertex boundary tournament on

  V={0,1,2,3,4,5,6},
  U={0,1,2,3,4,5},  q=6,

such that U is non-Hamiltonian, every puncture U-{y} is Hamiltonian, but

  U-{y}+{q} is non-Hamiltonian for EVERY y in U.          (ZF.1)

Thus one exterior vertex can contribute zero active-side replacement cells even against a critical six-core.

### 2. Compact exact boundary-tournament certificate
Use the foundational R893 definition in uniformity three. For each middle vertex b, list the 15 unordered endpoint pairs {a,c} subset V-{b} in lexicographic order, writing a<c. A bit 1 means the ordered triple (a,b,c) is tight; a bit 0 means its complete reversal (c,b,a) is tight. Exact reversal then determines all 105 middle-rooted orientation pairs.

The seven bit strings are

  b=0: 010011011000111
  b=1: 110000000000110
  b=2: 101010000101001
  b=3: 000000000101001
  b=4: 111101111000100
  b=5: 000110011011111
  b=6: 000011111001011.                                  (ZF.2)

Because R893 defines a 3-uniform boundary tournament by choosing exactly one orientation from each such reversal pair, (ZF.2) is a complete boundary-tournament specification, not a relaxation.

### 3. Explicit puncture Hamilton paths
For the six punctures of U, the following literal orders are tight Hamilton P5s under (ZF.2):

  U-0: (3,5,4,2,1),
  U-1: (3,2,0,5,4),
  U-2: (4,1,5,0,3),
  U-3: (0,5,4,2,1),
  U-4: (2,5,0,1,3),
  U-5: (0,4,3,1,2).                                    (ZF.3)

Every consecutive triple in each displayed word evaluates tight from the bit certificate. Hence U is deletion-Hamiltonian.

### 4. Exhaustive non-Hamiltonicity check
A deterministic verifier enumerates all 6!=720 vertex orders of each relevant six-set and checks its four consecutive triples against (ZF.2). It finds zero tight Hamilton P6 orders on U itself and zero on each of

  U-0+6, U-1+6, U-2+6, U-3+6, U-4+6, U-5+6.             (ZF.4)

Thus (ZF.1) is independently checkable from the displayed 105-bit certificate by 7*720 finite path tests. The certificate was found by a binary MILP encoding exact reversal, non-Hamiltonicity of U and the six replacement supports, and existence of a Hamilton P5 on every U-y; the displayed assignment and exhaustive verifier are the retained evidence, so reproducing the optimization search is not required to check the conclusion.

### 5. Strategic fence
This rules out every parent theorem whose only hypotheses are that U is a six-vertex non-Hamiltonian deletion-Hamiltonian block and q is an exterior vertex, if the conclusion demands even one Hamilton replacement U-y+q for that q. In particular, one cannot obtain the thirteen active cells needed in the 6+5 reciprocal threshold by summing a positive criticality-only contribution from the five exterior vertices.

The short-G1 3-of-6 certificate in `singleton-deep-p5-order11-reciprocal-exchange-closure` therefore spends genuine extra geometry. Likewise any CBCA proof at complement order five must couple different q in the fixed Hamilton rail, use common-complement puncture structure, or exploit stronger anchored/endpoint constraints.

This finite fence does NOT produce a smallest counterexample and does not contradict CBCA or the two-cover conjecture. It isolates exactly which naive local density upgrade is unavailable.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R893"
    }
]
```
