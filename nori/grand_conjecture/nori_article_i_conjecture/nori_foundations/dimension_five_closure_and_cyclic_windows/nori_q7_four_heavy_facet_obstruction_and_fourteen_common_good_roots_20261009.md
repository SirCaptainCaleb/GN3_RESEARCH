# Four heavy five-supports impossible in Q7; any fourteen supports share ≥4 good roots

# Four heavy rank-five supports cannot coexist in NORI Q7; fourteen-way common roots

**DEFINITIONS.** For any five-direction support B⊂[7], let E_B be the set of Q7 roots at which every 5-edge B-geodesic has alternating 3window colors. The proved exact possible counts are |E_B|∈{0,2,4,6,8,10,12,16}; say B is *heavy* if |E_B|≥10, *saturated* if |E_B|=16. The previous direct slope-zero argument proves that two heavy B,B′ must overlap in FOUR directions, so complements D=[7]\B are an intersecting family of edges.

**THEOREM 1 (four-heavy obstruction).** A legal reversal-odd coloring of Q7 has at most THREE distinct heavy five-supports.

**Reduction to four canonical facets of Q6.** If four heavy supports existed, their complementary 2edges would be four pairwise-intersecting edges of K7, and thus would all share one coordinate g (the only other intersecting-edge family type, a triangle, has three edges). The four supports have forms B_i=[7]\{g,i}, for distinct i. Each heavy B_i has an exterior antipodal pair (g,i) on which every 5face contains a 4vertex bad-root square and therefore carries one of exactly160 canonical H templates. Fix g=0. For each i choose the half-face with i=ε_i in this antipodal pair. Translate coordinates i independently to make all four ε_i=0, leaving the NORI antipodal condition invariant. The global coloring now induces four canonical H-colorings on the four facets x_0=0,...,x_3=0 of the six-dimensional cube on coordinates other than g. Two facet prescriptions agree on all ordered three-faces of their 4dimensional intersection.

The following deterministic finite certificate rules out four heavy supports. For each 5facet there are 10 square axis choices, eight 3bit addresses and two color complements, giving160 canonical templates. Restrict each template to the 48 ordered physical three-face states of any shared four-facet, encoded as a 48bit signature. The signature on facet0 uniquely determines the matching canonical template on each other facet. Out of the160 initial templates, exactly FOUR induce four mutually consistent canonical facets. For EACH of those four and EACH complementary opposite facet x_i=1, the fixed colors already prescribed on the other three canonical facets make every starting root fail the requirement that all120 B_i orders alternate. Thus the second exterior antipodal pair has ZERO bad roots. Each proposed heavy B_i consequently has exactly8 bad roots, contradicting heaviness.

**Complete reproducible certificate** (standard Python, exact integer parity propagation, no optimizer):
```python
from itertools import permutations, combinations
from collections import defaultdict
V=set(range(6))
H={'AAC':(1,1),'ACA':(1,0),'CAA':(1,1),
   'ACC':(0,1),'CAC':(0,0),'CCA':(1,1),'CCC':(1,0)}
mask=lambda a:sum(1<<d for d in a)

def choices(i):
    B=V-{i}
    return [(set(A),sorted(B-set(A)),z,eta)
            for A in combinations(sorted(B),2) for z in range(8) for eta in (0,1)]

def color(t,x,tpl):
    A,C,z,eta=tpl
    kind=''.join('A' if d in A else 'C' for d in t)
    base,slope=H[kind]
    s=sum((x>>d&1)^((z>>k)&1) for k,d in enumerate(C) if d not in t)&1
    return base^(slope*s)^eta

def overlap_signature(i,j,tpl):
    T=V-{i,j};bits=[]
    for t in permutations(sorted(T),3):
        d=next(iter(T-set(t)))
        for x_d in (0,1):bits.append(color(t,x_d<<d,tpl))
    return sum(b<<k for k,b in enumerate(bits))

L={i:choices(i) for i in range(4)}
forced={}
for j in range(1,4):
    inverse={overlap_signature(j,0,t):k for k,t in enumerate(L[j])}
    assert len(inverse)==160
    forced[j]=[inverse[overlap_signature(0,j,t)] for t in L[0]]
solutions=[]
for a in range(160):
    v={0:a,**{j:forced[j][a] for j in range(1,4)}}
    if all(overlap_signature(i,j,L[i][v[i]])==overlap_signature(j,i,L[j][v[j]])
           for i,j in combinations(range(4),2)):
        solutions.append(v)
assert len(solutions)==4

def forced_colors(choice):
    cols={}
    for i in range(4):
        tpl=L[i][choice[i]]
        for t in permutations(sorted(V-{i}),3):
            E=sorted(V-set(t))
            for b in range(8):
                x=sum(((b>>k)&1)<<d for k,d in enumerate(E))
                if x>>i&1:continue
                val=color(t,x,tpl)
                if (t,x) in cols:assert cols[t,x]==val
                cols[t,x]=val
    return cols

def bad_root_possible(i,root,colors):
    B=sorted(V-{i});adj=defaultdict(list)
    for p in permutations(B):
        w=[];s=0
        for k in range(3):
            t=p[k:k+3];w.append((t,(root^s)&(63^mask(t))));s^=1<<p[k]
        for u,v in zip(w,w[1:]):
            adj[u].append(v);adj[v].append(u)
    parity={}
    for seed in adj:
        if seed in parity:continue
        parity[seed]=0;todo=[seed];required_seed=None
        while todo:
            u=todo.pop()
            if u in colors:
                v=colors[u]^parity[u]
                if required_seed is None:required_seed=v
                if required_seed!=v:return False
            for v in adj[u]:
                needed=1^parity[u]
                if v in parity:
                    if parity[v]!=needed:return False
                else:parity[v]=needed;todo.append(v)
    return True

possible=0
for assignment in solutions:
    fixed=forced_colors(assignment)
    for i in range(4):
        for root in range(64):
            if (root>>i)&1:
                possible+=bad_root_possible(i,root,fixed)
assert possible==0
print('four-facet compatible templates:',len(solutions))
print('additional bad-root candidates:',possible)
```
Its output is
  four-facet compatible templates: 4
  additional bad-root candidates: 0.
In bad_root_possible, the implication that a root is bad is encoded by XOR=1 constraints between each consecutive two ordered three-window states of each of its120 literal five-direction orders, with all already prescribed actual-face colors enforced. The BFS checks all such parity constraints. Failure proves the root GOOD in every possible completion of the unknown face colors.

**LEMMA 2 (absorption of heavy roots by saturated roots).** If B is saturated and B′ is a different heavy support, then B,B′ overlap in four directions and at least eight of the bad roots of B′ belong to E_B. In particular |E_B′\E_B|≤4 when B′ is heavy and unsaturated.

**Proof/certificate.** Heavy B′ has an antipodal exterior pair carrying an exact four-root canonical square in each physical five-face. Compare its 160 possible canonical H templates on this ONE exterior pair against the 160² possible saturated templates of B on all actual ordered three-faces supported by B∩B′. There are only the two exterior pair types for B′. In the representative coordinates B={0,1,2,3,4}, B′={0,1,2,3,5}, for each exterior pair type the exact restriction signatures give160 compatible pairs. In EVERY compatible pair the B′-canonical antipodal pair contributes eight bad Q7 roots, all belonging to E_B. This is obtained by restricting the paired-support enumerator from the earlier ten-support item to a single B′ exterior antipodal class (the option signatures called options[cls]); its finite loops reproduce counts160 and containment intersection8 for each class. The overlap-three case was excluded directly by the heavy-support slope-zero argument. Therefore the eight required roots of B′ already lie in E_B. QED.

**THEOREM 3 (fourteen arbitrary five-supports have simultaneous good roots).** In ANY legal Q7 coloring and for ANY fourteen specified five-supports B_1,...,B_14 (repetitions allowed), there are at least FOUR starting cube vertices x for which every B_i admits a good rooted 5edge geodesic (at most one window-color switch). If at least one specified support is saturated, there are at least EIGHT such common good roots.

**Proof.** Repetitions do not alter the union of bad-root sets. Let h be the number of distinct heavy supports; by Theorem1, h≤3. Every light support has |E_B|≤8; every heavy unsaturated support has |E_B|≤12.

If none is saturated, the bad-root union has size at most
 h·12+(14−h)·8 ≤ 3·12+11·8 =124,
leaving at least 128−124=4 common good roots.

If a saturated B occurs, all saturated bad-root sets E_{B_s} coincide by the paired-support rigidity theorem. Any other heavy B′ contributes at most four additional bad roots outside E_B by Lemma2. Any light B′ contributes at most eight. Thus the bad-root union has size at most
 16+4(h−1)+8(14−h) = 124−4h ≤120,
where h≥1. Hence at least EIGHT common good roots remain. QED.

**Research significance.** Four-heavy exclusion is a literal physical-face gluing constraint stronger than the extremal bad-root density bound. The fourteen-way theorem is confined to rank-five root synchronization in Q7. The unrestricted NORI grand conjecture additionally demands ordering/phase compatibility leading to a full seven-direction one-switch geodesic.
