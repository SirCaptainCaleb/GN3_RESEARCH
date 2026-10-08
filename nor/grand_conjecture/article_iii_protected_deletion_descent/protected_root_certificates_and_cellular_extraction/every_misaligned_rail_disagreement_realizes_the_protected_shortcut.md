# Every misaligned rail disagreement realizes the protected shortcut

## Composition

(none yet)

## Development

## Every misaligned rail disagreement realizes the protected shortcut

Continue with the crossed shortcut ladder
X_i=alpha(x,w_i,w_{i+1}),
Z_i=alpha(z,w_i,w_{i+1}),
R_i=alpha(x,z,w_i),
with
R_{i+1} xor R_i = X_i xor Z_i.

At a rail disagreement X_i != Z_i, the rung toggles: R_{i+1}=1-R_i.

There are two cases.

### Aligned disagreement: X_i=R_i

Then Z_i=R_{i+1}. In the ordering
(x,z,w_i,w_{i+1})
the two consecutive statuses are R_i,Z_i=R_i,1-R_i, while the off-faces are X_i=R_i and R_{i+1}=1-R_i. This is the fully-curved pattern. Its complete K22 square has source shore {x,z} and target shore {w_i,w_{i+1}}.

Thus an aligned disagreement is exactly a source-pair barrier.

### Misaligned disagreement: X_i!=R_i

Then X_i=R_{i+1} and Z_i=R_i. Consider instead
(x,w_i,w_{i+1},z).
Its two consecutive statuses are X_i and Z_i, hence R_{i+1},R_i, a transition. The two off-faces are
alpha(x,w_i,z)=R_i
and
alpha(x,w_{i+1},z)=R_{i+1}.
These are the opposite ordered pair, so the tetrahedron is fully curved.

Its source shore is {x,w_i} and its target shore is {w_{i+1},z}. Therefore its complete K22 square contains the actual protected root
x -> z.

Consequently, in any counterexample branch where the protected shortcut x->z is not realized, EVERY rail disagreement is forced to be aligned:
X_i=R_i and Z_i=R_{i+1}.

Equivalently every toggle of the pair signature R is itself a source-pair K22 barrier at the common cut {x,z}.
