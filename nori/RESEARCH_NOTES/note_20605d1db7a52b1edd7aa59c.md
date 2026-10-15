# Seven-vertex reversal-odd boundary tournament with no one-switch Hamilton path from a prescribed root

- Stable ID: note_20605d1db7a52b1edd7aa59c
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiv_type_a_rook_gallery_topology
- Labels: boundary-tournaments, root-selection, finite-counterexample, coxeter-cosets
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_2
- Updated session: session_nori_r7547_2
- Disposition: none
- Successor: none

## Related references

- subsection:coxeter_element_cosets_and_a_unified_one_switch_conjecture

## Research note

**Computational counterexample (root selection is necessary for boundary Hamilton tight paths).** There exists an ordinary reversal-odd boundary 3-tournament on seven vertices such that every Hamilton tight path beginning at vertex \(0\) has at least two switches.

**Complete six-mask specification.** Let \(V=\{0,1,2,3,4,5,6\}\). At each middle vertex \(h=1,\ldots,6\), list the other six vertices in increasing order \(a_0<\cdots<a_5\), and enumerate the fifteen unordered outer pairs \((a_i,a_j)\), \(i<j\), lexicographically. Define
\[
b(a_i,h,a_j)=\text{bit}_{k}(M_h)\quad(i<j),
\qquad b(a_j,h,a_i)=1-b(a_i,h,a_j),
\]
where \(k\in\{0,\ldots,14\}\) is the zero-based index of the pair and
\[
(M_1,M_2,M_3,M_4,M_5,M_6)
=(\mathtt{3FF8},\mathtt{0FCC},\mathtt{6FD4},\mathtt{0067},\mathtt{4003},\mathtt{0245}).
\]
At \(h=0\), define \(b(a,0,c)=0\) for \(a<c\), and use reversal oddness for \(a>c\). This specifies all ordered triples and automatically satisfies \(b(c,h,a)=1-b(a,h,c)\).

**Finite exhaustive certificate.** Enumerating the \(6!=720\) rooted Hamilton orders \(p=(0,p_1,\ldots,p_6)\) gives the following switch-count distribution for the five-bit consecutive-triple word:
\[
\begin{array}{c|ccccc}
\text{switches}&0&1&2&3&4\\ \hline
\text{number of rooted Hamilton orders}&0&0&144&360&216.
\end{array}
\]
The following standalone Python 3 program reads only the six constants above and checks every order:

\`\`\`python
from itertools import combinations, permutations

M = [0x3FF8, 0x0FCC, 0x6FD4, 0x0067, 0x4003, 0x0245]
b = {}

for h in range(1, 7):
    others = [a for a in range(7) if a != h]
    for k, (a, c) in enumerate(combinations(others, 2)):
        bit = (M[h - 1] >> k) & 1
        b[a, h, c] = bit
        b[c, h, a] = 1 - bit

histogram = [0] * 5
for tail in permutations(range(1, 7)):
    p = (0,) + tail
    word = [b[p[i], p[i+1], p[i+2]] for i in range(5)]
    switches = sum(word[i] != word[i+1] for i in range(4))
    histogram[switches] += 1

assert histogram == [0, 0, 144, 360, 216]
\`\`\`

This counterexample does not contradict the unrooted reversal-odd boundary conjecture: it excludes only the specified initial vertex. It complements the fixed-root obstruction for NORI1, showing that a common one-switch selector must preserve freedom of the initial vertex in the type-A Hamilton setting as well as freedom of the cube root in type B.

**Status.** Finite computationally verified obstruction, specified in full by the six masks and an exhaustive 720-order checker. No general family or symbolic minimality assertion is claimed.
