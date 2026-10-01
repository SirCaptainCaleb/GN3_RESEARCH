# A cyclic sharp-shell deletion transversal necessarily exposes ordered disturbance

## Statement

In the setup of ff3284e79394, suppose the selected support graph J is cyclic. Then J is its n-edge odd cycle, whose edges e_v have pairwise distinct omitted-vertex labels. For any choice of one Hamilton order on each support vertex of J, some length-two subwalk of J exposes the disturbance alternative of astra004oddcycledisturb: inherited three-part support crossing or relative-order disagreement. In particular the repeated-label alternative of that theorem cannot occur.

## Body

By ff3284e79394, the cyclic selected graph J is a simple odd cycle containing all n selected edges. By construction there is exactly one selected edge e_v for each ground vertex v, so the edge labels around this cycle are pairwise distinct.

Apply the certified odd-cycle disturbance theorem astra004oddcycledisturb to J with arbitrary chosen Hamilton orders on its support vertices. It gives either:
(I) a length-two subwalk with inherited three-part crossing or relative-order disagreement; or
(II) an index i for which the cycle-edge labels satisfy x_{i+3}=x_i.

Alternative (II) is impossible because distinct edges of J have distinct omitted-vertex labels. Therefore alternative (I) must occur. ∎
