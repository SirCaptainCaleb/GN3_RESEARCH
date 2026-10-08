# Finite witnesses for a separated color inversion — preserved pre-item development

## Development


Let \(p\) be the first \(0\) and \(q\) the last \(1\) of a binary word. Then
\[
q\le p+1
\]
if and only if the word contains none of
\[
001,\qquad 011,\qquad 0101
\]
as consecutive subwords.

Indeed, failure means that some \(0\) is followed by a \(1\) at distance at least two. Choose such a pair with minimum separation. Separation two gives \(001\) or \(011\); separation three gives \(0101\); greater separation contradicts minimality.

Thus every violation of the width-one inversion relaxation has a witness on at most four bit positions. Under reverse-complement, \(001\) and \(011\) exchange while \(0101\) is fixed.

For NOR this supplies a finite local test for a useful relaxation of one-change behavior. It does not by itself characterize genuine one-change words.
