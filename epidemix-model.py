from mesa import Agent, Model
from mesa.time import RandomActivation # type: ignore
from mesa.space import MultiGrid
import random

# STEP 1: Create a dot (Agent)
class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "S"  # S = Susceptible, E = Exposed, I = Infectious, R = Recovered

    def step(self):
        if self.state == "I":
            for neighbor in self.model.grid.get_neighbors(self.pos, True, True, 1):
                if neighbor.state == "S" and random.random() < 0.4:
                    neighbor.state = "E"
            if random.random() < 0.2:
                self.state = "R"
        elif self.state == "E":
            self.state = "I"
class EpidemixModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            agent = PersonAgent(i, self)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

            # Infect 5 random people
            if i < 5:
                agent.state = "I"

    def step(self):
        self.schedule.step()

