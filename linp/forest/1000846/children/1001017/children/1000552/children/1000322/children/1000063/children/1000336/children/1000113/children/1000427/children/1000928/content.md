# A terminal-safe rotation state has endpoint deficiency at most three

## Statement

In the setting above, fix two vertices y,z not on P. Call a clean edge safe if it avoids y,z, so prepending it gives an (s+1)-edge path still ending at x and avoiding y,z. Call a single blocker safe if its blocker is not x and the edge avoids y,z, so the single-blocker rotation gives another s-edge path ending at x and avoiding y,z. If there is no safe clean edge and no safe single blocker at a, then δ-s<=3.

## Body

At most one clean edge through a can contain y and at most one can contain z, by linearity; hence if there is no safe clean edge then C<=2. For single blockers, at most one edge can have blocker x, at most one can contain y, and at most one can contain z, again because two distinct edges through a cannot share a second vertex. Thus absence of a safe single blocker gives S<=3. The deficiency-surplus inequality then yields 2(δ-s)<=2C+S<=7, and since δ-s is an integer, δ-s<=3.