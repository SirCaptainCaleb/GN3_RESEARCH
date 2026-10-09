# Odd-flipper six-residual closure reduces to a seven-dimensional one-flipper case

# Reduction of the odd-flipper frontier to seven dimensions

Suppose \(c\) is an antipodal-reversal-odd ordered-three-face coloring of \(Q_n\) and all but exactly six coordinates are universal exterior flippers. Write the six remaining coordinates \(B\), and \(r=n-6\). If \(r\) is even, the earlier parity-six closure theorem applies.

If \(r\) is odd, choose one flipper \(g\in A\) and put \(A'=A\setminus\{g\}\), so \(|A'|=r-1\) is even. Restrict to the seven-dimensional subcube with directions \(B\cup\{g\}\), fixing all \(A'\)-coordinates to zero, to define \(c'\). By the universal-flipper identity and even parity of \(|A'|\), the induced \(c'\) is antipodal-reversal-odd: reversing within the seven-dimensional subcube and complementing all fixed \(A'\)-bits changes the color by \(1\oplus |A'|=1\). The direction \(g\) remains a universal exterior flipper in \(c'\).

Apply the exact flipper lifting lemma to the set \(A'\): any one-change antipodal geodesic in \(c'\) lifts to a one-change antipodal geodesic in \(c\).

**Seven-dimensional bottleneck theorem.** To prove NORI for every coloring in every dimension having at most six nonflipper coordinates, it suffices to prove NORI for the class of \(Q_7\) colorings with *one universal exterior flipper*. Combined with the already proved even-flipper and five-nonflipper theorems, this is the sole outstanding configuration for that entire structured class.

The restriction is a sufficient reduction; it does not assert that arbitrary NORI counterexamples possess any universal flipper.
