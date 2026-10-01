# Any trapped quadratic minimum with a three-side has order at most eleven

## Statement

Let H be any boundary tournament and let A|B|C be a spanning three-cover that minimizes quadratic potential within a connected pairwise-repartition component containing no cover with at most two components. If |C|=3 and |A|>=|B|>=3, then |A|,|B|<=4 and hence |V(H)|<=11. Equivalently, no trapped componentwise Phi-minimal three-cover on at least twelve vertices has a three-vertex component.

## Body

Write a=|A| and b=|B|. If a>=6, apply threesidedescent6 to the pair C|A. It gives a legal pairwise repartition with strictly smaller quadratic potential, contradicting the assumed componentwise Phi-minimality. Hence a<=5.

Suppose a=5. The induced boundary tournament on V(A) union V(C) has eight vertices. By balanced8_conceptual_repair01 it has a partition into two Hamiltonian four-vertex induced subtournaments. Replacing the displayed 5|3 pair A|C by this 4|4 pair is one legal pairwise repartition in the same move component. Its pairwise quadratic contribution drops from 5^2+3^2=34 to 4^2+4^2=32, again contradicting Phi-minimality. Therefore a<=4. Since a>=b>=3, also b<=4, and n=a+b+3<=11.
