# All bad reversal-even Q6 coordinate-triple colorings are exactly two-mark templates

# Exact classification of bad reversal-even ternary labels on six directions

Let \(B\) contain six directions and let \(H(a,b,c)=H(c,b,a)\) be a binary label on ordered triples of distinct directions. A complete order \(p=(p_1,\ldots,p_6)\) has a four-window word \(H(p_1,p_2,p_3),\ldots,H(p_4,p_5,p_6)\).

**Theorem (exact finite classification).** If every complete six-direction order has at least two color changes, then, up to global color complementation, there is a two-element subset \(M\subset B\) with
\[
H(a,b,c)=\mathbf1_{\{b\notin M,\ (a\in M\text{ or }c\in M)\}}.
\]
Conversely, every such two-mark coloring and its complement has at least two changes in every complete order. There are exactly \(2\binom62=30\) bad reversal-even coordinate-triple colorings.

**Proof.** For any five distinct coordinates arranged cyclically, consider the five consecutive triple labels. If every ordered four-tuple had its two consecutive triple labels different, these five binary labels would alternate around an odd cycle, impossible. Hence some ordered four-tuple \((a,b,c,d)\) has equal consecutive labels. By relabeling and global complementation, normalize
\[
H(0,1,2)=H(1,2,3)=0.
\]
Reversal-evenness leaves 60 Boolean variables (the middle coordinate and an unordered pair of endpoints). A four-bit word with at least two changes belongs to exactly eight allowed patterns:
\[
0010,\ 0100,\ 0101,\ 0110,\ 1001,\ 1010,\ 1011,\ 1101.
\]
The 720 direction orders yield 360 distinct constraints, as reversing the full order reverses its word. Every constraint must have one of those eight words.

Use logically exact constraint propagation: given some known labels, filter each constraint's eight allowed words to those consistent with all known labels. Whenever the remaining allowed words agree at an unassigned position, assign that value. Repeat to closure. All deductions are forced in every valid completion.

From the normalized equal pair, propagation forces 20 of the 60 variables. Branch on \(H(4,3,5)\):
- Value 0 forces the remaining 40 variables and yields exactly the two-mark model \(M=\{1,2\}\).
- Value 1 forces 40 variables in total. Branch on \(H(2,4,5)\). Value 0 forces the remaining 20 and gives \(M=\{4,5\}\). Value 1 forces the remaining 20 and gives the global complement of the two-mark model \(M=\{0,3\}\).

This exhausts every normalized possibility, so after undoing symmetry all bad colorings are exactly the stated models. Conversely, check each of the 15 possible marked pairs and both global complements against all 360 distinct full-order constraints. All pass. The following **standard-library, integer-exact certificate** verifies the entire derivation, including the forced-domain counts and the 30 models:

~~~python
from itertools import permutations, combinations, product
V = tuple(range(6))
def key(a,b,c):
    return (min(a,c), b, max(a,c))
triples = {key(a,b,c) for a,b,c in permutations(V,3)}
paths = {
    min(t,t[::-1]) for p in permutations(V)
    for t in [tuple(key(*p[i:i+3]) for i in range(4))]
}
valid = [w for w in product((0,1),repeat=4)
         if sum(w[i]!=w[i+1] for i in range(3)) >= 2]

def force(A):
    A = dict(A)
    while True:
        nxt = {}
        for path in paths:
            options = [w for w in valid
                       if all(z not in A or A[z]==w[i]
                              for i,z in enumerate(path))]
            assert options
            for i,z in enumerate(path):
                if z not in A and all(w[i]==options[0][i]
                                      for w in options):
                    b = options[0][i]
                    if z in nxt: assert nxt[z]==b
                    nxt[z] = b
        if not nxt: return A
        A.update(nxt)

def two_mark(M, flip=0):
    return {key(a,b,c):
            int(b not in M and (a in M or c in M)) ^ flip
            for a,b,c in permutations(V,3)}

assert (len(triples),len(paths),len(valid))==(60,360,8)
initial=force({key(0,1,2):0,key(1,2,3):0})
assert len(initial)==20
u,v=key(4,3,5),key(2,4,5)
case0=force(initial|{u:0})
case1=force(initial|{u:1})
assert (len(case0),len(case1))==(60,40)
case10=force(case1|{v:0})
case11=force(case1|{v:1})
assert (len(case10),len(case11))==(60,60)
assert case0==two_mark({1,2})
assert case10==two_mark({4,5})
assert case11==two_mark({0,3},1)
for M in combinations(V,2):
    for flip in (0,1):
        H=two_mark(set(M),flip)
        assert all(sum(H[p[i]]!=H[p[i+1]]
                       for i in range(3))>=2 for p in paths)
~~~

This is a complete reproducible **finite/computer-assisted proof certificate**, with two Boolean branch decisions after normalization. It does not assume the classification from a heuristic solver.

**Scope.** This classifies position-independent reversal-even six-coordinate colorings. Arbitrary six-coordinate ordered-face colorings may depend on their three exterior fixed bits and remain outside the classification.
