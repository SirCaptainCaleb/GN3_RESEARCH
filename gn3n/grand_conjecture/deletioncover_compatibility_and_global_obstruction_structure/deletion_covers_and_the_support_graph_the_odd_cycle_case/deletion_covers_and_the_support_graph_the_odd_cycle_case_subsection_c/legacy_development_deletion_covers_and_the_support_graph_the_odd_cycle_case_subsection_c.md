# 6.2 Rank transport — preserved pre-item development

## Composition

(none yet)

## Development

For consecutive compatible covers,
\[
S_i\cap S_{i+2}=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]
Lemma 3 shows that \(P_i\) and \(P_{i+2}\) arise from a common order by inserting \(d_{i+1}\) and \(d_i\) in equal or adjacent slots. An adjacent-slot transition supplies a tight triple reversing the two inserted labels across the intervening common vertex.

**Lemma 10.** At least \(k-1\) of the \(2k+1\) step-two transitions use adjacent slots. Their number is congruent to \(k-1\pmod 2\), and every adjacent transposition of consecutive ranks \(1,\ldots ,k\) occurs at least once.

**Proof.** Follow the \(k\) positions of the support order while replacing \(d_{i+1}\) by \(d_i\) and advancing from \(S_i\) to \(S_{i+2}\). An equal-slot transition preserves the rank positions; an adjacent-slot transition applies one simple adjacent transposition. After one circuit, the deterministic replacement of labels induces a \(k\)-cycle on the rank positions. A factorization of a \(k\)-cycle into adjacent transpositions uses every simple generator and has at least \(k-1\) factors. Its parity is \(k-1\), giving the congruence. \(\square\)

Thus the odd cycle contains linearly many explicitly located reversals. Their existence is not the remaining difficulty.
