# Nonlinear nested returns: nonsingular cores, odd singular cores and slab transport

- Stable ID: note_nori_nonlinear_outer_return_forcing_r11785
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, nonlinear-gates, nested-core, dimension-uniform, whole-gate-replacement, parity-fibers, proved, singular-core, four-word-portfolio, shared-phase-identity, nonlinear-slab-transport
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11785_3
- Updated session: session_nori_r11785_3
- Disposition: none
- Successor: none

## Related references

- subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- note:note_nori_nested_core_phase_peeling_r11660
- note:note_nori_q8_no_universal_common_word_fiber_20261018_r11785

## Research note

# Nonlinear nested-return forcing and its symmetry hypothesis

The complete theorem and proof are in Subsection gauge_critical_switches_and_clustered_witnesses_on_full_paths, composition 183, “Nonlinear outer gates and nonsingular inner returns”, NO1–NO10. Outer gates may be arbitrary nonlinear functions reversing under complementation of the deeper pair bits. The inner gates are affine in the inner bits with a nonsingular matrix depending arbitrarily on frozen outer states. The common nested word has 2^k successful roots in every prescribed parity fiber. This extends note_nori_nested_core_phase_peeling_r11660 and permits whole legal replacement of the first outer gate.

## Scope obstruction

On four pairs use parity-independent gates f_0=q_2, f_1=q_0, f_2=q_3, f_3=q_2. Every gate is odd and ignores its own bit. With outer order (0,1) and inner block {2,3}, the inner matrix [[0,1],[1,0]] is nonsingular.

Nevertheless word (0,1,2,3,2,3,1,0) has no red antipodal root. Bit q_0 stays fixed between the two visits to label 1, so f_1 is unchanged and those two red moves traverse the same original dimension twice. This violates the theorem's earlier-bit invariance condition for the second outer gate.

This refutes dropping that condition from the prescribed-word theorem. The coloring itself has red full geodesics: from q=8 the smaller-cube dimension order (1,0,3,2) works. The alternative pair word (1,0,2,3,2,3,0,1) has q-roots 8,9,10,11.

## Verification

An independent matching simulator tested every q-root in every parity fiber of 43 generated legal systems. Parameters (m,k,systems,fibers,root trajectories) were (4,1,20,320,5120), (5,2,12,384,12288), (6,3,8,512,32768), (7,3,3,384,49152). All 1600 fibers had 2^k successful roots, and every successful walk used all 2m original dimensions once. Total: 99328 root trajectories.

Outer gate values were independently chosen on orbits of the required complementary shifts. Inner nonsingular zero-diagonal matrices varied over outer parity and complementary outer-q orbits. Their phase tables varied over the permitted parity keys, with global oddness imposed using the row parity of the chosen matrix. Seed: 117853. These finite checks audit the formula; the theorem is proved algebraically.

A separate complete check tested all 16 odd functions f_0(q_1,q_2,q_3) and all eight constant phases in f_1=q_2+alpha, f_2=q_3+beta, f_3=q_1+q_2+q_0+gamma. Each of the 128 systems has two successful roots for (0,1,2,3,1,2,3,0), in every parity fiber. The all-nonlinear strongly connected family NO9 was checked for k=3,...,8, with respectively 8,16,32,64,128,256 successful q-roots.

Portable verification of the exhaustive whole-gate test and scope example:

~~~python
def roots(f, word, m):
    out = []
    for q in range(1 << m):
        z = q
        directions = []
        for i in word:
            value = f(i, z)
            directions.append((i, value))
            if value == 0:
                z ^= 1 << i
        if z == q ^ ((1 << m) - 1):
            assert len(set(directions)) == 2 * m
            out.append(q)
    return out

for truth in range(16):
    for phases in range(8):
        def gate(i, z):
            q = [(z >> j) & 1 for j in range(4)]
            if i == 0:
                t = z >> 1
                u = min(t, t ^ 7)
                return ((truth >> u) & 1) ^ int(t > (t ^ 7))
            if i == 1:
                return q[2] ^ (phases & 1)
            if i == 2:
                return q[3] ^ ((phases >> 1) & 1)
            return q[1] ^ q[2] ^ q[0] ^ ((phases >> 2) & 1)
        assert len(roots(gate, [0,1,2,3,1,2,3,0], 4)) == 2

gate = lambda i, q: (q >> [2,0,3,2][i]) & 1
assert roots(gate, [0,1,2,3,2,3,1,0], 4) == []
assert roots(gate, [1,0,2,3,2,3,0,1], 4) == [8,9,10,11]
~~~

## Transfer boundary

The theorem supplies the hypotheses of the concurrent exterior-parity localization result: a successful root in every parity fiber of one word. Single paired-square switches therefore preserve success for m>=3. A union of t switches is tolerated if 4t<2^m or 16t<2^(m+k).

No proof currently derives the required decomposition from every hypothetical strict square boundary. The arbitrary-rank matrix-peeling conjecture and unrestricted NORI1 remain open. No boundary-tournament specialization or claim of grand closure is made.

Session session_nori_r11785_3.


## Odd singular cores and four-word forcing: continuation

Published in the same Subsection, composition 195, equations OPC1–OPC13, session session_nori_r11785_3.

For every odd r>=3, the ordinary paired-flat core with gates g_i=sum_(j!=i)q_j+theta_i(p_except_i), and arbitrary parity phases, has a fixed four-word portfolio giving four or twelve colored root-word pairs in every parity fiber. Pair up r-3 labels and use abab on each pair. On the remaining triple use one of 010212, 012012, 012021, 102012. The shared phase equations have coefficient XOR zero and right-side XOR one, so one or three are feasible. An affine-swap reduction removes each two-pair block while preserving a free center bit. This is a hand proof for all odd sizes; the core slope J+I is singular of rank r-1.

Surrounding this core with the nonlinear outer gates satisfying the earlier partial-complement condition gives four full words jointly covering every prescribed parity fiber in red. Their red root-word count is at least 2^(k+1) per fiber. A single common word covering every fiber is unnecessary. The counterexample in note_nori_q8_no_universal_common_word_fiber_20261018_r11785 is therefore consistent with this certificate mechanism.

The word-family transport lemma uses the UNION of exterior prefix-parity signatures of all candidate words. Their signature counts are one on an outer label, two in a completed abab block and three on a distinguished triple label. Arbitrary nonlinear rewrites on s_O,s_P,s_T exterior parity slabs preserve a red full geodesic whenever 2s_O+4s_P+6s_T<2^m. Every single slab in any pair can be rewritten in the new class. This permits up to 2^(m-2) independent square-parameter changes within that slab. The first outer gate may still be replaced on its whole domain.

The class allows every gate to be nonlinear and its directed q-influence graph to be strongly connected. The complete affine-in-inner block and ordered outer symmetries remain hypotheses. No argument derives them for all critical boundaries, and no boundary-tournament transfer is established.

Independent checks:
- All 4096 three-pair phase assignments: direct matching simulation confirmed all four displayed equations, one or three feasible words, and four colored roots per feasible word.
- Ordinary odd cores r=3,5,7: 31 generated phase systems and 464 prescribed parity fibers; the colored root-word total was always four or twelve.
- Legal odd systems with nonlinear outer gates: 18 systems on m=4,5,6,7, 640 prescribed parity fibers, 137216 red root-word trajectories. Every fiber was covered and met the 2^(k+1) lower bound; all successful walks used the original dimensions once.
- All 32 exterior parity slabs of one m=4 instance and all 192 slabs of one m=6 instance: a surviving portfolio path was found in a fiber outside the changed slab signatures, checking 224 slab-avoidance certificates.
- Signature sizes (1,2,3) were computed directly for several outer/core sizes, including an odd seven-pair core.

The following standard-library checker independently simulates the odd cores and verifies the four phase forms:

~~~python
import itertools, random
rng=random.Random(11785317)
W=[(0,1,0,2,1,2),(0,1,2,0,1,2),(0,1,2,0,2,1),(1,0,2,0,1,2)]
forms=[(0x503,1),(0x969,0),(0xc30,1),(0x05a,1)]
def pack(p,i):return (p&((1<<i)-1))|((p>>(i+1))<<i)
def corecount(r,phase,p,word):
 counts=[0,0]
 for col in range(2):
  for q in range(1<<r):
   pp,qq=p,q
   for i in word:
    f=((qq&~(1<<i)).bit_count()&1)^phase[i][pack(pp,i)]
    if f==col:qq^=1<<i
    pp^=1<<i
   counts[col]+=qq==q^((1<<r)-1)
 return counts
# Exhaustive three-pair audit at parity zero.
for theta in range(4096):
 phases=[[(theta>>(4*i+j))&1 for j in range(4)] for i in range(3)]
 cc=[sum(corecount(3,phases,0,w)) for w in W]
 assert all(cc[j]==4*(((theta&mask).bit_count()&1)==rhs) for j,(mask,rhs) in enumerate(forms)),(theta,cc)
 assert sum(x>0 for x in cc) in (1,3)
print('exhaustive triple phase tables: 4096; all four identities checked',flush=True)
for r,trials in [(3,20),(5,8),(7,3)]:
 pairs=[(a,a+1) for a in range(0,r-3,2)]
 prefix=tuple(i for a,b in pairs for i in (a,b,a,b))
 portfolio=[prefix+tuple(r-3+i for i in w) for w in W]
 fibers=0
 for t in range(trials):
  phases=[[rng.getrandbits(1) for _ in range(1<<(r-1))] for _ in range(r)]
  ps=range(1<<r) if r<=5 else rng.sample(range(1<<r),16)
  for p in ps:
   counts=[sum(corecount(r,phases,p,w)) for w in portfolio]
   assert all(x in (0,4) for x in counts),(r,p,counts)
   assert sum(counts) in (4,12),(r,p,counts)
   fibers+=1
 print('odd core',r,'systems',trials,'fibers',fibers,flush=True)

~~~
