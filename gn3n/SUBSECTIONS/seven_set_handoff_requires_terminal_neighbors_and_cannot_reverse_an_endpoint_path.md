# Seven-set handoff requires terminal neighbors and cannot reverse an endpoint path

## Metadata

- ID: seven_set_handoff_requires_terminal_neighbors_and_cannot_reverse_an_endpoint_path
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 127
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The seven-set endpoint handoff needs terminal, not unoriented, neighbors

The proof in [[seven_set_endpoint_handoff_either_absorbs_a_tail_or_advances_the_root]] says to orient a Hamilton order with prescribed endpoint c_2 so that its final two vertices are t_i,c_2. This does not follow from a prescribed-endpoint theorem for boundary tournaments.

A tight order is directed. If (v_1,...,v_s) is tight with s>=3, reversing it complements every consecutive status, so the reversed order is not tight. Having an anchor as an endpoint does not allow choosing which endpoint it is.

**Counterexample to the needed orientation inference.** Let U={r} union A with |A|=6. Prescribe
\[
h(r,u,v)=1\qquad(u,v\in A,\ u\ne v).
\]
Boundary antisymmetry then forces
\[
h(u,v,r)=0\qquad(u,v\in A,\ u\ne v).
\]
Choose the middle-r values antisymmetrically and all triples inside A arbitrarily.

Every three-set T subset A has a tight order (a,b,c), and
\[
(r,a,b,c)
\]
is a tight Hamilton order on {r} union T. The complementary three-set in A also has a tight order. Thus these give many (4|3) two-covers with r as an endpoint of the four-path.

There are at least four distinct possible neighbors immediately after r among these covers. Indeed, if the set of possible first labels of tight orders on triples of A had order at most three, its complement would contain a triple; a tight order of that triple would start outside the supposed set, a contradiction. Each such tight triple extends by prepending r.

Nevertheless no tight path of order at least three can end at r: its final triple (u,v,r) has status zero. In particular there is no Hamilton four-order on any support containing r with r terminal. Thus even abundant prescribed-endpoint neighbors do not supply a single terminal neighbor.

This is a counterexample to the proof's orientation step, not a claimed counterexample to its entire handoff-or-advance conclusion or to the grand theorem.

## Correct directional handoff statement

Let C=(c_2,c_3,c_4,...) be a tight path, U a seven-set with U intersect V(C)={c_2}. Define
\[
T^-(U,c_2)=\{t:\text{there is a }(4|3)\text{ two-cover }K|R\text{ of }U
\text{ with a tight four-order on }K\text{ ending }t,c_2\}.
\]

Then:
1. If some t in T^-(U,c_2) satisfies h(t,c_2,c_3)=1, append the contiguous tail c_3,c_4,... to its four-order. Together with R this is a two-cover of U union V(C).
2. If no such t exists, h(c_3,c_2,t)=1 for every t in T^-(U,c_2).
3. If, in addition, |T^-(U,c_2)|>=3, the three-common-hook packet consequence cited by the original handoff proof applies to the ordered pair (c_3,c_2).

**Proof.** In (1), all packet triples and all tail triples are tight; the only new triple is (t,c_2,c_3), which is tight by hypothesis. In (2), the failed junctions have status zero and boundary antisymmetry reverses them. Statement (3) then has exactly the three required distinct hooks. ∎

The existing prescribed-endpoint seven-set theorem supplies an unoriented endpoint-neighbor set, not the lower bound |T^-|>=3. The missing load-bearing theorem is directional endpoint control, or an alternative repartition that avoids this terminal requirement. No reverse-path or cyclic-rotation inference can fill that gap.

## Frontier

- Development version when composed: None
- Development version now: 1
