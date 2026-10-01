# Correction: reversible two-vertex pairs are vacuous and do not consume the cycle residue

## Statement

The statement of 850614657b07 is mathematically true but supplies no structural information: every ordered pair of distinct vertices is a tight path of order two in either orientation, so any pair is “reversible” in that weak sense. Therefore 850614657b07 must not be used as a bridge input. A meaningful reversed-edge witness must occur inside tight paths of order at least three (equivalently, the reversed pair must participate in actual tight triples on both sides, or lie on one displayed path and in a nontrivial reversing path). The pure tight-cycle outcome of aa6c87f1e473 is not eliminated by the two-vertex observation.

## Body

A tight path of order two has no consecutive triple, hence is tight vacuously. Thus for any distinct u,v both (u,v) and (v,u) are tight two-vertex paths, independently of all other structure. The conclusion of 850614657b07 therefore holds in every boundary tournament and cannot encode relative-order disagreement.

In the cycle arm of pathcalc01 one may indeed open the cycle to obtain a nontrivial tight path containing (v,u) and compare it with the two-vertex path (u,v), but the latter contributes no tight-triple data. Consequently endpoint-reversal consumers such as ac7bd525291b cannot be applied merely from this comparison. The live cycle residue remains the nontrivial cyclic support plus its complement obstruction family from f2bf5c6337c4.
