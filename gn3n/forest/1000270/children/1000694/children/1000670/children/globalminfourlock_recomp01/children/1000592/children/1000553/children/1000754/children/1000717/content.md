# A global quadratic minimum with a four-side yields a Hamiltonian kernel or doubled cross barriers at both middle labels

## Statement

Let H be a minimum counterexample and let X=(x_0,x_1,x_2,x_3)|P|Q be a globally Phi-minimal spanning three-cover with |P|,|Q|>=6. Then either H contains a proper Hamiltonian induced set W of order four or five such that H-W is non-Hamiltonian with path-cover number two, or both middle labels x_1 and x_2 carry doubled cross barriers across P and Q: for each k in {1,2} there exist p_k in V(P), q_k in V(Q) such that both (q_k,p_k,x_k) and (p_k,q_k,x_k) are tight.

## Body

Apply e72075d064f9 to x_1. If its Hamiltonian-kernel alternative occurs, the first conclusion follows. Otherwise there exist p_1 in P and q_1 in Q with both (q_1,p_1,x_1) and (p_1,q_1,x_1) tight. Apply e72075d064f9 independently to x_2. Again, if its Hamiltonian-kernel alternative occurs, the first conclusion follows. Otherwise there exist p_2 in P and q_2 in Q with both (q_2,p_2,x_2) and (p_2,q_2,x_2) tight. Thus if no Hamiltonian four- or five-support has already appeared, both middle labels carry doubled cross barriers. No claim is made that these cross barriers satisfy the different neighbor-anchored hypotheses of f193331ec40f.