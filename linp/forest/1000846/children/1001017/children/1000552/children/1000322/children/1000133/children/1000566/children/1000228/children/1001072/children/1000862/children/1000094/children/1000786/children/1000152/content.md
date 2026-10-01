# Zero-slack two-component critical cores always have a free-end cross connector

## Statement

Assume the extremal |D|=k color-complete normal form and zero slack m+2c=2k. If c=2, then some colored connector joins a free end of one forest component to a private vertex of the other. Consequently, for ell congruent to 0 or 2 modulo 3, the c=2 zero-slack case is impossible in a P_ell-free counterexample.

## Body

Let the two forest components have lengths a,b, so
a+b=m=2k-4.

Suppose for contradiction that no free end of either forest component has a colored mate in the other component. In zero slack, 1663a127e081 says every colored edge pairs two forest-degree-one vertices.

Fix a free end x of the a-edge component. By c15cf7354428, x has exactly one incident edge of each of the k colors, and the k colored mates are pairwise distinct. Under the assumption, all k mates are forest-private vertices of the same component.

An a-edge linear path component has exactly a+2 forest-degree-one vertices. Excluding x itself leaves only a+1 possible private mates. Therefore
a+1>=k,
so a>=k-1.

Applying the same argument to a free end of the b-edge component gives
b>=k-1.

Hence
a+b>=2k-2,
contradicting a+b=2k-4.

Thus some free forest end has a cross-component colored mate. The bridge-versus-cycle lemma ec447521d952 then gives, in the good residue classes ell≡0 or 2 mod 3, a linear path of length at least ell exactly as computed in aec1f9026ce4. Therefore the c=2 zero-slack case is impossible there.
