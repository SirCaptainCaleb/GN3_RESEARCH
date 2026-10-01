# At potential five, four charged ascending terminal edges contain at most two rank-four edges

## Statement

Let v be a vertex with phi(v)=5. Among any four potential-charged ascending nonspecial edges through v for which v is a terminal, at most two have rank four. Since every such terminal edge has rank at most five and the terminal-rank inequality forces rank at least four, the only possible ordered rank patterns are
  (4,4,5,5), (4,5,5,5), (5,5,5,5).
In particular the patterns (4,4,4,4) and (4,4,4,5) are impossible.

## Body

Apply a570b0ad0001 with q=4. Since
  phi(v)=5=2q-3,
there are at most two ascending nonspecial edges terminal at v of rank at most four.

Every charged edge in question is ascending nonspecial and terminal at v. Also terminality gives phi(e)<=phi(v)=5, while the certified terminal-rank inequality gives, for phi(v)=5,
  5<=2phi(e)-2,
hence phi(e)>=4.
Thus every rank lies in {4,5}, with at most two occurrences of 4. The listed three patterns are exactly the possibilities.