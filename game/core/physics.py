class Rigidbody:

    def __init__(self):

        self.velocity = [0, 0]
        self.acceleration = [0, 0]

        self.gravity = 900

    
        self.friction = 800 

        self.max_speed = 300

    def apply_gravity(self):
        self.acceleration[1] = self.gravity

    def apply_friction(self, dt):

        if self.velocity[0] > 0:
            self.velocity[0] -= self.friction * dt
            if self.velocity[0] < 0:
                self.velocity[0] = 0

        elif self.velocity[0] < 0:
            self.velocity[0] += self.friction * dt
            if self.velocity[0] > 0:
                self.velocity[0] = 0

    def clamp_velocity(self):

        if self.velocity[0] > self.max_speed:
            self.velocity[0] = self.max_speed

        if self.velocity[0] < -self.max_speed:
            self.velocity[0] = -self.max_speed

    def update(self, dt):

        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

        self.clamp_velocity()

        self.acceleration = [0, 0]
