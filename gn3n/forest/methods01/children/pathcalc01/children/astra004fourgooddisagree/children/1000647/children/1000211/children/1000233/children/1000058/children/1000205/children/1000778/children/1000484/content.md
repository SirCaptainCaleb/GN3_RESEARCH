# A span-three omitted-label cross creates a Hamiltonian five-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover with P=(p_0,...,p_{m-1}). Suppose for some 0<=j<=m-4 the cross triple (p_j,x,p_{j+3}) is tight. Then the five-set W={p_j,p_{j+1},p_{j+2},p_{j+3},x} is Hamiltonian. Consequently H-W is non-Hamiltonian with path-cover number two. Thus the span-three consecutive-pair deletion branch of f05c3c78500c already enters the anchored Hamiltonian five-window frontier.

## Body

Put u=p_j, a=p_{j+1}, b=p_{j+2}, and v=p_{j+3}. The displayed path P contains the tight four-vertex corridor (u,a,b,v), while the hypothesis is exactly the tight three-vertex corridor (u,x,v). These two corridors are internally disjoint and have the same endpoints u,v. Certified 53d257fcf0a8 therefore gives Hamiltonicity of their five-vertex union W={u,a,b,v,x}. Since H is a minimum counterexample and W is proper, H-W cannot be Hamiltonian, for otherwise Hamilton paths on W and H-W would two-cover H. Minimum-counterexample calculus then gives path-cover number two for H-W.
