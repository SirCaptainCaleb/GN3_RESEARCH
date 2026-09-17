# S9032 — Tested-Dimer Two-Witness Interaction

## Theorem

Let D=(a,b) be a fixed tested oriented physical dimer in a Strong Level-(1) boundary tournament, and let x,y be distinct witnesses outside {a,b}. A head certificate on D with witness w means the exact ordered turn (w,a,b) is tight; a tail certificate on D with witness w means the exact ordered turn (a,b,w) is tight. Then two witness-indexed certificates on this same tested orientation have the following exhaustive interaction. (HH) If (x,a,b) and (y,a,b) are tight, they are exactly the same-support two-head extension collision packet on D with distinct witnesses x,y. (TT) If (a,b,x) and (a,b,y) are tight, they are exactly the same-support two-tail extension collision packet on D. (HT) If (x,a,b) and (a,b,y) are tight, then (x,a,b,y) is a literal vertex-simple tight P4. (TH) If (y,a,b) and (a,b,x) are tight, then (y,a,b,x) is a literal vertex-simple tight P4. Thus opposite-polarity certificates on one tested oriented dimer have an explicit strict two-ended realization, while same-polarity certificates are the literal two-extension collision packet. Tested order is part of the datum: a certificate tested on (a,b) and one tested on the reverse dimer (b,a) are not licensed as a same-oriented-support interaction merely because they share the unordered physical support {a,b}. To compare reverse-tested certificates, first treat (b,a) as its own tested oriented dimer and apply this theorem there. No cyclic permutation or witness-order rearrangement of a certified turn is licensed.

## Proof

Fix D=(a,b). By definition, a head certificate witnessed by w is the tight turn (w,a,b), while a tail certificate witnessed by w is the tight turn (a,b,w), with this exact tested order retained. If x and y have the same polarity, the two displayed tight extensions with distinct witnesses are precisely the same-support two-extension collision packet; no further inference is needed. If x is head and y tail, then the consecutive turns (x,a,b) and (a,b,y) are tight, so the vertex sequence (x,a,b,y) is a tight P4. If y is head and x tail, the same argument gives (y,a,b,x). These exhaust the two polarities for two certificates on the fixed tested orientation. A certificate on (b,a) is different ordered data; nothing in the preceding concatenations allows replacing (a,b) by (b,a) or cyclically permuting a certified turn. Hence opposite tested orders must be kept separate unless an independent theorem relates them.

## Why this is reusable

This is the exact bookkeeping-safe local rule for two witness certificates on one tested oriented dimer. Opposite polarities concatenate to a literal P4; equal polarities remain a genuine same-support collision packet. The tested orientation is part of the data.

## Scope and nonclaims

No relation is implied between certificates tested on opposite orientations of the same unordered dimer unless another theorem supplies it.

## Provenance

Rescued from accepted archived result `R523`.
