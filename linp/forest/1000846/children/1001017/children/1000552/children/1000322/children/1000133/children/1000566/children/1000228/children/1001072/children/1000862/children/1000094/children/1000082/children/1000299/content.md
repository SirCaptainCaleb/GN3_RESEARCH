# Zero-slack critical cores are at absolute near-spanning order

## Statement

In the zero-slack |D|=k critical-core model one has |V(H)|=3k. With k=floor(2ell/3)+1, this equals 2ell+3, 2ell+1, or 2ell+2 according as ell is 0,1,2 mod3. Thus the forbidden P_ell would omit exactly 2,0,1 vertices respectively. Zero slack is therefore a spanning/all-but-one/all-but-two path problem, not a diffuse asymptotic configuration.

## Body

Assume the zero-slack extremal critical-core model 13500728c22f. Then |D|=k and the DXX color graph has |X|=2k vertices. Hence
  |V(H)|=|D|+|X|=3k.

Recall
  k=floor(2ell/3)+1.
Compare 3k with the 2ell+1 vertices used by a P_ell.

If ell=3m, then k=2m+1 and
  |V(H)|=6m+3=2ell+3.
Thus a P_ell would omit exactly two vertices.

If ell=3m+1, then k=2m+1 and
  |V(H)|=6m+3=2ell+1.
Thus a P_ell would be spanning.

If ell=3m+2, then k=2m+2 and
  |V(H)|=6m+6=2ell+2.
Thus a P_ell would omit exactly one vertex.

Therefore every zero-slack critical core lies at one of the three absolute critical orders n=2ell+1,2ell+2,2ell+3. In addition, zero slack itself requires 3|k by 380e96029ae8/dd3c7be64de2.

This recasts the zero-slack branch as a near-spanning path problem, directly analogous to the order-11/order-12 calibrations: the residue ell≡1 mod3 asks for a spanning path, ell≡2 asks for an all-but-one path, and ell≡0 asks for an all-but-two path. The one-factorized DXX layer plus the partition of X into forest triples is the extra structure available for this near-spanning problem.
