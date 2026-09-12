# Any q2-produced H-t row transports its d-y dimer to source or a named wrap shield

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-single-row-source-transport`

**Summary:** Every exact H-t row produced by q2 currentization contains d->y or y->d, and the omitted terminal t has the matching tight prepend turn in either case: (t,d,y) and (t,y,d). If the selected d/y state is not already at the source, the unique directed R548 tail rotation preserving it has one wrap seam; success keeps the exact H-t cover and decreases its source distance by exactly one, while failure gives a named reverse-wrap shield. Finite transport therefore either moves the d/y state to the source and closes H by prepending t, or stops at a current wrap shield. Thus even a single H-t reconstruction, not only a common-complement reversal pair, is genuine well-founded progress.


Retain the verified q2 insertion / amplification front through current `singleton-deep-q2-blocker-amplification` and the parent second-block 10 turns

  (t,d,y), (t,y,d) tight.                                 (ST.1)

Suppose q2 currentization yields ANY literal exact cover of the singleton-deletion fiber

  R | B  of H-t,                                           (ST.2)

where B is Hamiltonian and the active Hamilton path R selects the physical dimer {d,y} in either orientation. Thus for one ordered pair (e_0,e_1) equal to (d,y) or (y,d), R contains the selected state

  e_0 -> e_1,                                              (ST.3)

and (ST.1) gives the matching restoration turn

  (t,e_0,e_1) tight.                                       (ST.4)

This covers the one-gamma-success output as well as either member of a common-complement pair.

### 1. Source-distance transport
Write

  R=(r_0,...,r_m)

and suppose (r_a,r_{a+1})=(e_0,e_1). Define the source distance

  lambda(R;e_0,e_1)=a.                                    (ST.5)

If a=0, prepend the omitted vertex t. By (ST.4),

  (t,r_0,r_1,...,r_m)                                     (ST.6)

is Hamiltonian on V(R) union {t}. Together with the unchanged Hamilton complement B it is a spanning two-cover of H.

Assume a>0. Tail-rotate R:

  R'=(r_1,...,r_m,r_0).                                   (ST.7)

Accepted R548/P624 says the complete new-turn set is the singleton

  omega=(r_{m-1},r_m,r_0).                                (ST.8)

If omega is tight, R' is Hamiltonian on the same support. Since a>0, the selected state e_0->e_1 is not the cut state r_0r_1; it remains selected and its source distance decreases exactly by one:

  lambda(R';e_0,e_1)=lambda(R;e_0,e_1)-1.                (ST.9)

The cover R'|B is again exact on H-t. If omega is bad, R3 gives the exact reverse-wrap shield

  (r_0,r_m,r_{m-1}) tight,                                (ST.10)

attached to the current H-t representative while the selected d/y orientation remains current.

### 2. Finite singleton-row endgame
Iterate only successful tail rotations while lambda>0. Every successful move preserves the physical selected dimer, support, omitted label t, and literal complement B, while strictly decreasing the nonnegative integer lambda. Hence the process terminates.

If lambda reaches zero, (ST.6) closes H immediately. Otherwise a required wrap seam fails first and the exact shield (ST.10) is retained. Therefore every q2-produced exact H-t representative containing either orientation of {d,y} has the exact alternative

  spanning two-cover of H,
  OR a named R548 reverse-wrap shield at positive source distance. (ST.11)

This is stronger than requiring a paired common-complement reversal: a single exact H-t reconstruction is already subject to a genuine well-founded restoration transport because the omitted terminal t prepends to both d-y orientations.

### 3. Relation to the paired transport
If two common-complement H-t representatives selecting {d,y} oppositely are available, this source transport may be run on either row independently. The two-coordinate fixed-complement discrepancy transport remains valid and retains R561 as a symmetric endpoint consumer, but it is not required merely to consume a one-row q2 reconstruction.

No isolated successful cyclic rotation is called progress: the strict coordinate is lambda. No generic packet payment is used. This is established working exposition, not a certified exact unit.


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
    }
]
```
