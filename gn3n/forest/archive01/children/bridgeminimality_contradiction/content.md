# Bridge-minimality contradiction

## Statement

Conjecture that no Phi-minimal trapped three-cover can contain a canonical central bridge arising from a deletion state. More concretely: if A|C|B is one of the canonical 3- or 5-bridge states, with C the checked central bridge and A,B the inherited outer paths, then at least one of the pair unions A∪C or C∪B admits an exact two-cover whose squared-size sum is strictly smaller than the displayed pair, unless A|C|B already admits a merge to two components.

## Body

Why it might matter globally:
The certified two-move construction already places every deletion state inside a trapped canonical bridge component and strictly lowers Phi from the singleton lift. If canonical bridges themselves cannot be local minima for Phi, iterating inside a finite trapped component is impossible. This would prove the order-independent no-trapping statement and hence the grand theorem.

Plausible first attack:
Write the two canonical bridge forms explicitly and analyze only repartitions of the bridge with one neighboring inherited outer path. Use the three checked bridge triples plus boundary antisymmetry at the first outer triple to derive a dichotomy: either a direct concatenation merges components, or moving one/two endpoint vertices across the bridge yields a strictly more balanced exact two-cover of that pair union. The key is to prove this with path checks only, independent of ambient order.