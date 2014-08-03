This section contains different ways of producing an Occupancy Grid.

BreadCrumbs is the firt "map", where a trail is made taht shows where the robot has been,
but no obstacles are mapped.

The Real_OG should be used for creating a map with the physical E-Puck robot.

The Sim_OG should be used for creating a map with the simulated E-Puck robot.

Probability_OG is not quite finished. The idea is to multiply
by 1.1 a cell where an obstacle is detected, and 0.9 a cell that is empty.
However, More visible results were obtained by placing a '1' in occupied cells.