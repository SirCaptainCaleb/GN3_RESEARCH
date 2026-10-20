# Balanced six-cube: nonoptimal local root plateau for complementary monochromatic arms

- Stable ID: note_nori_q6_rooted_bichromatic_arm_plateau_20261019_r11913
- Author: unspecified; session provenance retained
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: NORI1, root-transport, balanced-cube, computational-certificate, method-obstruction, tensor-amplification, monochromatic-arms
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_2
- Updated session: session_nori_r11913_2
- Disposition: none
- Successor: none

## Related references

- note:note_a916d6521b5fc62715b8c654

## Research note

# Nonoptimal root-local plateaus for complementary monochromatic arms

Let \(n=2m\), and let \(c\) be a vertex-balanced antipodally odd coloring of the undirected edges of \(Q_n\). For \(\epsilon\in\{0,1\}\), let \(\mathcal F_\epsilon(x)\) consist of direction sets admitting an \(\epsilon\)-monochromatic geodesic from \(x\), including the empty set. Put
\[
J_c(x)=\max\{|S|+|T|:S\in\mathcal F_0(x),\ T\in\mathcal F_1(x),\ S\cap T=\varnothing\}.
\]
If J_c(x)=n, translating the reversed blue arm antipodally and concatenating it with the red arm gives a monochromatic full antipodal geodesic. If J_c(x)=n-1, inserting the unique unused direction between the two red arms yields a full geodesic with at most one exceptional-color edge. When that edge is internal, the color word can have two changes. The universal internal one-defect repair is OPEN and is equivalent to unrestricted NORI1 under the established normalization; J_c(x)>=n-1 alone is NOT a proven forcing criterion. The present local-plateau theorem and its independent verifier remain valid.

**Proposition (nonoptimal local plateau).** There is a legal vertex-balanced coloring \(c\) of \(Q_6\) such that
\[
J_c(0)=J_c(e_i)=5\quad(0\le i<6),
\qquad \max_x J_c(x)=6.
\]
The distribution is 22 roots with \(J=5\) and 42 roots with \(J=6\). In particular, the rule “every root with \(J(x)<n\) has a neighboring root with greater \(J\)” is false.

**Certificate.** For each direction \(i\), remove bit \(i\) from the six-bit vertex integer \(x\) to form \(\rho_i(x)=(x\bmod2^i)+2^i\lfloor x/2^{i+1}\rfloor\). Assign color
\[
c_i(x)=(T_i\gg\rho_i(x))\ \&\ 1
\]
with the following six 32-bit masks, in order:
\[
(T_0,T_1,T_2,T_3,T_4,T_5)=
(\texttt{a8ab2aea},\texttt{5faf0a05},\texttt{ff50f500},
\texttt{3b317323},\texttt{2200ffbb},\texttt{8004dffe}).
\]
Removal of the traversed direction bit makes the edge coloring undirected. Direct inspection verifies \(c_i(x)+c_i(\bar x)=1\) and \(\sum_i c_i(x)=3\) for all \(x,i\). The red full antipodal geodesic with root \(3\) and order \((3,1,2,5,0,4)\) verifies success independently of the \(J\)-enumeration.

The following self-contained Python certificate computes all rooted support families and independently verifies the claims:
\`\`\`python
from collections import Counter

T = (0xa8ab2aea, 0x5faf0a05, 0xff50f500,
     0x3b317323, 0x2200ffbb, 0x8004dffe)
n = 6

def c(x, i):
    r = (x & ((1 << i) - 1)) | ((x >> (i + 1)) << i)
    return (T[i] >> r) & 1

def F(x, color):
    levels = [{0}]
    for k in range(n):
        nxt = set()
        for S in levels[-1]:
            for i in range(n):
                if not (S & (1 << i)) and c(x ^ S, i) == color:
                    nxt.add(S | (1 << i))
        levels.append(nxt)
    return set().union(*levels)

def J(x):
    A, B = F(x, 0), F(x, 1)
    return max((S | U).bit_count()
               for S in A for U in B if S & U == 0)

for x in range(64):
    assert sum(c(x, i) for i in range(n)) == 3
    for i in range(n):
        assert c(x, i) == c(x ^ (1 << i), i)
        assert c(x, i) != c(x ^ 63, i)

values = [J(x) for x in range(64)]
assert values[0] == 5
assert all(values[1 << i] == 5 for i in range(n))
assert Counter(values) == {5: 22, 6: 42}
v = 3
for i in (3, 1, 2, 5, 0, 4):
    assert c(v, i) == 0
    v ^= 1 << i
assert v == (3 ^ 63)
\`\`\`

**Tensor amplification.** For two legal colorings on disjoint direction blocks, every monochromatic direction-simple path projects to one in each block, and any two chosen block paths may be concatenated. Therefore
\[
\mathcal F_\epsilon^{c\boxplus d}(x,y)
=\mathcal F_\epsilon^c(x)\times\mathcal F_\epsilon^d(y),
\qquad J_{c\boxplus d}(x,y)=J_c(x)+J_d(y).
\]
The \(k\)-fold product of this six-cube has \(J(0)=5k\), with every neighboring root also having value \(5k\), while some root has value \(6k\). Thus the failed neighbor-ascent rule can have a deficit linear in the dimension; even a universal prescribed-root \(n-o(n)\) near-cover estimate is false.

**Scope.** This refutes a local root-improvement hypothesis for witnessed red/blue support packing and does not refute existence of a favorable root or unrestricted NORI1. Any root-transport forcing proof must permit moves beyond strict one-edge ascent of this potential.
