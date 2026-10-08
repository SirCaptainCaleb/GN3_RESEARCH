# Codimension-one affine change images contain a good geodesic

## Development

Statement:
Fix n>=4 and a coordinate order p of the n coordinate moves. Suppose each ordered-three-face color on this order is an affine Boolean function of the starting vertex x in F_2^n (for example every c(F,pi) is affine in fixed exterior bits). Let w_p(x) in F_2^{n-2} be the window colors, and let Delta_p(x)=(w_1+w_2,...,w_{n-3}+w_{n-2}) be the change-indicator vector, with additions in F_2. If the linear part of the affine map Delta_p has rank at least n-4, there is a start x for which the order p has at most one color change. In particular in dimension n=6 a failed fixed order must have change-map rank at most one.

Proof:
Set r=n-3. The image of Delta_p is a nonempty affine subspace of F_2^r of dimension equal to the rank. If its dimension is r, it contains the zero vector. If its dimension is r-1, it is an affine hyperplane H={z: lambda dot z=b} for some nonzero lambda. If b=0 then 0 in H. If b=1, choose any coordinate i with lambda_i=1; the unit vector e_i lies in H. Thus some change vector has Hamming weight zero or one and the associated antipodal geodesic succeeds. This criterion requires neither oddness nor any special coefficients beyond affine dependence. It strengthens the full-row-rank monochromatic affine criterion already in the foundations.
