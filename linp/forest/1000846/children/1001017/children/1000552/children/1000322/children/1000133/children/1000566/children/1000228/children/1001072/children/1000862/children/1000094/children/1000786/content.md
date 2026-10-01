# Zero-slack critical cores with at most two forest components are impossible in the good residues

## Statement

Assume the extremal |D|=k color-complete normal form and the zero-slack case m+2c=2k. If c=1, then H contains P_ell for every ell>=4. If c=2 and ell is congruent to 0 or 2 modulo 3, then H also contains P_ell. Hence no P_ell-free minimal counterexample in either good residue class can have |D|=k, zero slack, and at most two components in H-D.

## Body

In the zero-slack case m+2c=2k, 1663a127e081 shows that every d-colored edge pairs two forest-degree-one vertices.

If c=1, the unique forest component has m=2k-2 edges. For ell>=4 and k=floor(2ell/3)+1 one has 2k-2>=ell, so the forest itself contains P_ell.

Now let c=2, with component lengths a>=b. Then a+b=2k-4.

We claim that some colored connector joins a free end of one component to a private vertex of the other. Suppose not. Choose any free end x of the a-edge component. In zero slack x has one incident connector of each color d in D, and all k mates are forest-private. Linearity makes those k mates pairwise distinct. Under the supposition they all lie in the same a-edge component, which has exactly a+2 forest-private vertices including x. Hence a+1>=k, so a>=k-1. Applying the same argument to a free end of the b-edge component gives b>=k-1. Thus a+b>=2k-2, contradicting a+b=2k-4.

Therefore there is a connector f={d,x,y} with x a free end of one component, say the a-edge component, and y a forest-private vertex of the b-edge component. Orient the entire a-component to end at x. Since y is private to a path edge of the b-component, the precise path-position bound in 8b1790d79d74 gives a b-component subpath of length at least ceil((b+1)/2) ending at y. Reversing that subpath and inserting f yields a linear path of length at least
  a+1+ceil((b+1)/2).

Because a>=b and a+b=2k-4, this expression is minimized at b<=k-2.

If ell=3r, then k=2r+1, so b<=2r-1 and the path has length at least
  (2r-1)+1+r=3r=ell.

If ell=3r+2, then k=2r+2, so b<=2r and the path has length at least
  2r+1+(r+1)=3r+2=ell.

Thus H contains P_ell in both good residue classes, contradiction.