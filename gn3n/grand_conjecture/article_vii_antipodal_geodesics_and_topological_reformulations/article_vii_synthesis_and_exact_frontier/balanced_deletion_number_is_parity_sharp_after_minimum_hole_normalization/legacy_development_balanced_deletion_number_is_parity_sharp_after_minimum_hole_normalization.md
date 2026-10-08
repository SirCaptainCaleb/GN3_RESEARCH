# Balanced deletion number is parity-sharp after minimum-hole normalization — preserved pre-item development

## Development

## The balanced deletion number is parity-sharp after minimum-hole normalization

For a boundary tournament \(H\), define the balanced two-cover deletion number
\[
\zeta_2(H)
=
\min\{|Y|:\ H-Y=A\mid B\text{ with }|A|=|B|\}.
\]
Let
\[
k=\kappa_2(H).
\]

Choose a minimum deletion set \(X\), \(|X|=k\), and among all two-covers
\[
H-X=P\mid Q
\]
choose one minimizing
\[
\Psi(P,Q)=|P|^2+|Q|^2.
\]
Write
\[
r=|P|\le s=|Q|.
\]

If \(s\ge r+2\), the imbalanced minimum-hole theorem already enters the bounded four-component/deletion-distance descent interface. Exclude that bounded branch. Then
\[
s-r\in\{0,1\}.
\]

### Balanced parity

If \(s=r\), then \(X\) itself is a balanced deletion set, so
\[
\zeta_2(H)\le k.
\]
By definition \(\zeta_2(H)\ge\kappa_2(H)=k\). Hence
\[
\boxed{\zeta_2(H)=k.}
\]

### Odd complementary parity

If \(s=r+1\), choose either endpoint \(q\) of the displayed tight path \(Q\). Then
\[
Q-q
\]
is an inherited tight path of order \(r\), and therefore
\[
H-(X\cup\{q\})=P\mid(Q-q)
\]
is a balanced two-cover of profile
\[
r\mid r.
\]
Thus
\[
\zeta_2(H)\le k+1.
\]

On the other hand every balanced deletion set \(Y\) satisfies
\[
|V(H)|-|Y|\equiv0\pmod2,
\]
so
\[
|Y|\equiv |V(H)|\pmod2.
\]
In the present case
\[
|V(H)|-k=|P|+|Q|=2r+1
\]
is odd, hence \(k\) has parity opposite to \(|V(H)|\). Therefore no balanced deletion set can have order \(k\). Since every deletion set has order at least \(k\),
\[
\boxed{\zeta_2(H)=k+1.}
\]

Consequently, outside the bounded imbalance interface,
\[
\boxed{
\zeta_2(H)=
\begin{cases}
k,& |V(H)|-k\text{ even},\\[1mm]
k+1,& |V(H)|-k\text{ odd}.
\end{cases}}
\]

Equivalently, the minimum possible deficiency of a zero exact-root chamber is already determined up to the bounded four-component branch: it is exactly the least integer at least \(\kappa_2(H)\) having the parity of \(|V(H)|\).

This sharpens the current exact-root frontier. The phrase “ideally force a zero-root chamber with hole order \(\kappa_2(H)\)” is correct only in the parity-compatible case. When \(|V(H)|-\kappa_2(H)\) is odd, equality is impossible; the sharp target is \(\kappa_2(H)+1\), and a normalized minimum-hole complement constructs such a balanced deletion state directly.

For \(\kappa_2(H)=2\), the hard branch therefore splits canonically:
- if \(|V(H)|\) is even, there is a balanced genuine two-deletion state;
- if \(|V(H)|\) is odd, there is a balanced three-deletion state obtained by adjoining one endpoint of the long side to a genuine minimum pair.

No topology is needed for this parity-sharp existence statement.
