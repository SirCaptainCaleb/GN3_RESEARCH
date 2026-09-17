# S9024 — Two-Cut Singleton Cross-Swap Augmentation

## Theorem

Let an edge-ordered complete graph have a spanning three-path cover A sqcup B sqcup {z}, with A and B nontrivial increasing paths. Orient A,B increasingly. Choose selected edges q->w of A and p->v of B. Let L(x) denote the incoming selected-edge label, with L(source)=-infinity, and U(x) the outgoing selected-edge label, with U(terminal)=+infinity. If L(q)<lambda(qz)<lambda(zv)<U(v) and L(p)<lambda(pw)<U(w), then deleting q->w and p->v and adding q->z, z->v, and p->w yields a spanning cover by two vertex-disjoint increasing paths. Explicitly the new paths are A_prefix_through_q followed by z followed by B_suffix_from_v, and B_prefix_through_p followed by A_suffix_from_w.

## Proof

Write A=A^- q,w A^+ where A^- ends immediately before q if nonempty and A^+ begins immediately after w if nonempty; equivalently let A_q be the prefix of A ending at q and A_w the suffix beginning at w. Likewise write B_p for the prefix of B ending at p and B_v for the suffix beginning at v. Delete the selected edges q->w and p->v. This splits A into A_q and A_w and B into B_p and B_v. Now form P1=A_q,z,B_v and P2=B_p,A_w. These two sequences are vertex-disjoint and together use every vertex exactly once. Every consecutive edge internal to A_q,A_w,B_p,B_v is inherited from the original increasing rails. At the new junctions of P1, the edge entering q (when present) has label L(q), followed by qz and then zv, followed by the old outgoing edge from v (when present) of label U(v). The hypothesis L(q)<lambda(qz)<lambda(zv)<U(v), interpreted with -infinity/+infinity endpoint conventions, therefore makes every new turn at q,z,v increasing. At the unique new junction of P2, the edge entering p (when present) has label L(p), then pw, then the old outgoing edge from w (when present) has label U(w); the hypothesis L(p)<lambda(pw)<U(w) makes these turns increasing. Hence P1 and P2 are increasing paths. Since two old edges were removed and three cross edges added, the component count drops from three to two, but the explicit path construction already proves the claimed spanning two-cover.

## Why this is reusable

A concrete two-cut surgery that absorbs a singleton and converts a spanning three-cover into a two-cover under explicit local inequalities. It is a useful augmentation move beyond the one-cut splice of `S9015`.

## Scope and nonclaims

The theorem is sufficient, not existential: it does not assert that suitable cuts always exist and does not license arbitrary longer alternating-path augmentations.

## Provenance

Rescued from accepted archived result `R958`.
