# Pure alternating orientations have no two-element front circuits — preserved pre-item development

## Composition

(none yet)

## Development

Pure alternating triangle orientations admit no two-element fixed-tail support circuit. Fix an ordered tail F=(f_1,f_2) and a color tau. Suppose {x} and {y} are tau-feasible at F. Then alpha(x,f_1,f_2)=alpha(y,f_1,f_2)=tau. If {x,y} were minimally infeasible, neither ordering (x,y,F) nor (y,x,F) could be tau-tight. In the first ordering the second window alpha(y,f_1,f_2) is already tau, so failure forces alpha(x,y,f_1)=1-tau. In the second ordering the second window alpha(x,f_1,f_2) is tau, so failure forces alpha(y,x,f_1)=1-tau. But alpha is alternating, hence alpha(y,x,f_1)=1-alpha(x,y,f_1). The two forced equalities are impossible. Therefore every pair of tau-feasible singletons has at least one tau-tight two-element witness at the same tail.

Consequences. (1) Every minimal infeasible front circuit in the pure-orientation sector has size at least three. (2) The shifted two-circuit alternative from insertion sliding cannot occur when h=alpha; every failed internal insertion transition must instead be carried by the centered-triangle/backward-blocker alternative (or the separately audited protected-front wedge when applicable). (3) A pure-orientation counterexample cannot contain a monochromatic path missing exactly two vertices. The general two-hole cage would force alpha(x,y,v_1)=alpha(y,x,v_1)=sigma, immediately contradicting alternation.

Thus the smallest genuine pure-orientation obstruction is the three-element cyclic circuit, not the two-circuit. This sharply separates the pure alternating problem from the unrestricted reversal-odd problem.
