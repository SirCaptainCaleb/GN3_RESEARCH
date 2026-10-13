# Fixed-order freedom and the necessity of coupled root-order selection

# Fixed-order freedom and coupled root-order selection

## The root-fiber realization theorem

**Theorem 1.** Fix \(n\ge2\) and a permutation \(\pi=(i_1,\ldots,i_n)\) of the cube dimensions. For every \(k\), independently choose any function \(F_k:\mathbb F_2^n\to\mathbb F_2\) satisfying
\[
F_k(x\oplus e_{i_k})=F_k(x),
\qquad
F_k(\bar x)=1-F_k(x).
\]
There is a unique antipodally odd coloring \(c\) of the undirected edges of \(Q_n\) such that, for every root \(x\), the \(k\)-th edge of the full \(\pi\)-geodesic beginning at \(x\) has color \(F_k(x)\).

**Proof.** Set \(S_{k-1}=\{i_1,\ldots,i_{k-1}\}\) and define
\[
c_{i_k}(y)=F_k(y\oplus\mathbf1_{S_{k-1}}).
\]
The first condition makes this independent of the selected endpoint of the dimension-\(i_k\) edge. The second gives antipodal oddness. The \(k\)-th edge of the \(\pi\)-geodesic from \(x\) begins at \(y=x\oplus\mathbf1_{S_{k-1}}\), so its bit is \(F_k(x)\). These formulas specify every edge of the cube and prove uniqueness. \(\square\)

Thus a prescribed dimension order imposes no cross-position constraints among the independently selected rooted edge-bit functions; the missing dependencies appear only when comparing distinct direction orders on shared cube edges.

## A fixed-order obstruction despite global closure

**Theorem 2.** For every \(n\ge4\) and any prescribed direction order \(\pi\), there is an antipodally odd NORI1 edge coloring for which
\[
\min_{x\in Q_n}\operatorname{sw}(P(x,\pi))=n-2,
\]
yet a monochromatic full antipodal geodesic exists.

**Proof.** Rename the prescribed order \(1,\ldots,n\), and color the undirected edges by
\[
c_1(x)=x_2,\qquad c_k(x)=x_1\oplus(k\bmod2)\quad(2\le k\le n).
\]
Each \(c_k\) ignores \(x_k\), and complementing all \(n\) vertex bits reverses every color. On the prescribed order, after the first step the remaining \(n-1\) bits alternate, independently of the root. Thus the \(n-2\) internal comparisons among them all switch; the first comparison can be made equal by selecting the root, giving equality.

For closure choose a root with \(x_1=0,x_2=1\). Traverse all odd-indexed dimensions in \(\{2,\ldots,n\}\), then direction \(1\), then all even-indexed dimensions. The pre-pivot edges have bit \(1\), the pivot bit is \(x_2=1\), and the post-pivot edges also have bit \(1\). \(\square\)

## Exponential rarity of successful permutation orders

**Theorem 3.** For every \(n\ge4\), put \(N=n-1\). There is an antipodally odd NORI1 edge coloring admitting a monochromatic full geodesic such that the fraction of dimension permutations admitting *any* root with at most one switch is at most
\[
\boxed{\frac{N}{\binom N{\lfloor N/2\rfloor}}}
=O(N^{3/2}2^{-N}).
\]

**Proof.** Modify the preceding coloring to \(c_1(x)=x_2\) and \(c_k(x)=x_1\oplus\alpha_k\) for \(k\ge2\), where \(\alpha_2=0\) and among the \(N\) bits \(\alpha_2,\ldots,\alpha_n\), precisely \(p=\lfloor N/2\rfloor\) are \(1\) and \(q=N-p\) are \(0\). Choosing \(x_1=0,x_2=1\) and following all \(\alpha=1\) dimensions, then dimension \(1\), then all \(\alpha=0\) dimensions gives a color-\(1\) full geodesic.

For any permutation \(\sigma\), delete direction \(1\) and read the resulting ordered sequence \(\beta\) of \(\alpha\)-bits. All edges before direction \(1\) have colors \(x_1\oplus\alpha_k\); all those after it have colors \(1\oplus x_1\oplus\alpha_k\). Thus every transition within \(\beta\) forces a corresponding switch on the full path, except perhaps the one comparison interrupted by direction \(1\). Hence
\[
\min_x\operatorname{sw}(P(x,\sigma))\ge T(\beta)-1,
\]
where \(T(\beta)\) counts changes between consecutive \(\beta\)-bits. A one-switch path therefore requires \(T(\beta)\le2\).

Among the \(\binom Np\) binary words with \(p\) ones and \(q\) zeros, precisely \(N\) have at most two switches. Two have one switch; among words with two switches, there are \(p-1\) of the form \(1^a0^q1^{p-a}\) and \(q-1\) of the form \(0^a1^p0^{q-a}\). A uniform random permutation of dimensions induces a uniform balanced \(\beta\), so the claimed bound follows. \(\square\)

## Boundary comparison: sparse winning permutations

**Theorem 4.** On ordered triples of distinct vertices \(a,b,c\in[n]\), define \(b(a,b,c)=\mathbf1_{\{a<c\}}\). It is reversal odd and has a monochromatic Hamilton path \(1,2,\ldots,n\). Nevertheless, if \(k=\lceil n/2\rceil\) and \(\ell=\lfloor n/2\rfloor\), a uniformly random Hamilton ordering has a triple-color word with at most one switch with probability at most
\[
\boxed{\frac{2^k-2}{k!}\cdot\frac{2^\ell-2}{\ell!}},
\]
which decays faster than exponentially.

**Proof.** Its consecutive triple labels compare \(v_i\) with \(v_{i+2}\). The odd-position word \(v_1,v_3,\ldots\) and even-position word \(v_2,v_4,\ldots\) have independent uniform relative orders. If the full interleaved comparison word has at most one switch, each of those two subsequences is monotone or changes monotonicity once. For \(h\ge2\), precisely \(2^h-2\) relative permutations have this property: increasing-then-decreasing permutations are determined by the set preceding their maximum (\(2^{h-1}\) choices), decreasing-then-increasing permutations by the set preceding their minimum (another \(2^{h-1}\)), and the two monotone permutations have been counted twice. Multiply the two independent upper probabilities. \(\square\)

## What this establishes for the common problem

Both motivating families can possess a good complete path while suitable dimension or vertex orders are rare. Their restrictions to a *frozen order* allow extensive independent prescriptions, so neither choosing a root after freezing the order nor selecting a random order is a universal method. A common topological selection theorem must exploit the *overlaps among different complete permutations*, together with root changes in NORI1; its proof cannot rely on favorable behavior of a predetermined chamber. This is an obstruction to proposed selection methods, not an existence proof of the full common conjecture.

Research note with expanded comparisons: note_d7af56d7da1b8654fcf6a404.
