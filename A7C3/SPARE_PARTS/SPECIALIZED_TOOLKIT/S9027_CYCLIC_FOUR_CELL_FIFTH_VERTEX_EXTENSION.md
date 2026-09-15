# S9027 — Every Fifth Vertex Hamilton-Extends the Cyclic No-P4 Four-Cell

## Theorem

Let X={a,b,c,z} be the four-cell whose tight-turn representatives are listed below; after labelling, the representatives are abc,bca,cab,zba,azb,baz,acz,cza,zac,zcb,bzc,cbz. Then every fifth vertex d outside X lies in a Hamilton tight P5 on X∪{d}, and d can be placed one step from an end: its position is 1 or 3 in a five-vertex order numbered 0,...,4.

## Proof

Write uvw when the displayed turn is tight. Every candidate below places d in position 1 or 3. Assume none is a tight P5. Each candidate has one X-only turn certified by the displayed cyclic four-cell, so its failure converts a tight antecedent mixed turn into the tight complete reversal of its other mixed turn by boundary antisymmetry.

Starting with dab:
dab ⇒ adz (zdabc) ⇒ czd (adzcb) ⇒ bdz (aczdb) ⇒ dba (cabdz) ⇒ bdc (cdbaz) ⇒ dbz (azbdc) ⇒ bda (adbzc) ⇒ cad (bdacz) ⇒ zda (bcadz) ⇒ bad (zdabc).

Starting with bad:
bad ⇒ cda (zbadc) ⇒ dcz (bzcda) ⇒ cdb (bdcza) ⇒ abd (cdbaz) ⇒ zdb (cabdz) ⇒ cbd (zdbca) ⇒ adb (zcbda) ⇒ daz (czadb) ⇒ adc (cdazb) ⇒ dab (zbadc).

The turns dab and bad are complete reversals, so exactly one is tight by boundary antisymmetry. Either choice forces the other, contradiction. Hence at least one of the sixteen candidate orders is a tight Hamilton P5, and inspection of the displayed candidate names shows d is always in position 1 or 3.

## Why this is reusable

The cyclic four-cell is universally Hamilton-extendable by any fifth vertex, with the new vertex near an endpoint. The theorem is a clean local eliminator for cyclic no-P4 residues.

## Scope and nonclaims

The theorem concerns only the explicitly displayed cyclic four-cell. It does not treat transitive no-P4 cells and does not prescribe which near-end position occurs.

## Provenance

Rescued from accepted archived result `R593`.
