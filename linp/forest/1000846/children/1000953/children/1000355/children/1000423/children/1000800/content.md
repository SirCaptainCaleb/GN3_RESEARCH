# Crossed missing-color chords force the opposite endpoint chord

## Statement

In the crossed-chord normal form for a hypothetical proper 6-coloring of K_{6,6} with no rainbow P_6, normalize a rainbow P_5 as x_0y_0x_1y_1x_2y_2 with colors 1,2,3,4,5 and suppose the missing color 6 occurs on x_0y_1 and x_1y_2. Then x_0y_2 has color 3.

## Body

Consider the rotated five-edge path
y_2, x_2, y_1, x_0, y_0, x_1.
Its edge colors are respectively
5,4,6,1,2,
so it is rainbow and its unique missing color is 3.

Because the graph has no rainbow P_6, the color-3 edge incident with the endpoint y_2 cannot go to any left-side vertex outside this path: such an edge could be prepended and would extend the displayed rainbow P_5 to a rainbow P_6.

Hence the color-3 mate of y_2 lies among the three used left-side vertices x_0,x_1,x_2. It cannot be x_2 because x_2y_2 has color 5, and it cannot be x_1 because x_1y_2 has color 6. Therefore it must be x_0. Thus x_0y_2 has color 3.
