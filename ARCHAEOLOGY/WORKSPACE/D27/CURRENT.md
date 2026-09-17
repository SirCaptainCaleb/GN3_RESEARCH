# D27 — Tested-order four-cell classification and common-anchor signatures

Complete tested-order-safe four-cell development: the rigid aligned special cell, the invalid strict-order/parity ancestors, exact R516/R517 signatures and quotients, the accepted R518 compiler, and R519/R520/R521 common-anchor consequences.

## Rigid double-contact cell and matching-height quotient

R275 starts from a four-set `{a,b,c,d}` with five specified tight turns from the historical double-contact packet. Assuming there is no Hamilton tight P4, test seven explicit Hamilton orders. In each test one consecutive turn is already tight, so no-P4 forces the other turn bad; boundary antisymmetry fixes its reverse. The seven forced choices determine all twelve reversal pairs. Hence the no-P4 branch is one unique labeled orientation, not an unspecified family.

R276 packages that orientation by the three opposite-edge perfect matchings
`B1={ab,cd}`, `B2={ac,bd}`, `B3={ad,bc}`.
At every middle vertex the incident matching blocks have the same strict order `B1>B2>B3`. Thus the rigid cell has a vertex-uniform transitive matching-block quotient. This remains a useful special aligned corner of the later four-signature theorem.



## Why the historical local-order and parity classifications failed

Historical R280 tried to allow arbitrary tested dimer orders while retaining a strict local-order table. The reverse contacts it forced are sound, but the displayed strict-order classification is false. R282 then computed a quotient from that false table and incorrectly called the doubly misaligned cell quotient-inhomogeneous. R298 repeated that wrong “correction.” R307 additionally tried to rescue the old strict-spoke count and still overclaimed a universal t=3 interaction. These are invalid routes.

R516 is the exact repair. Let `C=(a,b,c)` be tight and let a fourth vertex y sign the two terminal physical dimers with the same polarities as C, but with arbitrary tested orders. If no P4 exists, the reverse contacts `(b,a,y)` and `(y,c,b)` are forced. Define alignment bits
`A=[(a,b,y) tight]`, `B=[(y,b,c) tight]`.
For each of the four bit pairs, five of the twelve reversal-pair orientations are fixed. Exhaust the remaining seven binary choices against the exact no-P4 predicate on all 24 vertex orders. Exactly one assignment survives for each `(A,B)`. Thus there are exactly four no-P4 signatures, with the full twelve-turn tables recorded in R516/P531. No transitivity of the three comparisons at a fixed middle is assumed; in the `00` signature those local comparisons are cyclic.

R517 then reads the opposite-edge matching quotient directly from the correct R516 tables. Signatures `11,10,01` are vertex-uniform transitive, up to block permutation. Signature `00` is vertex-uniform **cyclic**. This is a noteworthy repair genealogy: abandoned R283 had in fact written the cyclic-00 formulation, an interim audit incorrectly replaced it by the inhomogeneous R298 picture, and final R517 restores the exact cyclic conclusion by direct turn-table computation. The historical abandoned status of R283 is preserved, but new use should cite R516/R517.

R520 is the tested-order-safe correction to common-anchor parity. The `00` four-cell with common middle gives t=3 where every spoke receives the expected two witness certificates but the two certificates on each spoke use opposite tested dimer orders. Therefore neither the old strict-spoke count nor even a universal t=3 R38 comparison follows. The exact replacement is R519 in D25: with t≥4, three or more certificates on a spoke force two to share one of the two tested orders by pigeonhole; only then may R38 be applied.



### Common-anchor parity failure and the tested-order correction

Historical R252 tried to count how many spokes at a common anchor have opposite-polarity witness pairs by multiplying parity relations around centered trimers. It is invalid because the same physical spoke may be tested in opposite dimer orders in different trimers. R308 tried to repair the theorem by choosing arbitrary witness pairs, but that still does not guarantee the same tested order. Descendants R253/R286 and the R309 route that relies on R308 therefore do not establish their promised strict-spoke threshold.

The correct tested-order theorem is R519. Let e be a common anchor and X an outer set of size t. Every spoke `{e,x}` receives one signed certificate from each other witness in `X-{x}`, and the tested orientation of every certificate is retained. When `t≥4`, each spoke has at least three certificates but only two possible tested orders; two certificates therefore share one tested order, so the same-support two-witness theorem applies. When `t=3`, no such universal interaction is forced. In particular, there is no tested-order-free lower bound on the number of strict opposite-polarity spokes.

This repair also invalidates the older parity descendants R262/R292 and the quotient-based R310 route. The safe surviving consequence is the exact tested-order fan R519, not any inherited “positive strict spoke fraction.”



## Universal P4-or-exact-signature four-cell compiler

The final stage C256 went through several false or abandoned formulations: R274 had an unresolved tested-order gap; R281 depended on a false parity repair; R284 mixed that with the invalid fresh-capture route; R297 still used the false quotient picture. R477 was explicitly rejected: its claim that mixed no-P4 contact signatures force P5 is false, because signatures sharing the core need not mix in the asserted way.

R518 is the accepted replacement. Start with a tight trimer `C=(a,b,c)` and fourth vertex y. Compare y's signed certificates on the two terminal physical dimers **with their tested orders retained**. If either comparison has opposite polarity on a common tested orientation, R263 gives a tight P4. Otherwise one is in the no-P4 same-polarity branch, which has exactly four tested-order signatures. Those signatures are later reconstructed explicitly as R516, and their matching-block quotients as R517. R518 is therefore the safe universal four-cell compiler: **P4 or one exact tested-order signature**, never an unaligned parity conclusion.

R521 is the corrected common-anchor normal form built on R519/R518. For a proper carrier and an exterior reservoir of size at least five, every carrier-exterior spoke has a same-tested-order two-witness interaction by the pigeonhole theorem. For every exterior triple, the corresponding four-cell is either a P4 or one of the exact no-P4 signatures. The quotient types are three transitive signatures and one cyclic signature after the later R516/R517 correction. No positive proportion of strict/P4 spokes is claimed.



## Exact status discipline and use boundary

R516 and R517 are the exact signature and quotient theorems. R518 is the universal four-cell compiler. R519 is the common-anchor tested-order pigeonhole theorem for at least four outer witnesses; R520 records the t=3 failure exposed by the 00 signature; R521 packages the corrected global spoke/four-cell normal form. R477 is rejected and remains a counterexample to the false mixed-signature P5 inference. The earlier parity and quotient revisions remain historical diagnostics only.