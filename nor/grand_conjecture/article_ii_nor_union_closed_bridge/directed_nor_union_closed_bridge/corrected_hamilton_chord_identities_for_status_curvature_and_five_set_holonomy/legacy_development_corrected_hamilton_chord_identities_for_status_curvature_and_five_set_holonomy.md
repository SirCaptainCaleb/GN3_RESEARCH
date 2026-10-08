# Corrected Hamilton chord identities for status curvature and five-set holonomy — preserved pre-item development

## Composition

(none yet)

## Development

Work in the coboundary-flat alternating ternary sector with the convention
alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a),
t(v,u)=1 xor t(u,v).
Switch a tournament representative so every adjacent edge of a chosen LINEAR order points forward, meaning t(v_i,v_{i+1})=1. Write x_i=t(v_i,v_{i+2}) and z_i=t(v_i,v_{i+3}).

Status identity: alpha(v_i,v_{i+1},v_{i+2})=x_i.

For a,b,c,d consecutive, direct substitution gives
alpha(a,b,d)=1 xor x_{i+1} xor z_i,
alpha(a,c,d)=1 xor x_i xor z_i.
Thus kappa_i=alpha(a,b,d) xor alpha(a,b,c)
=1 xor x_i xor x_{i+1} xor z_i.
At a transition x_i xor x_{i+1}=1, this reduces to kappa_i=z_i.

Therefore a transition is fully curved iff z_i=1 (the distance-three chord is forward), and flat iff z_i=0 (the chord is backward). This agrees with §147 and corrects the missing constant in §139. The claims in §§140,142,145 that depend on the opposite convention require rederivation; their other arguments are not audited here.

For a double-full singleton on 0,1,2,3,4 with statuses 0,1,0, the full boundaries force t(0,3)=t(1,4)=1. Its residual bit h=alpha(0,1,4) therefore satisfies
h=1 xor 1 xor 1 xor (1 xor t(0,4))=t(0,4).
So h is the distance-four chord bit, rather than its complement as asserted in §165. With these conventions the two-sided tau=1 resolution occurs at h=1, hence a FORWARD distance-four chord. The opposite chord exports a boundary mismatch.

These are identities, not a closure theorem. They should be used as a single consistent convention before combining chord transport with full-curvature surgery.
