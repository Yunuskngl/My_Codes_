# Instructions  

In this assignment, you'll be plotting a rocket's trajectory as it tries to escape the Earth's gravitational pull! An example trajectory is found in `rocket_crash.png`, which corresponds to the default parameters in `rockets.py`. 

To start making your own plots, you'll need to implement some **functions**. We've already implemented the `launch_rocket` function, check it out to see where we're headed.

## Relevant Equations
1. Newton's Second Law: $$F = ma$$
2. Newton's Law of Gravitation: $$F_g = \frac{GM_em_m}{r^2}$$
3. Calculating updated velocity of a body: $$v = v_0 + at$$
4. Calculating the change in position of a moving body: $$\Delta x = v_0t + \frac{1}{2}at^2$$

## Required Task 
1. For our code to run, you'll need to implement the "helper" functions used in `launch_rocket`: `calculate_gravitational_force`, `calculate_acceleration`, `calculate_new_velocity`, and `calculate_new_distance`. These mostly involve "translating" physics equations into code.
2. Once you've implemented all the functions, run our code! You should see a plot similar to the one in `rocket_crash.png`.
3. Update our plotting code to add labels to our axes.
4. Play around with the rocket parameters. See how close you can get to escaping before crashing!

## Creative Tasks 
When it comes to plotting, there's a massive range of modifications you can make! Here are a couple ideas that you could implement to make your rocket plot(s) super cool: 

1. Change the line style (i.e. making it dashed) and color of your plots.
2. Use `matplotlib`'s "subplots" feature to make a graph with the trajectory and velocity lines side-by-side
3. Plot multiple trajectories on the same graph, differentiating the lines by color, and adding a legend to label them.
 
