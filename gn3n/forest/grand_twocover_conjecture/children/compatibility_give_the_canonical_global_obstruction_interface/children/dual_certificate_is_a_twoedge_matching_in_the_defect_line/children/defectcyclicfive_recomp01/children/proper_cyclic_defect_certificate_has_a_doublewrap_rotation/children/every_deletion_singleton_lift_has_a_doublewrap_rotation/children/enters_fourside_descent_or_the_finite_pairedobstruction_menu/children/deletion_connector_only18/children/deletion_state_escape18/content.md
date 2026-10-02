# Above order seventeen every deletion state enters strict quadratic descent or explicit order disagreement

## Statement

Let H be a minimum counterexample of order n>=18 and let H-x=P|Q be any one-vertex deletion two-cover. Then the pairwise-repartition component reached from its canonical double-wrap four-side state contains either a spanning three-cover of strictly smaller quadratic potential than that four-side state, or H contains explicit order disagreement. Equivalently, none of the five paired-noninsertion outputs of d26d8171978f remains a separate large-order obstruction.

## Body

Apply d26d8171978f to the deletion two-cover H-x=P|Q. It supplies the canonical double-wrap spanning three-cover S|R|T, where S is a tight four-path and H-S=R|T is a two-cover.

Since |R|+|T|=|V(H)|-4>=14, at least one of R,T has order at least seven. Relabel so |R|>=7.

Apply the certified arbitrary-state theorem a25b748fb338 to the spanning three-cover S|R|T and the long path R. Either one legal repartition of S|R strictly decreases the quadratic potential from the canonical four-side state itself, or H contains explicit order disagreement.

Thus the pairwise-repartition component containing the canonical double-wrap four-side state contains a strictly lower-Phi three-cover unless order disagreement already occurs. No paired-noninsertion, interval-connector, or opposite-endpoint-cross analysis is needed.