# Every span-three ordering has a reversed cyclic endpoint hook

## Statement

Let H be a boundary tournament with pc(H)>2 and let pi=(v_1,...,v_n) be a spanning ordering of defect span exactly three. Then at least one of the two cyclic wrap triples (v_{n-1},v_n,v_1) and (v_n,v_1,v_2) is non-tight. Consequently boundary antisymmetry forces at least one of the reverse endpoint hooks (v_1,v_n,v_{n-1}) and (v_2,v_1,v_n) to be tight.

## Body

The ordinary defect line of pi has matching number exactly two by the defect-line formula ca8dc4ee0bde, because its defect span is three and pc(H)>2. Close pi cyclically and form the cyclic defect graph Gamma from 52f5b958156e. The only cyclic defect tests not already present in the linear ordering are the two wrap triples centered at v_n and v_1, namely (v_{n-1},v_n,v_1) and (v_n,v_1,v_2). If both were tight, Gamma would have exactly the same defect edges as the ordinary linear defect graph, and hence nu(Gamma)=2. But 86a22f6fc031 gives nu(Gamma)=3 for every proper cyclic certificate arising from a c=3 ordering; the only full-cycle exception in the span-three reduction is C5, where both wrap edges are certainly present. Therefore at least one wrap triple is non-tight. Boundary antisymmetry reverses that triple while fixing its middle vertex, giving respectively (v_1,v_n,v_{n-1}) or (v_2,v_1,v_n) tight.