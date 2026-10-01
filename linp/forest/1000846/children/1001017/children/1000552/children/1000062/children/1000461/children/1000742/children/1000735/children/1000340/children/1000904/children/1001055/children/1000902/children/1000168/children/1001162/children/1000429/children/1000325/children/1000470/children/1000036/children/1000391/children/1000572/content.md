# Every all-top edge manufactures a balanced endpoint lens

## Statement

Let L be the global maximum linear-path length and let h={a,b,c} be any edge with phi(a)=phi(b)=phi(c)=L. Fix any maximum L-edge endpoint path P_a ending at a. Then P_a contains at least one of b,c. Consequently, if y is such a contained vertex and P_y is any maximum L-edge path ending at y, the paths P_a and P_y contain a clean balanced elementary endpoint lens. In particular every nonascending top-rank rotation output from 57d5e4c71035 canonically forces a balanced-lens state among top-potential endpoint paths.

## Body

If h itself occurs on P_a, then P_a contains both b and c and the first assertion is immediate. Otherwise suppose P_a contains neither b nor c. Since a is the last vertex of P_a, h then meets V(P_a) exactly at a. Appending h to P_a through a gives an (L+1)-edge linear path, contradicting the definition of L. Hence P_a contains some y in {b,c}. Because phi(y)=L, choose any maximum L-edge endpoint path P_y ending at y. Now y is a vertex of the maximum path P_a distinct from its endpoint a, so b35b0fd4e4cd applies directly: P_a and P_y have a second common vertex and contain a clean elementary lens adjacent to y whose two sides have equal edge length. The final assertion follows from 57d5e4c71035, which shows that every nonspecial nonascending top-rank rotation output has all three vertex potentials equal to L.
