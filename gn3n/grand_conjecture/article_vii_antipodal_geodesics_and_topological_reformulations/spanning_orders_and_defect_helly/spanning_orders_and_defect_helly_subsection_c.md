# Local forbidden patterns and witness handoff

### Positive local witnesses

A status word satisfies \(q\le p+1\) if and only if it avoids
\[
\boxed{001,\qquad 011,\qquad 0101.}
\]
For the forward direction each displayed word contains a zero followed by a one at distance at least two. Conversely, choose such a pair with minimum separation. Separation two gives \(001\) or \(011\); separation three gives \(0101\); greater separation contradicts minimality.

Thus failure of the two-cover criterion is certified by one of three positive words on at most four consecutive status positions, equivalently on at most six consecutive vertices. Reverse-complement interchanges \(001\) and \(011\) and fixes \(0101\). Hence this positive witness family is antipodally closed and may be used consistently for both protection and repair. No opposite-polarity witness family is used below.
