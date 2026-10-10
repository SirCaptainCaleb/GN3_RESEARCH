# Sharp seven-support synchronization: eight legal Q20 five-support bad-root sets partition all roots

# Sharp failure of eightfold rank-five root synchronization in a legal NORI cube

**Theorem.** There is a legal antipodal-reversal-odd binary coloring of ordered physical three-faces of Q_20 and EIGHT DISTINCT five-coordinate supports B_α, indexed by α∈F_2^3, such that for every cube root x at least one B_α admits NO good five-edge direction-distinct geodesic rooted at x. In fact, for each α, the B_α-bad-root set is exactly {x:x_C=α}, a codimension-three affine subcube, and these eight sets partition Q_20. Thus the existing theorem guaranteeing a common good physical root for any seven specified five-supports is sharp even under full active NORI oddness and even for distinct five-supports.

**Construction.** Partition the 20 coordinates as
V = C ⊔ {g} ⊔ (disjoint union over α∈F_2^3 of A_α),
where |C|=3, g is one extra coordinate, and each A_α is a TWO-element set; all A_α are pairwise disjoint. Identify C with the three coordinate positions of α and put B_α=C∪A_α, so |B_α|=5.

Define a template H_{A,C} for an arbitrary five-face with directions A⊔C, where |A|=2, |C|=3. For any ordered free triple t, let P(t) be its word of A/C memberships and let
s_α(F,t)=sum_{j∈C outside t}(x_j(F)+α_j) in F_2.
The template has values
  H=1+s_α for patterns AAC, CAA, CCA;
  H=1 for ACA, CCC;
  H=s_α for ACC;
  H=0 for CAC.
These are simply the explicit rigid-square bad-root coloring from the companion Q5 result, with B there renamed C here.

For each ordered physical three-face (F,t) whose three free directions are contained in B_α, prescribe
  c(F,t) = x_g(F) + H_{A_α,C}(F,t).
This prescription is UNAMBIGUOUS: for distinct α,β, the triple intersection B_α∩B_β equals C; a free triple contained in both supports must be exactly C, and the template on its CCC pattern is the same constant 1, so both prescriptions give x_g(F)+1. Every prescribed free triple omits g, so x_g(F) is a legitimate fixed face bit.

**Antipodal legality.** The five-coordinate template H is reversal-even under complementation of all five of its coordinates:
 H_{A,C}(bar F, reverse t)=H_{A,C}(F,t).
Indeed AAC and CAA exchange while the parity of two exterior C bits is unchanged; ACC and CCA exchange while the parity of their sole exterior C bit flips and the constant term flips; ACA, CAC, CCC are individually reversal-invariant constant cases. Translating by α in C does not affect this identity. Under full Q_20 complementation the exterior bit x_g flips, so for every prescribed face
  c(bar F,reverse t)=1+c(F,t).
The collection of prescribed faces is closed under the full antipodal-reversal involution. Assign arbitrary complementary colors on all remaining involution pairs, obtaining a globally legal NORI coloring.

**Exact bad-root sets.** Fix α and the 15 exterior coordinates of the five-face on B_α. All its paths have the constant external x_g bit and experience only the template H, plus a constant color complement. Whenever the starting root has x_C=α, the C bit deviations x_C+α vanish and the three consecutive window colors of EVERY five-direction order alternate. An elementary complete ten-pattern check gives, with each order indicating which two of its five travel directions are in A_α:
 AACCC:101; ACACC:101; ACCAC:010; ACCCA:010; CAACC:101; CACAC:010; CACCA:010; CCAAC:101; CCACA:101; CCCAA:101.
The constant x_g changes all three colors together and leaves alternation unchanged. Hence all roots with x_C=α are B_α-bad. Conversely the earlier unconditional Q5 theorem allows at most FOUR bad roots in each fixed exterior five-face, and exactly four roots in that fiber have x_C=α. Thus no other roots are B_α-bad:
  Q_20 \ G_{B_α} = {x:x_C=α}.
The eight values of α partition all roots. Their complements of good-root sets cover Q_20 exactly, so intersection over all eight G_{B_α} is empty.

**The separation from grand closure is real.** The unconstrained face colors can be completed to exhibit a genuinely MONOCHROMATIC FULL 20-edge geodesic. Enumerate A_α={u_α,v_α} in any order α_0,...,α_7, and enumerate C={c_0,c_1,c_2}. Take the full travel order
 (u_α0,...,u_α7,c_0,v_α0,...,v_α7,c_1,g,c_2).
Every consecutive three-direction support in this order either contains directions from TWO DIFFERENT A_α blocks or contains g; in particular no such triple is contained in any prescribed B_α. Its 18 physical ordered-face window colors are therefore unassigned, and these 18 windows belong to distinct antipodal-reversal orbits because their ordered free-direction triples are distinct. Set all 18 colors to zero and give their partners color one before completing all remaining orbits. This produces a full monochromatic witness alongside the complete failure of eightfold rank-five common-root synchronization.

**Implication.** Every specified rank-five support has at least 7/8 good starting roots, and any seven supports have a common root by the union bound. The present construction attains equality in all eight bad densities with zero overlap, while respecting every physical-face identity and global NORI antipodal symmetry. Global closure arguments must use the actual direction orders, terminal memory, support growth, or stronger path exchanges, rather than expecting rank-five good-root density alone to synchronize arbitrary eight supports.
