# Three compatible one-vertex extensions have a common-endpoint normal form — preserved pre-item development

## Composition

(none yet)

## Development

## Three compatible one-vertex extensions have a common-endpoint normal form

Let \(C\) be a vertex set and let \(a,b,c\notin C\) be distinct. Suppose
\[
C\cup\{a\},\qquad C\cup\{b\},\qquad C\cup\{c\}
\]
are Hamiltonian. Choose Hamilton orders on these three supports.

Then at least one of the following holds.

1. Two chosen Hamilton orders have relative-order disagreement on \(C\).

2. For some distinct \(x,y\in\{a,b,c\}\), the support
\[
C\cup\{x,y\}
\]
is Hamiltonian.

3. There is a Hamiltonian four-set consisting of two consecutive vertices of a common order on \(C\) together with two of \(a,b,c\).

4. There is a tight triple through two of \(a,b,c\) reversing the core vertex separating two adjacent insertion gaps.

5. All three chosen extensions induce one common order
\[
C=(c_1,\ldots,c_m)
\]
and insert \(a,b,c\) into the same endpoint gap of this order. In particular \(C\) itself is Hamiltonian, and all three extensions are rooted on the same side of the same Hamilton path on \(C\).

### Proof

If two chosen orders disagree on \(C\), outcome 1 holds. Assume therefore that all three induce the same relative order on \(C\). Each chosen Hamilton path is obtained by inserting its exceptional vertex into one of the \(m+1\) gaps of that common order, including the two endpoint gaps.

Take any two exceptional labels \(x,y\).

- If their insertion gaps are separated by at least one gap, the compatible one-vertex extension theorem gives a Hamilton order on
  \[
  C\cup\{x,y\},
  \]
  giving outcome 2.

- If the gaps are adjacent, the same theorem gives either a Hamilton order on \(C\cup\{x,y\}\) or the boundary flip of the unique new mixed triple, which is a positioned reversal across the intervening core vertex. These are outcomes 2 or 4.

- If the gaps coincide at an internal edge of \(C\), the same theorem gives a Hamiltonian four-set on that core edge together with \(x,y\), giving outcome 3.

Hence, if outcomes 2--4 are absent, every pair among \(a,b,c\) must occupy one common endpoint gap. Pairwise equality then forces all three to occupy the same endpoint gap. Deleting the exceptional endpoint from any of the three displayed Hamilton paths leaves the common order on \(C\), so \(C\) itself is Hamiltonian. This is outcome 5. \(\square\)

### Johnson-triangle consequence

Suppose three Hamiltonian \(r\)-supports form a Johnson-star triangle
\[
A_a=C\cup\{a\},\qquad
A_b=C\cup\{b\},\qquad
A_c=C\cup\{c\}.
\]
Then the triangle either already exposes an order disagreement, a positioned reversal, a bounded Hamiltonian four-support, or a Hamiltonian \((r+1)\)-support obtained by adjoining two exchange labels; otherwise all three supports arise by same-side endpoint extensions of one Hamiltonian \((r-1)\)-core \(C\).

Thus a quiet recurrent simple-root Johnson triangle has a canonical rooted common core.
