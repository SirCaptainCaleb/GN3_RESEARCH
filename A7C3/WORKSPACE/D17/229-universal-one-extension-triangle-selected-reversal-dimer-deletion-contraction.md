# A pair-core triangle selected reversal is fixed-complement transport unless its outside block is non-Hamiltonian, which forces universal high transition

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-triangle-selected-reversal-dimer-deletion-contraction`

**Summary:** Retain the pair-core triangle selected-reversal residue: Hamilton P5s P_c on U-t and P_t on U-c select one common dimer D={u,v} oppositely. Put C=U-{c,t,u,v} and E=V(H)-U. The decisive split is graph-intrinsic. If E is Hamiltonian, then P_c|E and P_t|E are exact singleton-deletion rows H-t and H-c with one literal common complement. SV27136 currentizes the neighboring reversal: an internal exchanged label gives a fresh pair-deletion maximum forest, while the endpoint-endpoint branch yields two exact H-{c,t} covers with identical support partition and complement E selecting D oppositely; SV7559 then transports D monotonically to R561 or named reverse-wrap shields. If E is non-Hamiltonian, every exact two-cover F of H-D has at least three selected transitions in the fixed four-class partition C,{c},{t},E: the two F rails satisfy b_C+b_c+b_t+b_E=2+tau, while b_C>=1, b_c=b_t=1, and b_E>=2. Thus the last selected-reversal residue is exactly fixed-complement transport or a universal high-transition common-dimer deletion portal.

### 1. Selected-reversal input from the pair-core triangle
Retain the SELECTED-REVERSAL output of `universal-one-extension-pair-core-triangle-fourth-puncture-currentization` SV32145 inside a hypothetical smallest Strong Level-(1) counterexample H.

Thus U is the non-Hamiltonian six-set from the quiet pair-core triangle, t is one core label whose puncture U-t has a retained Hamilton path, and c is the exchanged exterior label from one perimeter puncture. Retain Hamilton paths

  P_c on U-t,
  P_t on U-c,

whose R435 comparison selects one common physical dimer

  D={u,v}

in opposite directions. The names P_c and P_t indicate which exchanged label is present, not a path orientation convention.

The common physical vertex set of the two paths is U-{c,t}. Remove D from that four-set and write

  C=U-{c,t,u,v},

so |C|=2. Put

  E=V(H)-U.

The universal-one-extension setup gives |V(H)|>=11, hence E is nonempty.

### 2. The graph-intrinsic split is Hamiltonicity of E
There are two cases.

#### Case H: E is Hamiltonian
Choose a Hamilton tight path B on E. Since P_c spans U-t and P_t spans U-c, the literal covers

  P_c | B                                                   (SR.1)
  P_t | B                                                   (SR.2)

span H-t and H-c respectively.

Both are exact. If H-t were Hamiltonian, a Hamilton path of H-t together with singleton {t} would two-cover H, contradicting pc(H)=3; the same applies to H-c.

Hence (SR.1)-(SR.2) are exact singleton-deletion rows with the SAME literal Hamilton complement B, while their active Hamilton paths retain the original selected reversal of D. The pair-core selected reversal has therefore entered fixed-complement neighboring-puncture geometry without any representative synchronization assumption.

Apply `fixed-complement-r435-adjacent-reversal-pair-deletion-currentization` SV27136.

If c is internal in P_c or t is internal in P_t, deleting the exchanged pair {c,t} splits the corresponding active path. The exact pair-deletion representative supplied in SV27136 crosses the split components, and the reversal currentizes to a fresh maximum-three-forest portal. If both exchanged labels are internal, one common pair-deletion representative crosses both decompositions.

If instead c is an endpoint of P_c and t is an endpoint of P_t, trimming those endpoints gives two Hamilton P4s on the common support

  X=U-{c,t}=D union C.

Pairing each with B gives two exact two-covers of the SAME residue H-{c,t}, with identical support partition X|E and the same literal complement B. The physical dimer D is selected in opposite directions on the two X-orders.

Now apply `fixed-complement-selected-reversal-normal-form` SV7559. Repeated successful R548 rotations preserve X,B and the named reversal D while strictly decreasing its boundary-distance coordinate. The process terminates either at an R561 boundary-reversal witness on X or at one/two named reverse-wrap shields blocking the still-positive boundary distances. No anonymous order discrepancy is exported.

Thus Hamiltonicity of E routes the selected-reversal residue completely into existing fixed-complement representative dynamics.

### 3. Non-Hamilton E forces high transition in every common-dimer deletion cover
Assume now that E is non-Hamiltonian.

A two-vertex dimer is a proper tight path. By accepted R4, H-D has exact path-cover number two. Let

  F=F_1|F_2

be an arbitrary literal exact two-cover of H-D.

Partition its vertex set into the four nonempty physical classes

  Pi={ C, {c}, {t}, E }.                                  (SR.3)

Let tau_Pi(F) be the number of selected F-states whose endpoints lie in different Pi-classes. If b_X(F) denotes the number of maximal contiguous blocks of class X in the two F-rails, the elementary block identity gives

  b_C+b_c+b_t+b_E = 2 + tau_Pi(F).                        (SR.4)

The two singleton classes each contribute exactly one block:

  b_c=b_t=1.                                               (SR.5)

The pair C is nonempty, so

  b_C>=1.                                                  (SR.6)

Since E is non-Hamiltonian, its vertices cannot form one contiguous spanning F-block. Therefore

  b_E>=2.                                                  (SR.7)

Substituting (SR.5)-(SR.7) into (SR.4) yields

  2+tau_Pi(F)>=1+1+1+2=5,

hence

  tau_Pi(F)>=3.                                            (SR.8)

Because F was arbitrary, (SR.8) holds for EVERY exact two-cover of H-D.

### 4. Exact contraction statement
The remaining selected-reversal output of the pair-core triangle therefore has the exact dichotomy

  E Hamiltonian
    => fixed-complement neighboring-puncture reversal
       => fresh pair-deletion maximum forest, or
          fixed-support reversal transport to R561 / named wrap shields;

  E non-Hamiltonian
    => every exact H-D two-cover has at least three selected transitions
       across C | {c} | {t} | E.                          (SR.9)

In the second branch, D|F is an actual maximum spanning three-forest for every exact F, so the residue is a current UNIVERSAL HIGH-TRANSITION common-dimer deletion portal. It is no longer two unrelated R4 representatives and no longer an uncurrentized local R435 certificate.

No claim is made here that the high-transition branch (SR.9) already yields a spanning two-cover.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
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
