# In Arm M every flat completed-anchor dimer exit is strict height gain or a terminal cap-support transition

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-flat-anchor-exit-cap-transition`

**Summary:** Work in R927 Arm M with n=2k+1, k>=5. Run the largest-rail/fixed-turn phased Morse continuation of SV40879/SV41376 and let A* be its terminal marked rail of order L. Suppose a rank-zero R434/R436 productive exit is the genuinely flat case isolated by R1: a new tight dimer D through a completed fixed-turn outer anchor e in A*, with no larger geometric output yet. Accepted R4 gives an exact two-cover U|V of H-D. Arm M forbids every tight path of order k+1 or more, while |U|+|V|=2k-1, so {|U|,|V|}={k,k-1}. Hence D|U|V is a literal maximum three-forest with a unique k-rail U. If L<k, currentizing the flat exit strictly improves the global largest-rail record from L to k and therefore restarts the Morse descent below the old forest height. If L=k, U is another cap-size Hamilton support. Because e lies in D and in A*, U omits e, so U!=A*: the flat exit is a genuine cap-support change. No inward slide into U can exist, since it would create a tight (k+1)-path, so the new forest is already terminal for the largest-rail rewrite. Comparing the old and new terminal forests by SV40898, this cap transition either exposes one of the bounded C4/C6 or repeated-crossing nuclei, an R435/trimer portal, or factors through at most two support-changing one-edge exchanges. Thus the flat R436 exit is not an unstructured rank-zero replay: below cap it is strict global height improvement, and at cap it is a terminal support transition living entirely in the already bounded/factorized recompletion quotient.


### 1. Input: the only genuinely flat productive exit
Work in the uniform branch (M) of accepted R927:

  |V(H)|=2k+1,  k>=5,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                            (FE.1)

Run the working largest-rail descent SV40879 and the phased fixed-turn continuation SV41376. Let

  F*=A*|B*|C*                                             (FE.2)

be the terminal marked forest reached before pair payment, and write

  L=|A*|.                                                 (FE.3)

The Arm-M support cap implies L<=k: if a tight path had at least k+1 vertices, any contiguous k+1 subpath would Hamiltonize its support, contradicting (FE.1).

Now enter the fixed-turn paid lineage of SV41376. The flat productive exit isolated in the R1 analysis is the following special R434/R436 event at a completed outer anchor e of the retained turn: a genuinely later nontrivial signed support through e is only a DIMER

  D=(x,e)  or  D=(e,x),                                  (FE.4)

rather than a longer growth path, proper cycle, or reverse-contact/reversal trimer. Here e is a physical vertex of A*, because the retained fixed turn was chosen on A*.

We consume exactly this flat dimer exit.

### 2. R4 currentization forces a k | (k-1) complement
The dimer D is a proper graph-intrinsic tight path. Apply accepted R4 proof-aware to D. Its complement

  W=H-V(D)                                                (FE.5)

has path-cover number at most two. It cannot be Hamiltonian: a Hamilton path of W together with the retained dimer D would be a spanning two-cover of H. Hence W has an exact two-cover

  W=U|V.                                                  (FE.6)

Restoring D gives the literal maximum spanning three-forest

  F_D=D|U|V.                                              (FE.7)

By the Arm-M cap, every tight path has order at most k. Therefore

  |U|<=k,  |V|<=k.                                       (FE.8)

But

  |U|+|V|=|W|=2k-1.                                      (FE.9)

Consequently, after relabelling,

  |U|=k,  |V|=k-1.                                       (FE.10)

Thus EVERY flat completed-anchor dimer exit in Arm M canonically currentizes to a maximum forest of size profile

  k | (k-1) | 2.                                         (FE.11)

No choice of exact complement cover can avoid the presence of a k-rail.

### 3. Below the cap, the flat exit is strict global Morse improvement
Suppose first that the old terminal marked rail satisfies

  L<k.                                                    (FE.12)

Mark the k-rail U in F_D. Then its largest-rail deficit is

  d(F_D,U)=2k+1-k=k+1,                                   (FE.13)

whereas the old terminal record was

  d(F*,A*)=2k+1-L > k+1.                                 (FE.14)

Hence the currentization (FE.7) strictly improves the global largest-rail record. In any global rank which retains the best achieved largest-rail deficit as its primary coordinate, this productive exit re-enters strictly below the old forest height before any secondary pair-lineage coordinate is consulted.

Therefore a flat dimer exit can fail to give strict height improvement only after the largest-rail Morse process has already reached the Arm-M cap L=k.

### 4. At the cap, the flat exit is a genuine support change
Assume now

  L=k.                                                    (FE.15)

The new k-rail U cannot have the same physical support as A*. Indeed the completed fixed-turn anchor e lies in A*, while e lies in the dimer D and hence is absent from U. Thus

  V(U) != V(A*).                                         (FE.16)

So a non-improving flat exit is not stationary replay of the same cap support. It is a genuine transition from one Hamilton k-support to a different Hamilton k-support.

Moreover F_D is already terminal for the largest-rail A-growth rewrite when U is marked. Any inward SLIDE into U would produce a literal tight path of order k+1, forbidden by (FE.1). Hence

  cap flat exit = terminal cap state -> terminal cap state.       (FE.17)

The only remaining motion is support transport at fixed maximal rail size.

### 5. The cap transition lies in the bounded/factorized recompletion quotient
Compare the two literal maximum forests F* and F_D. Their support partitions differ by (FE.16); in fact they cannot be equal as unordered partitions because the new dimer D contains e in A* and k>=5.

Apply the working universal recompletion factorization SV40898. Exactly one of its parent outputs occurs:

- a physical C4 or C6 support-incidence nucleus;
- a repeated-crossing nucleus on at most four seam vertices;
- same-cell R435 reversal/trimer/cycle geometry;
- a current mixed-seam trimer;
- or a factorization of F* -> F_D through at most two reversible support-changing one-edge transfers.  (FE.18)

The last branch lies in the portal-relative triangle-square simply connected one-edge sector of SV39912; the first four are already bounded or named portals. Hence the flat dimer exit introduces no new unbounded recompletion species at rank zero.

### 6. Productive-exit reentry consequence
For Arm M, the flat R434/R436 anchor-contact exit has therefore been reduced to the exact dichotomy

  STRICT LARGEST-RAIL RECORD IMPROVEMENT,
  OR
  TERMINAL CAP-SUPPORT TRANSPORT THROUGH THE BOUNDED RECOMPLETION QUOTIENT.   (FE.19)

In particular, after the first nonclosing flat exit the global Morse obstruction may be assumed to live at the hard cap |A|=k. Repeating the phased descent cannot wander at sub-cap height through dimer remints: every such remint jumps immediately to a k-rail.

Thus PRODUCTIVE-EXIT REENTRY in large-k Arm M is now concentrated further. Proper-cycle and reversal/trimer exits remain named portals; the previously flat completed-anchor dimer exit is either strict primary descent or a cap-to-cap support transition. The remaining global problem is to extinguish recurrence among those cap supports, using the bounded nuclei / one-edge relations of SV40898-SV39912 together with the retained paid ancestry carried by the exit.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
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