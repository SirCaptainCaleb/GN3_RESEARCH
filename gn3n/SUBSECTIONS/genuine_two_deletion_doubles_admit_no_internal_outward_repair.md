# Genuine two-deletion doubles admit no internal outward repair

## Metadata

- ID: genuine_two_deletion_doubles_admit_no_internal_outward_repair
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 63
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Genuine two-deletion doubles cannot be repaired inside their determining span

Let J=[a,b+4] be the full determining span of a protected positive span-two reflected double, and suppose
[
kappa_2(H[J])=2.
]
Then, by definition,
[
operatorname{pc}(H[J])>2.
]

Consider any spanning reorder (omega) of the vertices of J, leaving all vertices outside J fixed. Suppose (omega) were an outward repair at the selected reflected edge.

Every positive witness occurrence wholly inside J has a start between the two outer boundaries of the current reflected determining span. Such a start represents either the current unsigned witness edge or an edge strictly closer to the center; it is never farther outward than the selected edge. Therefore outwardness forces the internal status word of (omega) on J to avoid
[
001,qquad011,qquad0101
]
entirely.

By the exact forbidden-word theorem, an order on H[J] avoids these three words if and only if it yields a two-cover of H[J]. Hence outwardness of a repair confined to J implies
[
operatorname{pc}(H[J])le2,
]
contradicting (kappa_2(H[J])=2).

Thus:

**No-internal-repair lemma.**
In the genuine two-deletion reflected-double branch, no surgery supported entirely on the full determining span J can move the selected positive witness strictly outward.

This changes the research target. Packet, attachment, and small-support lemmas confined to J can still prove that a purported kappa_2=2 case actually has a two-cover, thereby eliminating it. But if the kappa_2=2 case genuinely exists, an outward terminalization step must do at least one of the following:

1. enlarge the mutable window beyond J and use exterior vertices;
2. change the witness/carrier map so the reflected-double zero crossing is bypassed rather than repaired chamberwise; or
3. return to an exact-root/deletion-distance argument rather than the local-depth iteration.

In particular the protected frozen-window carrier construction cannot by itself solve a genuine kappa_2=2 double by freezing J: its required base chamber in X_{r+1} does not exist inside that support.

The four-end reversal theorem [[genuine_two_deletion_doubles_reverse_all_four_corridor_ends]] remains valuable because it is the sharp structure of any genuine two-deletion residue, but it should now be used either to contradict kappa_2=2 or to design an enlarged-window repair.
