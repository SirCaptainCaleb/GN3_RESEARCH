# Maximal geodesic blockers and snake exchanges

# Rooted blockers, physical exchanges, and the limit of support coverage

Let a legal NORI coloring assign bits to physical ordered three-faces with antipodal-reversal oddness. Good paths have at most one change. The following established lemmas separate rooted availability from globally compatible extension. They **do not** contradict the unrooted grand conjecture.

## Rooted short-path coverage without a full rooted path

THEOREM (legal NORI root with every short rooted path good and every full rooted path bad). For EVERY n>=6 there exists an antipodally reversal-odd binary coloring of physical ordered 3-faces of Q_n and a fixed cube root x=0 such that:
(i) EVERY directed geodesic starting at x and using k distinct coordinate directions, 3<=k<=floor(n/2)+1, has a three-window color word with AT MOST ONE switch;
(ii) EVERY FULL n-edge antipodal geodesic from that SAME root x has AT LEAST TWO switches, regardless of its direction order.
Moreover, in dimension n=7 every one of the 21 five-coordinate supports has at least one good rooted five-edge geodesic from x even though no full rooted path is good. For n>=8, every five-edge geodesic from x, on every support, is good.

PROOF. Let q=n-3 be the number of exterior fixed coordinates of a physical ordered three-face F; let z(F) be the number of exterior coordinates fixed to 1. Along ANY distinct-direction path rooted at x=0, the i-th ordered-three-face window (i starting at1) has precisely i-1 exterior 1 bits: all already traversed directions have become1 and all untraversed directions remain0. Thus z(F_i)=i-1 independently of direction order and support.

EVEN n=2m>=6: q=2m-3=2h+1 where h=m-2>=1. Define the symmetric-complement-odd layer table f on 0<=j<=q by f(0)=0, f(j)=1 for 1<=j<=h, and f(q-j)=1-f(j) for 0<=j<=h. Color EVERY ordered physical three-face by c(F,pi)=f(z(F)); the ordered triple is ignored. Since z(bar F)=q-z(F), the NORI axiom c(bar F,reverse pi)=1-c(F,pi) holds exactly. Every full path from root0 has window word 0,1^h,0^h,1, hence THREE switches. Every rooted path of length k<=h+3=m+1=floor(n/2)+1 reads just the initial segment f(0),...,f(k-3), namely 0 followed by 1s (possibly just0), and has at most one switch.

ODD n=2m+1>=7: q=2m-2=2h where h=m-1>=2. Prescribe f(0)=0, f(j)=1 for 1<=j<=h-1, and f(q-j)=1-f(j) for 0<=j<=h-1. At all exterior weights j!=h set c(F,pi)=f(j). On the self-complementary central weight j=h choose ANY tournament t on the n directions with t(a,c)+t(c,a)=1, and set c(F,(a,b,c))=t(a,c). The central ordered triple is reversal-odd by tournament skewness; all noncentral weights satisfy antipodal oddness by the layer complement prescription. Every full path rooted at0 has first two window colors f(0),f(1)=(0,1) and last two f(q-1),f(q)=(0,1), independently of its direction order and all central values. The first seam and last seam are therefore distinct mandatory switches, proving (ii). Every rooted k-edge path with k<=h+2=m+1=floor(n/2)+1 reads only weights 0,...,k-3<=h-1 and has color word 0 followed by 1s, proving (i).

SPECIAL Q7 STRENGTHENING: Here q=4,h=2. Every five-edge path from root0 has three colors (0,1,t(p_3,p_5)). Given ANY five-coordinate support B, select distinct a,c in B with t(a,c)=1; make them the third and fifth directions of the support path and arrange the other directions arbitrarily. Its word is (0,1,1), hence good. Thus ALL 21 five-supports have good rooted witnesses at x=0 while all full seven-edge paths from x remain bad.

SCOPE. These colorings are fully legal GLOBAL NORI colorings. Other starting cube vertices may have good full antipodal geodesics, as required by the grand conjecture. This theorem refutes every proposed implication of the form: simultaneous same-root good paths on every k-support, with k<=floor(n/2)+1, force a full same-root good path. It also refutes the all-21-five-support version in Q7. Any successful local-to-global proof must use terminal ordered-face memory, compatible phases, larger support, or change the starting root. This construction is a layer-weight obstruction and complements the team's rank-five common-root packing results.

## Sharp explicit Q7 certificate beyond the half-rank barrier

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

## Local swaps and extremal terminal walls

# Physical adjacent-transposition localization

**Lemma.** In a physical k-edge direction-distinct cube geodesic P rooted at x, interchange consecutive directions p_i and p_(i+1) to obtain P'. Both paths have the same root, endpoint, and direction support. Their genuine ordered-three-face windows W_j are *identical as physical ordered faces* for all j outside [i-2,i+1] intersect [1,k-2]. Consequently their color words differ in at most four consecutive positions under an arbitrary active NORI coloring.

**Proof.** Both direction words flip the same coordinates. Their prefix vertices are identical up through step i-1 and again from step i+1 onward, because coordinate flips commute. Every triple window whose indices avoid i and i+1 has the same ordered directions and the same preceding prefix vertex, hence determines the same physical ordered face. The only potentially modified starts j obey j<=i+1 and j+2>=i. QED.

**Exchange application and scope.** An adjacent direction swap therefore preserves the entire certified color word outside one four-window interval; only that interval and its boundary color comparisons need rechecking. This provides an exact root- and support-preserving operation for studying globally maximal one-switch geodesics. It does not force an improving exchange, missing-coordinate extension, or grand closure.

# Global LONGEST ≤1-switch geodesics have two-sided antipodal snake blockers

Let n>=5 and c be arbitrary active NORI coloring of actual ordered 3-faces with c(bar F,reverse pi)=1-c(F,pi). Define a GOOD direction-distinct cube geodesic as one whose ordered three-face window color word has at most ONE change; no antipodality/ full dimension requirement for shorter paths. Assume the unrestricted GRAND conjecture fails. Choose P to have globally MAXIMUM edge length k among all GOOD geodesics in the whole Q_n (all roots, supports, direction orders). Then 4<=k<=n−1. Write
 P: x -- (p_1,...,p_k) --> y,
its ordered-three-face window colors as q repeated s times followed by r repeated t times, with s,t>=1 and q≠r, s+t=k−2. Let a=p_(k−1), b=p_k, initial α=p_1, β=p_2 and T=[n]\{p_1,...,p_k}, m=n−k>=1.

**THEOREM (TWO-SIDED GOOD-SNAKE BLOCKER LAW).** P NECESSARILY has EXACTLY ONE color switch. For every missing direction d∈T, the physical three-face windows at the two ends are FORCED:
   c(F_y({a,b,d});(a,b,d)) = q = 1−r;
   c(F_x({d,α,β});(d,α,β)) = r = 1−q.
Consequently the genuine full-direction-distinct (k+1)-edge geodesics
   P followed by d (root x) have color word q^s r^t q;
   d followed by P (root x xor d) have color word r q^s r^t.
Both have EXACTLY TWO switches, with the same ACTUAL interior P window colors. Their new root locations are distinct because prepending d begins at x xor d, and both paths are actual cubes, not abstract words. Under active antipodal reversal these blocked caps give the dual certified incoming and outgoing three-face fans:
   c(F_bar_y({a,b,d});(d,b,a))=r;
   c(F_bar_x({d,α,β});(β,α,d))=q.
The terminal r-colored opposite-corner incoming snake of P lies in a Boolean T-root cube, and the initial r-colored prepend 3-face fan is at the OTHER endpoint.

**PROOF.** If the maximal good P were MONOCHROMATIC, any unused direction d could be appended; it creates exactly one new window, so the resulting (k+1)-edge path would still have at most one switch, contradicting maximality. Hence P is genuinely q^s r^t with q≠r. Appending d creates exactly one new physical window (a,b,d). If this were color r, the longer path would still be good, contradiction. Therefore its color is 1−r=q. Prepending d from root x xor d creates exactly one new physical window (d,α,β) and leaves the original P window sequence on the SAME physical faces (because the new first step d ends at x); if it were q, the longer path would remain good, contradiction. Therefore its color is 1−q=r. Reversing at antipodal physical faces gives the dual colors. The proof uses neither any claimed long mono path nor a freely reorderable tail. QED.

**NEAR-FULL n−1 CASE.** If k=n−1 then T={d} and bar y=x xor d (since y=x xor ([n]\{d})). Thus the prepended full path d+P starts EXACTLY AT bar y, while the appended full path P+d begins at x. Their color words are forced r q^s r^t and q^s r^t q, respectively, with two switches. Meanwhile the global antipodal reversal ΘP starts at bar y and has complementary reversed window word q^t r^s. This gives a concrete *two-by-two antipodal rectangle of full/near-full cube paths* where the two end-caps are opposite phases. The geometry does NOT by itself imply a good full path, because the cap free-coordinate triples at two ends differ and their colors can be independently assigned consistently with the oddness axiom when all directions of P are distinct.

**EXACT LIMITATION.** A longest good path P gives an opposite-corner fan in its LAST phase r, whereas its FIRST phase q differs. In contrast to the monochromatic maximal-path fan, splicing a fan branch through P_s would generally make TWO switches, not one. Thus neither the maximal-q rank bound nor its top-rank extraction transfers automatically to globally maximal *good* paths. To find a genuine descent, use a new defect measure that tracks both phases and both endpoint ordered pairs.

**GLOBAL STRATEGIC VALUE.** This is the proper maximal-defect analogue of the Devine–Milans snake method, directly about the target property rather than only about monochromatic paths: a hypothetical counterexample produces mandatory, bidirectional, oppositely colored extension walls at BOTH ends of a globally longest good partial cube geodesic. Progress requires constructing an extension or root exchange that breaks one wall while preserving one-switch coloring. The theorem does not solve unrestricted grand closure.

## Logical boundary

Universal existence of good paths on proper supports, even at one root, does not imply a rooted full good geodesic. Nor do forced caps yield a globally decreasing exchange automatically: new seam windows are actual physical faces. An unrooted extraction mechanism may move roots and retain terminal-order memory. Further improvements to support counts should be interpreted only with such a mechanism.
