# A legal Q15 counterexample to unrooted NORI via a three-class reversal-even word obstruction

# A legal Q15 counterexample to the unrooted NORI grand conjecture

## Main theorem

**Theorem.** There exists a binary coloring of the physical ordered three-faces of \(Q_{15}\) satisfying
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w))
\]
for every ordered three-face, for which **every** full antipodal geodesic has at least two changes among its thirteen consecutive ordered-three-face colors. Consequently, the unrooted NORI grand conjecture, as stated for all dimensions, is false.

The construction is explicit except for an arbitrary fixed linear order on fourteen distinguished coordinates. Its only finite verification has 252,252 ternary words and also admits an exact 1,427-state dynamic-programming evaluation.

## 1. Reversal-even three-letter obstruction

Let \(\Sigma=\{0,1,2\}\), and set
\[
h(a,b,c)=\begin{cases}
1,& b>\min\{a,c\}\ \text{or }(a,b,c)=(0,0,0),\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]
In particular, \(h(a,b,c)=h(c,b,a)\).

**Lemma (four-switch ternary obstruction).** Every word \(q=q_1\cdots q_{14}\) with precisely four zeros, five ones, and five twos has at least four switches in its consecutive-triple word
\[
H(q)=(h(q_1,q_2,q_3),\ldots,h(q_{12},q_{13},q_{14})).
\tag{2}
\]
The bound is attained.

**Proof (exhaustive finite recurrence with reproducible certificate).** For a partial word, retain its three letter counts, last two letters, and last defined triple color. Appending \(w\) incurs one switch exactly when the old and newly defined triple colors differ. Thus the minimum number of switches to complete a prefix obeys the following backward recurrence. The sentinel 3 denotes an absent letter and the sentinel 2 denotes an absent triple color; neither is a letter of the word's alphabet in these states. This self-contained Python 3 implementation evaluates that finite recurrence exactly:

\`\`\`python
from functools import lru_cache

target = (4, 5, 5)

def h(a, b, c):
    return int(b > min(a, c) or (a == b == c == 0))

@lru_cache(None)
def minimum(counts, a, b, last):
    if counts == target:
        return 0
    candidates = []
    for c in range(3):
        if counts[c] == target[c]:
            continue
        current = h(a, b, c) if a != 3 else 2
        increment = int(last != 2 and current != 2 and last != current)
        updated = list(counts)
        updated[c] += 1
        candidates.append(
            increment + minimum(tuple(updated), b, c, current)
        )
    return min(candidates)

assert minimum((0, 0, 0), 3, 3, 2) == 4
\`\`\`

All legal completions are considered, because at each state the recurrence branches on each symbol whose multiplicity has not been exhausted. The terminal value is zero and the recursion strictly increases total multiplicity; induction on the number of letters remaining proves exactness. An independent direct enumeration of all \(14!/(4!5!5!)=252252\) words gives the histogram of switch counts
\[
\begin{array}{c|rrrrrrrr}
\text{switches}&4&5&6&7&8&9&10&11\\
\hline
\text{number of words}&314&3724&19802&51232&76938&64924&29730&5588
\end{array}
\]
with zero words of 0, 1, 2, or 3 switches. As one explicit equality witness, the word
\(00122001221112\) has triple-color word \(011100111000\), containing exactly four switches. \(\square\)

## 2. Explicit physical-face coloring

Partition a set \(D\) of fourteen distinct coordinate directions as
\[
D=D_0\sqcup D_1\sqcup D_2,\qquad
(|D_0|,|D_1|,|D_2|)=(4,5,5),
\]
and let \(\tau(d)=i\) for \(d\in D_i\). Adjoin a fifteenth direction, denoted \(s\), and fix any total ordering \(<\) of the fourteen directions in \(D\).

For a physical three-face \(F\), let \(z_s(F)\) be its fixed \(s\)-coordinate whenever \(s\) is not one of its three varying directions. Define the bit \(c(F,(u,v,w))\) as follows.

1. If \(u,v,w\in D\), put
\[
c(F,(u,v,w))=
z_s(F)\ \oplus\ h(\tau(u),\tau(v),\tau(w)).
\tag{3}
\]
2. If \(s\) is in the ordered triple, put
\[
c(F,(s,u,v))=1,\quad
c(F,(u,v,s))=0,\quad
c(F,(u,s,v))=\mathbf 1_{\{u>v\}} .
\tag{4}
\]
Here \(u,v\in D\) are distinct and the inequality is in the fixed total ordering.

These definitions depend only on the physical face and its ordered varying directions; in particular, they are independent of the traversing corner.

**Lemma (legality).** The coloring (3)--(4) is antipodal-reversal-odd.

**Proof.** If \(s\) is outside the ordered triple, the fixed \(s\)-coordinate flips when \(F\) is replaced by \(\bar F\), while \(h\) is reversal-even by (1); thus (3) complements. If \(s\) is first or last, reversal interchanges the first two cases of (4), whose values are 1 and 0. If \(s\) is middle, reversal interchanges the two distinct outside directions, so \(\mathbf1_{\{u>v\}}+\mathbf1_{\{v>u\}}=1\). These exhaust all ordered faces. \(\square\)

## 3. Every full antipodal geodesic has at least two changes

Fix an arbitrary root \(x\in\{0,1\}^{15}\) and any permutation \(p\) of the fifteen directions; it specifies an antipodal geodesic. Let \(k\in\{1,\ldots,15\}\) be the position of \(s\) in \(p\), and let \(q=(q_1,\ldots,q_{14})\) be the ordered list obtained by deleting \(s\) from \(p\).

Define \(H_i=h(\tau(q_i),\tau(q_{i+1}),\tau(q_{i+2}))\) for \(1\le i\le12\). By the four-switch lemma, \(H_1,\ldots,H_{12}\) has at least four switches.

Of the thirteen length-three windows in \(p\), the windows avoiding \(s\) appear in two contiguous segments. The first segment corresponds, in order, to
\[
H_1,\ldots,H_{k-3},
\]
and the second to
\[
H_k,\ldots,H_{12},
\]
where out-of-range intervals are empty. In the first segment, all the physical colors are \(H_i\oplus x_s\); in the second, they are \(H_i\oplus (1-x_s)\), because the \(s\)-coordinate flips once along the geodesic, when the direction \(s\) is traversed. Thus **every switch strictly inside either surviving segment is retained**.

Passing from the original twelve-term word \(H\) to those two segments deletes at most the two terms \(H_{k-2},H_{k-1}\), and therefore removes at most three of its adjacent comparisons. Consequently, for \(4\le k\le12\) the two surviving segments together retain at least \(4-3=1\) switch. In this range all three \(s\)-containing windows occur; by (4), their color word is
\[
0,\quad \varepsilon,\quad1,\qquad \varepsilon\in\{0,1\},
\]
which has an additional switch. The full geodesic therefore has at least two switches.

If \(k\notin\{4,\ldots,12\}\), then deleting the terms at positions \(k-2,k-1\) removes at most two actual comparisons of \(H\): the two deleted entries touch an end or are partly out of range. Hence the surviving segments already retain at least \(4-2=2\) switches, independently of the colors of any \(s\)-containing windows.

In every case, the full antipodal geodesic has at least two changes. The root and permutation were arbitrary, establishing the theorem. \(\square\)

## 4. Independent checks, scope, and consequence

A separate direct enumeration evaluates all \(252252\) three-class direction words, fifteen insertion positions for \(s\), both possible initial \(s\)-coordinate bits, and **both** possible middle-\(s\) window colors. Across \(252252\cdot15\cdot2\cdot2=15135120\) resulting color words there are zero with zero or one switch (indeed, the minimum is three in this finite enumeration). This second check allows an adversarial choice of the middle-\(s\) bit and so is stronger than the face rule (4) on the tested class words. A further independent direct physical-face implementation checked random antipodal ordered-face pairings and randomly rooted full geodesics. All agree with the mathematical proof above.

The construction refutes the **unrooted, unrestricted, antipodal-reversal-odd, physical ordered-three-face** grand conjecture already in dimension fifteen. It preserves the established Q5 and Q6 positive theorems; it does not claim dimension fifteen is minimal. The ternary finite lemma is the sole computer-assisted step, with complete recursion and direct enumeration cross-check given above.

The main conceptual point is that a reversal-even local triple word obstructed by four switches can be inserted across one distinguished exterior coordinate: at most three of its switches are lost, while the distinguished triple windows contribute the final forcing switch. This yields an actual physical-face counterexample rather than a prescribed-root obstruction.

## Sharpening: the exact minimum is three switches in Q15

**Theorem (sharp switch certificate).** For the physical coloring (3)--(4), *every* full antipodal geodesic has **at least three**, and some full antipodal geodesic has **exactly three**, consecutive ordered-three-face color changes. Thus this construction already refutes the proposed universal two-switch NORI3 bound in ambient dimension fifteen. The original two-switch lower bound above remains valid but is superseded by this strengthening.

**Proof and smaller complete certificate.** Write \(\sigma\) for the change count. The proved four-switch ordinary-word lemma gives \(\sigma(H)\ge4\), and the sentinel insertion inequality gives \(\sigma(C)\ge\sigma(H)-2\) for every sentinel position, initial sentinel bit \(z\), and arbitrary middle-sentinel bit \(\varepsilon\). Consequently, **only** ordinary class words with \(\sigma(H)=4\) could possibly produce \(\sigma(C)\le2\). There are exactly 314 such words among the \(14!/(4!5!5!)=252252\) ordinary class words, by the independently recorded histogram in Section 1.

The following standalone Python 3 certificate enumerates these 314 critical words, all fifteen sentinel slots and both choices each of \(z,\varepsilon\). It checks the stronger bound \(\sigma(C)\ge3\) for all \(314\cdot15\cdot4=18840\) cases:

~~~python
from itertools import combinations

def h(a,b,c):
    return int((a==b==c==0) or b>min(a,c))

def sw(bits):
    return sum(x != y for x,y in zip(bits,bits[1:]))

critical=0
checked=0
hist={}
for zeros in combinations(range(14),4):
    remain=[i for i in range(14) if i not in zeros]
    for ones in combinations(remain,5):
        q=[2]*14
        for i in zeros: q[i]=0
        for i in ones: q[i]=1
        H=[h(*q[i:i+3]) for i in range(12)]
        assert sw(H)>=4
        if sw(H)!=4: continue
        critical+=1
        for k in range(15):
            p=q[:k]+[3]+q[k:]
            for z in (0,1):
                for eps in (0,1):
                    C=[]
                    for j in range(13):
                        a,b,c=p[j:j+3]
                        if a==3: v=1
                        elif c==3: v=0
                        elif b==3: v=eps
                        else: v=z^(j>k)^h(a,b,c)
                        C.append(v)
                    t=sw(C)
                    assert t>=3
                    hist[t]=hist.get(t,0)+1
                    checked+=1

assert (critical,checked)==(314,18840)
assert hist=={3:1592,4:2632,5:13024,6:1136,7:456}
~~~

The bit \(\varepsilon\) is allowed adversarially, so this covers every actual choice induced by the strict order of the two ordinary directions adjacent to \(s\). In fact, equality is realized: an abstract direction-class order
\[
(0,s,0,1,2,2,0,0,1,2,2,1,1,1,2)
\]
with starting sentinel bit \(z=1\) and middle-sentinel bit \(\varepsilon=1\) has physical color word
\[
1111100111000
\]
and exactly three changes. Choose the first of the two adjacent class-0 directions greater than the second in the prescribed strict direction order to realize \(\varepsilon=1\); all directions are distinct and all classes retain their prescribed multiplicities. Other initial vertex bits are arbitrary. Therefore the actual physical minimum is **exactly three**. \(\square\)

**Relation to amplification.** The later multilevel construction forces four changes already on \(Q_{37}\) and unboundedly many as \(n\) grows. The present sharp \(Q_{15}\) result supplies a substantially smaller explicit violation of the conjectural NORI3 two-switch budget. No dimension-minimality claim is made.
