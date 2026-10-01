# Two barriers from one block force a mixed four-vertex path across the other blocks

## Statement

In the setting of astra006nearbalancedsync01, suppose X=(...,x_{p-1},x_p) has barrier interfaces X|Y and X|Z, with Y=(y_1,y_2,...) and Z=(z_1,z_2,...). Then at least one of (y_2,y_1,x_p,z_1) and (z_2,z_1,x_p,y_1) is a tight path. Thus two barriers sharing the terminal pair of X force a tight four-vertex path that uses two vertices from one neighboring block, the endpoint x_p of X, and one vertex from the other neighboring block.

## Body

The barrier X|Y gives the tight triples (y_2,y_1,x_p) and (y_1,x_p,x_{p-1}); the barrier X|Z gives (z_2,z_1,x_p) and (z_1,x_p,x_{p-1}). Apply boundary antisymmetry to the reversal pair (y_1,x_p,z_1),(z_1,x_p,y_1). If (y_1,x_p,z_1) is tight, prepend the already tight triple (y_2,y_1,x_p), obtaining the tight path (y_2,y_1,x_p,z_1). Otherwise (z_1,x_p,y_1) is tight, and prepending (z_2,z_1,x_p) gives (z_2,z_1,x_p,y_1). No path reversal or ambient-order argument is used.