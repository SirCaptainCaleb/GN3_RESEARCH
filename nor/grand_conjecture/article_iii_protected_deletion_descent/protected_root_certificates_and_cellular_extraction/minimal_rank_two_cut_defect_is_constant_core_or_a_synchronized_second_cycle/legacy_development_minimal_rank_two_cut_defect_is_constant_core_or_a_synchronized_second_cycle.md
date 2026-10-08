# Repeated partners split the defect circulation but not the protected root cycle — preserved pre-item development

## Composition

(none yet)

## Development

For the endpoint-induced protected root cycle of root 84,
rho_i=e_{x_i}-e_{x_{i+1}},
with carrying cuts C_i={x_i,a_i}, the cut-defect vectors are
D_i=e_{a_{i+1}}-e_{a_i}
cyclically, so sum_i D_i=0.

If all a_i are equal, every D_i=0 and the attained rank-two cuts concatenate exactly along the physical root cycle.

If a partner value repeats nontrivially, say a_i=a_j with 0<j-i<k, then the DEFECT vectors on that interval telescope:
sum_{t=i}^{j-1} D_t=e_{a_j}-e_{a_i}=0.
Hence the secondary cut-defect circulation has a proper zero-sum subcirculation.

However the corresponding physical roots do not close:
sum_{t=i}^{j-1} rho_t=e_{x_i}-e_{x_j},
which is nonzero on a simple physical root cycle. Therefore this defect support reduction does NOT produce a shorter synchronized protected-root obstruction and must not be fed back into the protected carrier without an additional witness/gluing theorem.

The correct full-cycle dichotomy is only:
1. constant partner: zero cut defect and an exact one-token Johnson orbit C_i={a,x_i};
2. if the full cyclic partner word is pairwise distinct, then its defect walk a_0->a_1->...->a_{k-1}->a_0 is itself a simple coordinate cycle of the same length, synchronized index-by-index with the physical protected-root cycle;
3. otherwise the defect circulation decomposes into shorter abstract zero-sum pieces, but those pieces are not synchronized with closed physical root cycles.

Thus repeated partners simplify the secondary defect geometry but not automatically the original protected obstruction. The live extraction theorem must either preserve the chronological physical cycle while reducing defect, or transfer genuine protected provenance to one of the shorter defect subcycles.
