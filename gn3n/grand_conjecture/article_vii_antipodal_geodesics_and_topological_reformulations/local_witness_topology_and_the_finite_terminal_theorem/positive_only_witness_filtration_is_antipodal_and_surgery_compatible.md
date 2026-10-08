# Positive-only witness filtration is antipodal and surgery-compatible

## Composition

### One witness predicate throughout

Use only
\[
\mathcal W_+=\{001,011,0101\}.
\]
This family is closed under reverse-complement, so witness depth and reflected orientation are antipodally compatible. Protection means absence of a strictly inward positive witness. A repair is valid only when it removes the positive witness predicate defining the selected depth. No negative witness language is introduced at any stage of compression or repair.

## Development

Use only W+={001,011,0101} as witness words. Reversal of a spanning order sends the status word to reverse-complement, so rc(001)=011, rc(011)=001, rc(0101)=0101. Hence the positive witness family is closed under reversal and the reflected-location witness path can be oriented intrinsically exactly as before: reversal preserves unsigned depth and reverses orientation, with the external gauge needed only for the same tie/self-reflecting cases already present in the labeling rule. No negative words are needed for antipodality. Under this depth rule, protection means absence of strictly inward positive witnesses. The repaired five-position obstruction and tuple-compression lemmas use only positive protection; exclusive disjoint span-two windows are adjacent, so their union has at most ten vertices; exclusive disjoint alternating windows are impossible; overlap-one alternating windows are impossible by the positive tuple argument; all remaining centered/overlapping supports are at most ten. Therefore every terminal support is covered by the audited ten-vertex two-cover theorem. Reordering that support by a two-cover order removes exactly the positive predicate defining depth. Thus compression, terminal classification, and terminal surgery now use one consistent witness language.
