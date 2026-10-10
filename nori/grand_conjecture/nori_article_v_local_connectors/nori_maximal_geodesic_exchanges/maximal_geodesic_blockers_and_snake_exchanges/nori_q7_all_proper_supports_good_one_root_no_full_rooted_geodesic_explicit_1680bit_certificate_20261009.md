# Q7 exact legal root obstruction: all proper supports good and two-color monochromatic coverage through rank five

EXPLICIT FINITE CERTIFICATE (Q7 all proper supports good at one root; no full rooted good geodesic).

There exists a fully legal antipodally reversal-odd binary coloring c of ordered PHYSICAL three-faces of Q7 and a root x=0000000 such that:
(i) For EVERY nonempty proper coordinate support B subset of [7] with 3<=|B|<=6, at least one ordering p of B gives a rooted directed geodesic starting at x whose 3-window colors have at most ONE switch.
(ii) For EVERY full permutation p of [7], the actual rooted 7-edge antipodal path from x has AT LEAST TWO switches.
Thus even simultaneous same-root good paths on EVERY proper support, including all seven six-supports and all 21 five-supports, do not by themselves imply a full one-switch path rooted there. The construction respects every global NORI antipodal-reversal identity and is independently checked by a short exact enumerator.

COMPLETE COLORING CERTIFICATE. Represent each physical ordered face by key (t,z), where t is an ordered triple of distinct vertex direction labels 0..6, and z is an integer bitmask of fixed exterior coordinates equal to 1, z disjoint from the bits of t. Define its reversal-odd mate theta(t,z)=(reverse(t), ((1<<7)-1)^support_mask(t)^z). These 3360 ordered physical-face states form 1680 two-element orbits. Sort lexicographically the 1680 canonical representatives min((t,z),theta(t,z)). Assign to the j-th canonical representative the j-th little-endian bit in the following 210-byte BASE64 certificate (j=0 first bit). Give the other orbit member the complementary color.

BASE64:
AAAAAAAAAAAAAAEAAAAAAAAAAAABAAEAAAAAAAAAAQABAAAAAAAAAAEAAQABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIUBAIERARGAAQAAgACAAYAQgBSABIAFgRCAkIAAgACBAKAAgACAAYAAAAAAAAAAAAUBAIERARGAGIEYgRgBHIEcgRyBmIEYgRihGKEIoQiBAAAAAAAAGQEZARkBGIAYgBmBPIE8gTyAHKE4oTiBAAAAADyBPQE8gTyBHIE8gRyhOIEAAD0DPIM8ARyB

A PURE-PYTHON VERIFIER (no SAT solver):
import base64,itertools as it
Z='AAAAAAAAAAAAAAEAAAAAAAAAAAABAAEAAAAAAAAAAQABAAAAAAAAAAEAAQABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIUBAIERARGAAQAAgACAAYAQgBSABIAFgRCAkIAAgACBAKAAgACAAYAAAAAAAAAAAAUBAIERARGAGIEYgRgBHIEcgRyBmIEYgRihGKEIoQiBAAAAAAAAGQEZARkBGIAYgBmBPIE8gTyAHKE4oTiBAAAAADyBPQE8gTyBHIE8gRyhOIEAAD0DPIM8ARyB'
n=7; M=(1<<n)-1; reps=set()
for t in it.permutations(range(n),3):
    free=sum(1<<d for d in t)
    for z in range(1<<n):
        if z&free: continue
        mate=(t[::-1],(M^free)^z)
        reps.add(min((t,z),mate))
reps=sorted(reps)
assert len(reps)==1680
index={key:j for j,key in enumerate(reps)}
bits=int.from_bytes(base64.b64decode(Z),'little')
def color(t,z):
    t=tuple(t);free=sum(1<<d for d in t)
    key=(t,z);mate=(t[::-1],(M^free)^z)
    return ((bits>>index[min(key,mate)])&1) ^ int(key>mate)
def switches(p):
    prefix=0;w=[]
    for i in range(len(p)-2):
        w.append(color(p[i:i+3],prefix))
        prefix|=1<<p[i]
    return sum(w[j]!=w[j+1] for j in range(len(w)-1))
assert min(switches(p) for p in it.permutations(range(n)))>=2
for k in range(3,n):
    good_per_support=[
        sum(switches(p)<=1 for p in it.permutations(B))
        for B in it.combinations(range(n),k)
    ]
    assert min(good_per_support)>0
    print(k,len(good_per_support),min(good_per_support),max(good_per_support))

Output from independent verification:
  support length3: 35 supports, good permutation counts all 6;
  support length4: 35 supports, good permutation counts all 24;
  support length5: 21 supports, good permutations min 6, max 103;
  support length6: 7 supports, good permutations min 117, max 307.
  Full support7: exactly 5040 tested permutations, min switches2, max4, ZERO good.

This is a 1680-bit explicit globally legal coloring; all counts follow by exhaustive permutation enumeration with no solver trust required. The base64 string fixes the entire coloring uniquely.

STRATEGIC CONSEQUENCE. A proof based exclusively on requiring good partial paths on every proper support at the SAME ROOT is insufficient, even when the support rank is n-1 (Q7). Closing the grand conjecture needs shared ordered-terminal memory/phase compatibility or the freedom to change root and exchange full paths. This sharply strengthens the analytic half-rank all-short-path counterexample and the Q7 all-21-five-support obstruction documented in the companion Item nori_all_dimensions_same_root_every_half_rank_path_good_no_full_path_and_q7_all21_supports_20261009. The COLORING IS NOT A COUNTEREXAMPLE TO THE GRAND CONJECTURE: it rules out full paths at one fixed root, while the grand conjecture requires a good full path at some root.

EXPLICIT POSITIVE GLOBAL WITNESS FOR THE SAME COLORING. At a DIFFERENT root x=1 (bit0=1, other bits0) and full direction order p=(0,1,2,4,6,3,5), the certificate yields the actual physical full-window word (0,0,1,1,1), with exactly one switch. This was checked by extending the verifier's face address to z=(x XOR traversed_prefix_mask) AND exterior_coordinate_mask. Thus the finite construction explicitly demonstrates the necessity of root mobility and satisfies the grand conclusion for this coloring.

STRICT STRENGTHENING: BOTH monochromatic colors on EVERY smaller support. An INDEPENDENT SECOND globally legal physical Q7 coloring, encoded by exactly the same 1680-orbit canonical-bit prescription above, has the following simultaneous root x=0 properties:
  * For each of all35 three-supports, all35 four-supports, and all21 five-supports, at least ONE fully monochromatic rooted path of color 0 AND at least ONE fully monochromatic rooted path of color 1 exist.
  * For each of all7 six-supports, at least112 different rooted six-edge orders are at most one-switch good.
  * For each of all5040 full seven-direction orders, the rooted path has 2 to4 switches and NONE is good.
The second coloring has an explicit GOOD full path at a different root x=1 (coordinate0 initially1) with direction order (0,1,2,5,3,4,6) and true color word (1,1,1,1,0), one switch.

SECOND BASE64 ORBIT CERTIFICATE (210 bytes; replace Z in the complete pure-Python verifier above):
X81XzTYHw3dDgHTYC97CAXdSwrRYJ9M98FyHvUYxXJ1efk9ZdvXWBXdBEvkQ8TIFBXP2jaPQtl4WSJ5PkpWnpfbxf8lOvBBx9/YRjhPmv2zR/Vh4RT96/DKlciATlD6FtBFzt3EePbMrvnHZrdaibeo5jy+GFMoLVp/bdnNR9Up2Gn78Ki3St6IFjdbAllKcky7Svt9d4DTlzf69biRq9HgelWdjH6JB9hirDFRMVK9KNFPMqhCQnszdXRxHkkapUCFX/Nutkvy1kCW9MWlSPtKk

An additional independent check for BOTH monochromatic colors on each k-support, k=3,4,5: for every B in combinations(range(7),k), generate all permutations p of B, compute w=[color(p[i:i+3],sum(1<<d for d in p[:i])) for i in range(k-2)], and assert that an all-zero w and an all-one w each occur. Exact checked minima over all supports are 1 for each color at every k=3,4,5. Existing full and rank6 verifier loops on this second certificate return no full rooted one-switch order and six-support good-permutation counts ranging from112 to144. Thus even complete both-color monochromatic support COVERAGE through rank n-2, coupled to one-switch coverage at rank n-1, fails to force a full same-root good path. The missing ingredient is precise reversed-two-tail terminal memory and phase matching or a different starting root. This second witness substantially strengthens the support-level obstruction while satisfying global antipodal reversal.
