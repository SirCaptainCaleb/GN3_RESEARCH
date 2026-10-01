# Order-preserving near-longest paths admit a noncrossing omission-to-insertion charging

## Statement

In the setting of 4d26ca2c1961, write O=V(A)-V(C) and E=V(C)-V(A), so |O|-|E|=d. Partition both O and E into the ordered gaps determined by the common vertices A∩C, including the initial and final gaps. Then there is an injection mu:E->O such that for every exterior vertex x in E, the omitted A-vertex mu(x) lies in the same gap as x or in an earlier gap. Equivalently, the exterior insertions can be charged injectively, from left to right, to previously available omissions. Exactly d omitted A-vertices remain unmatched.

## Body

Order the gaps by the common A/C order. The prefix-balance identity of 4d26ca2c1961 says that immediately before every surviving A-vertex, the cumulative number of exterior C-vertices already encountered is at most the cumulative number of omitted A-vertices already encountered. The same inequality for the final gap follows from the total count |O|-|E|=d>=0. Thus for every initial segment of gaps, cumulative exterior demand is at most cumulative omitted supply. Greedily scan the gaps from left to right and, whenever an exterior vertex is encountered, match it to any still-unmatched omitted vertex already encountered. The prefix inequalities guarantee that this never gets stuck. This yields an injection mu with the stated order property. Since |O|-|E|=d, exactly d omissions remain unmatched. Equivalently, after ordering E by gap and choosing the matched O labels in matching order, the matching is noncrossing with respect to the common-core line.
