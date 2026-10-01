# Minimum-imbalance two-covers force nested endpoint-segment Hamiltonicity blockades

## Statement

Let K be a boundary tournament admitting a spanning two-cover. Choose a displayed two-cover A|B minimizing the component-size imbalance, and orient the names so a=|A|>=b=|B|. Write d=a-b. If d>=2 and A=(a_1,...,a_a), then for every integer t with 1<=t<=d-1, both induced subtournaments
K[V(B) union {a_1,...,a_t}]
and
K[V(B) union {a_{a-t+1},...,a_a}]
are non-Hamiltonian.

## Body

Suppose for some t with 1<=t<=d-1 that the prefix X={a_1,...,a_t} Hamiltonizes with B. Since X is an initial segment of the displayed tight path A, the remaining suffix A-X=(a_{t+1},...,a_a) is also a tight path. Hence
(A-X) | (B union X)
is a spanning two-cover of K.

Its component orders are a-t and b+t, so its imbalance is
|a-t-(b+t)|=|d-2t|.
Because 0<t<d, one has |d-2t|<d. This contradicts the minimum choice of the imbalance of A|B.

The suffix case is identical: deleting the final t vertices of A leaves an inherited tight prefix, and Hamiltonicity of B together with that suffix would again produce imbalance |d-2t|<d.

Thus every proper endpoint segment of A whose length is strictly smaller than the original imbalance is blocked from Hamiltonizing with B. ∎