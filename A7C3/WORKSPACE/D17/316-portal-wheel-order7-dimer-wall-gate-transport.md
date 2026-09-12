# The order-seven dimer wall has a SLIDE or transports through a bounded P6 reversal to R561 or a current wrap shield

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-order7-dimer-wall-gate-transport`

**Summary:** Continue SV66530 with its maximum forest F0=S|D|Q, D={e,f}, where both e,f Hamilton-extend S and both Q+e,Q+f are non-Hamiltonian. The four ordered merge seeds between the dimer D and the two ends of Q are dimer-incident gates. By the dimer-root local theorem, each is either a one-edge SLIDE or a DOUBLE with an explicit reverse P4. If any gate SLIDEs, F0 already has a literal support-changing neighboring maximum forest. If none does, all four are DOUBLE. Their four reverse P4s concatenate into two Hamilton P6s on the same boundary six-set X={q0,q1,e,f,q_{m-1},q_m}: A=(q1,q0,e,f,q_m,q_{m-1}) and B=(q1,q0,f,e,q_m,q_{m-1}). Choose one exact two-cover U|V of H-X by R4. Then A|U|V and B|U|V are maximum three-forests with identical spectator rails selecting ef oppositely. SV36339 transports this reversal with U,V frozen to R561 support escape/closure or a named reverse-wrap shield, and every shield is a proper trimer current in maximum-forest space. Thus the bilateral dimer/Q wall has no static all-DOUBLE residue: locally it exits by SLIDE, R561 support change/closure, or current wrap curvature.


### 1. The asymmetric dimer-root state
Retain SV66530. Thus there is a literal maximum spanning three-forest

  F_0 = S | D | Q,
  D={e,f},                                                 (DG.1)

where S is a Hamilton P5, D is a freely orientable dimer, and

  Q=(q_0,q_1,...,q_m),   m>=3                             (DG.2)

is a literal Hamilton path. The two dimer roots satisfy the asymmetric extension pattern

  S+e and S+f are Hamiltonian,
  Q+e and Q+f are non-Hamiltonian.                         (DG.3)

Consequently the direct endpoint attachments of both e and f to both ends of Q fail, and R3 gives the bilateral reverse wall recorded in SV66530:

  (q_1,q_0,e), (q_1,q_0,f),
  (e,q_m,q_{m-1}), (f,q_m,q_{m-1}) tight.                (DG.4)

We now consume the four physical merge gates between D and Q.

### 2. Every dimer-Q gate is SLIDE or DOUBLE
A dimer may be displayed in either orientation. Consider the four ordered dimer-incident merge seeds obtained by using the two orientations at the two ends of Q:

  e -> q_0,  f -> q_0,  q_m -> e,  q_m -> f,              (DG.5)

where the dimer orientation is chosen so the displayed seed is the relevant boundary state.

Apply the dimer-root local gate theorem SV22582 to the maximum forest F_0. For every seed in DG.5, complete success of both splice seams would merge D and Q and leave S untouched, producing a spanning two-cover of H, impossible. Hence each seed is blocked. The exact dimer-root dichotomy is:

- exactly one blocked seam: the seed has the unique one-edge SLIDE response, an actual neighboring maximum three-forest;
- both seams blocked: the seed is DOUBLE and R3 gives the explicit reverse P4 rebuild.              (DG.6)

Therefore if ANY one of the four gates is singly blocked, the order-seven residue already exits through a literal dimer-Q SLIDE. Retain that actual support-changing maximum forest and stop.

Assume from now on that no dimer-Q gate SLIDEs. Then ALL FOUR gates in DG.5 are DOUBLE.

### 3. Four DOUBLE gates assemble two opposite-dimer Hamilton P6s
Run the two source-side DOUBLE gates with the two dimer orientations. The explicit SV22582 reverse-P4 formulas give

  L_e=(q_1,q_0,e,f),
  L_f=(q_1,q_0,f,e)                                      (DG.7)

as tight P4s.

Run the two terminal-side DOUBLE gates. The dual formulas give

  R_e=(e,f,q_m,q_{m-1}),
  R_f=(f,e,q_m,q_{m-1})                                  (DG.8)

as tight P4s.

The matching middle dimers concatenate. Hence on the common physical six-set

  X={q_0,q_1,e,f,q_{m-1},q_m}                            (DG.9)

we have the two literal Hamilton tight paths

  A=(q_1,q_0,e,f,q_m,q_{m-1}),
  B=(q_1,q_0,f,e,q_m,q_{m-1}).                           (DG.10)

They have the same endpoints, the same four Q-boundary vertices, and select the physical dimer {e,f} in opposite directions. Thus complete failure of all four dimer-Q SLIDEs does not leave four unrelated reverse P4s; it collapses to ONE same-support selected-reversal cell on six vertices.

### 4. One common complement currentizes the P6 reversal with frozen spectators
The path A is proper because the disjoint five-set V(S) survives outside X. Apply accepted smallest-counterexample minimality R4 to the proper tight path A. Its complement H-X has an exact two-cover; retain one literal cover

  U | V  of H-X.                                         (DG.11)

Because B is a Hamilton path on the SAME support X, the same literal spectator cover gives two actual maximum spanning three-forests

  F_A=A|U|V,
  F_B=B|U|V.                                              (DG.12)

These forests have identical support partition and the identical literal spectator rails U,V, while the active Hamilton words A,B select e->f and f->e respectively.

Therefore the exact hypotheses of SV36339, `compatible-forest-selected-reversal-two-rail-transport`, hold. Apply its finite discrepancy transport. Every successful R548 rotation keeps U,V literally frozen and decreases the boundary distance of the named ef reversal. The process terminates in one of two ways:

1. R561: one active Hamilton order begins with e,f and the other ends with f,e. Then every exterior vertex Hamilton-extends X. SV36339 gives either a spanning two-cover or an actual support-changing maximum forest by absorbing an endpoint of U or V into X.

2. SHIELD: a required rotation fails and R3 produces the named reverse-wrap shield trimer. The shield is a proper graph-intrinsic tight path and R4 currentizes it as a rail of an actual maximum spanning three-forest.        (DG.13)

Thus the all-DOUBLE dimer-Q gate is itself finite transport, not a static bounded obstruction.

### 5. Local extinction statement
Combining Sections 2-4, the bilateral dimer/Q wall of SV66530 has the exact alternative

  DIMER-Q SLIDE,
  or R561 SUPPORT ESCAPE / TWO-COVER,
  or CURRENT REVERSE-WRAP TRIMER.                         (DG.14)

In particular there is no residual state in which all four dimer-Q gates merely remain DOUBLE. Four DOUBLE gates automatically manufacture the same-support P6 reversal that SV36339 consumes.

This strictly sharpens the order-seven quotient. The rigid two-ended necklace first becomes the asymmetric P5|dimer|Q forest of SV66530, and its special short-rail wall then exits into ordinary support-changing or explicit-current maximum-forest dynamics.

### 6. Scope fence
DG.14 is local dimer-wall extinction, not global maximum-three-forest holonomy extinction. A SLIDE may later participate in a closed representative circuit; an R561 support escape is a genuine support change but is not asserted to lower the global phased rank; and a wrap shield is current curvature rather than an immediate contradiction. No epsilon_* or Phi decrease is claimed.

The gain for G24 is that the order-seven bad-singleton shell no longer contributes an independent quiet short-rail species. Any surviving reconstruction-closed family must absorb one of the already-global maximum-forest currencies in DG.14, while the same order-seven parent still carries the bad-row common-center anchor star SV66139.


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