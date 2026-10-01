# Some deletion cover is incompatible with half the family

## Statement

Under the hypotheses of d1572b057d93, some deletion label d is incompatible with at least floor((m-1)/2) of the other m-1 chosen deletion covers.

## Body

# Proof

Let G be the compatibility graph on the m deletion labels. By d1572b057d93,
e(G)<=floor(m^2/4)+1.
Hence the number I of incompatible pairs satisfies
I>=binom(m,2)-floor(m^2/4)-1.

If m=2r is even, then
I>=r(2r-1)-r^2-1=r^2-r-1.
Thus the average incompatible degree is at least
2I/m >= r-1-1/r.
Since incompatible degrees are integers, some vertex has incompatible degree at least r-1=floor((m-1)/2).

If m=2r+1 is odd, then
I>=r(2r+1)-r(r+1)-1=r^2-1.
The average incompatible degree is at least
2(r^2-1)/(2r+1)=r-(r+2)/(2r+1).
For r>=3 this is strictly greater than r-1, so some integer incompatible degree is at least r=floor((m-1)/2).

Therefore in every case m>=7 one chosen deletion cover is incompatible with at least floor((m-1)/2) others.
