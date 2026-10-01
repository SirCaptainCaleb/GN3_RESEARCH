# The longest-path paired-noninsertion menu reduces from five outcomes to four

## Statement

Let P be a globally longest tight path and x,y distinct vertices outside P. Then at least one of four outcomes holds: (1) a Hamiltonian four-set using one of x,y and three consecutive vertices of P; (2) a Hamiltonian five-set using x,y and three consecutive vertices of P; (3) a tight cross triple (x,p_i,y) or (y,p_i,x); or (4) a direct tight interval connector from one of x,y through a nonempty subpath of P to the other. The exceptional cyclic-four-kernel alternative in a8c9883902b1 is redundant here because adjoining the other exterior vertex Hamiltonizes that four-set, yielding outcome (2).

## Body

Both x and y are noninsertable into P by global maximality, so a8c9883902b1 applies. Its only apparently extra alternative is the exceptional cyclic non-Hamiltonian four-set K consisting of one exterior label, say x, and three consecutive vertices of P, together with the assertion that adjoining any exterior vertex to K gives a Hamiltonian five-set. The other label y is exterior to K. Hence K∪{y} is Hamiltonian, exactly the five-set outcome already present in the menu. Thus only four coarse outcome types are needed. In particular a deterministic coloring of outside pairs uses four rather than five colors, improving the elementary density bound to at least one quarter of all outside pairs.