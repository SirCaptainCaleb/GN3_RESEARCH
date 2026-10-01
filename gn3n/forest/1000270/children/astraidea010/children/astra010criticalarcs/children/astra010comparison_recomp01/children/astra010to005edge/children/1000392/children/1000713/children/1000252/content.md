# A two-vertex companion gives an exact 2-by-2 Hall obstruction at every inseparable cut

## Statement

Let G be an edge-orderable boundary tournament with a spanning two-cover A|B, where A=(a_0,...,a_m) is increasing and B has vertex set {x,y}. Let s=a_i and t=a_j, i<j, be inseparable by spanning two-covers of G. For any cut k with i<=k<j, put p=a_k and r=a_{k+1}. Let ell be the incoming path edge a_{k-1}p when k>0 and formal -infinity when k=0; let u be the outgoing path edge r a_{k+2} when k+1<m and formal +infinity when k+1=m. Define L_k={z in {x,y}: ell < pz} and R_k={z in {x,y}: zr < u}. Then there are no distinct labels z_L in L_k and z_R in R_k. Equivalently, for every such cut, either L_k is empty, or R_k is empty, or L_k=R_k={z} for one z in {x,y}.

## Body

Fix a cut k between s and t. Suppose there are distinct labels z_L in L_k and z_R in R_k. The inherited prefix P=(a_0,...,p) is an increasing path, and by the definition of L_k the appended path (a_0,...,p,z_L) is increasing: if p=a_0 this is automatic, while otherwise its last comparison is ell<pz_L. Likewise the inherited suffix Q=(r,a_{k+2},...,a_m) is increasing, and by the definition of R_k the prepended path (z_R,r,a_{k+2},...,a_m) is increasing: if r=a_m this is automatic, while otherwise its first comparison is z_R r<u.

Because {z_L,z_R}={x,y}, these two paths are vertex-disjoint and together span V(G). The first contains s and the second contains t, so they form a spanning two-cover separating s and t, contrary to inseparability. Hence no distinct-label choice exists.

It remains only to translate this into the stated 2-by-2 Hall form. If either L_k or R_k is empty there is clearly no distinct-label choice. Suppose both are nonempty. If their union contains both x and y and they are not the same singleton, then one can choose different labels from the two sets: for example if L_k contains x and R_k contains y we are done, while if one set is {x,y}, choose from it the label different from any label in the other nonempty set. Therefore absence of a distinct-label choice with both sets nonempty forces L_k=R_k={z} for one label z. The converse is immediate. ∎
