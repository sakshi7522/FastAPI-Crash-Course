from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return f"WELCOME TO TEA HOUSE"


@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea :Tea):
    teas.append(tea)
    return f"{tea} added successfully"


@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea ):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return f"Tea updates successfully"

        return f"error: Tea not found."
    
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id : int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return f"{deleted} tea has been removed from the house"
        
        return f"error: Tea not found."
    





























# foods = {
#     'indian' : ['samosa', 'dosa'],
#     'american': ['burger', 'hot dog'],
#     'italian': ['ravioli', 'pizza']

# }

# class availableFood(str, Enum):
#     indian  = "indian"
#     american = "american"
#     italian = "italian"


# @app.get("/get_food/{food}")
# def get_food(food : availableFood):
#     return foods.get(food)




# @app.get("/hello/{name}")
# def hello(name):
#     return f"Hello {name}"



# @app.get("/")
# def hello():
#     return "Hello world"