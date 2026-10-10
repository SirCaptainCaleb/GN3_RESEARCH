# Explicit Q7 odd face coloring blocks every good full path with designated direction in slot 3 or 5

# Explicit unrestricted physical Q7 obstruction to fixed-sentinel third-slot extraction

**Computer-verified counterexample.** There exists an antipodally reversal-odd coloring of ALL physical ordered three-faces of Q7 and a designated direction g such that EVERY full antipodal seven-direction geodesic whose third direction is g has at least two switches in its five ordered-three-face colors. By reversing a direction order from the same root and applying the antipodal-reversal law, the same statement holds with g in the fifth slot. This refutes the universal fixed-g, g-third 2-SAT UNSAT property proposed as a potential proof step in Item nori_q7_unrestricted_conditional_2sat_physical_gthird_reduction_20261009; that Item's exact equivalence of its 2-SAT encoding remains correct.

**Concrete 1680-bit face-color certificate**, g=6, labels 0,...,6. Enumerate all 105 ordered distinct triples p with p lexicographically smaller than reversed(p), in itertools.permutations(range(7),3) order. For each p enumerate 16 4-bit exterior masks m in increasing order, using increasing exterior coordinate labels as bit positions. The bit number 16*index(p)+m of this hex byte stream (least-significant bit first within each byte) is the color c(p,m). Define c(reverse(p),mask)=1−c(p,mask xor 15). This satisfies physical antipodal-reversal oddness.

```
00017d70130a828acccc55550f0ff0f03333ccccf8f8f0f0f0f00000ffff3333f0f00f0f0f0ff0f03333333300000f0ff0f033333333ffff0f0f0f0f5555400013333333cccc5c48333373bfccccd0d0d0d00040ffff333300000d0ff0f03b3300000f0ff0b43333ffff0f0f0f0f0f0ff0f03333ccccf0b07b7a4767ccccf0f00000ffff0f0f0f0ff0f000000f0ff0f0ffff0f0f0f0f0f0fc0c0ff00624000002b020f0f5050ff005050ff00ffffffff000000000f0ff0f048c8f0f00f0ff0f00000ffff00ffff00f0f0f0f0f0f0ffff00ff
```

**Independent, exhaustive pure-Python check:**
```python
from itertools import permutations
H='00017d70130a828acccc55550f0ff0f03333ccccf8f8f0f0f0f00000ffff3333f0f00f0f0f0ff0f03333333300000f0ff0f033333333ffff0f0f0f0f5555400013333333cccc5c48333373bfccccd0d0d0d00040ffff333300000d0ff0f03b3300000f0ff0b43333ffff0f0f0f0f0f0ff0f03333ccccf0b07b7a4767ccccf0f00000ffff0f0f0f0ff0f000000f0ff0f0ffff0f0f0f0f0f0fc0c0ff00624000002b020f0f5050ff005050ff00ffffffff000000000f0ff0f048c8f0f00f0ff0f00000ffff00ffff00f0f0f0f0f0f0ffff00ff'
b=bytes.fromhex(H)
T=[p for p in permutations(range(7),3) if p<p[::-1]]
ind={p:i for i,p in enumerate(T)}
assert len(b)==210 and len(T)==105
def color(p,m):
    if p<p[::-1]:
        j=16*ind[p]+m
        return (b[j//8]>>(j%8))&1
    return 1-color(p[::-1],m^15)
for t in permutations(range(7),3):
    for m in range(16):
        assert color(t,m)+color(t[::-1],m^15)==1
count=0
for p in permutations(range(7)):
    if p[2]!=6: continue
    pos={v:i for i,v in enumerate(p)}
    for root in range(128):
        w=[]
        for i in range(5):
            t=p[i:i+3]
            ex=[v for v in range(7) if v not in t]
            mask=sum(((((root>>v)&1)^int(pos[v]<i))<<j)
                     for j,v in enumerate(ex))
            w.append(color(t,mask))
        assert sum(w[i]!=w[i+1] for i in range(4))>=2
        count+=1
assert count==92160
```
The checker completed successfully. Direct enumeration of ALL full seven-direction geodesics under the same coloring gives good-geodesic counts by position of g=6 equal to (17794,11204,0,1400,0,11204,17794), with 92160 paths per position. Thus this is a conditional-method counterexample, NOT a counterexample to full NORI.

**Research implication.** Universal extraction with a predetermined sentinel in position three or five fails even in Q7. Genuine unrestricted extraction must move the sentinel's slot, vary its direction, or impose additional exterior sensitivity constraints. Fixed-root and fixed-slot index arguments cannot be promoted to an unrestricted theorem without a new transport step.
