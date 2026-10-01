# Every degree-three sharp-shell support star forces a disturbed two-edge walk

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1 with lambda>=3, and let G be its Hamiltonian-support odd graph. Suppose a Hamiltonian lambda-support S has three distinct neighbors T_x,T_y,T_z, where the incident edges are labelled x,y,z respectively. Choose arbitrary Hamilton orders on S,T_x,T_y,T_z. Then at least one of the three length-two walks
T_x-S-T_y, T_y-S-T_z, T_z-S-T_x
exposes a disturbance alternative of astra004twowalk: inherited three-part crossing or relative-order disagreement. Equivalently, the rigid same-end omission-swap alternative cannot hold simultaneously for all three walks.

## Body

Write R=V(H)-S. Then T_x=R-{x}, T_y=R-{y}, and T_z=R-{z}.

Assume for contradiction that all three displayed length-two walks take the rigid same-end alternative of astra004twowalk. For each label d in {x,y,z}, let F_d=T_d|S be the deletion cover of H-d using the chosen Hamilton orders.

Apply astra004twowalk to T_x-S-T_y. In the rigid alternative, after deleting y from T_x and x from T_y, the two induced covers of H-{x,y} coincide on the common support R-{x,y}, while the S-component is already identical. Hence F_x and F_y are compatible on their common domain. The same argument for the other two walks shows that F_x,F_y,F_z are pairwise compatible.

Now apply compattriangle01 to this compatible deletion triangle. The fixed support is S, and on the other support the three labels x,y,z are all inserted into one common gap of a common Hamilton order on
C=R-{x,y,z}.
Thus, in F_x, the two labels y,z occur consecutively in one gap of the order C.

On the other hand, the rigid alternative for T_x-S-T_y says y is an endpoint of the chosen Hamilton order on T_x. The rigid alternative for T_x-S-T_z says z is also an endpoint of that same chosen Hamilton order on T_x. Since y and z are distinct, they are the two endpoints of T_x.

But |C|=|R|-3=(lambda+1)-3=lambda-2>=1. Two consecutive labels inserted into one gap of a nonempty linear order cannot simultaneously be the two endpoints of the resulting order: if the gap is internal neither inserted label can occupy both ends; if the gap is an endpoint, at most one of the two consecutive inserted labels is an endpoint while the other is adjacent to the nonempty core.

This contradiction proves that at least one of the three two-edge walks is disturbed. ∎
