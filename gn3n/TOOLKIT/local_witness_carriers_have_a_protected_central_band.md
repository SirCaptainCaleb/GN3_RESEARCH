# Local-witness carriers have a protected central band

**Summary:** Order the fixed witness path from its centered pendant edge outward. In any balanced carrier face, the innermost occurring label determines a common central band in which every chamber avoids all three forbidden two-cover patterns; both reflected orientations of the first possible bad witness occur at the band boundary.

## Statement

In the local-witness path topology, order the edges of T_m from the centered pendant edge outward and choose the first represented edge in each bad word. If F is a zero carrier face and e is the earliest path edge occurring among its chamber labels, then no chamber of F contains a forbidden-pattern witness on any earlier edge, while F contains labels in both orientations of e. Hence all chamber status words have a common central interval free of 001, 011, and 0101, so that interval has two-cover form 1*0* or 1*010*.

## Body

Use the path T_m from [[local_bad_patterns_label_a_fixed_path]] and order its edges starting at the pendant edge for the centered witness and then moving outward along the path. Choose the first represented edge under this order when labeling a bad word. Let F be a zero carrier face supplied by [[local_witness_path_topology]], and let e be the earliest tree edge occurring among the chamber labels of F. By definition of the selected label, every chamber of F contains no forbidden-pattern occurrence represented by an edge earlier than e. Tree-edge balance gives chambers labeled by both orientations of e. The edges earlier than e represent exactly the reflected pairs of forbidden-pattern locations closer to the center of the status word. Therefore all chambers have a common central band containing no occurrence of 001, 011, or 0101, and the first possible bad witness is realized on both reflected sides by chambers of F. By [[two_cover_words_avoid_three_local_patterns]], any binary word segment avoiding these three patterns has the restricted local form 1*0* or 1*010* on that band.

## Metadata

- ID: local_witness_carriers_have_a_protected_central_band
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
