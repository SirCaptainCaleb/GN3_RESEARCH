# Failure of both central balanced restorations forces a Hamiltonian five-window across the cut

## Statement

In case (3) of c9a565669909, write the Hamilton path of K-x as P=(v_1,...,v_{2r-1}), r>=3, with central vertex m=v_r. Put a=v_{r-2}, b=v_{r-1}, d=v_{r+1}, and e=v_{r+2}. Then at least one of the five-sets {a,b,m,d,x} and {b,m,d,e,x} is Hamiltonian. If the first is non-Hamiltonian, the second has the explicit Hamilton order (x,b,m,d,e); if the second is non-Hamiltonian, the first has the explicit Hamilton order (a,b,m,d,x). Thus simultaneous failure of the two balanced central restorations always creates a bounded Hamiltonian five-window straddling the central cut.

## Body

Case (3) of c9a565669909 says x is noninsertable into both L=(v_1,...,v_{r-1}) and R=(v_{r+1},...,v_{2r-1}). In particular, appending x to L fails, so (a,b,x) is non-tight and boundary antisymmetry gives (x,b,a) tight. Prepending x to R fails, so (x,d,e) is non-tight and (e,d,x) is tight. The five consecutive vertices (a,b,m,d,e) form an inherited tight path of P. Apply the opposite-reverse-hook five-window lemma to this five-path and x. Its two outer five-windows are exactly {a,b,m,d,x} and {b,m,d,e,x}, with the stated explicit orders in the corresponding non-Hamiltonian opposite branch.