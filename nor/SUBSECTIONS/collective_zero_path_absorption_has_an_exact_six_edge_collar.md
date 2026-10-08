# Collective zero-path absorption has an exact six-edge collar

## Metadata

- ID: collective_zero_path_absorption_has_an_exact_six_edge_collar
- Parent Section: monochromatic_connector_blocks
- Position: 22
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

A zero path of length at least two can be inserted as a block when its three left and three right boundary incidences match the square-path pattern, up to complementing its path-normalizing switch. The outside order and ports remain fixed for interior insertion. This elevates four-bit vertex insertion to whole-path absorption.

## Development

In square-path gauge, inserting a disjoint zero path as one block changes only the two-coordinate collar on each side. For a block P=(p1,...,pr) inserted between consecutive connector coordinates c_i,c_{i+1}, the only new requirements are that the two preceding connector coordinates dominate the first two block coordinates in the square-path pattern, and that the last two block coordinates dominate the two succeeding connector coordinates. With a fixed path-normalizing switching on P this is a six-incidence pattern with three equal left bits and the opposite three right bits. Complementing all switching bits on P flips the six incidences, so the two legal collar patterns are complementary. The r=1 case is exactly the existing four-bit vertex insertion rule. Hence whole zero paths from the canonical shore decomposition may be absorbed collectively; ternary locality leaves only a width-two block collar obstruction.
