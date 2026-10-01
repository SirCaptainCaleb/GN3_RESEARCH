# All three all-equal support paths have explicit endpoint-edge reversals

## Statement

Assume the all-equal {1,1,1} support-triangle normalization, with P_i=(t_i,M_i,t_{i+1}) and M_i beginning at b_i and ending at a_i. Then every displayed support path P_i has an explicit initial-edge reversing triple: (b_i,t_i,a_{i-1}) is tight. Thus all three support paths simultaneously lie in the endpoint-edge-reversal interface, independently of whether any transferred-label insertion succeeds.

## Body

The initial ordered edge of P_i is (t_i,b_i). The certified synchronized-boundary theorem aff724a01002 gives the tight triple (b_i,t_i,a_{i-1}) for every i modulo three. In the terminology of pathcalc01, a tight triple (x,y,z) reverses an ordered edge of P when (y,x) or (z,y) is that ordered edge. Here (y,x)=(t_i,b_i), exactly the initial ordered edge of P_i. Hence (b_i,t_i,a_{i-1}) reverses the initial edge of P_i for each i. Applying cyclically gives simultaneous endpoint-edge reversals on all three supports. No insertion hypothesis is used.