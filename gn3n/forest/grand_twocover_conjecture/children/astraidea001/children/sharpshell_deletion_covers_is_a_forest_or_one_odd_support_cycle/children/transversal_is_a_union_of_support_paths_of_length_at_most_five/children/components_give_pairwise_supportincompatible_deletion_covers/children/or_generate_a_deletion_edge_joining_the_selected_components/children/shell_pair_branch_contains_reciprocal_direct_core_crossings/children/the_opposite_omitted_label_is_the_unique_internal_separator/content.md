# A fully crossed deletion pair gives a second direct crossing unless the opposite omitted label is the unique internal separator

## Statement

Let H be in the sharp half-order shell and let F_a,F_b be two lambda|lambda deletion covers as in c30a4d92d20b. On U=V(H)-{a,b}, write the induced support partitions as A|B for F_a and C|D for F_b, with all four intersections nonempty. Label so that in F_a the component containing b restricts to support A and the component avoiding b has support B. Then the B-component contains an ordinary U-edge crossing C|D. Moreover exactly one of the following holds for the A-component of F_a:
(i) it also contains an ordinary U-edge crossing C|D;
(ii) b is internal in that path, deleting b splits it into exactly two nonempty contiguous subpaths, one supported on A∩C and the other on A∩D. In particular b is the unique separator between the two C|D classes along that component.
The symmetric assertion holds with a,b and A|B,C|D interchanged.

## Body

The first assertion is c30a4d92d20b.

Let R be the component of F_a containing b, so V(R)-{b}=A. Because A∩C and A∩D are both nonempty, vertices of both C|D classes occur in R after b is deleted.

Assume R contains no ordinary edge with both endpoints in U crossing C|D. If b were an endpoint of R, then R-b would remain one contiguous path on all of A. Reading that path from one end to the other, both C and D occur, so some consecutive pair would cross C|D, contradiction. Hence b is internal.

Deleting the internal vertex b splits R into exactly two nonempty contiguous subpaths R_1,R_2. By assumption neither subpath contains a C|D crossing edge, so every vertex of each R_i lies in a single one of C,D. Since together they cover A and both A∩C and A∩D are nonempty, one subpath has support A∩C and the other support A∩D. Thus b is the unique separator between the two classes along R.

If R does contain a direct U-edge crossing C|D, we are in (i). The symmetric statement follows by interchanging the two deletion covers. ∎