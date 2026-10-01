# The minimal one-low high-rail residue is a balanced terminal-terminal lens

## Statement

Retain the one-low source-rail state of 3ada869c2396 and suppose Q_1,Q_3 and Q_2,Q_3 are uniquely intersecting, while V(Q_1) intersect V(Q_2)={u_0,u_3}. Then u_0 and u_3 are internal vertices of both q-edge high source rails Q_1,Q_2, and the two Q_1/Q_2 segments between u_0 and u_3 form a clean balanced lens. In addition u_0 is a joint at the same path index on Q_1,Q_2,Q_3.

## Body

The two simple pairs through Q_3 are reciprocal-terminal by 5570b54b0046. Hence Q_1 and Q_2 both contain u_0 from their low-edge contacts and both contain u_3 from their contacts with e_3. By hypothesis these are their only common vertices. Since the four offending edges share only v, linearity makes u_0,u_3 distinct from the high sources x_1,x_2, so neither lens endpoint is the endpoint of Q_1 or Q_2. Thus the two rail segments between consecutive common vertices u_0,u_3 form a clean internal lens. The clean-lens balance lemma 390e818020e1 gives equal edge lengths on the two sides. Finally Q_1 intersect Q_3={u_0} and Q_2 intersect Q_3={u_0}; universal aligned-joint rigidity 5854d853a44b puts u_0 at the same joint index on each of Q_1,Q_2,Q_3.