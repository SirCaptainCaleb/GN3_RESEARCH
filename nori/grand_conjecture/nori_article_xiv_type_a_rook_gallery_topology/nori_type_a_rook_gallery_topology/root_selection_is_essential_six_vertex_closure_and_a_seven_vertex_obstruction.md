# Root selection is essential: six-vertex closure and a seven-vertex obstruction

# Root selection: six-vertex rooted closure and seven-vertex obstruction

Let \(b(a,h,c)\in\mathbb F_2\) be an arbitrary coloring of pairwise distinct ordered triples satisfying \(b(c,h,a)=1-b(a,h,c)\). A Hamilton tight path rooted at \(a\) is a permutation of all original vertices beginning with \(a\).

**Theorem 1 (computer-assisted six-vertex closure).** On six vertices, every such coloring has a Hamilton tight path starting at any prescribed vertex whose four triple bits have at most one switch.

*Finite exhaustive proof.* Relabel the root as \(0\). There are 60 reversal pairs of triples, represented by tuples \((a,h,c)\) with \(a<c\). There are \(5!=120\) Hamilton orderings beginning at \(0\). To deny the conclusion, every one of their four-bit words must avoid the eight words with at most one switch. Each forbidden favorable word gives a clause requiring one of its four entries to differ from the specified entry. This yields 960 clauses on 60 Boolean variables. Global complementation preserves the hypotheses and switch counts, so fix \(b(0,1,2)=0\).

Here is a standalone exhaustive Boolean verifier. It uses unit propagation followed by complete binary branching. Every branch is considered.

\`\`\`python
from itertools import permutations, product
V = range(6)
reps = sorted(t for t in permutations(V,3) if t[0]<t[2])
idx = {t:i for i,t in enumerate(reps)}
clauses = []
for tail in permutations(range(1,6)):
    p = (0,)+tail
    triples = [p[j:j+3] for j in range(4)]
    for w in product((0,1),repeat=4):
        if sum(w[j]!=w[j+1] for j in range(3))>1:
            continue
        C = []
        for t,v in zip(triples,w):
            flip = t[0]>t[2]
            rep = t[::-1] if flip else t
            C.append((idx[rep],1-(v^flip)))
        clauses.append(C)
calls = 0
def sat(a):
    global calls
    calls += 1
    while True:
        changed = False
        for C in clauses:
            if any(a[i]==v for i,v in C): continue
            free = [(i,v) for i,v in C if a[i]<0]
            if not free: return False
            if len(free)==1:
                i,v = free[0]
                a[i] = v
                changed = True
        if not changed: break
    weights = [0.0]*len(a)
    for C in clauses:
        if any(a[i]==v for i,v in C): continue
        free = [i for i,_ in C if a[i]<0]
        for i in free: weights[i] += 1/(len(free)**2)
    if max(weights)==0: return True
    i = weights.index(max(weights))
    for v in (0,1):
        b = a.copy()
        b[i] = v
        if sat(b): return True
    return False
a = [-1]*len(reps)
a[idx[(0,1,2)]] = 0
assert len(reps)==60 and len(clauses)==960
assert not sat(a)
print("UNSAT",calls)  # UNSAT 8085
\`\`\`

The verifier explores 8085 recursive nodes and establishes infeasibility. An independently coded binary integer feasibility model with XOR constraints also reports infeasibility. Thus no counterexample exists for root \(0\), and relabeling proves the theorem for any root. \(\square\)

**Corollary.** In every reversal-odd boundary tournament on at least six vertices, each specified root begins some vertex-simple six-vertex tight path with at most one switch. Choose any six vertices containing the root and restrict the coloring.

**Theorem 2 (seven-vertex rooted obstruction).** There is a reversal-odd boundary 3-tournament on \(V=\{0,\ldots,6\}\) such that every Hamilton ordering beginning at \(0\) has at least two switches, although some Hamilton ordering has zero switches.

*Explicit construction and proof.* List lexicographically all 105 triples \((a,h,c)\) of distinct vertices with \(a<c\), indexed \(j=0,\ldots,104\). Set
\[
H=\mathtt{0x18651ceb71780f8fd20583f5729}.
\]
For the \(j\)-th listed triple, set \(b(a,h,c)\) to bit \(j\) of \(H\), counting from the least significant bit; set \(b(c,h,a)=1-b(a,h,c)\). The following independent short verifier checks every rooted and unrestricted Hamilton ordering:

\`\`\`python
from itertools import permutations
V = range(7)
rep = sorted((a,h,c) for a,h,c in permutations(V,3)
             if a<c)
index = {t:i for i,t in enumerate(rep)}
H = int("18651ceb71780f8fd20583f5729",16)
def bit(a,h,c):
    if a<c: return (H>>index[(a,h,c)])&1
    return 1-bit(c,h,a)
def switches(p):
    w = [bit(*p[i:i+3]) for i in range(5)]
    return sum(x!=y for x,y in zip(w,w[1:]))
assert len(rep)==105
assert min(switches((0,)+p)
           for p in permutations(range(1,7)))==2
assert min(switches(p) for p in permutations(V))==0
\`\`\`

Indeed, \((1,2,4,0,6,5,3)\) is a monochromatic Hamilton ordering with word \((0,0,0,0,0)\). The rooted ordering \((0,1,2,3,5,4,6)\) has word \((1,0,1,1,1)\), attaining the rooted minimum of two changes. \(\square\)

**Consequence for the unified conjecture.** The starting vertex of the boundary Hamilton path must be free to vary. This parallels the rooted-geodesic obstruction in NORI1, even though the two root parameters arise from different combinatorial data. The computer-assisted six-vertex theorem is suitable for replacement by an analytic proof, while the seven-vertex obstruction is specified by a reproducible finite certificate.
