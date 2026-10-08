# Persistent face labels isolate the double-persistent zero-root locus — preserved pre-item development

## Composition

(none yet)

## Development

## Face-level persistent labels isolate the genuinely double-persistent obstruction

Fix one reflected positive span-two witness depth (r) in the protected complex (X_r). For a protected face (Fsubset X_r), let
[
P_L(F)=1
]
when the left depth-(r) occurrence is present in every chamber of (F), and let (P_R(F)) be defined symmetrically.

Define
[
sigma_r(F)=
egin{cases}
+1,&P_L(F)=1, P_R(F)=0,\
-1,&P_L(F)=0, P_R(F)=1,\
0,&P_L(F)=P_R(F).
end{cases}
]

**Lemma 1 (oddness).** Reversal sends (sigma_r(F)) to (-sigma_r(F)).

**Proof.** Chamber reversal exchanges the left and right reflected positive occurrences. Hence
[
P_L(	au F)=P_R(F),qquad P_R(	au F)=P_L(F),
]
which gives the claim. (square)

**Lemma 2 (chain compatibility).** If (Gsubseteq F), the pair (sigma_r(G),sigma_r(F)) can never be (+1,-1) or (-1,+1).

**Proof.** Persistence is monotone downward: if an occurrence is present in every chamber of (F), then it is present in every chamber of (G).

Suppose (sigma_r(G)=+1) and (sigma_r(F)=-1). Since (P_R(F)=1), downward persistence gives (P_R(G)=1), contradicting (sigma_r(G)=+1), which requires (P_R(G)=0). The other orientation is symmetric. (square)

Thus (sigma_r) has exactly the monotonicity needed for the usual barycentric separator construction: no chain contains both nonzero signs.

The zero faces have an exact structural description:
[
sigma_r(F)=0
]
if and only if either

1. **neither occurrence persists** on (F); or
2. **both occurrences persist** on (F).

Now suppose the two determining windows have full span at least thirteen. Equivalently their starts satisfy the separated-window hypothesis (b-age8).

In case (1), there is a chamber of (F) where the left occurrence is absent and a chamber where the right occurrence is absent. By [[separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape]], (F) contains an outward chamber.

Therefore every long-span zero face of this persistent-label separator satisfies the dichotomy
[
oxed{
	ext{same-face outward chamber}
quadeequad
	ext{both reflected occurrences persist in every chamber}.
}
]

Consequently the arbitrary tie-choice compatibility problem has disappeared. The only unbounded zero faces not already exposing a same-face escape are the **double-persistent faces**
[
P_L(F)=P_R(F)=1.
]

Every other zero face is either bounded to full determining span at most twelve or already contains an outward chamber.

### Strategic consequence

This is strictly earlier than the rooted packet problem. The packet machinery is needed only if the double-persistent locus itself must be repaired. Long faces in which one occurrence can disappear are handled by the separator before any two-cover of their determining span is sought.

Moreover every chamber of a double-persistent reflected span-two face is a symmetric exact-root chamber on its full determining span by [[unbounded_positive_doubles_are_exactly_symmetric_zero_root_obstructions]]. Thus the remaining unbounded Article VII obstruction is simultaneously:

- the double-persistent part of the positive-witness separator; and
- the identically zero-root part of the exact-root geometry.

The next elevated target should therefore be a theorem about the topology or face structure of the **double-persistent zero-root locus**, rather than a packet theorem for an arbitrary single reflected double.

This statement does not assign a sign to double-persistent faces and does not claim their outward locus is acyclic. [[separated_window_outward_loci_are_products_and_can_be_disconnected]] shows that such local acyclicity cannot be inferred from product splicing alone.
