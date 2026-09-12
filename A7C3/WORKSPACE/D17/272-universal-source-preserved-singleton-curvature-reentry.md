# Arm U carries its source label through Morse normalization and payment, but anchor contact alone is not curvature cancellation

**Workspace:** D17
**State:** established
**Key:** `universal-source-preserved-singleton-curvature-reentry`

**Summary:** Fix an Arm-U source universe Omega with Hamilton complement B, good source label q, actual puncture path P_q, and bad deletion z. The q-labelled source curvature of SV45572 can be carried through a largest-rail normalization without losing q: in F_q=P_q|B|{q}, q can never be used as an A-growth donor because that would leave only two rails and close H. Thus q persists as the same singleton through every chosen A-growth continuation, and in the portal-free sector through the unique SV41625 terminal normal form. At every such state q reverse-signs both boundary dimers of the marked rail. At the terminal state singleton q and one reverse boundary dimer form an opposite-polarity singleton+dimer pair, so accepted R428 yields closure or a genuine paid both-singleton floor preserving q. This is a real cross-phase preservation theorem. However the further R436 contact with the old q-labelled curvature trimer does NOT by itself give Morse progress: when the historical signed support is a singleton, R436 strict-growth may simply recognize that already-existing trimer as a nontrivial extension. Hence the earlier productive-exit wording is retracted. The Arm-U stress test shows that a universal cancellation theorem cannot use only “paid signed singleton + curvature path through its anchor”; it needs an additional rank-aware currentization, pair-deletion/fixed-complement structure, or canonical return invariant. Working/unreviewed exposition only.


### 1. Fixed-universe input and the retained curvature label
Let H be a hypothetical smallest counterexample and retain the Arm-U fixed-universe packet of SV45572:

  V(H)=Omega disjoint_union B,

where B is a literal Hamilton path, Omega is non-Hamiltonian, q is a GOOD deletion label with an ACTUAL Hamilton puncture path

  P_q=(p_0,p_1,...,p_m)

on Omega-q, and z is a BAD deletion label with Omega-z non-Hamiltonian. Thus

  C_q=P_q | B

is an exact singleton-deletion source of H-q. SV45572 gives a graph-intrinsic proper tight trimer

  K=J(q,z;P_q)                                             (US.1)

containing q, obtained by reversing one of the at most three failed literal substitution windows around z. Preserve the exact failed window, the actual source word P_q, z, q, B, and the trimer order K.

The purpose here is not to currentize K immediately and forget its source. We first ask which part of its source ancestry survives the global forest normalization.

### 2. The source label q is a four-wall singleton
Restore the omitted source label as a singleton. Then

  F_q=P_q | B | {q}                                       (US.2)

is a literal maximum spanning three-forest.

More generally, let R be either source rail P_q or B. This rail cannot be a singleton: if R={u}, then the tight dimer (q,u) together with the untouched other source rail is a spanning two-cover of H. Hence |R|>=2. Write R=(r_0,...,r_s), so s>=1. The turn

  (q,r_0,r_1)

cannot be tight: otherwise (q,R) together with the untouched other source rail is a spanning two-cover of H. Hence R3 gives

  (r_1,r_0,q) tight.                                      (US.3)

Dually,

  (r_{s-1},r_s,q)

cannot be tight, since (R,q) together with the untouched source rail would two-cover H. Therefore

  (q,r_s,r_{s-1}) tight.                                  (US.4)

Thus the SAME physical singleton q tail-signs the reverse initial boundary dimer and head-signs the reverse terminal boundary dimer of BOTH literal source rails. This uses counterexamplehood plus the exact source representative, not deletion-Hamiltonicity of all of Omega.

### 3. q is inert under largest-rail A-growth
Choose one of P_q,B of maximum order and mark it as A in the SV40879 largest-rail rewrite. The third rail is the singleton {q}.

At any later literal A-growth descendant in which q is still singleton, an A-growth move using q as the donor would attach q to one end of the marked rail and remove the singleton component. The result would have only the grown marked rail and the untouched other rail, hence would be a spanning two-cover of H. Therefore no such q-move exists in a counterexample.

Consequently every chosen A-growth continuation has the form

  A_i | X_i | {q},                                       (US.5)

with the SAME physical singleton q at every stage. Only endpoints of X_i can move into A_i.

The integer deficit n-|A_i| decreases on every actual A-growth move by SV40879, so the chosen continuation terminates. If the reachable A-growth system is portal-free, SV41625 makes the terminal representative unique:

  N_q=A^* | X^* | {q}.                                   (US.6)

If an A-growth critical pair emits a trimer/cycle/augmentation portal instead, retain that portal together with the still-current singleton q; no descent across that portal is asserted here. The remainder concerns the portal-free terminal branch.

### 4. The terminal wall pays directly while preserving q
Write

  A^*=(a_0,a_1,...,a_r).

SV40879 gives |A^*|>=3. Independently of its other terminal witnesses, the singleton q itself cannot merge into either end of A^*. Hence the same literal argument as in Section 2 gives

  (a_1,a_0,q) tight,                                      (US.7)
  (q,a_r,a_{r-1}) tight.                                  (US.8)

Put

  D_R=(a_r,a_{r-1}).

Equation (US.8) head-signs D_R by witness q. In the signed-support convention used in the order-three branch of SV40879, the same tight turn also makes the singleton support (q) a tail-signed support with witness a_r via the vacuous tight dimer (q,a_r). Therefore

  (q)  and  D_R                                           (US.9)

are physically disjoint opposite-polarity signed supports, with support profile 1+2.

Apply accepted R428 to this balanced pair, designating singleton q as the preserved coordinate. There is a finite certificate-retaining continuation to

  TWO-COVER,

or an ancestry-bearing both-singleton balanced floor

  (q) | (s)                                               (US.10)

for some physical s, with q retained literally as the same signed singleton throughout the payment. Preserve the terminal forest N_q, D_R, the sign witness a_r, and the full R428 refund ledger.

This is the durable positive conclusion: Arm U can choose a genuine paid floor so that its original source label q survives both the forest phase and the payment phase as one physical ancestry coordinate.

### 5. The old curvature remains anchored, but R436 does not supply a rank decrease
The curvature trimer K from (US.1) is graph-intrinsic and has never ceased to be valid. By construction

  q in V(K),
  |V(K)|=3.                                               (US.11)

At the floor (US.10), q is an ancestry-bearing signed singleton. Accepted R436 applies formally to the signed singleton support and the proper tight path K. Since K contains q and is not the stationary singleton replay, R436 places the situation in its at-anchor nonquiet alternatives.

However the singleton specialization of the FULL R436 proof is an essential fence. When the old signed support P is literally the singleton (q), any nontrivial tight path Q containing q already counts as strict growth of P. Taking Q=K, the R436 growth output may therefore be exactly the pre-existing trimer K itself. No new selected representative, new support, new turn, or strict phased-Morse inequality follows merely from invoking R436 at this point.

Thus the correct conclusion is only

  the q-labelled curvature remains an ancestry-bearing contact
  at the q-preserving paid floor.                         (US.12)

It is NOT yet a consumed productive exit. This distinction is required by the project fence that generic R436 growth, especially from singleton support, need not constitute provenance or Morse progress.

### 6. Stress-test conclusion: what a true parent cancellation theorem must remember
Arm-M completed-anchor curvature SV42888 is generated downstream of a completed historical anchor inside a much richer fixed-cap geometry. Sections 1-4 show that Arm U can nevertheless reach a comparable CROSS-PHASE ANCHOR COORDINATE:

  ARM U source curvature
    -> q-preserving largest-rail normalization
    -> q-preserving genuine paid singleton floor.         (US.13)

But Section 5 separates coordinate preservation from curvature cancellation. A theorem with hypotheses only

  historical paid singleton q
  + proper curvature path K containing q

is too weak: R436 can discharge tautologically through the already-known growth K.

Therefore the G18 Arm-U stress test identifies a necessary extra datum for any common parent theorem. Curvature cancellation must additionally control at least one of:

1. a CURRENT pair-deletion or fixed-complement representative carrying the curvature;
2. a canonical A-growth return normal form which can be compared to the pre-curvature checkpoint;
3. a retained two-ended wall / puncture-family relation tying the curvature to another actual representative;
4. another genuinely well-founded cross-portal coordinate.

The next Arm-U target should therefore not be another contact theorem. It should lift the source curvature to a wall-bearing pair-deletion/fixed-complement cell, or prove a rank-aware currentization theorem for the q-labelled portal. This is exactly the information available on the Arm-M side of G18 and absent from the bare singleton-contact abstraction.

Status: complete internal working mathematics, unreviewed exposition. The q-preservation and genuine R428 payment conclusions are retained. The former wording that called the later R436 recognition a productive-exit cancellation interface is explicitly withdrawn.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R436"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```