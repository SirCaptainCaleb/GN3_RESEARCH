# A witnessed product-cell Brouwer carrier removes the averaging provenance gap — preserved pre-item development

Work in ternary arity under counterexamplehood on the switch prism X=P_V x I, with target space W direct-sum R. Use the natural polytopal cell structure whose cells are F x J, with F a permutahedron face and J either a cut vertex or a cut interval. Barycentrically subdivide this cell structure.

Choose ONE genuine bad switch state q_C incident with every cell C, and label the barycenter of C by one genuine violating-window label L_C=(rho_C,s_C) from q_C. For interior cells the choice is arbitrary. On boundary cells choose it as follows.

1. Vertical cap cells F x {k_min} or F x {k_max}. At an extreme cut all ternary windows lie on the same threshold side. Counterexamplehood forbids a monochromatic spanning order, so every incident full order has a violating window. Choose one. Its side coordinate s has the fixed cap sign, hence pairs strictly with the inward vertical normal after fixing the global sign convention.

2. Horizontal side cells F x I with F a proper permutahedron face. Choose a NOR-good order on every proper block of F and concatenate them in F-block order. The resulting ambient full order is bad, so its ternary word has an actual 10 transition crossing F-blocks. Put the switch between the two transition windows. Both windows violate the 0|1 target. If their coordinate block ranks are a<=b<=c<=d with a<d, then at least one of the two window roots e_{v_i}-e_{v_{i+2}} or e_{v_{i+1}}-e_{v_{i+3}} crosses F strictly; otherwise a=c and b=d would force a=b=c=d. Choose a violating window with strict crossing root.

3. Mixed boundary cells F x {k_extreme} need no extra physical strictness: choose a cap violation as in (1). The vertical normal component is already strict, while its physical component is irrelevant to boundary separation.

Now consider a barycentric boundary simplex C_0<...<C_m=G. Every state chosen on a smaller cell C_i is incident with C_i and therefore lies in the largest cell G. If G is a horizontal side F x I, every chosen physical root is weakly forward in the F-block order and the label chosen for G is strictly forward. Pairing with the F-block normal is therefore strictly one-signed on the relative interior of the flag simplex. If G lies on a vertical cap, every chosen state has the same cap side sign, so the vertical coordinate is strictly one-signed. Thus the affine boundary carrier is zero-free.

The same largest-face normal gives a zero-free straight homotopy to the standard inward normal carrier on the boundary. Hence the normalized boundary map has the nonzero Brouwer degree of the inward radial map.

Extend affinely over the full barycentric subdivision using the chosen genuine cell labels. Nonzero boundary degree forces an interior zero.

Crucially, if a zero lies in a barycentric simplex C_0<...<C_m, every vertex label is ONE genuine violating state and all those states lie in the common largest product cell C_m. Therefore every support-minimal positive dependence extracted from this zero has exact same-cell state provenance; no expansion of averaged labels is needed.

This witnessed carrier repairs the averaging/provenance defect of the older switch-prism construction. It is not required to be antipodally odd: ordinary Brouwer degree follows from boundary face-normal separation.

Consequences. All existing same-cell extraction theorems can be applied literally to support-minimal zeros of this carrier. Lower-dimensional removable circuits may be handled by their proved same-cell blow-ups. Any surviving connected spanning bicyclic circuit is now represented by distinct genuine carrier vertices rather than hidden inside averages, so domain-dimension and vertical-edge arguments become available after the lower-dimensional zero-removal step.

This theorem does not yet show that the final controlled repair closes NOR; it supplies the missing compatible topological carrier on which such a closure argument can legitimately operate.
