# Antipodal roots with identical direction order have switch vectors differing by the exact coboundary of physical same-face triple-reversal asymmetry

# An exact antipodal-root switch-coboundary identity for physical ordered faces

Let \(n\ge5\) and \(c\) be any active NORI coloring of PHYSICAL ordered three-faces, satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
Fix ANY full direction order \(p=(p_1,\ldots,p_n)\) and ANY physical root \(x\). Let \(L=n-2\), and let \(F_j=F_j(x,p)\) be the actual physical three-face at the jth window, with ordered free direction triple \(t_j=(p_j,p_{j+1},p_{j+2})\). Define the same-face **local triple-reversal asymmetry bit**
\[
r_j(x,p)=c(F_j,t_j)\oplus c(F_j,\operatorname{rev}t_j)\in\mathbb F_2.
\tag{1}
\]
Unlike reversal-oddness across *antipodal physical faces*, this is a comparison of two orders ON THE SAME physical face, and may be 0 or 1 independently as the coloring varies.

**Theorem (exact antipodal-root discrete gauge/coboundary identity).** Write the actual ordered-face word \(w_j(x,p)=c(F_j,t_j)\) and switch bits \(s_j(x,p)=w_j(x,p)\oplus w_{j+1}(x,p)\), \(1\le j\le L-1=n-3\). At the ANTIPODAL root \(\bar x=x\oplus[n]\), with the SAME direction order \(p\), one has:
\[
\boxed{w_j(\bar x,p)=1\oplus w_j(x,p)\oplus r_j(x,p),}
\tag{2}
\]
\[
\boxed{s_j(\bar x,p)=s_j(x,p)\oplus r_j(x,p)\oplus r_{j+1}(x,p).}
\tag{3}
\]
Thus the two full switch vectors differ by the \(\mathbb F_2\) discrete coboundary \(\delta r\) of the actual local order-reversal asymmetry 0-cochain along the window-index path:
\[
\boxed{s(\bar x,p)\oplus s(x,p)=\delta r.}
\tag{4}
\]
The reversal-asymmetry word is itself antipodally ROOT-INVARIANT and full-order-reversal covariant:
\[
r_j(\bar x,p)=r_j(x,p),\qquad
r_j(x,\operatorname{rev}p)=r_{L+1-j}(x,p).
\tag{5}
\]
The endpoints of \(r\) agree if and only if the two antipodal-root paths have the SAME switch-count parity:
\[
\bigoplus_{j=1}^{L-1}s_j(\bar x,p)
=\bigoplus_{j=1}^{L-1}s_j(x,p)
\quad\Longleftrightarrow\quad r_1=r_L.
\tag{6}
\]

**Proof.** At the same progress rank, the rooted path from \(\bar x\) has the SAME window free directions and all exterior fixed bits complemented, so its physical window face is literally \(\bar F_j\). The active axiom applied with reversed free order gives
\[
c(\bar F_j,t_j)=1\oplus c(F_j,\operatorname{rev}t_j)
=1\oplus w_j(x,p)\oplus r_j(x,p),
\]
which is (2). XOR consecutive window identities: the two constant 1s cancel, giving (3)-(4). Applying the same argument to the reversed order on \(\bar F_j\) shows
\[
r(\bar F_j,t_j)=c(\bar F_j,t_j)\oplus c(\bar F_j,\operatorname{rev}t_j)
=r(F_j,t_j),
\]
so \(r_j(\bar x,p)=r_j(x,p)\). The actual full-path antipodal reversal at the FIXED root \(x\) sends \(p\mapsto\operatorname{rev}p\) and transforms the physical color word to the reversed complement. Its corresponding reversal-asymmetry comparison therefore gives the reversed \(r\)-word, proving the second identity in (5). Finally XOR (3) across all \(j\); the interior \(r\) terms cancel in pairs, yielding (6). \(\square\)

**Corollary (antipodally synchronized endpoint-balanced paths have a closed reversal gauge).** For a full permutation \(p\) that is endpoint-opposed at BOTH \(x\) and \(\bar x\), the two switch vectors have odd parity, hence
\[
\boxed{r_1(x,p)=r_L(x,p).}
\tag{7}
\]
The synchronized full-path corridors from Item \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` therefore provide, at every prescribed antipodal root pair in \(n\ge10\), an entire \((n-6)!\)-packet of actual full paths with a CLOSED reversal-asymmetry cochain (identical first/last gauge bits), while their internal switch vectors differ by its exact derivative. Moreover the endpoint-closed condition is EXACTLY the two-root equality of reversal-orbit signatures used in that theorem.

**Why this is mathematically useful.** Earlier permutohedral Tucker labels track internal switch positions but do not control how switches change when ROOT is antipodally complemented. Formula (3) supplies that missing PHYSICAL comparison without inventing an abstract sign-vector action: at any fixed complete order, the antipodal root transfer is a gauge transformation by a same-face reversal asymmetry word. It is compatible with order-reversal and is an actual 1-dimensional chain-complex coboundary identity. It suggests constructing a two-parameter root/order carrier with the switch-change 1-cochain and its cross-root gauge \(r\), then deriving a nontrivial holonomy obstruction when certified cells are glued around root-cube and permutohedral exchange cycles.

**Crucial limitation.** The cochain may be identically zero: a coloring independent of reversing local three-direction order has \(r_j=0\) everywhere, and the two antipodal-root switch vectors then coincide, even if BOTH contain many switches (as in the valid full exterior-parity coloring). Consequently the coboundary identity alone cannot reduce switches or force grand closure. A proof must combine it with genuine root mobility over MORE THAN one antipodal pair and/or with a nontrivial coupled topological class. No universal holonomy contradiction is asserted.
