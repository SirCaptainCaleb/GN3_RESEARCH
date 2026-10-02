# Four endpoints force two incompatibilities, three isolated neighbors, or the four-kernel frontier

## Statement

Let H be a minimum counterexample with chosen deletion covers and compatibility graph G, and fix an anchor cover F_d=P|Q. Among the four displayed endpoints of P,Q, at least one of the following holds: (1) at least two endpoint labels y have F_y incompatible with F_d; (2) at least three endpoint labels are compatibility neighbors of d that are isolated vertices of G[N_G(d)]; or (3) an endpoint compatibility triangle occurs and hence the endpoint cyclic four-kernel frontier of 93109600e88d occurs.

## Body

Apply b84585664a1d to each of the four displayed endpoints. If outcome (3) of that theorem occurs for any endpoint, we obtain alternative (3) here. Otherwise every endpoint is either incompatible with the anchor or is an isolated compatibility neighbor in G[N_G(d)]. If at least two are incompatible, alternative (1) holds. If at most one is incompatible, at least three of the four endpoints are isolated compatibility neighbors, giving alternative (2).