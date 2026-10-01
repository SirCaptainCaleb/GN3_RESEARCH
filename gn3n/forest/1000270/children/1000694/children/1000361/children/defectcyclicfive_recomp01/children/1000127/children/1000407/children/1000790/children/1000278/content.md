# Every nonuniform equitable matching cube has a three-step neutral transport from one antipode to the other

## Statement

Assume the base profile g of a {1,1,1} cube is equitable but not all equal. Then the two antipodal equal-profile states 000 and 111 are joined inside the cube by a path of three singleton transfers, every one of which is Phi-neutral. Along this path the component-order multiset is constant: {r+1,r,r} when n=3r+1, or {r+1,r+1,r} when n=3r+2. Each step transfers one vertex from a component of order r+1 to one of order r, so the exceptional component-size label moves cyclically through the three component positions. At the end all three cuts have shifted to the opposite endpoints of their isolated defect edges while the ordered base size profile is restored.

## Body

By cyclic relabeling suppose first g=(r+1,r,r). The size formula gives
000:(r+1,r,r),
100:(r,r,r+1),
101:(r,r+1,r),
111:(r+1,r,r).
Thus 000-100-101-111 is a cube path, each edge flips one bit, and each size change is a transfer r+1 -> r. The transfer formula gives Delta Phi=2(r-(r+1))+2=0 at each step. For g=(r+1,r+1,r), similarly
000:(r+1,r+1,r),
100:(r,r+1,r+1),
110:(r+1,r,r+1),
111:(r+1,r+1,r),
so 000-100-110-111 is the desired neutral path. Other placements of the exceptional size follow by cyclic relabeling. The endpoint statement is exactly the interpretation of 000 versus 111 in the cut-bit parametrization.
