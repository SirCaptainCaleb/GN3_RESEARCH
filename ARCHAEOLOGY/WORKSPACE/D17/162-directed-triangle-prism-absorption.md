# Two directed endpoint triangles linked by a Hamilton prism force a selected reversal or a spanning two-cover

**Workspace:** D17
**State:** working
**Key:** `directed-triangle-prism-absorption`

**Summary:** In the endpoint-prism residue with physical directed source and terminal triangles and three Hamilton pair-union rails joining them, each pair-union rail can be tested against the complementary solo petal by one source and one terminal seam. Failure at both ends gives a pair of exact reverse boundary trimers. Across the three rails these six failures force, by parity around the two directed triangles, one pair-union rail to carry opposite boundary orientations on the same physical endpoint pair; cyclic rotation then yields a fixed-support R561 witness. Thus the double-triangle prism is absorbable outside an explicit R548 wrap shield. Working proof requires exact endpoint-neighbor synchronization.

### Setup
Retain the endpoint prism with physical directed source triangle

  S=(s_L,s_B,s_Z)

and terminal triangle

  T=(t_L,t_B,t_Z),

one source and one terminal vertex on each petal. Retain Hamilton solo paths L,B,Z from s_* to t_* and Hamilton pair-union paths on L+B, L+Z, B+Z with endpoints prescribed by the prism assignment.

Assume the pair-union endpoint assignment is cyclic, e.g.

  P_{LB}: s_L -> t_B,
  P_{BZ}: s_B -> t_Z,
  P_{LZ}: s_Z -> t_L.

The other cyclic orientation is dual.

### One-rail complementary-petal test
Consider P_{LB} with complementary solo petal Z=(s_Z,...,t_Z). Let the first two vertices of P_{LB} be (s_L,x) and last two (y,t_B). Test source insertion of s_Z and terminal insertion of t_Z:

  alpha=(s_Z,s_L,x),
  beta=(y,t_B,t_Z).

If both are tight, then

  (s_Z,P_{LB},t_Z)

is Hamiltonian on Z-endpoints plus L+B. The remaining internal Z path after deleting endpoints is a contiguous tight path, and together the two paths span H, giving a spanning two-cover.

If alpha is bad, R3 gives

  (x,s_L,s_Z) tight.

If beta is bad, R3 gives

  (t_Z,t_B,y) tight.

Thus a nonclosing pair-union rail carries one or two exact reverse boundary trimers tied to its physical endpoint neighbors.

### Three-rail parity
Apply the same test cyclically to P_{BZ} and P_{LZ}. If any rail passes both seams, H closes. Suppose every rail fails at least one seam. Record S-failure/T-failure bits around the three rails.

If two adjacent rails fail on opposite ends, the directed-triangle orientation on S or T and the retained solo petal between them can be used to cross-splice their reverse trimers into a Hamilton P4/P5 joining the two pair-union supports; with the third petal complement this closes H. Therefore a surviving pattern must have all three failures on the same side or all three rails fail both sides.

In the all-source-failure pattern, the three reverse turns at S combine with the directed S-triangle to produce opposite boundary orientations for one pair-union source dimer. In the all-terminal-failure pattern the dual holds at T. If all three fail both sides, both conclusions hold.

Once one pair-union support has two Hamilton representatives with opposite orientations of one boundary dimer, accepted R548 cyclic rotations move the reversed state to opposite boundaries. Successful rotations strictly reduce boundary distance; a failed rotation gives an exact wrap shield. If transport reaches the opposite boundary, accepted R561 gives universal extension by the missing complementary endpoint and closes with the remaining petal path.

### Scope
This is a working prism-absorption proof outline, not yet a fully audited exact section. The critical parity-to-same-support-reversal step requires explicit case bookkeeping on the first/last neighbor vertices of the three pair-union paths; no path reversal may be assumed. Until audited, retain the double-directed-triangle prism as a finite bounded endpoint configuration with six named seam tests, not as closed mathematics.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
