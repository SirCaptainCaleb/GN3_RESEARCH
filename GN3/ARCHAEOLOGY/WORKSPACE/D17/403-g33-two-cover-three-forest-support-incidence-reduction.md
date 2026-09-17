# A two-cover versus defect-one three-forest has at most four support cells and no quiet two-cut residue

**Workspace:** D17
**State:** established
**Key:** `g33-two-cover-three-forest-support-incidence-reduction`

**Summary:** Let F be the old exact two-cover and J either canonical low-transition cut three-forest from the G33 defect-one proposal. The 2-by-3 support-incidence graph either has a four-cell cyclic overlap nucleus or, in the acyclic branch, only three or four cells. Noncontiguous cells give repeated-crossing geometry; contiguous cell words synchronize by accepted R435 outside reversal/reverse-trimer/proper-cycle output. The remaining seam graph is a forest. With three cells, J literally refines F by deleting one old X|B seam, forcing tau(F)=3,tau(J)=2 and, by SV101138, b_X=2,d_F(v)=1,b_B=3. With four cells, there are two old seams and one new seam. Each old/new hybrid is either blocked by one explicit R3 trimer or is an exact two-cover. If both hybrids are exact and neither lowers tau, all three seams are X|B transitions; but the three exact pairwise seam combinations then certify their full union as an acyclic tight matching with |G|-1 edges, Hamiltonizing G, impossible. Finally the two canonical cuts of the same bad triple cannot both realize the three-cell quiet residue: each would express F as the proposal matching with a different one of the two bad-triple edges removed and one F-only seam added, forcing the same symmetric difference to contain two different proposal edges. Hence every defect-one packet has, for at least one canonical cut, a strict transition descent or one bounded explicit physical output (C4 overlap, repeated crossing, R435 geometry, or local R3 trimer). The generic defect-one kernel has no completely quiet support-incidence residue.

### 1. Input and the two canonical cut forests
Retain the G33 defect-one normal form SV103530. Thus on the same top fiber

  G=H-{A,C}=X union V(B),

the actual old source representative

  F=F_1|F_2

is a literal exact two-cover with

  tau(F)>=3.

The low endpoint-cut proposal P=P_1|P_2 has exactly one bad consecutive turn

  eta=(u,v,w)

and at most two selected X|B adjacencies. Cutting the proposal edge uv gives one literal spanning tight three-path forest J^-, while cutting vw gives a second one J^+. For either choice J in {J^-,J^+},

  tau(J)<=2.                                               (SI.1)

The omitted B-active spoke s, its actual old incidence s-h, the low-cut coordinates, eta and its R3 reverse, and the source trimer (A,s,C) remain retained. We first analyze one arbitrary J and then use the fact that both canonical cuts coexist.

### 2. Support-incidence graph and the cyclic nucleus
For one fixed J=J_1|J_2|J_3, form the bipartite SUPPORT-INCIDENCE graph I=I(F,J) with left vertices F_1,F_2 and right vertices J_1,J_2,J_3. Join F_i to J_j exactly when

  S_ij=V(F_i) intersect V(J_j)

is nonempty. Call each nonempty S_ij a CELL. All five support vertices are nonisolated.

If I contains a cycle, then because the left shore has only two vertices every shortest cycle is a C4. Retain its four cyclic cells and one physical vertex from each. This is a bounded four-vertex SUPPORT-OVERLAP NUCLEUS with exact old/new support ancestry. No tight graph cycle is asserted.

Henceforth assume I is acyclic.

### 3. The acyclic incidence graph has only three or four cells
Let e be the number of nonempty cells and c the number of connected components of I. Since I is a forest on five nonisolated vertices,

  e=5-c<=4.                                               (SI.2)

Every J_j is nonempty, so e>=3. Therefore

  e in {3,4}.                                             (SI.3)

### 4. Noncontiguous cells and order disagreement are already explicit outputs
If a cell occurs in two separated intervals along either literal rail containing it, choose the first return to that cell. The two successive block boundaries around the intervening interval are two actual selected cross-cell seams on at most four named boundary vertices. Retain this REPEATED-CROSSING output with its old/new ancestry.

Assume every cell is contiguous in both rails. Restrict F_i and J_j to one cell S_ij. These are two actual tight Hamilton words on the same support. Apply accepted R435 proof-aware. At the first reverse-order consecutive contact, its proof gives either the adjacent reversed state, one of the two exact reverse seam trimers forced by R3, or the proper tight cycle formed by the ear plus the old cell segment. Retain that exact R435 output.

Outside these outputs, every cell has one common literal oriented path word in F and J. All internal cell edges are therefore common; only cross-cell seams differ.

### 5. The complete seam graph is a forest
Let O be the old cross-cell seams of F and N the new cross-cell seams of J. At an F rail incident with d cells there are d-1 old seams, hence

  |O|=e-2.                                               (SI.4)

Similarly

  |N|=e-3.                                               (SI.5)

No seam belongs to both sets: a common seam would join two distinct cells sharing both an F support and a J support.

Contract every common cell path to one atom and draw one edge for each seam in O union N. Call this seam graph Lambda. Within each connected incidence component, the old and new component paths connect exactly its cells, so Lambda has exactly c connected components. It has e vertices and

  |E(Lambda)|=(e-2)+(e-3)=2e-5=e-c,                     (SI.6)

because c=5-e. Hence Lambda is a FOREST. Any physical directed cycle in a locally tight hybrid made from these synchronized cell paths would contract to a cycle in Lambda and is therefore impossible.

### 6. Three cells force the absolute transition floor
Suppose e=3. Then |O|=1 and |N|=0. Thus every J rail is exactly one common cell path and F is obtained from J by adding one old seam o that merges two J rails. Therefore

  tau(F)-tau(J)=chi(o),                                  (SI.7)

where chi(o)=1 exactly when o crosses X|B. The left side is positive by (SI.1), so chi(o)=1 and the gap is exactly one. The inequalities tau(F)>=3 and tau(J)<=2 force

  tau(F)=3,   tau(J)=2.                                  (SI.8)

Call this the ONE-TRANSITION SEAM-DELETION residue. By the exact old-source degree law SV101138,

  tau(F)=2 b_X+d_F(v)-2,
  b_B=b_X+d_F(v),
  b_X>=2,  d_F(v) in {1,2}.                              (SI.9)

Substituting tau(F)=3 gives uniquely

  b_X=2,   d_F(v)=1,   b_B=3.                            (SI.10)

So any three-cell quiet residue already lies at the absolute source-fragmentation floor and makes v a physical endpoint of the old source cover.

### 7. Four cells give two exact one-seam hybrid tests
Suppose e=4. Then c=1 and I,Lambda are connected trees. Write

  O={o_1,o_2},   N={n}.                                  (SI.11)

For i=1,2 form the hybrid selected set M_i consisting of all common internal cell edges together with {n,o_i}. The common cell paths contribute |V(G)|-4 edges, so M_i has exactly |V(G)|-2 selected adjacencies.

Each seam separately is compatible with every common cell edge because o_i occurs in F and n occurs in J. The only possible bipartite-matching failure is direct copy competition between n and o_i. If they are v->x and v->y, or x->v and y->v, R3 on {x,v,y} gives one literal tight trimer in one of the complete-reversal orders. Retain this COPY-COMPETITION trimer.

Assume no competition. Then the only genuinely new predecessor-successor turn can occur where n and o_i meet at one physical cell endpoint. If that mixed turn is bad, R3 gives its exact reverse tight trimer. Retain this MIXED-SEAM trimer.

If the mixed turn is absent or tight, every selected local turn of M_i is tight. A directed cycle is impossible by Section 5, since it would project to a cycle in the two-edge subgraph {n,o_i} of the seam tree. Hence M_i is a literal exact two-cover T_i of G. Thus each i gives

  local R3 trimer,
  or exact two-cover T_i.                                  (SI.12)

### 8. The nominal four-cell minimum residue is impossible
Assume both hybrids are legal exact covers T_1,T_2 and neither lowers the transition count from F. Put

  tau_0 = number of X|B edges internal to the common cell words,
  a=chi(o_1), b=chi(o_2), c=chi(n).

Then

  tau(F)=tau_0+a+b,
  tau(J)=tau_0+c,
  tau(T_1)=tau_0+c+a,
  tau(T_2)=tau_0+c+b.                                   (SI.13)

Non-descent gives c>=b and c>=a, while tau(F)>tau(J) gives a+b>c. The only binary solution is

  a=b=c=1.                                               (SI.14)

Thus every seam o_1,o_2,n crosses X|B. More importantly, the three exact covers F,T_1,T_2 certify EVERY pair of these three seams:

  F contains {o_1,o_2},
  T_1 contains {n,o_1},
  T_2 contains {n,o_2}.                                  (SI.15)

Install all three seams simultaneously together with the common cell paths. Pairwise matching compatibility follows from (SI.15): any two seam edges occur together in one exact cover. Every selected physical turn uses zero, one, or two seam edges. Zero-seam turns are internal to common cell paths; one-seam turns are inherited from one of the exact covers; and every two-seam turn is inherited from the corresponding cover in (SI.15). Hence the full union is a locally tight bipartite matching.

It has

  (|V(G)|-4)+3=|V(G)|-1                                  (SI.16)

selected edges. It cannot contain a directed cycle, because after contracting common cell paths such a cycle would project to a cycle in the full seam graph Lambda, which is a tree. Therefore the full union is one Hamilton tight path on G. But G cannot be Hamiltonian: together with the automatic dimer on {A,C} it would give a spanning two-cover of H. Contradiction.

Hence in the four-cell branch, if neither hybrid is blocked by its explicit local trimer, at least one legal hybrid is an exact strict old-source transition descent. There is NO quiet all-three-transition seam-tree residue.

### 9. The two canonical cuts cannot both be three-cell quiet residues
Return to the same bad proposal P with eta=(u,v,w). Let

  e_-=uv,   e_+=vw

be its two distinct selected proposal edges. Their cut forests satisfy

  M_{J^-}=M_P-{e_-},
  M_{J^+}=M_P-{e_+}.                                    (SI.17)

Suppose for contradiction that BOTH J^- and J^+ realize the three-cell quiet residue of Section 6. Then there are F-only old seams o_-,o_+ such that

  M_F=M_P-{e_-}+{o_-},
  M_F=M_P-{e_+}+{o_+}.                                  (SI.18)

In a three-cell residue the added old seam cannot already belong to M_P: otherwise deleting e_- or e_+ and adding an already-present edge would leave only |V(G)|-3 edges, not the |V(G)|-2 edges of F. Thus each o_-,o_+ lies outside M_P. Consequently (SI.18) says the matching symmetric difference M_F triangle M_P is simultaneously

  {e_-,o_-}

and
  {e_+,o_+}.                                            (SI.19)

But e_- and e_+ are distinct edges of M_P, while o_-,o_+ are not in M_P. The two two-element sets in (SI.19) cannot be equal. Contradiction.

Therefore at most ONE of the two canonical cuts can lie in the quiet three-cell residue.

### 10. G33 contraction
Apply Sections 2-8 separately to J^- and J^+. Since the four-cell quiet branch is impossible and Section 9 forbids both cuts from taking the only remaining three-cell quiet branch, at least one canonical cut yields one of the following explicit outputs:

1. a four-cell cyclic support-incidence nucleus;
2. a repeated-crossing seam pair;
3. an R435 adjacent reversal, reverse trimer, or proper cycle inside one cell;
4. a copy-competition or mixed-seam R3 trimer in a four-cell hybrid; or
5. an exact two-cover of G with tau strictly below tau(F).

Thus the generic defect-one exchange has NO completely quiet support-incidence residue. The only non-descent outcomes are bounded physical overlap/order/seam objects retaining the exact old source cover, low-cut coordinates, B-active spoke s, old incidence s-h and source ancestry.

This is still a reduction, not full G33 extinction: outcomes 1-4 require consumers. Its gain is that unbounded matching/cycle complexity and both nominal minimum-gap silent cells are gone. Any surviving non-descent packet is physically bounded and explicitly located.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
