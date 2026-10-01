# Path-cover number above two forbids three isolated cyclic defects in every span-three ordering

## Statement

Let H be any boundary tournament with pc(H)>2, and let pi=(v_1,...,v_n) be a spanning ordering of defect span three. Then the cyclic defect graph associated with pi cannot have run type {1,1,1}. Thus exclusion of the three-isolated-defect geometry uses only pc(H)>2; no minimum-order hypothesis is required.

## Body

Let i be the leftmost defect center and put x=v_{i+1}, P=(v_1,...,v_i), Q=(v_{i+2},...,v_n). Because every defect center lies among i,i+1,i+2, every consecutive triple internal to P or Q is tight, so H-x=P|Q. Since pc(H)>2, the two outer joins through x are defective: if either were tight, x could be absorbed into the corresponding path and the other path would give a two-cover.

Form the cyclic defect graph Gamma of the cyclic order P,x,Q. The three path boundaries of P|{x}|Q form a vertex cover of Gamma, so tau(Gamma)<=3. If tau(Gamma)<=2, cutting at such a cover gives a two-cover of H by cyclic tight intervals, contrary to pc(H)>2. Hence tau(Gamma)=3.

Suppose Gamma had run type {1,1,1}. By 2923b2b2b233 its eight minimum cut sets form the full three-cube of three-covers, and by 810c33003128 their component orders have the form s_j=g_j+x_{j+1}-x_j cyclically. Choose the zero state to be the displayed singleton lift P|{x}|Q. One component then has order g_j=1. Set x_j=1 and x_{j+1}=0, leaving the third bit arbitrary. The formula gives s_j=0, contradicting that every cube state is a three-cover with nonempty components. Therefore Gamma is not {1,1,1}.
