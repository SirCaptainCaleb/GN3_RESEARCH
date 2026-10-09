# Sharp rooted obstructions to one-change antipodal geodesics

# Rooted obstructions and sharp dimension-five root density

A root \(x\in Q_n\) is called *bad* when every full geodesic beginning at \(x\) has at least two changes among its consecutive ordered-three-face colors. We assume the NORI reversal law \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\).

**Theorem 1 (failure of rooted strengthening).** For each \(n\ge5\) and prescribed root \(x\), there is a legal NORI coloring making \(x\) bad. The number of changes along every full \(x\)-rooted geodesic may be made equal to \(2\) for \(n=5\), to \(n-3\) for even \(n\ge6\), and to \(n-4\) for odd \(n\ge7\).

**Proof.** Translate \(x\) to \(0^n\). Let \(k\) be the number of exterior coordinates fixed to 1 on a physical ordered three-face. For even \(n\), color by \(k\bmod2\). Since \(n-3\) is odd, antipodal complementation reverses the bit. Every rooted order visits the successive exterior weights \(0,\ldots,n-3\), yielding complete alternation.

For odd \(n\ge7\), write \(n-3=2s\) and fix a reversal-odd ordered-triple bit \(h(a,b,c)=1-h(c,b,a)\). Color faces of exterior weight \(k<s\) by \(k\bmod2\), of weight \(k=s\) by \(h\), and of weight \(k>s\) by \(1+(k\bmod2)\). Exterior weights are paired by \(k\mapsto2s-k\), so this is NORI-odd. The left and right window strings alternate, with opposite values directly adjacent to the central window. Exactly one central comparison changes, giving \(2(s-1)+1=n-4\) changes. The \(n=5\) construction is furnished by Theorem 2. \(\square\)

**Theorem 2 (exact rooted \(Q_5\) classification).** Put \(V=[5]\). For each \(t\in V\) and \(P\subset V\setminus\{t\}\) of size two, choose a bit \(H(P,t)\) satisfying
\[
H((V\setminus\{t\})\setminus P,t)=1+H(P,t).
\tag{1}
\]
For a physical ordered face with directions \((a,b,c)\) and exterior-one set \(S\), define
\[
c(F,(a,b,c))=
\begin{cases}
H(\{a,b\},c)&|S|=0,\\
1+H(S\cup\{a\},b)&|S|=1,\\
H(S,a)&|S|=2.
\end{cases}
\tag{2}
\]
Precisely these \(2^{15}\) legal NORI colorings make \(0^5\) bad.

**Proof.** At a bad root every three-window word is \(010\) or \(101\). The first and last windows consequently agree. Exchanging the first two directions fixes the physical last window, so the first-window color has the form \(H(\{a,b\},c)\). Forced alternation then determines the middle and last window values as (2). Every ordered face occurs in some \(0^5\)-rooted full path, so these formulas exhaust the coloring. Antipodal reversal of the rank-zero and rank-two faces gives (1), which also enforces reversal oddness at rank one. Conversely (1)–(2) produce the word \((H(\{a,b\},c),1+H(\{a,b\},c),H(\{a,b\},c))\) for every rooted order \((a,b,c,d,e)\). For each \(t\), the six possible \(P\)'s form three complementary pairs; one free bit per pair gives \(3\cdot5=15\) independent choices. \(\square\)

**Theorem 3 (sharp good-root density).** Every legal NORI coloring of \(Q_5\) has at most two bad roots, and any two bad roots are adjacent. Consequently at least \(30\) of its \(32\) vertices admit good full geodesics. The bound is attained with any prescribed adjacent pair as the exact bad set.

**Proof.** Translate one bad root to \(0^5\) and use the classification (1)–(2). Suppose a second bad root is at Hamming distance \(k\ge2\), with first \(k\) of the coordinates \(a,b,c,d,e\) equal to 1. A bad three-window word at that root has its first and last bits equal, distinct from its middle bit. Substituting (2) gives the following contradictions (all equations in \(\mathbb F_2\)):

For \(k=2\), orders \(bdeac,abdce,bedac\) yield
\[
H(bc,a)+H(ab,d)=1,\quad H(ab,d)+H(ab,e)=1,\quad
H(ab,e)+H(bc,a)=1,
\]
whose sum is \(0=1\). For \(k=3,4\), orders \(adebc,badce\) demand simultaneously \(H(bc,a)+H(ab,e)=1\) and \(=0\). For \(k=5\), orders \(abcde,adebc\) demand simultaneously \(H(bc,a)+H(ad,c)=0\) and \(=1\). Hence two distinct bad roots are adjacent; three pairwise adjacent vertices cannot exist in a hypercube.

For sharpness fix coordinate \(a\), and in (1) set \(H(P,t)=\mathbf1_{\{a\notin P\}}\) for \(t\ne a\), choosing any complementary-pair assignment for \(t=a\). Formula (2) makes \(0^5\) bad. For a path rooted at \(e_a\), place \(a\) at position \(j\) in its direction order. Its full color word is \(010\) for \(j=1,2\), \(101\) for \(j=4,5\), and \((h,1+h,h)\) for \(j=3\), with \(h=H(\{p_1,p_2\},a)\). Thus \(e_a\) is bad too; the upper bound makes every other vertex good. \(\square\)

The rooted strengthening therefore fails for every \(n\ge5\), whereas the unrooted five-dimensional theorem has the stronger conclusion that at least \(15/16\) of the roots succeed. This makes root mobility an essential part of any global topological or inductive extraction.
