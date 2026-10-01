# Payment at one terminal does not yet supply payment at the minimum-rank terminal

## Statement

The certified extraction 9fba15f1495c provides payment at at least one terminal, not necessarily a minimum-rank terminal. Thus a sublinear bound requiring a paid certificate at the assigned minimum-rank terminal needs an additional transfer or mass estimate before applying 7e6abf77cbc5.

## Body

Let Epp be the extracted distinct edge family, with |Epp| >= (1/16-o(1))S. For each e choose a minimum-rank terminal m(e). Define A to consist of edges that admit a paid switching certificate at m(e), and B=Epp\A. A proposed local bound g(phi(v))=o(phi(v)) with payment required at v gives |A| <= sum_v g(phi(v))=o(S), by exactly the finite-threshold argument of 7e6abf77cbc5. It gives no estimate for B. In 9fba15f1495c, an edge is retained because it belongs to G_w for some terminal w. Both terminals have rank above the edge rank, but phi(w)<=phi(other terminal) is not established. Payment is defined relative to the chosen maximum path at w and its occupied cell; it is not an intrinsic assertion at both terminals. Therefore changing the assignment from w to m(e) preserves source-cleanliness, both terminal-single conditions and strict gaps, but does not by itself preserve payment at the assigned terminal.

The original conditional consumer remains valid if 'paid-certified' means certified somewhere and the assumed local bound covers that larger class. The stronger at-the-assigned-terminal hypothesis in the present research target is a different interface. Sufficient repairs are: prove |B|=o(S); prove |A|>=cS for some fixed c>0; transfer a certificate to a minimum-rank terminal; or prove the local bound without requiring payment at the assigned terminal. No realizable counterexample to transfer is claimed here. This is an exact missing implication, not a refutation of the four-edge spacing conjecture.
