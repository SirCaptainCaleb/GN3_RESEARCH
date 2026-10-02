# Sharp half-order endpoint probes always expose support or order disagreement

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let A=(a_0,...,a_{lambda-1}) be globally longest. Choose arbitrary exact two-covers G_0 of H-a_0 and G_1 of H-a_{lambda-1}. Then the two endpoint probes necessarily expose explicit support/order disagreement: either some endpoint cover already has a relative-order reversal/reversing triple/tight-cycle witness against A, or the two endpoint covers induce different ordered two-cover states on their common two-end deletion. Equivalently, there is no completely order-compatible endpoint-crossing residue of any multiplicity in the sharp equality shell.

## Body

Put U=V(H)-V(A). Suppose first that one endpoint cover already orders two surviving A-vertices differently from A or supplies a tight triple reversing an ordered edge of A. Then the required ordered-disagreement witness is present, so assume neither endpoint cover does this.

Apply the position-lock theorem 09df8f30b6d6 to the left endpoint cover G_0. Its two lambda-vertex components have positions 0,...,lambda-1. In the no-disagreement branch, every surviving a_i, 1<=i<=lambda-1, occurs at position exactly i in whichever component contains it, and at each such position the other component contains a U-vertex. Let x_i record which component contains a_i.

We claim the ownership word x_1,...,x_{lambda-1} is constant. Suppose not, and let k be the first index with x_k != x_{k+1}. Let C=(c_0,...,c_{lambda-1}) be the component containing a_1, so
c_i=a_i for 1<=i<=k,
while c_{k+1} is a U-vertex.

Consider
S=(a_0,c_1,c_2,...,c_{lambda-1}).

All consecutive triples except possibly the first are inherited from C. If k>=2, the first triple is (a_0,a_1,a_2), inherited from A, so S is a tight path. If k=1, the only uncertain triple is (a_0,a_1,c_2). If it is non-tight, boundary antisymmetry gives (c_2,a_1,a_0) tight, explicitly reversing the ordered edge (a_0,a_1) of A, contrary to our standing assumption. Hence in the no-reversal branch that triple is tight and S is again a tight path.

Thus S is a globally longest path of order lambda, beginning with a_0,a_1. Because x_{k+1} differs from x_k, the vertex a_{k+1} does not occur in C at position k+1; by position-locking it occurs in the other component and therefore is exterior to S. The half-order longest-path barrier theorem bcfa72bc175f applies to S and the exterior vertex a_{k+1}, forcing
(a_1,a_0,a_{k+1})
tight. This again explicitly reverses the first ordered edge (a_0,a_1) of A, contradiction.

Therefore the left ownership word is constant. The crossing formula in 09df8f30b6d6 then gives exactly one A|U crossing in G_0.

The right endpoint is symmetric: under the same no-disagreement assumption its ownership word is constant and its crossing number is exactly one.

Now apply the certified two-end endpoint theorem 7b2d1a6cf904 to G_0 and G_1. Its one-crossing equality branch says that if both endpoint covers have exactly one crossing, the two endpoint probes expose support disagreement or relative-order disagreement on the common two-end deletion. This is precisely the desired conclusion.

Hence every pair of endpoint deletion probes of a globally longest path in the sharp half-order equality shell exposes explicit support/order disagreement. In particular all multiple-crossing neutral states are consumed: crossing multiplicity is no longer an unresolved branch in this shell. ∎