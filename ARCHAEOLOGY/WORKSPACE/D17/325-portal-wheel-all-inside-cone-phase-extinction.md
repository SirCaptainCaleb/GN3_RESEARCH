# The all-inside coherent cone is phase-one unstable by one singleton-row internal puncture

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-all-inside-cone-phase-extinction`

**Summary:** Retain the only residue of SV68752: the hub x and all five P5 roots K lie in the non-Hamiltonian block Omega, the fixed complement Q is Hamiltonian, and every spoke pair deletion has exact coherent cover (Omega-{x,d})|Q, so Omega-{x,d} is Hamiltonian for all d in K. Choose any exact singleton-deletion row C_x of H-x and restore x as singleton, obtaining a phase-1 maximum three-cover. The five K-roots all survive in C_x, but two path rails have at most four distinct physical endpoints, so some d in K is internal on its C_x rail. Puncturing d gives a literal three-cover of H-{x,d}; the coherent spoke fiber supplies an exact two-cover of that same residue. This is exactly the internal-puncture source-visible phase-lift of SV68110 (and also the source-labelled pair portal theorem SV68431): before payment it produces a proper trimer and then TWO-COVER or phased rank strictly below both source checkpoints. Hence the all-inside coherent cone cannot occur in a nonclosing phase-rank-minimal family. Combining with SV68752, every surviving coherent portal wheel is forced into a full fixed-complement deletion-Hamiltonian critical block. No singleton-goodness assumption is needed.


### 1. Retain the unique residue of the coherent-cone compression
Work in a hypothetical smallest counterexample H inside a nonclosing reconstruction-closed family chosen minimal for the legitimate phased rank. Retain the all-inside residue isolated by `portal-wheel-coherent-cone-critical-or-all-inside` SV68752:

  V(H)=Omega disjoint_union Q,                             (AI.1)

where Q is a literal Hamilton path, Omega is non-Hamiltonian, the common hub x lies in Omega, and all five vertices of the retained Hamilton P5 K lie in Omega. Thus

  {x} union V(K) subset Omega.                             (AI.2)

For every root d in K, the coherent spoke pair fiber H-{x,d} has exact support partition

  (Omega-{x,d}) | Q.                                      (AI.3)

Both rails in (AI.3) are Hamiltonian, so in particular

  Omega-{x,d} is Hamiltonian for every d in K.             (AI.4)

No singleton-puncture Hamiltonicity is assumed.

### 2. One arbitrary x-row cannot expose all five roots as endpoints
Choose any literal exact two-cover

  C_x=A|B                                                   (AI.5)

of H-x. Such a cover exists by smallest-counterexample minimality. Restore the omitted vertex x as a singleton:

  F_x={x}|A|B.                                              (AI.6)

Since pc(H)=3, F_x is a literal minimum spanning three-cover, hence a phase-1 checkpoint.

All five distinct roots d in K survive in C_x because x is disjoint from K. A path has at most two distinct physical endpoints; therefore the two rails A,B expose at most four distinct physical endpoints in total. Hence by pigeonhole there exists

  d in K                                                    (AI.7)

which is INTERNAL on its displayed C_x rail.

Write that rail as

  (...,u,d,v,...),                                         (AI.8)

with both inherited sides nonempty after deleting d. Puncturing d from C_x therefore gives a literal three-cover

  R=C_x-d                                                   (AI.9)

of the pair-deletion residue H-{x,d}.

### 3. The same pair residue already has a coherent exact two-cover
By (AI.3), H-{x,d} also has the literal exact two-cover

  T=P_{x,d}|Q,                                              (AI.10)

where P_{x,d} is a Hamilton path on Omega-{x,d}.

Thus the pair residue H-{x,d} carries simultaneously:

  the three-cover R obtained by an INTERNAL puncture of the actual singleton row C_x,
  and the coherent exact two-cover T from the spoke fiber.  (AI.11)

Component counting forces T to select a physical state crossing two components of R. This is exactly the source-visible one-step 3-to-2 packet of Section 3 of `common-residue-prepayment-phase-lift` SV68110 with

  D_0={x},   z=d.                                          (AI.12)

Equivalently, it is a source-labelled current pair portal eligible for SV68431.

### 4. Phase descent before payment
SV68110 constructs the two phase-1 source forests

  F_x={x}|C_x,
  G_{x,d}=(x,d)|T,                                         (AI.13)

and from the selected T-crossing plus one inherited C_x edge exposes a proper tight trimer BEFORE any R159/R176 payment. Applying the phase-1 absorber gives either

  TWO-COVER,                                               (AI.14)

or a checkpoint of phased rank strictly below BOTH forests in (AI.13), in particular strictly below the actual singleton source F_x.

This contradicts nonclosing phase-rank minimality. Therefore the all-inside residue (AI.2) cannot occur.

The endpoint count is the whole extra ingredient: five coherent spoke fibers are one more than the four endpoint slots of an arbitrary exact singleton row, so one spoke is forced to become an INTERNAL source-labelled pair portal, which G25's phase-lifting machinery immediately spends.

### 5. Wheel consequence
Combine this extinction with SV68752. A phase-minimal coherent full-root portal wheel has only two possibilities there:

1. the non-Hamiltonian global block Omega is already deletion-Hamiltonian at every vertex, with fixed Hamilton complement Q;
2. all six wheel vertices lie in Omega.

Section 4 eliminates possibility 2. Hence every surviving support-coherent portal wheel is already a FULL FIXED-COMPLEMENT CRITICAL BLOCK:

  Omega non-Hamiltonian,
  Omega-y Hamiltonian for every y in Omega,
  Q Hamiltonian.                                          (AI.15)

Together with SV68111, this means the entire portal-wheel architecture has been reduced, at a nonclosing phased-rank minimum, to the existing fixed-complement critical-block architecture. There is no remaining wheel-specific coherent or incoherent kernel.

### 6. Scope fence
The theorem uses five distinct spoke roots. The endpoint pigeonhole would not follow from only four. It also uses the exact coherent pair-deletion covers (AI.3), not merely abstract Hamiltonicity of the pair punctures.

The result does not itself extinguish a full fixed-complement deletion-Hamiltonian critical block. It removes the last wheel-specific residue and hands the problem to the already-developed critical-block consumer. No R24 or R5 is used.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```