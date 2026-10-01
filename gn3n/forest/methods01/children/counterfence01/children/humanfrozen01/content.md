# Human threshold certificate for a frozen seven-set

## Statement

For the explicit edge order 46<01<26<15<03<04<06<35<13<05<56<12<23<34<14<02<16<24<36<25<45 on {0,1,2,3,4,5,6}, A={0,1,2,3,4,5} is Hamiltonian, the full seven-set is non-Hamiltonian, and every replacement six-set (A-{z}) union {6} is non-Hamiltonian. One-sided threshold path capacities at vertex 6 prove all assertions without exhaustive permutation checks.

## Body

# Human threshold certificate for a frozen seven-set

Let the complete graph on `A union {6}`, where `A={0,1,2,3,4,5}`, have edge order

`46 < 01 < 26 < 15 < 03 < 04 < 06 < 35 < 13 < 05 < 56 < 12 < 23 < 34 < 14 < 02 < 16 < 24 < 36 < 25 < 45`.

An increasing ordinary path represents a tight path in the associated edge-orderable boundary tournament.

The six-set `A` is Hamiltonian because
`01 < 12 < 23 < 34 < 45`,
so `(0,1,2,3,4,5)` is increasing.

We prove, without exhaustive enumeration, that the full seven-set `A union {6}` is non-Hamiltonian and that, for every `z in A`, the replacement six-set
`(A-{z}) union {6}`
is non-Hamiltonian.

Write `r(v)` for the rank of the edge `v6`. Then
`r(4)=1, r(2)=3, r(0)=7, r(5)=11, r(1)=17, r(3)=19`.

For `x in A`, let `L(x)` be the maximum number of vertices in an increasing path contained in `A`, ending at `x`, all of whose edge ranks are less than `r(x)`.
For `y in A`, let `R(y)` be the maximum number of vertices in an increasing path contained in `A`, starting at `y`, all of whose edge ranks are greater than `r(y)`.

We claim

| vertex | 4 | 2 | 0 | 5 | 1 | 3 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `r(v)` | 1 | 3 | 7 | 11 | 17 | 19 |
| `L(v)` | 1 | 1 | 2 | 4 | 4 | 4 |
| `R(v)` | 4 | 4 | 4 | 2 | 1 | 1 |

Here is a complete threshold verification.

### Left capacities

- `L(4)=1`: there is no edge of `A` below rank `1`.
- `L(2)=1`: the only edge of `A` below rank `3` is `01`, so `2` is isolated in the permitted-edge graph.
- `L(0)=2`: the possible final edges are `01=2`, `03=5`, and `04=6`. If the final edge is `01`, nothing can precede it. If it is `03`, no unused edge incident with `3` has rank below `5`. If it is `04`, no unused edge incident with `4` has rank below `6`. Thus no three-vertex permitted path can end at `0`.
- `L(5)=4`: the possible final edges are `15=4`, `35=8`, and `05=10`. The first and third cases give at most three vertices. In the middle case, the only way to obtain four vertices is
  `01 < 03 < 35`,
  giving the unique maximum path `(1,0,3,5)`.
- `L(1)=4`: the possible final edges are `01=2`, `15=4`, `13=9`, `12=12`, and `14=15`. The first four cases give at most three vertices. For final edge `14`, the preceding edge into `4` must be `04=6` or `34=14`. This gives exactly the four-vertex possibilities
  `(3,0,4,1)`, `(0,3,4,1)`, `(5,3,4,1)`, and `(2,3,4,1)`.
  None can be extended farther to the left. In particular every maximum `L(1)` path contains `3`.
- `L(3)=4`: the possible final edges have ranks `03=5`, `35=8`, `13=9`, `23=13`, and `34=14`. If the final edge is `34`, the only unused predecessor edge into `4` below rank `14` is `04=6`, and then at most `01=2` can precede it, giving `(1,0,4,3)`. If the final edge is `23`, the only unused predecessor edge into `2` below rank `13` is `12=12`, which can be preceded by either `01=2` or `15=4`. If the final edge is `35`, the only predecessor edge into `5` below rank `8` is `15=4`, which can only be preceded by `01=2`, giving `(0,1,5,3)`. The final-edge cases `03` and `13` give at most three vertices. Hence `L(3)=4`.

### Right capacities

- `R(3)=1`: no edge of `A` incident with `3` has rank above `19`.
- `R(1)=1`: no edge of `A` incident with `1` has rank above `17`.
- `R(5)=2`: the only permitted first edges are `25=20` and `45=21`; after either one there is no unused larger continuation.
- `R(0)=4`: the only permitted first edges are `05=10` and `02=16`. The `05` branch has at most three vertices. From `02`, the only four-vertex continuations are
  `(0,2,4,5)` with ranks `16<18<21`, and
  `(0,2,5,4)` with ranks `16<20<21`.
  Thus every maximum `R(0)` path contains both `2` and `4`.
- `R(2)=4`: the possible first edges have ranks `12=12`, `23=13`, `02=16`, `24=18`, and `25=20`. The last three branches have at most three vertices. The first two produce exactly
  `(2,1,4,5)`,
  `(2,3,4,1)`, and
  `(2,3,4,5)`.
  Hence every maximum `R(2)` path contains `4`.
- `R(4)=4`: the possible first edges have ranks `04=6`, `34=14`, `14=15`, `24=18`, and `45=21`. Every branch except `04` has at most three vertices. Through `04` one obtains, for example, `(4,0,5,2)` with ranks `6<10<20`, so `R(4)=4`; a fifth vertex cannot follow because any continuation after rank `20` would have to use `45=21` and repeat `4`.

### The full seven-set is non-Hamiltonian

Suppose `A union {6}` had an increasing Hamilton path. If `6` were first, the remaining six vertices would form an `R(y)` path for the second vertex `y`, impossible because every `R(y)<=4`. Likewise, if `6` were last, the preceding six vertices would form an `L(x)` path, impossible because every `L(x)<=4`.

Thus `6` is internal. Let `x,6,y` be the consecutive segment through `6`. Then `r(x)<r(y)`. The prefix ending at `x` is an `L(x)` path and the suffix starting at `y` is an `R(y)` path; these two disjoint pieces together contain all six vertices of `A`. Hence `L(x)+R(y)>=6`. But from the displayed rank order
`4 < 2 < 0 < 5 < 1 < 3`
and the capacity table, every ordered pair with `r(x)<r(y)` satisfies `L(x)+R(y)<=5`. This contradiction proves that the full seven-set is non-Hamiltonian.

### Every replacement six-set is non-Hamiltonian

Now fix `z in A` and suppose, for contradiction, that `(A-{z}) union {6}` has an increasing Hamilton path.

If `6` is the first vertex, the remaining five vertices would form an `R(y)` path for the second vertex `y`, but `R(y)<=4` for every `y`. Similarly, if `6` is last, the preceding five vertices would form an `L(x)` path, but `L(x)<=4` for every `x`. Thus `6` is internal.

Let `x,6,y` be the consecutive three-vertex segment through `6`. Since the whole path is increasing,
`r(x)<r(y)`.
The vertices before `6`, including `x`, form an `L(x)` path, while the vertices after `6`, including `y`, form an `R(y)` path. These two paths are disjoint and together contain all five vertices of `A-{z}`. Hence necessarily
`L(x)+R(y)>=5`.

Using the rank order
`4 < 2 < 0 < 5 < 1 < 3`
of the six edges incident with `6`, together with the table above, the only ordered neighbor pairs `(x,y)` satisfying both `r(x)<r(y)` and `L(x)+R(y)>=5` are

`(4,2), (4,0), (2,0), (5,1), (5,3), (1,3)`.

Each is impossible:

- for `(4,2)`, every maximum right path from `2` contains `4=x`;
- for `(4,0)`, every maximum right path from `0` contains `4=x`;
- for `(2,0)`, every maximum right path from `0` contains `2=x`;
- for `(5,1)`, the unique maximum left path into `5` contains `1=y`;
- for `(5,3)`, the unique maximum left path into `5` contains `3=y`;
- for `(1,3)`, every maximum left path into `1` contains `3=y`.

In every case the left and right pieces would repeat a vertex, contradicting simplicity of the Hamilton path.

Therefore every replacement six-set `(A-{z}) union {6}` is non-Hamiltonian. Since `A` itself is Hamiltonian, the vertex `6` is the unique vertex whose deletion from the non-Hamiltonian seven-set `A union {6}` leaves a Hamiltonian six-set.