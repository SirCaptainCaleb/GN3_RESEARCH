# Ten arbitrary Q7 five-supports share ≥4 good roots; maximal bad sets coincide

# Q7 rigidity of maximal rank-five bad-root sets; ten-support common-root theorem

Consider a legal reversal-odd coloring of ordered physical three-faces of Q7. For a five-coordinate support B, let E_B⊂Q7 consist of starting roots x for which **all** 5-direction orders on B have their three physical window colors alternating. Call B *saturated* when |E_B|=16.

**THEOREM A (paired-support rigidity).** For any two different 5supports B,B′:
(i) if |B∩B′|=3, B and B′ cannot both be saturated;
(ii) if |B∩B′|=4 and B,B′ are both saturated, then E_B=E_B′ (in fact, all 160 compatible saturated template pairs have equal 16-element bad-root sets).
Thus all simultaneously saturated supports have the SAME bad-root set.

**THEOREM B (ten-support synchronization).** Given any ten specified five-coordinate supports B_1,...,B_10 (repetitions permitted), there are at least FOUR vertices x∈Q7 that are good for all ten supports: for each i some 5-edge geodesic rooted at x using exactly B_i has ≤1 color switch. If none of the supports is saturated, at least EIGHT common good roots exist.

**Proof of Q5 fiber classification needed for both.** On an arbitrary physical Q5, the previously proved sharp bad-root theorem and its diagonal-root rigidity show the possible numbers of bad roots are 0,1,2,4; in the four-root case the roots form a coordinate square and the full ordered 3face coloring is the unique canonical template H or its global complement. A template is determined by (A,z,eta), where A is the 2-coordinate free square axis set (10 options), z assigns 0/1 bits to the other 3 coordinates (8 options), and eta selects H or H+1 (2 options): 160 possibilities. Write C=B\A, s(F,t)=sum_{j∈C\set(t)}(x_j(F)+z_j) mod2, and let P be the A/C membership pattern of ordered triple t. Then H=base(P)+slope(P)*s(F,t) mod2 with table

P: AAC ACA CAA ACC CAC CCA CCC
base: 1 1 1 0 0 1 1
slope:1 0 1 1 0 1 0.

**The antipodal exterior-pair lemma.** Write D=[7]\B, |D|=2. Under full NORI antipodal reversal, a five-support path rooted at x maps to the reversed order rooted at y with y_B=x_B and y_D=x_D+(1,1). Thus E_B is invariant under complementing both D-bits at fixed x_B. Opposite D-fibers have the same number t∈{0,1,2,4} of bad roots. Therefore
 |E_B|=2(t_0+t_1)∈{0,2,4,6,8,10,12,16}.
In particular nonsaturated supports have |E_B|≤12. If B is saturated then EVERY D-fiber is a rigid H-square: the two antipodal pairs 00/11 and 01/10 each choose independently one of the 160 (A,z,eta) patterns, and antipodal partners carry the same (A,z) and opposite eta. There are exactly 160²=25,600 such parameter choices per support.

**Proof of Theorem A(i), direct.** If B∩B′=T has size3, their private direction pairs P=B\T, Q=B′\T each have size2. Fix Q. A saturated B induces one canonical H-template on its 5face. Among the six orders t of T, choose one whose A/C pattern has slope=0: CCC if A∩T=∅; CAC if |A∩T|=1; ACA if |A∩T|=2. In this orientation, the ordered face color is INDEPENDENT of the fixed P-bits, since H is constant base+eta. For saturated B′, P are precisely its TWO exterior directions; antipodal pairing forces the SAME ordered T-face color to change by one when both P bits are toggled while all of Q and T's exterior bits are held fixed. Contradiction.

**Proof of Theorem A(ii), finite exact certificate.** There are only two possible mutual intersection sizes for distinct five-supports in Q7: 3 or4. By coordinate symmetry take B={0,1,2,3,4}, B′={0,1,2,3,5} (intersection4) or B′={0,1,2,5,6} (intersection3). For each support enumerate all 25,600 pairs of canonical square templates, compute a signature of the entire physical ordered 3face coloring on the common ordered triples (all 16 exterior assignments per triple), and group by signature. Any two saturated prescriptions on B and B′ are compatible iff their signatures are equal, since the common physical ordered faces are the only faces they jointly prescribe. The following pure Python code exhaustively checks every possibility; it uses two 160-choice template lists (one for each exterior antipodal pair), combines their disjoint signature bitmasks, and records a 128-bit bad-root mask:

```python
from itertools import permutations, combinations
from collections import defaultdict
V=range(7)
H={'AAC':(1,1),'ACA':(1,0),'CAA':(1,1),
   'ACC':(0,1),'CAC':(0,0),'CCA':(1,1),'CCC':(1,0)}

def all_maximal(B, B2):
    B=set(B); D=sorted(set(V)-B)
    T=list(permutations(sorted(B & set(B2)),3))
    faces=[]
    for t in T:
        outside=sorted(set(V)-set(t))
        for z in range(1<<len(outside)):
            x=sum(1<<j for i,j in enumerate(outside) if z>>i&1)
            w=(x>>D[0]&1)|((x>>D[1]&1)<<1)
            faces.append((t,x,w))
    options=[[],[]]
    for aa in combinations(sorted(B),2):
      A=set(aa); C=sorted(B-A)
      for zz in range(8):
        target={j:zz>>i&1 for i,j in enumerate(C)}
        for eta in range(2):
          signatures=[0,0]
          for i,(t,x,w) in enumerate(faces):
            pattern=''.join('A' if d in A else 'C' for d in t)
            base,slope=H[pattern]
            exterior_parity=sum((x>>d&1)^target[d] for d in C if d not in t)&1
            bit=base^(slope*exterior_parity)^eta^(w in (2,3))
            if bit: signatures[w in (1,2)]|=1<<i
          bad=[0,0]
          for root in range(128):
            w=(root>>D[0]&1)|((root>>D[1]&1)<<1)
            if all((root>>d&1)==target[d] for d in C):
              bad[w in (1,2)]|=1<<root
          for cls in (0,1): options[cls].append((signatures[cls],bad[cls]))
    configs=defaultdict(list)
    for p in options[0]:
      for q in options[1]:
        configs[p[0]|q[0]].append(p[1]|q[1])
    return configs

B={0,1,2,3,4}
for B2, expected in [({0,1,2,5,6},0),({0,1,2,3,5},160)]:
    R=all_maximal(B,B2); S=all_maximal(B2,B)
    matches=[(a,b) for signature,A in R.items() for a in A
                      for b in S.get(signature,[])]
    assert len(matches)==expected
    assert all(a==b and a.bit_count()==16 for a,b in matches)
    print('intersection',len(B&B2),'matches',len(matches))
```

Exact output: intersection3 → 0 matching pairs; intersection4 → exactly 160 matching pairs. In EVERY matching intersection4 pair, the two 128-bit bad-root masks are identical and have 16 bits set. In particular the asserted equality E_B=E_B′ follows for ANY legal coloring. The intersection3 case supplies an independent computational verification of the preceding direct argument. The verifier visits all literal ordered face states in the common support and all 25,600 canonical saturated choices; no random search or external optimizer is used.

**Proof of Theorem B.** Every unsaturated support has |E_B|≤12. If none of ten supports is saturated, then the union of their bad-root sets has size at most 10·12=120<128, leaving ≥8 common good roots. Otherwise, by Theorem A all saturated E_B are equal, so their UNION has size exactly16; with k≥1 saturated supports, the union of all ten E_B has size at most 16+(10−k)·12≤16+9·12=124. Thus at least 128−124=4 common good roots. QED.

**Scope.** The theorem holds for arbitrary legal Q7 physical odd NORI colorings. It upgrades the universal seven-support good-root union bound to TEN simultaneous supports in dimension seven. It does not yet give a full seven-direction ≤1-switch geodesic: the ten compatible five-support paths may have unrelated orders and phases. The decisive remaining task is to couple their ordered endpoint states into a seven-direction path.
