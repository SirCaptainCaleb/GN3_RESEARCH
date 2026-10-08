# The exceptional 11 width-two type is the rigid six-set and forces a left double-full packet — preserved pre-item development

## Development

## The exceptional (r,s)=(1,1) width-two type is exactly the rigid six-set

Continue with the exact lexicographic width-two table of §264. Set
\[
r=s=1.
\]
Then the table becomes
\[
abc=0,quad abd=abe=abf=1,
\]
\[
acd=ace=acf=0,
\]
\[
ade=1,quad adf=0,quad aef=1,
\]
\[
bcd=bce=bcf=bde=bef=1,quad bdf=0,
\]
\[
cde=1,quad cdf=0,quad cef=1,quad def=0.
\]

In particular, for each \(x\in\{d,e,f\}\),
\[
\alpha(a,b,x)=1,qquad
\alpha(a,c,x)=0,qquad
\alpha(b,c,x)=1,
\]
and the right-hand four-set values are exactly
\[
cde=1,quad cdf=0,quad cef=1,quad def=0.
\]

After relabeling \((a,b,c,d,e,f)=(0,1,2,3,4,5)\), this is precisely the rigid six-set table of §221. Therefore every local consequence of that table, including the stronger §226 weave, is available without importing any maximal-threshold-band rotation argument.

### Apply the stronger weave

Replace
\[
(a,b,c,d,e,f)
\]
by
\[
(a,d,b,c,e,f).
\]
Its internal word is
\[
0,1,1,1.
\]
It preserves the first coordinate \(a\) and the ordered final pair \((e,f)\). Hence the right exterior is fixed exactly and only one immediate left crossing bit can change.

Write the old ambient prefix as
\[
\ldots,p,q,a,b,c,d,e,f,\ldots
\]
when two left exterior coordinates exist, and put
\[
z:=\alpha(q,a,d).
\]
The farther crossing window \(\alpha(p,q,a)\) remains unchanged and equals zero in the old leading zero run.

If \(z=0\), the new full order is still of the form
\[
0^A1^{B'}0^{C'}
\]
with the same leading zero run and \(B'\ge3>2\), contradicting lexicographic maximality.

Therefore every exceptional extremal state has
\[
\boxed{z=1.}
\]

By §226 the five consecutive coordinates
\[
(q,a,d,b,c)
\]
then carry the exact double-full singleton word
\[
1,0,1.
\]

### Corrected width-two frontier

The lexicographically extremal width-two branch is now rigorously reduced as follows, entirely within its own admissible state class:

- if \((r,s)\ne(1,1)\), §265 gives the forced right reconnection kernel \(01\);
- if \((r,s)=(1,1)\), the local table is exactly rigid and the §226 weave forces a double-full \(101\) packet on the left.

Thus every width-two extremal state exports one of two explicit singleton reconnection kernels on a specified side. No unconstrained six-coordinate residue remains.
