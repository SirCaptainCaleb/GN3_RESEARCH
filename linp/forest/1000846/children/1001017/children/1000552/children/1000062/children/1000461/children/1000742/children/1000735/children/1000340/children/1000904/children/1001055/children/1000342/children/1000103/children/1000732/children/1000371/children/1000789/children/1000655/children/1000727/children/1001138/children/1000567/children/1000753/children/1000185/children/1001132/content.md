# Five-elevenths retention upgrades the disjoint inside-outside packets

## Statement

Let P=(g_1,...,g_p) be the chosen maximum p-edge path at a low-defect active misaligned vertex v, and suppose the switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. Then the terminal-retained subfamily U_v contains
  k >= (25/88-o(1))p
edges e_i={x_i,v,u_i}. Consequently:
(1) the x_i are distinct vertices outside P and
  sum_i phi(x_i) >= (9425/61952-o(1))p^2;
(2) U_v yields at least (25/88-o(1))p distinct vertices of P of vertex rank at least p arising as last vertices of p-edge switching rotations.
The outside source packet and on-path rotation packet are vertex-disjoint.

## Body

The structural packet theorem cb99a895c603 applies to any terminal-retained family U of size k. It gives distinct omitted entrances x_i outside P with
  sum_i phi(x_i) >= (p/2)k+k(k+1)/8,
and at least k-O(1) distinct on-path rotation last vertices of rank at least p.

Under the near-minimal source-mass hypothesis, the strengthened terminal-retention theorem 28f6933b98de gives
  k >= (25/88-o(1))p.
The source lower bound is increasing in k, so
  sum_i phi(x_i)
  >= [25/176 + (1/8)(25/88)^2-o(1)]p^2
  = [8800/61952+625/61952-o(1)]p^2
  = (9425/61952-o(1))p^2.
The rotation packet has size k-O(1)=(25/88-o(1))p. The two packets are disjoint because all x_i lie outside P while the rotation last vertices lie on P.