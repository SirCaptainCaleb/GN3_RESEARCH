# From order eighteen onward trapped quadratic minima have minimum side six or order disagreement

## Statement

Let H be a minimum counterexample of order n>=18, and let C=A|B|X be a spanning three-cover minimizing the quadratic potential Phi within a connected pairwise-repartition component containing no cover with at most two components. Then either H contains explicit order disagreement, or every component of C has order at least six.

## Body

Assume no explicit order disagreement is present. By the certified order-seventeen normalization 5ca0bb01c7c0, every component of C has order at least five.

Write a>=b>=c for the three component orders. Suppose c=5. Since n>=18,
a+b=n-5>=13,
so a>=7. Let X be the five-vertex component and A the component of order a.

The cover C is Phi-minimal in its connected pairwise-repartition component. Therefore the five-side endpoint theorem 83353015664a applies to X|A|B and forces explicit relative-order disagreement at each displayed endpoint of A, contrary to assumption.

Hence c cannot equal five. Therefore c>=6.
