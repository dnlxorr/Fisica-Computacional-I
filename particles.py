import numpy as np
import matplotlib.pyplot as plt

K = 9e+9
DELTA_T = 1e-3
L=1000

class Particle():

    def __init__(self):
        self.mass = 1
        self.charge = 1
        self.trajectory = []
        self.pos = np.array([0.0,0.0])
        self.vel = np.array([0.0,0.0])
        self.acc = np.array([0.0,0.0])

    def set_position(self, pos):
        self.pos = pos
        self.trajectory.append(pos)

    def set_velocity(self,vel):
        self.vel = vel

    def set_acceleration(self, acc):
        self.acc = acc

    def update_dynamics(self, force, delta_t):
        self.acc = force/self.mass
        self.vel = self.vel + self.acc*delta_t
        self.set_position(self.pos + self.vel*delta_t)

    def apply_periodic_boundary_conditions(self, L):
        if self.pos[0] > L:
            self.set_position(np.array([self.pos[0] - L, self.pos[1]]))
        elif self.pos[0] < 0:
            self.set_position(np.array([self.pos[0] + L, self.pos[1]]))
        elif self.pos[1] > L:
            self.set_position(np.array([self.pos[0], self.pos[1] - L]))
        elif self.pos[1] < 0:
            self.set_position(np.array([self.pos[0], self.pos[1] + L]))




def calculate_force(a, b):
    r_ab=b.pos-a.pos
    magnitud_r = np.sqrt(r_ab[0]**2 + r_ab[1]**2)
    f = K*a.charge*b.charge/(magnitud_r**3)
    f_ab = f*r_ab
    return f_ab



particle_a = Particle()
particle_a.set_position(np.array([900,900]))
particle_a.set_velocity(np.array([-1000,0]))
particle_b = Particle()
particle_b.set_position(np.array([100,100]))
particle_b.set_velocity(np.array([1000,0]))

t_0 = 0

for i in range(1000):
    t_0+=DELTA_T
    force = calculate_force(particle_a,particle_b)
    particle_b.update_dynamics(force,DELTA_T)
    particle_a.update_dynamics(-1*force,DELTA_T)
    particle_a.apply_periodic_boundary_conditions(L)
    particle_b.apply_periodic_boundary_conditions(L)


print(particle_a.trajectory)

# Separate x and y coordinates
x = [point[0] for point in particle_a.trajectory]  # Extracts x values: [1, 3, 5, 7, 9]
y = [point[1] for point in particle_a.trajectory]  # Extracts y values: [3, 5, 2, 8, 4]

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o', label='Data Points')
# Separate x and y coordinates
x1 = [point[0] for point in particle_b.trajectory]  # Extracts x values: [1, 3, 5, 7, 9]
y1 = [point[1] for point in particle_b.trajectory]  # Extracts y values: [3, 5, 2, 8, 4]

# Create a scatter plot
plt.scatter(x1, y1, color='red', marker='^', label='Data Points')
# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot of [x, y] Coordinates')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()