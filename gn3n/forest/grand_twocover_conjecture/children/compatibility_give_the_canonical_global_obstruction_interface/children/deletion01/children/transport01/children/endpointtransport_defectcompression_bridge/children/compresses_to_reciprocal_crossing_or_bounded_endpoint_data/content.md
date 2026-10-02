# A direct mixed-support crossing compresses to reciprocal crossing or bounded endpoint data

## Statement


Let H be a minimum counterexample, let R=(r_0,...,r_m), m>=3, be a displayed tight path, let y be one displayed endpoint of R, and let T be a two-cover of H-y containing an ordinary edge from an exterior class X to V(R)-{y}. Assume every T-component preserves the relative order of its surviving R-vertices. Then at least one of the following occurs:

(1) reciprocal support crossing: some inherited edge r_i r_{i+1} of R-y has endpoints in different T-components;

(2) bounded reversal: a tight path contains a reversed inherited edge r_{i+1},r_i consecutively, or an explicit tight triple reverses a displayed endpoint edge;

(3) bounded Hamiltonian support: H contains a proper Hamiltonian five-set W meeting an inherited edge of R, and H-W is non-Hamiltonian with path-cover number two;

(4) bounded paired reverse triples: for some inherited edge a,b, an adjacent inherited vertex s, and an exterior detour endpoint u, either both (u,s,b),(s,u,b) are tight or both (a,s,u),(a,u,s) are tight;

(5) H has a spanning two-cover;

(6) the singleton lift associated with T admits a strict quadratic-potential decrease; or

(7) a Phi-neutral singleton transfer occurs.

Thus, after excluding relative-order disagreement, every direct mixed-support crossing is consumed into reciprocal support separation, one of the standard bounded defect-compression inputs, immediate closure, strict descent, or a neutral singleton transfer.


## Body


Apply e2ffb6f50728.

If its reciprocal-support alternative occurs, we are in (1).

Suppose its leave-and-return alternative occurs. Because relative order is preserved, 09c38d41b038 shows that two consecutive inherited blocks are separated by a nonempty exterior detour replacing one single inherited edge ab of the surviving displayed path R-y. Write this tight detour as
D=(a,u_1,...,u_k,b), k>=1.

If ab is internal in R-y, let p be its predecessor and q its successor in the surviving displayed order. By 214a634b4fd9, either the detour support has a tight path containing the reversed consecutive pair b,a, giving (2), or one of the wrap triples
(a,b,u_k), (u_1,a,b)
is tight. The inherited path supplies (p,a,b) and (a,b,q). In the first wrap case, apply 69c0240a434e to (p,a,b), (a,b,q), and (a,b,u_k); in the second use its symmetric half with (u_1,a,b). We obtain either a Hamiltonian five-set meeting the inherited edge ab or one of the paired reverse-triple configurations in (4). The five-set is proper because mincex01 gives |V(H)|>10, and mincex01 then gives path-cover number two for its complement; that complement is non-Hamiltonian, since otherwise the two complementary Hamilton paths would two-cover H.

If ab is the first or last inherited edge of R-y, the surviving displayed path has at least three vertices because m>=3. Hence 53e7dc227829 applies. Its outcomes are again a tight path containing the reversed old edge or an explicit reversing triple through that endpoint edge, giving (2); a Hamiltonian five-set, giving (3) by mincex01; or two explicit same-side reverse triples of the form recorded in (4).

It remains the one-block endpoint-attachment alternative of e2ffb6f50728. Since T is a deletion two-cover and the intact surviving R-block has a direct exterior attachment at one of its block endpoints, 295ead2879dc applies. It yields an explicit endpoint-edge reversing triple, giving (2); a spanning two-cover, giving (5); a strict quadratic-potential decrease, giving (6); or the neutral boundary case, which is exactly a Phi-neutral singleton transfer and gives (7).

These cases exhaust the direct mixed-support crossing under preserved inherited order.
