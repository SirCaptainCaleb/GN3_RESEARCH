# In the order-eleven design branch every Hamiltonian four-set outside the Steiner family is extendable

## Statement

Let H be a hypothetical order-eleven minimum counterexample, X a three-set, U=V(H)-X, and suppose the no-blocked-overlap branch of order11_design_boolean_recomp01 holds, producing the 14-block 3-(8,4,1) family F of blocked Hamiltonian four-sets. Then every Hamiltonian four-set C subset U with C not in F satisfies that H[X union C] is Hamiltonian. Moreover, with D=U-C, D is non-Hamiltonian and every H[X union C union S], for nonempty proper S subset D, is non-Hamiltonian with path-cover number two. Thus the Boolean-shell conclusion holds for all Hamiltonian four-sets outside F, not merely for a selected set of fourteen centers.

## Body

Fix any Hamiltonian four-set C outside F. Each triple T of C lies in a unique block A_T of the 3-(8,4,1) family F, and the four A_T are distinct. If X union C were non-Hamiltonian, then C and any A_T would be two Hamiltonian four-sets meeting in three vertices whose unions with X are both non-Hamiltonian, contradicting the no-blocked-overlap branch. Hence X union C is Hamiltonian. Put D=U-C. If D were Hamiltonian, Hamilton paths on X union C and D would form a spanning two-cover of H, impossible. Therefore D is non-Hamiltonian, and fourset_boolean_pc2_01 applied to D gives the full punctured Boolean shell around X union C. The previous theorem's pair-incidence argument separately guarantees that at least fourteen such outside Hamiltonian centers exist.