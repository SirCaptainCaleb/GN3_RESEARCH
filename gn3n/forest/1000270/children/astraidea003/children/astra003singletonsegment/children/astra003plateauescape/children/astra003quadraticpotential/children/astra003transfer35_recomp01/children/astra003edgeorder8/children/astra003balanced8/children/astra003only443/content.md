# Balanced order eight reduces every quadratic-minimal 3-side state to 4|4|3 at order eleven

## Statement

Let H be a minimum counterexample and let A|B|C be a Phi-minimal spanning three-cover in a trapped Astra-003 component with |A|>=|B|>=|C|=3. Then |V(H)|=11 and the component-order multiset is {4,4,3}.

## Body

Let
[
A|B|C
]
be a quadratic-potential minimum in a trapped Astra-003 component of a minimum counterexample, with
[
|A|ge |B|ge |C|=3.
]

The certified small-side reduction d1e3453f5ffe gives
[
|A|,|B|le5.
]

If either (A) or (B) had order five, its union with (C) would have order eight. By astra003balanced8, every eight-vertex boundary tournament has an exact (4|4) two-cover. Repartitioning that (5|3) pair as (4|4) would lower its quadratic contribution from
[
25+9=34
]
to
[
16+16=32,
]
contradicting (Phi)-minimality.

Hence
[
|A|,|B|le4.
]
A minimum counterexample has order greater than ten, while
[
|V(H)|=|A|+|B|+3le11.
]
Therefore
[
|V(H)|=11
]
and necessarily
[
|A|=|B|=4.
]

Thus the unique surviving quadratic-minimal trapped profile with a three-vertex component is
[
4|4|3
]
at order eleven.
