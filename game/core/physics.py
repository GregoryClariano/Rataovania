class Rigidbody:

    def __init__(self):

        self.velocity = [0, 0]
        self.acceleration = [0, 0]

        self.gravity = 900

        # NOVO
        self.friction = 800  # força de desaceleração

        self.max_speed = 300  # limite horizontal

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

        # v = v + a * dt
        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

        # LIMITAR velocidade
        self.clamp_velocity()

        # reset aceleração
        self.acceleration = [0, 0]
