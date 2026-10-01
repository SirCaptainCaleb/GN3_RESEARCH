# Near-equality forces linearly many cross-period double contacts

## Statement

In the fixed-entrance setup of the periodic near-equality theorem 88db9b4e8337, suppose |J_q(v)|=M-r. After deleting O(r+1) exceptional cells and O(1) boundary cells, partition each remaining critical interval into disjoint full four-cell blocks following the period-four equality pattern. Let B be the number of such blocks. Then at least (B-u)/2 double contact sets have their two contact vertices in different blocks or have one endpoint outside the good-block union, where u is the number of unused contact vertices. Consequently there are at least q/8-O(r+1) such cross-period double contacts.

In the gap-one switching setup, put delta=M-(t-X_v^T). By f6c9ded0ae63, at most |J|-t<=delta of these cross-period doubles belong to edges outside the ascending-terminal family T, and at most X_v^T<=delta members of T remain double on the maximum path. After discarding both classes, at least q/8-O(delta+1) cross-period switching edges remain.

## Body

Each good four-cell block contains eight contact vertices. Along the critical transfer cycle its singleton weights are 0,0,2,1 up to phase, so exactly three vertices are singleton contacts. Thus five vertices in the block are nonsingleton. Internal double contact sets use vertices in pairs and therefore cover an even number of these five vertices. Hence every good block has at least one defect vertex which is either unused or belongs to a double contact set whose other contact lies outside that block. Summing this parity obligation over the B disjoint good blocks, unused vertices account for at most u obligations, while each double contact set crossing block boundaries or leaving the good-block union accounts for obligations in at most two blocks. Therefore the number D_cross of such double contacts satisfies B<=u+2D_cross, so D_cross>=(B-u)/2.

By 88db9b4e8337, at most O(r+1) transitions/cells are exceptional and u<=2r+1; deleting cells adjacent to noncritical transitions and taking full four-cell blocks leaves B=q/4-O(r+1). Hence D_cross>=q/8-O(r+1).

Now specialize to the gap-one setup and write delta=M-(t-X_v^T). By f6c9ded0ae63, |J|-t<=delta and X_v^T<=delta. Thus among the cross-period double contacts, at most delta belong to edges outside the ascending-terminal family T. Of the remaining T-edges, at most X_v^T<=delta are also double on the maximum path. Every other surviving edge is double on the anchor path and single on the maximum path, hence is a switching edge. Therefore at least q/8-O(delta+1) cross-period switching edges remain.
