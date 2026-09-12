# The five-cell residue and its exact transition tax

**Workspace:** D1
**State:** established
**Key:** `setting`

**Summary:** Deleting q_2,q_{m-2} produces five tight source cells; every exact two-cover has t_G=3+sigma_G, and sigma=0 means literal contiguity of all five cells.

Put D={q_2,q_{m-2}} and W=H-D. In the crossed inward-anchor frame the five pairwise disjoint tight source paths are
G_0=Q[0,1], G_1=Q[3,m-3], G_2=Q[m-1,m], G_3=(a,c), G_4=(b,z).
They partition W. For an exact two-cover T of W let b_i be the number of maximal nonempty T-blocks lying in G_i, B=sum_i b_i, let t_G(T) be the number of T-edges joining different cells, and define sigma_G(T)=B-5.

Because each G_i is itself one path, the intrinsic partition-cover deficit identity R7 gives
 t_G(T)=sum_i pc(G_i)-2+sigma_G(T)=5-2+sigma_G(T)=3+sigma_G(T).
Hence t_G>=3. Equality holds exactly when sigma_G=0, equivalently b_i=1 for all five i, so every source cell occurs as one contiguous T-block. This is R862. Every intercell transition is a physical transition in the residue W; R176 may therefore use either deleted anchor as its separate spare coordinate when a downstream cross-state upgrade is invoked. Nothing in this count asserts a paid floor or synchronizes different exact covers.
