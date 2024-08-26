This program was created as a tool to visualize an experiment I conceived. I shall explain it below.

Consider a 1-dimensional cellular automata, consisting of a strip of 8 "bits", and a rule for them each to follow.
This rule can be any of a set of 255 rules, which each can be represented by an 8-bit unsigned binary number.
The rules define a set of 8 behaviors, corresponding to the 8 possible situations that any given bit on the strip can be in.
These "situations" are given by the "states" (1 or 0) of the bit itself, and its neighbors.
With 3 seperate variables for any given situation, each having 2 states, gives us our 2^3 (8) possible situations, and 8 needed behaviors.
The first bit of the behavior number defines what each cell is to do when it is in the first situation, where the bit and both it's neighbors are in the 0 state, or 0-0-0.
the second bit defines what each cell is to do when it is in the second situation, or 0-0-1, and so forth.
This experiment applies a rule to itself iteratively, graphing the decimal number corresponding to the rule as it goes.
It then produces that graph for each "starter" rule and overlays them all atop each other, forming one large graph (plot.png)
In this graph, the x-axis is the iteration, and the y axis is the decimal value.
All numbers seem to either fall into one of the many numbers that yield themselves when iterated, or fall into the singular 2-element loop.
There is also a more colorful graph where each line is given a unique color, although im working on the colormapping right now so it looks quite bad.