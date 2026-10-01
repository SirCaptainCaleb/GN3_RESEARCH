# From order seventeen onward trapped quadratic minima have minimum side five or order disagreement

## Statement


Let H be a minimum counterexample of order n>=17, and let C=A|B|X be a spanning three-cover that minimizes the quadratic potential Phi within a connected pairwise-repartition component containing no cover with at most two components. If H contains no explicit order disagreement of the standard four-side type, then every component of C has order at least five.

Equivalently, any trapped Phi-minimal three-cover of order at least seventeen having a four-vertex component already forces explicit order disagreement.


## Body


Write a=|A|>=b=|B|>=c=|X|.

By d1e3453f5ffe, since n>=14 every component of a trapped Phi-minimal three-cover has order at least four. Hence c>=4.

Suppose c=4. Since a+b=n-4 and a>=b,
a >= ceil((n-4)/2) >= ceil(13/2)=7.

Apply a25b748fb338 to the four-vertex path X and the component A of order at least seven. That theorem gives either a legal pairwise repartition strictly decreasing Phi, or explicit order disagreement.

The strict-descent alternative contradicts the choice of C as Phi-minimal in its connected pairwise-repartition component. Therefore the order-disagreement alternative holds.

Consequently, if no such order disagreement is present, c cannot equal four, and hence c>=5.
