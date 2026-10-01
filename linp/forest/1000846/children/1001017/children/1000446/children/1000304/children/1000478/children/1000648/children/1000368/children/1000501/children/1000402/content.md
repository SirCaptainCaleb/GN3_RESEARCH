# Strict potential-rise terminal degree is at most two

## Statement

Let H be a finite linear 3-graph and fix a vertex v. There are at most two ascending nonspecial edges e={x,v,u} for which v is a terminal vertex and the opposite terminal satisfies φ(u)>φ(v).

## Body

This is the strict-rise half of the potential-oriented route. It avoids the known unbounded raw terminal-degree examples, whose excess edges run toward lower-potential opposite terminals. By the certified top-band bound a7b7670e955a, every such charged edge has edge rank q satisfying q>=ceil((φ(v)+2)/2), so only the upper half of the rank interval can occur. A proof with any absolute constant in place of two would already contribute to the 2/3-leading-coefficient reduction 6eab2b03f554; the constant two is the current sharp target suggested by exact small-system exploration but is not asserted as proved.
