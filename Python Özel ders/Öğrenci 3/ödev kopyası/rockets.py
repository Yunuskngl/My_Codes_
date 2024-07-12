import math
import matplotlib.pyplot as plt

# Constants -- these values are physical!
EARTH_MASS = 5.97e24  # kg
EARTH_RADIUS = 6378e3  # km
G = 6.67e-11  # N m^2 / kg^2


# Returns the acceleration on a body given the force
# acting on it, and its mass.
# Uses Newton's Second Law, F = ma. (relevant equation 1)
def calculate_acceleration(force, mass):
    return force / mass


# Returns the gravitational force on our rocket.
# Use Newton's law of gravity between two masses. In this case, the two
# masses are our rocket and Earth. The Earth's mass and radius, as well as
# the constant "G" are given above. (relevant equation 2)
def calculate_gravitational_force(distance, mass):
    return G * EARTH_MASS * mass / (EARTH_RADIUS + distance) ** 2


# Returns the updated velocity of the rocket given its current position
# and velocity. The acceleration acting on the rocket should be due to
# gravity, and the new velocity based on kinematics. We want to use the
# equation for an updated velocity, given an acceleration and a time.
# (relevant equation 3). Note that this equation does not use the current
# position, but we need it to calculate the radius between our body and
# earth.
def calculate_new_velocity(velocity, curr_x, mass, dt):
    force = calculate_gravitational_force(curr_x, mass)
    acceleration = calculate_acceleration(force, mass)
    return velocity - acceleration * dt  # Negative sign due to gravity


# Returns the new distance of the rocket (the current position, plus the
# amount it moves), based on the current velocity and position. Acceleration
# should come from the gravitational force on the rocket. This method also
# uses a kinematics equation, this time solving for "delta x", given the
# the current velocity, and time. (relevant equation 4)
def calculate_new_position(curr_x, velocity, mass, dt):
    force = calculate_gravitational_force(curr_x, mass)
    acceleration = calculate_acceleration(force, mass)
    return curr_x + velocity * dt - 0.5 * acceleration * dt ** 2


# Returns three lists:
#   1. Times, which are the discrete timesteps that info was calculated
#   2. Trajectory, which are the rocket's vertical position at the given times
#   3. Velocities, which are the corresponding velocities of the rocket
#
#   Uses all of the input rocket parameters and kinematics to calculate the
#   rocket trajectory.
#
#   Takes in the rocket mass, the initial velocity of the rocket, how long
#   the flight should last for, and the "time step" that we will be using
#   for kinematics equations.
def launch_rocket(r_mass, initial_velocity, flight_t, dt):
    times = [0]
    trajectory = [0]
    velocities = [initial_velocity]

    for i in range(int(flight_t * (1 / dt))):
        # Grab the current height from the end of our list
        current_height = trajectory[-1]

        # "Store" our updated position and velocity, and the corresponding time
        trajectory.append(
            calculate_new_position(current_height, velocities[-1], r_mass, dt))
        velocities.append(
            calculate_new_velocity(velocities[-1], current_height, r_mass, dt))
        times.append(times[-1] + dt)

        # Check for crash! Return info to plot if it does.
        if trajectory[-1] < 0:
            print(f"Your rocket crashed! It flew for {times[-1]} seconds.")
            return times, trajectory, velocities

    # Return info after a successful flight
    return times, trajectory, velocities


# Barebones plotting.
def plot_data(filename, x, y, xlabel, ylabel, title):
    plt.clf()  # Clear the current figure
    plt.plot(x, y, linestyle='--', color='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True) 
    plt.savefig(filename)


# Parameters -- change these to adjust your rocket!
ROCKET_MASS = 25e4  # kg
INIT_VELOCITY = 5e2  # m/s
FLIGHT_TIME = 1200  # s
TIME_STEP = .1  # s

times, trajectory, velocities = launch_rocket(ROCKET_MASS, INIT_VELOCITY,
                                              FLIGHT_TIME, TIME_STEP)

plot_data("rocket_trajectory.png", times, trajectory, "Time (s)", "Altitude (m)", "Rocket Trajectory")
plot_data("rocket_velocities.png", times, velocities, "Time (s)", "Velocity (m/s)", "Rocket Velocities")
