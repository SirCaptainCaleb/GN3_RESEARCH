# Exact affine rank-two-defect obstruction: attainable two-switch pairs form a complete bipartite graph

# Exact codimension-two affine no-closure obstruction: complete bipartite two-switch support

Consider ANY ordered-three-face coloring affine in the physical exterior bits. Fix a full direction order pi in Q_n, n>=5. Its switch/change vector has the affine form D_pi(x)=b+M x∈F2^m, m=n−3. Suppose rank M=m−2=n−5 and NO full pi-geodesic from any root has <=1 color change. Let H be any 2×m full-row-rank parity-check matrix with ker H=im M, and let s=H b∈F2².

**Theorem (exact bipartite syndrome structure).** Necessarily s is one of the three nonzero vectors, no column H_j equals s, and the nonzero columns of H are partitioned into TWO NONEMPTY classes
 I={j:H_j=u},  J={j:H_j=v}
with u,v the two distinct nonzero vectors other than s (thus u+v=s). All remaining columns are zero.

For distinct change positions i,j, a root x whose color-word has EXACTLY two changes at i and j exists if and only if one of i,j lies in I and the other in J. For EVERY cross pair (i,j)∈I×J there are EXACTLY 2^(n−rank M)=2^5=32 distinct cube roots x realizing that EXACT two-switch pattern. Thus the graph on change positions indicating attainable two-switch color words is the COMPLETE BIPARTITE graph K_(|I|,|J|), plus isolated positions corresponding to zero H columns. At least 32 |I||J| full pi-geodesics have exactly two switches.

**Proof.** As im M=ker H, the attainable switch vectors are precisely {y:H y=s}. No-root-with-≤1-switch means y=0 and all unit vectors e_j are excluded. Equivalently s≠0 and H e_j=H_j≠s for all j. In F2² there are exactly three nonzero vectors; the two nonzero vectors different from s are u,v and satisfy u+v=s. Since H has row rank2, both types u and v must actually occur (columns of type0 or only one nonzero type would have rank at most1). A weight-two vector e_i+e_j is attainable iff H_i+H_j=s, which occurs iff H_i,H_j are u,v in either order. Each attainable y has exactly 2^(n−rank M)=32 affine preimages under D_pi. QED.

**Research interpretation.** This theorem exhibits a sharply constrained *bipartite* space of near-closure witnesses at maximal counterexample rank. Global NORI closure would follow for the affine subclass if one can prove that face-coloring compatibility, neighboring-direction exchanges, or antipodal reversal forces a NON-bipartite (odd-cycle) two-switch-position constraint for at least one order pi. The usual 5-cyclic equal-color connector already creates nontrivial odd parity of local equal-window positions; one must establish an actual compatible lift of those local pentagons to the above fixed-order syndrome classes before inferring any contradiction. Such a lift is unproved, and the theorem does not itself close NORI.

This is a nontrivial exact algebraic restriction conditional on codimension 2, not a proof that a maximal-rank order pi exists.
