# Two diagonal bad roots rigidify every Q5 ordered face and force exactly four square bad roots

# Rigidity of two diagonal bad roots in physical Q5

A root is *bad* when every full five-direction path starting there has an alternating three-window word 010 or 101. The physical ordered-three-face coloring is arbitrary; no oddness assumption is made.

**Theorem.** If two bad roots have Hamming distance two, then the coloring is unique up to global complementation, the other two corners of their coordinate square are also bad, and all other roots are good. Consequently an arbitrary physical Q5 coloring has exactly 0, 1, 2, or 4 bad roots. Two bad roots without others must be adjacent or antipodal; four bad roots form a square.

**Explicit classification.** Translate and relabel the two given bad roots to 0 and 3=e_0+e_1. Partition V={0,1,2,3,4} into A={0,1}, B={2,3,4}. For a physical face with ordered free triple t=(a,b,c), let P be its A/B membership pattern and let s be the parity of the fixed bits x_j(F) over j in B outside {a,b,c}. Define H(F,t) by this table (mod 2):

- P=AAB, BAA, or BBA: H=1+s.
- P=ABA or BBB: H=1.
- P=ABB: H=s.
- P=BAB: H=0.

Then the only possible colorings are H and 1+H. For a translated square with fixed B-address z, replace s by the parity of x_j(F)+z_j over exterior B directions.

**Proof that H has exactly the four bad square roots.** At a root whose B bits are all zero, a window has s equal to the parity of the B directions preceding that window. The ten possible five-letter A/B travel patterns produce the following complete three-color words:

AABBB:101; ABABB:101; ABBAB:010; ABBBA:010; BAABB:101; BABAB:010; BABBA:010; BBAAB:101; BBABA:101; BBBAA:101.

These are independent of initial A bits. For nonzero B-start bits, symmetry among the three B coordinates reduces to three cases. For representative root masks 4, 12, 28 (B Hamming weights 1, 2, 3), the direction orders 01324, 01234, 01234 produce respectively the good words 001, 001, 111. Thus the four square corners are exactly the bad roots.

**Proof of uniqueness by an exact finite connectivity certificate.** Consider the graph on all 240 ordered physical three-face states (t,z), where t is an ordered triple and z is the five-bit exterior mask, zero on t. For each root r in {0,3} and every permutation p of V, join the first and second physical three-windows and join the second and third windows of the rooted p-geodesic. On every graph edge a bad-root coloring has opposite binary colors. This graph is connected; here is a self-contained verification of its complete vertex set and connectivity:

```python
from itertools import permutations
V = tuple(range(5))
mask = lambda a: sum(1 << j for j in a)
states = {(t,z) for t in permutations(V,3)
          for z in range(32) if (z & mask(t)) == 0}
adj = {v:set() for v in states}
for root in (0,3):
    for p in permutations(V):
        w, prefix = [], 0
        for j in range(3):
            t = p[j:j+3]
            w.append((t, (root ^ prefix) & (31 ^ mask(t))))
            prefix ^= 1 << p[j]
        for u,v in zip(w,w[1:]):
            adj[u].add(v)
            adj[v].add(u)
start = next(iter(states))
seen, todo = {start}, [start]
while todo:
    for v in adj[todo.pop()]:
        if v not in seen:
            seen.add(v)
            todo.append(v)
assert len(states) == len(seen) == 240
```

For two colorings satisfying the bad-root constraints, their pointwise XOR is constant along every graph edge and therefore on all 240 vertices. The displayed H satisfies the constraints, so all solutions are H and its complement. The certificate uses only 240 states and two sets of 120 literal five-orders.

**Bad-root cardinalities.** Existing physical-Q5 odd-cycle certificates exclude pairs of bad roots at distance 3 or 4, and exclude five bad roots. A bad antipodal pair at distance 5 excludes a third bad root. Among any three distinct cube vertices with pairwise distances at most 2 there is a distance-two pair (the cube graph is triangle-free). Such a pair forces all four corners of its square to be bad by the theorem, and the five-bad-root exclusion rules out any additional root. Thus cardinality three is impossible and the classification follows.

**Reversal-evenness of maximally bad fibers.** The canonical H satisfies H(bar F, reverse t)=H(F,t) under *five-dimensional* face antipodality: reversing AAB/BAA complements two exterior B bits, reversing ABB/BBA complements one and exchanges constants 0/1, and the other pattern types have constant values. This describes the exact color geometry of maximally bad induced five-faces. A physical five-face inside a larger NORI cube need not itself satisfy oddness.

This is a proved finite structural theorem, sharpening the existing 7/8 good-root estimate; it does not settle the all-dimensional grand conjecture.
