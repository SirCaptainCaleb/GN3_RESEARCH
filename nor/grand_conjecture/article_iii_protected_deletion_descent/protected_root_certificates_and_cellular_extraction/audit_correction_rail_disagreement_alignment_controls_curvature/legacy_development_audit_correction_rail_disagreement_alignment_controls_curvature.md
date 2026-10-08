# Audit correction: rail disagreement alignment controls curvature — preserved pre-item development

## Composition

(none yet)

## Development


The preceding subsection 322 contains an orientation mistake: alpha(x,w_i,z)=1-R_i, not R_i. The corrected local dichotomy is as follows.

At a disagreement X_i!=Z_i, one has R_{i+1}=1-R_i.

If X_i=R_i, then Z_i=R_{i+1}. In the order (x,z,w_i,w_{i+1}) the status transition is fully curved, with source shore {x,z} and target shore {w_i,w_{i+1}}.

If X_i!=R_i, then X_i=R_{i+1} and Z_i=R_i. In the order (x,w_i,w_{i+1},z) the local statuses are R_{i+1},R_i. Alternation gives the off-faces 1-R_i and 1-R_{i+1}, so the transition is flat. Swapping the first pair yields equal local statuses R_i,R_i; swapping the last pair yields equal local statuses R_{i+1},R_{i+1}. Thus the misaligned case is a two-sided flat transition-removal cell, not a direct protected shortcut.

The valid dichotomy is therefore: aligned disagreement = source-pair K22 barrier; misaligned disagreement = flat cell with repairs available toward either side.
