# A minimal whole-shore obstruction is deletion-critical with exact blocker words

## Metadata

- ID: a_minimal_whole_shore_obstruction_is_deletion_critical_with_exact_blocker_words
- Parent Section: monochromatic_connector_blocks
- Position: 32
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

An inclusion-minimal whole-shore connector obstruction has shore size at least seven. Each one-vertex deletion has a spanning compatible connector, and its omitted vertex has exact interior and endpoint insertion blockers. This gives an omission-exchange family, but connectivity of its proper-support state graph alone does not force spanning insertion; augmentation, component union closure, or boundary exclusion is still needed.

## Development

Assume A is inclusion-minimal among shore sets for which no spanning compatible monochromatic connector on A union {x,z} exists. By the small-support theorem, |A|>=7.

For every a in A, the proper shore A minus {a} has a spanning compatible connector C_a. Since A itself is obstructed, a cannot be compatibly inserted into C_a. In path-normalized square-path gauge for C_a, its incidence word therefore:
1. avoids 0011 and 1100 at every interior position;
2. fails the compatible prepend endpoint equality;
3. fails the compatible append endpoint equality.

Thus a minimal obstruction supplies a canonical deletion-critical family: every vertex is the unique omitted vertex of some compatible connector and is blocked from that connector by the exact binary obstruction.

This is stronger than support maximality of one connector. For any distinct a,b, there exist connector states C_a containing b and C_b containing a. Hence the obstruction cannot be attributed to a permanently unreachable vertex; it is an exchange obstruction between deletion states.

The next closure target is therefore a reversible omission-exchange theorem: connect C_a to some connector omitting b through support-preserving square-path repairs while retaining endpoint compatibility. Any such exchange graph that is connected would force an insertion somewhere, since every label occurs as both omitted and included across the deletion-critical family.

Elevation audit: deletion-critical witnesses and exact insertion blockers are valid. Connectivity of an omission-exchange graph alone does not force an insertion or spanning state: a connected graph may consist entirely of proper-support states. A closure theorem needs an additional union-closure, augmentation, or boundary-exclusion property. Retain reversible omission exchange as a candidate interface, not a sufficient theorem.
