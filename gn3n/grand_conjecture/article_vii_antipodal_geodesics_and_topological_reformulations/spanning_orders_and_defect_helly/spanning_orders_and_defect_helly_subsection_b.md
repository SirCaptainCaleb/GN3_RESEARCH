# Exact inversion-window criterion

### Inversion windows and deletion distance

For a spanning order \(\pi=(v_1,\ldots,v_n)\) with status word \(\epsilon_1,\ldots,\epsilon_m\), put
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
with \(p=m+1\) when there is no zero and \(q=0\) when there is no one.

**Theorem.**
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\quad q(\pi)\le p(\pi)+1.
\]
If \(q\le p+1\), a cut \(j\) with \(q\le j\le p+1\) gives the tight prefix \((v_1,\ldots,v_j)\) and, by boundary antisymmetry, the tight reversed suffix \((v_n,\ldots,v_{j+1})\). Conversely, a two-cover \(P\mid Q\), written as \((P,Q^{\rm rev})\), satisfies the displayed inequality.

Set
\[
d_2(\pi)=\max\{0,q(\pi)-p(\pi)-1\}
\]
and let \(\kappa_2(H)\) be the minimum number of deleted vertices required to obtain a two-cover. Then
\[
\boxed{\kappa_2(H)=\min_\pi d_2(\pi).}
\]
For positive deficiency the canonical paths are the prefix through \(v_{p+1}\) and the reversed suffix beginning at \(v_{q+1}\); the uncovered interval has exactly \(d_2(\pi)\) vertices.

If \(X\) is a minimum deletion set, \(|X|=\kappa_2(H)\), and \(H-X=P\mid Q\), then for every \(Y\subseteq X\),
\[
\boxed{\kappa_2\!\left(H-(X\setminus Y)\right)=|Y|.}
\]
Indeed, deleting \(Y\) gives the displayed two-cover, while a smaller deletion in the intermediate graph would produce fewer than \(|X|\) deletions in \(H\).

Consequently every nonempty \(Y\subseteq X\) is absolutely nonaugmentable relative to \(P\mid Q\): neither \(P\cup Y\) nor \(Q\cup Y\) is Hamiltonian, and no partition \(Y=Y_P\sqcup Y_Q\) makes both \(P\cup Y_P\) and \(Q\cup Y_Q\) Hamiltonian. This minimum-hole heredity will be used repeatedly below.
