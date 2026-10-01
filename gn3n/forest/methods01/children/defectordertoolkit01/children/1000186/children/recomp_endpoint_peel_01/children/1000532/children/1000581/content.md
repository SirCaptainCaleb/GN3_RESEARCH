# Correction: the two-end peel does not form a tight cycle

## Statement

The proof of a597270c938a is invalid, and consequently the dependent theorem 1a3877a3dbdb must not be used. In the connector-free branch, the tight path T=(q_s,p_0,...,p_r,q_0) and the original tight path Q=(q_0,...,q_s) are internally disjoint opposite corridors, but their union is not automatically a tight cycle: the cyclic splice triples (p_r,q_0,q_1) and (q_{s-1},q_s,p_0) are not supplied by either displayed path. In fact 70435ae42299 proves that both are necessarily non-tight, so their reverses (q_1,q_0,p_r) and (p_0,q_s,q_{s-1}) are tight. The correct connector-free residue is therefore the two-end peel plus two reverse cross hooks, not a contradiction.

## Body

A tight cycle obtained by gluing two opposite corridors requires the consecutive triples across both shared endpoints to be tight. T certifies triples internal to q_s,P,q_0, and Q certifies triples internal to q_0,Q^circ,q_s, but neither certifies (p_r,q_0,q_1) or (q_{s-1},q_s,p_0). Thus the cycle assertion in a597270c938a omitted two genuine conditions.

Moreover, if (p_r,q_0,q_1) were tight then the sequence
(q_s,p_0,...,p_r,q_0,q_1,...,q_{s-1})
would be a Hamilton path of H-x, contradicting pc(H)>2 after adding singleton {x}. Hence it is non-tight and (q_1,q_0,p_r) is tight. The symmetric argument gives non-tightness of (q_{s-1},q_s,p_0) and tightness of (p_0,q_s,q_{s-1}), exactly as in 70435ae42299.

Since 1a3877a3dbdb assumes the false unconditional connector conclusion of a597270c938a, it is also blocked pending a separate hypothesis that an actual connector exists.