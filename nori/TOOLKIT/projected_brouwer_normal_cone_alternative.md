# Projected Brouwer normal-cone alternative

**Summary:** Project x-epsilon V(x) back to a convex polytope and apply Brouwer. A fixed point is either a zero of V or a boundary point where V is normal to a supporting face. This gives a parity-free fixed-point alternative useful for carrier-support descent.

## Statement

Let Q be a nonempty compact convex polytope in a Euclidean space and V:Q->E continuous. Then there exists x in Q such that -V(x) lies in the normal cone N_Q(x). In particular either x is interior and V(x)=0, or x is on a proper face and V(x) has inward normal sign against every feasible direction.

## Body

## Theorem

Let Q be a nonempty compact convex polytope in a Euclidean space E, and let V:Q->E be continuous. For any epsilon>0 define

T_epsilon(x)=Proj_Q(x-epsilon V(x)),

where Proj_Q is Euclidean nearest-point projection.

Then T_epsilon has a fixed point x, and every such fixed point satisfies

-V(x) in N_Q(x),

where

N_Q(x)={n:<n,z-x><=0 for every z in Q}

is the outward normal cone.

Equivalently,

<V(x),z-x> >= 0

for every z in Q.

## Proof

Metric projection onto a nonempty compact convex set is continuous, so T_epsilon:Q->Q is continuous. Brouwer gives x=T_epsilon(x).

The characterization of metric projection says that p=Proj_Q(q) exactly when

<q-p,z-p><=0

for every z in Q.

Take p=x and q=x-epsilon V(x). Dividing by epsilon>0 yields

<-V(x),z-x><=0

for every z in Q, which is the claimed normal-cone condition.

If x is in the relative interior of Q, its normal cone inside aff(Q) is {0}, so the tangential component of V vanishes; when V takes values in the direction space of aff(Q), this gives V(x)=0.

If V is zero-free in the relative interior, every projected Brouwer fixed point lies on a proper face.

## Why this complements hairy ball

Hairy ball forces a tangential zero on an even-dimensional sphere and therefore has a parity condition. Projected Brouwer instead uses convexity and gives a zero-or-normal-face alternative in every dimension.

The price is different: one needs a continuous field on the whole convex carrier Q, not merely on its boundary, and a boundary normal point is weaker than a vector zero. In applications where boundary faces represent strictly smaller carrier support, the normal alternative can be used as an induction or localization mechanism.

## NOR relevance

For Article III, take Q to be a convex hull of attained protected p-cuts inside the centered hypersimplex. A protected root is a hypersimplex edge vector z_C-z_C', and the side/full-cut perturbations remain in the same type-A space. If a continuous protected-state field V can be built on Q and algebraic perturbations exclude interior zeroes, projected Brouwer forces V to a proper face of Q. A closure argument may then minimize Q and try to show that such a proper-face normal state either realizes the forced Johnson exchange, enlarges the threshold band, or contradicts minimal carrier support.

This theorem does not supply the protected-state field or prove that normal-face localization preserves all provenance.

## Metadata

- ID: projected_brouwer_normal_cone_alternative
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
