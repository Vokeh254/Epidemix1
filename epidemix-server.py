from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from epidemix_model import EpidemixModel, PersonAgent

# Color the agents
def agent_portrayal(agent):
    if agent.state == "S":
        color = "blue"
    elif agent.state == "E":
        color = "orange"
    elif agent.state == "I":
        color = "red"
    else:
        color = "green"
    return {"Shape": "circle", "Color": color, "Filled": "true", "r": 0.8}

grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
server = ModularServer(EpidemixModel, [grid], "Epidemix ABM", {"N": 100, "width": 20, "height": 20})
