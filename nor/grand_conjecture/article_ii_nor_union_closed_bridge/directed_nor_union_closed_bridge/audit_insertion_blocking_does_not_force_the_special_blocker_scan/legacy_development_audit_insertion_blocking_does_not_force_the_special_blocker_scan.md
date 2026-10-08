# Audit insertion blocking does not force the special blocker scan — preserved pre-item development

## Composition

(none yet)

## Development

The claimed unique perfect-blocker scan 1^(p+1)0^q is not a consequence of failure of all insertions into a prescribed alternating ternary carrier. This premise is used in §§178-200 and in the flat-sector closure §§187,188,191.

Parametric counterexample. Let O=(v_1,...,v_m), m=p+q+2, have word 0^p1^q with p,q>=2. Assign an exterior vertex x the scan s_i=alpha(x,v_i,v_{i+1}) with
s=11 0^(p+q-1).
It differs from the asserted scan since s_3=0 whereas the asserted scan has s_3=1.

All insertion positions fail. Prepending gives 1,0^p,1^q; appending gives 0^p,1^q,0. Inserting after v_1 gives 0,1,0^(p-1),1^q. After v_2 the packet is 1,0,0, followed by the old suffix, giving 1,0^p,1^q. After v_3 the packet is 1,1,0 with an inherited initial zero and a later one: if p>=3 this gives 0,11,0^(p-2),1^q; if p=2 it gives 0,11,0,1^(q-1). Every interior gap i>=4 with i<=m-2 has packet (s_{i-1},1-s_i,s_{i+1})=010, already bad. At the final interior gap i=m-1 the packet is truncated to 01; its inherited prefix ends in 1 because q>=2, giving a 101 subsequence. Hence all m+1 insertion positions have at least two changes.

Global flat realizability. Use alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a). Set every t(v_i,v_{i+1})=1 and every t(v_i,v_{i+2}) equal to the i-th desired carrier bit. These edge prescriptions are disjoint. Set q_i=t(x,v_i), choose q_1 arbitrarily, and recursively set q_{i+1}=1 xor q_i xor s_i. Then alpha(x,v_i,v_{i+1})=1 xor q_i xor q_{i+1}=s_i. Assign all remaining tournament edges arbitrarily. This defines an alternating orientation with zero tetrahedral coboundary everywhere and realizes both the carrier and the alternative blocking scan.

Consequences. The example is not a counterexample to NOR. It disproves the uniqueness lemma FROM INSERTION BLOCKING, even in the globally flat sector and for arbitrarily long phases. A minimum full counterexample has stronger global restrictions, but a new argument must establish the special scan from those restrictions or handle the other scans. Neither closure audit §§188,191 supplies that argument; they assume the same special scan.

The protected replacement calculation remains valid under the explicit special-scan hypothesis. The unconditional flat-sector closure, tube pattern, run lower bounds derived from that scan, and curvature-corridor necessity must not be promoted without repairing this premise. For arbitrary scans the correct replacement bridge at p>=3 is
(s_{p-2}, 1 xor s_{p-1} xor s_p xor kappa_{p-1}, s_{p+1}),
where kappa_{p-1}=delta alpha({x,v_{p-1},v_p,v_{p+1}}) and w_{p-1}=0. Flatness sets kappa_{p-1}=0 but does not by itself make this packet 111.
