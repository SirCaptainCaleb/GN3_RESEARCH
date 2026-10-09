# Exact 32-branch certificate excludes uniform sensitivity in bad reversal-even Q6; affine one-flipper NORI closes

# No uniformly sensitive ordered face in a bad reversal-even six-cube

Let \(h\) be a binary coloring of ordered three-dimensional faces of \(Q_6\) satisfying
\[
h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
Call an ordered free triple uniformly sensitive to an exterior coordinate \(d\) when complementing the fixed \(d\)-bit complements its color for every assignment of the other two exterior coordinates.

**Theorem (uniform-sensitivity exclusion; finite exact certificate).** If some ordered face triple is uniformly sensitive in an exterior coordinate, there is a full six-direction geodesic with at most one color change.

**Proof.** Suppose all full geodesics have at least two changes. Relabel the coordinates \(0,1,2,3,4,5\), so the uniformly sensitive triple is \((0,1,2)\) and its distinguished exterior coordinate is \(3\). Writing \(x_3,x_4,x_5\) for the exterior bits, we have
\[
h(F,(0,1,2))=x_3\oplus g(x_4,x_5),
\tag{1}
\]
where \(g:\mathbb F_2^2\to\mathbb F_2\) is an *arbitrary* binary function, with 16 possibilities, allowing nonlinear dependence.

By the preceding proved **uniform complementary-face collapse theorem**, Item \`nori_uniform_exterior_sensitivity_even_q6_collapse_20261008\`, there is \(K\in\mathbb F_2\) such that all ordered faces of each of the six triples
\[
(1,2,3),(1,0,3),(3,4,5),(3,5,4),(5,4,3),(4,5,3)
\]
have constant color \(K\), independently of the exterior bits; and all faces of the four triples
\[
(2,3,4),(2,3,5),(0,3,4),(0,3,5)
\]
have constant color \(1\oplus K\). Reversal-even antipodality also fixes the colors of their antipodal reversed partners. These ten classes are forced, so the only remaining apparent freedom within (1) is the 16 possible truth tables \(g\) and two possible bits \(K\).

An **exact unit-propagation certificate** eliminates all \(16\cdot2=32\) cases. Treat each ordered face and its antipodal-reversal mate as one Boolean variable. There are
\[
\frac{\binom63\cdot 6\cdot 2^3}{2}=480
\]
variables. Since reversal of a complete six-geodesic induces an equivalent four-window constraint, only \(360\cdot64=23040\) full geodesic constraints need be checked. Each such word must belong to the eight four-bit patterns with at least two changes. Whenever all admissible patterns consistent with known face colors agree in some unassigned window, that window value is logically forced. Repeated implication alone, with no search over unassigned face variables, produces a contradiction in every one of the 32 cases.

Here is a complete reproducible certificate using only the Python standard library. Bit masks encode exterior-one directions, and the canonical \`face\` function identifies precisely the antipodal-reversal pairs. The assertions establish the variable and constraint counts, the correct forced seed sizes, and contradiction in every branch.

~~~python
from itertools import permutations, product
from collections import deque
V = tuple(range(6))

def face(T, exterior_ones):
    E = tuple(i for i in V if i not in T)
    first = (T, tuple((exterior_ones >> i) & 1 for i in E))
    other = (T[::-1], tuple(1 - ((exterior_ones >> i) & 1) for i in E))
    return min(first, other)

ids, paths = {}, set()
for p in permutations(V):
    if p > p[::-1]:
        continue
    free = [sum(1 << z for z in p[i:i+3]) for i in range(4)]
    prefix = [sum(1 << z for z in p[:i]) for i in range(4)]
    for x in range(64):
        row = []
        for i in range(4):
            S = ((x ^ prefix[i]) & ~free[i]) & 63
            name = face(p[i:i+3], S)
            if name not in ids:
                ids[name] = len(ids)
            row.append(ids[name])
        paths.add(tuple(row))
paths = tuple(sorted(paths))
touches = [[] for _ in ids]
for index, path in enumerate(paths):
    for vertex in path:
        touches[vertex].append(index)
bad = tuple(w for w in product((0, 1), repeat=4)
            if sum(w[i] != w[i+1] for i in range(3)) >= 2)
assert (len(ids), len(paths), len(bad)) == (480, 23040, 8)

def impossible(seed):
    known = dict(seed)
    queue = deque(i for vertex in known for i in touches[vertex])
    while queue:
        path = paths[queue.popleft()]
        options = [w for w in bad
                   if all(v not in known or known[v] == w[j]
                          for j, v in enumerate(path))]
        if not options:
            return True
        for j, vertex in enumerate(path):
            if vertex not in known and all(w[j] == options[0][j]
                                           for w in options):
                known[vertex] = options[0][j]
                queue.extend(touches[vertex])
    return False

constant_K = [(1,2,3), (1,0,3), (3,4,5),
              (3,5,4), (5,4,3), (4,5,3)]
constant_notK = [(2,3,4), (2,3,5), (0,3,4), (0,3,5)]

def seed(g, K):
    known = {}
    def assign(T, mask, value):
        label = ids[face(T, mask)]
        assert label not in known or known[label] == value
        known[label] = value
    for T, value in ([(T, K) for T in constant_K] +
                     [(T, K ^ 1) for T in constant_notK]):
        E = [i for i in V if i not in T]
        for bits in range(8):
            mask = sum(((bits >> j) & 1) << E[j] for j in range(3))
            assign(T, mask, value)
    for bits in range(8):
        mask = sum(((bits >> j) & 1) << (3+j) for j in range(3))
        value = (bits & 1) ^ ((g >> ((bits >> 1) & 3)) & 1)
        assign((0,1,2), mask, value)
    assert len(known) == 72
    return known

assert all(impossible(seed(g, K))
           for g in range(16) for K in range(2))
~~~

To see the logical validity of the propagation: any hypothetical globally bad coloring supplies one binary value to every canonical face variable and must satisfy *all* 23040 four-window constraints. Restricting each path's eight bad patterns to those consistent with currently known values cannot remove its true pattern. A color common to all remaining patterns is therefore forced, and an empty set of patterns is a rigorous contradiction. The certificate makes only forced assignments, so its exhaustive 32-case contradiction proves the theorem. \(\square\)

**Corollary 1 (classification of bad affine reversal-even Q6 colorings).** If a reversal-even ordered-three-face coloring of \(Q_6\) is Boolean affine in the fixed exterior bits of each ordered triple and has no one-change six-geodesic, then it is position-independent and is a two-mark template, up to global complementation and relabeling.

**Proof.** If any exterior linear coefficient is nonzero, its Boolean derivative is identically one, contradicting the theorem under global failure. Thus a globally bad affine coloring must be position-independent. The previously established exact classification of bad reversal-even coordinate-triple colorings then forces the two-mark templates; these templates are indeed globally bad. Thus every bad affine reversal-even \(Q_6\) coloring is a coordinate-only two-mark template, up to complementation and relabeling. \(\square\)

**Corollary 2 (one-flipper affine-residual NORI closure).** Every antipodal-reversal-odd \(Q_7\) coloring with a universal exterior flipper \(g\) whose induced reversal-even six-dimensional residual is Boolean affine in its fixed exterior bits has a full one-change antipodal geodesic. Indeed, if that residual has a good six-geodesic, exact flipper elimination lifts it. Otherwise it is coordinate-only by the theorem and therefore one of the classified two-mark templates; the established sparse two-mark seven-dimensional forcing theorem supplies the full good path, with all \(g\)-containing ordered faces arbitrary.

**Corollary 3 (all dimensions with six nonflipper directions).** If a NORI coloring has exactly six coordinates outside a set of universal exterior flippers, and the induced six-dimensional coloring is Boolean affine in its fixed exterior bits, then NORI holds in every dimension. For an even number of flippers, the induced six-cube is antipodal-reversal odd, so the established six-dimensional NORI theorem and flipper elimination suffice. For an odd number, retain one flipper to form the preceding seven-dimensional affine-residual class, and eliminate the remaining even number of flippers.

**Scope and remaining problem.** Uniform sensitivity is now completely eliminated from any globally bad reversal-even six-dimensional residual; arbitrary *nonuniform* Boolean sensitivity, including quadratic and cubic dependence on exterior bits, is still possible. The result closes the entire affine six-residual lifting family, but not the unrestricted one-flipper \(Q_7\) case or the full NORI conjecture.
