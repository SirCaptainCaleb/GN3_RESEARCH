# Six neutral wraps reach a Hamiltonian support or a doubled endpoint barrier

## Statement

Continue the six-clean-wrap arithmetic-progression residue of 748392026c03. Write the resulting common-middle square over M=B_0 with left corner labels b_1,a_2 and right corner labels b_q,a_{p-1}. Then either W=V(B_0) union {b_1,a_2,b_q,a_{p-1}} is Hamiltonian, in which case H-W is non-Hamiltonian of path-cover number exactly two, or one endpoint side has a doubled reverse barrier: either both (m_1,a_2,b_1) and (m_1,b_1,a_2) are tight, or both (a_{p-1},b_q,m_h) and (b_q,a_{p-1},m_h) are tight, where B_0=(m_1,...,m_h). Thus six clean neutral wraps already reach a Hamiltonian-support/complement interface or an explicit doubled local barrier.

## Body

By 748392026c03, after six clean wraps the four paths (b_1,M,b_q), (b_1,M,a_{p-1}), (a_2,M,b_q), and (a_2,M,a_{p-1}) are all tight. Apply the common-middle-square dichotomy e7ae8b93ef41 with a=b_1, ell=a_2, c=b_q, and r=a_{p-1}. It gives exactly the three alternatives in the statement: Hamiltonicity of the full square support W, the doubled left reverse barrier, or the doubled right reverse barrier. In the Hamiltonian branch W is proper in the minimum counterexample H. Its complement cannot be Hamiltonian, since a Hamilton path on W together with one on H-W would two-cover H. By minimum-counterexample minimality, H-W has path-cover number at most two, hence exactly two.
