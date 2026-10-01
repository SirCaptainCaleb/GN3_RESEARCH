# Backward color-terminal collisions are stabbed by strict rank jumps

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_i={x_i,v_{i-1},v_i}, with nondecreasing edge ranks r_1<=...<=r_k.
For every color-terminal collision x_i=v_j, put I_i={j+1,...,i-1}.

Then I_i contains an index t with r_t<r_{t+1}. Equivalently, every backward collision chord crosses a strict parent-rank jump.

Consequently:
(1) every contiguous constant-rank block of the terminal path is strong-rainbow;
(2) if r_k-r_1=D, all collision chords are stabbed by at most D cuts between consecutive path edges;
(3) if there are C collision chords and D>0, some strict-rank cut is crossed by at least ceil(C/D) collision chords;
(4) some strong-rainbow contiguous subpath has at least ceil(k/(D+1)) edges.

## Body

By c9a012c1b82e, a collision x_i=v_j satisfies j<=i-2 and every terminal-path edge incident with v_j has rank at most r_i-1. In particular E_{j+1} is incident with v_j, so
r_{j+1}<=r_i-1<r_i.
Since r_{j+1},...,r_i is a nondecreasing integer sequence, there is some t in {j+1,...,i-1} with r_t<r_{t+1}. This proves the first assertion.

For (1), an internal color-terminal collision in a constant-rank block would have to cross a strict rank jump inside that block, impossible. Since the ambient graph path is rainbow, the block is therefore strong-rainbow.

For (2), select every cut t with r_t<r_{t+1}. Each collision chord is crossed by at least one such cut. The number of strict jumps is at most r_k-r_1=D, because each jump increases the integer rank by at least one.

Statement (3) is immediate by pigeonhole. For (4), the nondecreasing rank sequence has at most D+1 nonempty constant-rank blocks, so one block has at least ceil(k/(D+1)) edges, and (1) applies.
