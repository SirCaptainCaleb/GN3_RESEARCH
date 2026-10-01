# Zero-slack two-component critical cores are impossible in the good residues

## Statement

In the zero-slack |D|=k critical-core setting m+2c=2k with c=2, some physical forest endpoint must have a colored connector into the other component. Consequently, for ell congruent to 0 or 2 modulo 3, the physical-bridge lemma yields P_ell and the case is impossible.

## Body

Assume the zero-slack |D|=k critical-core setting m+2c=2k and c=2. Let the two forest components have lengths a,b, so
  a+b=m=2k-4.

By 1663a127e081, every colored DXX edge pairs two forest-private vertices. Hence every physical endpoint x of either component has exactly one incident colored edge of each color d in D, and the k corresponding mates are distinct forest-private vertices.

Suppose, for contradiction, that every physical endpoint has all k colored mates inside its own component. Choose one physical endpoint x in the a-edge component. That component has exactly a+2 forest-private vertices, so there are only a+1 possible private mates other than x. Since the k colored mates are distinct,
  a+1>=k,
hence a>=k-1.

Likewise, choosing a physical endpoint in the b-edge component gives
  b>=k-1.
Therefore
  a+b>=2k-2,
contradicting a+b=2k-4.

Thus some physical endpoint has a colored mate in the other component.

By aec1f9026ce4, in the good residue classes ell congruent to 0 or 2 mod 3, any such physical cross connector creates a P_ell. Therefore the zero-slack c=2 case is impossible in those residue classes.
