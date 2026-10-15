# Twisted involution stabilizers and dyadic block actions

### Twisted involution stabilizers and the dyadic separation

**Theorem 1 (common stabilizer criterion).** Let \(R\) be a free involution on a finite set \(X\), and let \(G\) act on \(X\) commuting with \(R\). Fix a character \(\chi:G\to\mathbb F_2\). There is a coloring \(c:X\to\mathbb F_2\) satisfying \(c(Rx)=c(x)+1\) and \(c(gx)=c(x)+\chi(g)\) if and only if
\[
gx=x\ \Longrightarrow\ \chi(g)=0,
\qquad gx=Rx\ \Longrightarrow\ \chi(g)=1
\tag{1}
\]
for all \(x,g\).

*Proof.* Necessity is immediate. For sufficiency, let \(G\times C_2\) act on \(X\), with the second factor acting by \(R\). The prescribed color-change character is \((g,\epsilon)\mapsto\chi(g)+\epsilon\). Conditions (1) state precisely that this character vanishes on every point stabilizer. Choose a representative of each group orbit and assign it color zero, then transport by the character. The stabilizer condition makes the coloring well-defined. QED.

The theorem applies to antipodal cube edges and to ordered distinct triples with reversal \(R(a,b,c)=(c,b,a)\), yielding the same abstract coloring criterion for both unrestricted systems.

**Theorem 2 (semiregular automorphism 2-groups of triple colorings).** For every reversal-odd coloring of ordered distinct triples on \(n\ge3\) vertices, each 2-subgroup \(P\) of its color-preserving automorphism group acts freely on the vertices. Consequently \(|P|\mid n\), and for odd \(n\) its full color-preserving automorphism group has odd order. Conversely, every free vertex action of a finite 2-group admits an invariant reversal-odd triple coloring.

*Proof.* If a nonidentity element \(g\in P\) fixes \(e\), write its order as \(2^k\), and select a cycle of length \(2^k\). Then \(h=g^{2^{k-1}}\) fixes \(e\) and exchanges two vertices \(a,c\) of that cycle. It sends \((a,e,c)\) to \((c,e,a)\), forbidden by (1) with \(\chi=0\). Thus all nonidentity group elements are fixed-point-free, and all group orbits have size \(|P|\). If the full automorphism group has even order on odd \(n\), Cauchy's theorem supplies a forbidden involution. Conversely, in a free action no nonidentity element fixes a triple or sends one to its reversal, since the latter would fix its middle vertex. Apply Theorem 1 with the zero character. QED.

**Theorem 3 (dyadic block actions separate the two original models).** Partition the symbols into \(A\sqcup B\), with \(|A|=2^r\), \(|B|=2^s\) and \(r,s\ge1\). Let \(G=E_r\times E_s\), each elementary-abelian factor acting regularly on its own block and trivially on the other.

(a) A reversal-odd ordered-triple coloring can transform uniformly by a character \(\chi:G\to\mathbb F_2\) only if \(r=s=1\). In that case such a coloring exists, with \(\chi\) equal to one on each factor generator. In particular a strictly \(G\)-invariant triple coloring never exists.

(b) A strictly \(G\)-invariant antipodally odd cube-edge coloring exists for every \(r,s\ge1\).

*Proof.* Every nonidentity \(t\in E_r\) exchanges \(a\) and \(a+t\) while fixing any \(e\in B\). Hence it sends \((a,e,a+t)\) to its reversal. Theorem 1 requires \(\chi(t)=1\) for every nonidentity \(t\). For \(r\ge2\) this contradicts additivity, since \(\chi(t+u)=\chi(t)+\chi(u)=0\) for distinct nonzero \(t,u\). The same argument applies to \(E_s\). For \(r=s=1\), take the character that is one on both generators; only individual factor generators can reverse a triple, and there are no nontrivial stabilizers of ordered triples. Theorem 1 then provides the coloring.

For (b), choose nonzero translations \(t_A\in E_r\), \(t_B\in E_s\) and define a fixed-point-free permutation \(\sigma\) on \(A\sqcup B\) by these translations. The abelian group \(G\) commutes with \(\sigma\). For a cube edge in direction \(i\), set
\[
\boxed{c(\{x,x\oplus e_i\})=x_{\sigma(i)}.}
\tag{2}
\]
It is well-defined since \(\sigma(i)\ne i\), it complements under \(x\mapsto\bar x\), and it is unchanged by the simultaneous action of \(G\) on directions and vertex entries. QED.

**Interpretation.** The nonzero equivariant Euler-class obstruction for dyadic permutahedral products is compatible with globally invariant cube colorings but incompatible with globally invariant reversal-odd boundary triple colorings. Even twisting every color by a group character fails for block sizes at least four. Thus a unified argument should keep the abstract stabilizer criterion, but cannot assume identical untwisted block symmetries in both models.
