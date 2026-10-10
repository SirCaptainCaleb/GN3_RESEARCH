# Hereditary sentinel-word contraction and NORI counterexamples in every dimension at least nine

# Hereditary sentinel-word contraction and counterexamples in all dimensions \(n\ge9\)

## Theorem

**Theorem.** For every integer \(n\ge9\), there is a legal antipodal-reversal-odd coloring of the physical ordered three-faces of \(Q_n\) for which **every** full antipodal geodesic has at least two ordered-three-face color changes. Consequently the unrooted NORI grand conjecture fails in *each* dimension \(n\ge9\).

This strengthens the explicit \(Q_9\) counterexample in *A dimension-nine counterexample to the physical NORI conjecture* by a dimension-free contraction principle. The finite \(Q_9\) obstruction requires only 2,016 comparisons; the new hereditary lemma is certified by 22,272 local comparisons of length at most seven, independently of \(n\).

## 1. The abstract sentinel word

Use symbols \(0,1,s\), with exactly one \(s\) in each word. Define the reversal-even triple rule on ordinary symbols by
\[
h(a,b,c)=\mathbf1_{\{(a,b,c)=(0,0,0)\ \mathrm{or}\ [b=1\ \mathrm{and}\ (a=0\ \mathrm{or}\ c=0)]\}}.
\]
Fix two bits \(z,\varepsilon\). For any word \(w=(w_1,\ldots,w_m)\) containing exactly one \(s\), define its \((m-2)\)-term color word \(C_{z,\varepsilon}(w)\) as follows. For each ordered triple \((w_j,w_{j+1},w_{j+2})\),

* if it avoids \(s\), its color is \(h(w_j,w_{j+1},w_{j+2})\oplus z\oplus\mathbf1_{\{s\text{ precedes the triple}\}}\);
* if \(s\) is first, its color is \(1\);
* if \(s\) is last, its color is \(0\);
* if \(s\) is middle, its color is \(\varepsilon\).

When no sentinel appears in a local subword, use \(h\oplus z\) for every triple there. Let \(V_{z,\varepsilon}(w)\) be the number of adjacent color differences in this word (zero when it has fewer than two colors).

**Deletion lemma.** If \(d\ne s\) is any occurrence of an ordinary letter in \(w\), and \(w\setminus d\) is the word obtained by deleting that occurrence, then
\[
V_{z,\varepsilon}(w\setminus d)\le V_{z,\varepsilon}(w).
\tag{1}
\]

**Proof.** A color difference between two adjacent triple windows is determined by their four consecutive letters, the position of the unique sentinel relative to them, and the fixed bits \(z,\varepsilon\). Deleting a letter at position \(k\) leaves every four-letter comparison unaffected except those whose original four-letter window contains position \(k\), or whose new window joins the two sides of that position. All affected letters lie in the at-most-seven-letter interval from \(k-3\) through \(k+3\). Comparisons outside this interval correspond one-to-one with identical old and new comparisons.

If \(s\) lies outside the interval, every affected ordinary triple has the same exterior-\(s\) parity, before and after deletion. The resulting comparisons are therefore identical to the no-sentinel local model, up to a common bit complement that preserves changes. If \(s\) lies inside the interval, its local position and the two bits \(z,\varepsilon\) determine the affected comparisons exactly as in the abstract model. Thus it is sufficient to verify (1) for all words of lengths four through seven over \(\{0,1\}\), with either no sentinel or one sentinel, for all sentinel positions, both \(z\), both \(\varepsilon\), and every ordinary deletion position. Lengths at most three are immediate.

Here is a complete, executable finite certificate, with no external library or solver. The four sizes require respectively \(640,1920,5376,14336\) checks; their sum is \(22272\).

~~~python
from itertools import product

def h(a, b, c):
    return int((a == b == c == 0) or
               (b == 1 and (a == 0 or c == 0)))

def changes(w, z, eps):
    s = w.index(2) if 2 in w else -1
    colors = []
    for j in range(len(w) - 2):
        a, b, c = w[j:j + 3]
        if a == 2:
            colors.append(1)
        elif c == 2:
            colors.append(0)
        elif b == 2:
            colors.append(eps)
        else:
            colors.append(h(a, b, c) ^ z ^
                          int(s >= 0 and j > s))
    return sum(a != b for a, b in
               zip(colors, colors[1:]))

checks = 0
for n in range(4, 8):
    for slot in [-1] + list(range(n)):
        for q in product((0, 1),
                         repeat=n - int(slot >= 0)):
            w = (list(q) if slot == -1 else
                 list(q[:slot]) + [2] + list(q[slot:]))
            for z in (0, 1):
                for eps in (0, 1):
                    before = changes(w, z, eps)
                    for k in range(n):
                        if w[k] == 2:
                            continue
                        after = changes(w[:k] + w[k + 1:],
                                        z, eps)
                        assert after <= before
                        checks += 1
assert checks == 22272
~~~

This exhausts the local cases and proves the deletion lemma for arbitrary word length. \(\square\)

## 2. All-dimensional legal physical-face coloring

Let \(n\ge9\), partition the coordinate directions into
\[
V=A\sqcup B\sqcup\{s\},\qquad |A|=3,\quad |B|=n-4\ge5,
\]
and assign types \(0\) to \(A\) and \(1\) to \(B\). Fix any strict total order on \(A\sqcup B\).

For a physical ordered three-face \((F,(u,v,w))\), define
\[
c(F,(u,v,w))=
\begin{cases}
z_s(F)\oplus h(\tau(u),\tau(v),\tau(w)),&s\notin\{u,v,w\},\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s .
\end{cases}
\tag{2}
\]
The first case uses the fixed \(s\)-bit of the face. Each case depends solely on the physical face and free-coordinate order, never on the traversal corner.

**Legality.** For triples avoiding \(s\), antipodal complementation flips \(z_s(F)\), while reversal preserves \(h\). For triples with \(s\) first or last, reversal interchanges the complementary constants \(1,0\). For triples with \(s\) middle, reversal interchanges two distinct ordinary directions, complementing the strict-order indicator. Thus \(c(\bar F,(w,v,u))=1-c(F,(u,v,w))\) for every face.

**No good geodesic.** Fix any root and any full direction order. Replace the ordinary directions by their types, leaving the sentinel in place. The actual physical window-color word is precisely \(C_{z,\varepsilon}(w)\) for \(z\) equal to the root's \(s\)-bit and \(\varepsilon\) equal to the order comparison between the two directions adjacent to \(s\) (when this middle window exists). Delete \(n-9\) occurrences of type \(1\), leaving a nine-letter abstract word with three zeros, five ones, and one sentinel, while retaining the same formal \(z,\varepsilon\). Repeated application of (1) gives
\[
V_{z,\varepsilon}(w)\ \ge\
V_{z,\varepsilon}(w_{\mathrm{reduced}}).
\]
The exact \(Q_9\) finite certificate (*A dimension-nine counterexample to the physical NORI conjecture*) checks all \(\binom83\cdot9\cdot2\cdot2=2016\) possible reduced words and parameters and proves that the right side is at least two. Hence every rooted full geodesic for (2) has at least two changes. \(\square\)

## 3. Significance

The hereditary lemma identifies the missing dimension-lifting mechanism for the explicit sentinel construction. Rather than embedding a finite forcing *proof* with inconsistent exterior-bit holonomy, it enlarges a globally legal counterexample while retaining a monotone obstruction under deletion of ordinary direction occurrences. The chosen total order on distinct directions realizes one value of \(\varepsilon\); allowing both values in the reduced certificate makes the proof independent of the changing identities adjacent to the sentinel.

The original \(Q_9\) physical-face proof remains the base case. The \(Q_{15}\) three-class construction and its independent verification remain valid historical certificates but are dimensionally superseded. This argument establishes failure for every \(n\ge9\); dimensions \(7\) and \(8\) are not decided by it.
