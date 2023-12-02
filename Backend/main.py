from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()

#global variables
generated_propositions = [...]
vegan_diet: bool
vegetarian_diet: bool
no_lactose: bool
Diabetes: bool
Calories: int
Meal_type: str
Preferences: str

#   class that contains types of requested information in the first method (/generate-dish-propositions/)
class DishRequest(BaseModel):
    vegan_diet: bool = Query(...)
    vegetarian_diet: bool = Query(...)
    no_lactose: bool = Query(...)
    Diabetes: bool = Query(...)
    Calories: int = Query(...)
    Meal_type: str = Query(...)
    Preferences: str = Query(...)


# API key to connect to gpt-3.5-turbo
openai = OpenAI(api_key="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")

# method that generates dish propositions and stores them in global variable generated_propositions
@app.post("/generate-dish-propositions/")
async def generate_dish_propositions(request: DishRequest):

    user_message = (
        f"Give me 5 dish propositions (only the names of the dishes and nothing more) with the following preferences:"
        f" Vegan: {request.vegan_diet}, Vegetarian: {request.vegetarian_diet},"
        f" No Lactose: {request.no_lactose}, Diabetes: {request.Diabetes},"
        f" Calories: {request.Calories}, Meal Type: {request.Meal_type},"
        f" Preferences: {request.Preferences}."
    )

    messages = [
        {"role": "system", "content": "You are someone who gives dishes propositions."},
        {"role": "user", "content": user_message},
    ]


    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
    )

    global generated_propositions
    generated_propositions = [...]
    global vegan_diet
    global vegetarian_diet
    global no_lactose
    global Diabetes
    global Calories
    global Meal_type
    global Preferences
    vegan_diet = request.vegan_diet
    vegetarian_diet = request.vegetarian_diet
    no_lactose = request.no_lactose
    Diabetes = request.Diabetes
    Calories = request.Calories
    Meal_type = request.Meal_type
    Preferences = request.Preferences
    generated_propositions = [{"name": name.strip()} for name in response.choices[0].message.content.split("\n")]
    return {"ok": "ok"}

#method that sends generated dishes back to the website
@app.get("/generate-dish-propositions/sending-with-get-method")
async def get_generated_dish_propositions():
    global generated_propositions
    if not generated_propositions:
        raise HTTPException(status_code=404, detail="No generated dish propositions available.")
    return {"generated_propositions": generated_propositions}



#method that gives ingredients and instructions to meal selected from prevoiusly generated meals
@app.get("/generate-dish-instructions/{index}")
async def generate_dish_instructions(index: int):
    global generated_propositions
    index = index

    if not (0 <= index <= len(generated_propositions)):
        raise HTTPException(status_code=400, detail="Invalid selected dish index.")

    selected_dish = generated_propositions[index-1]["name"]

    user_message_2 = (
        f"Give me list of ingredients and instructions (separate ingredients and instruction with '***') how to prepare {selected_dish} with the following preferences: "
        f" Vegan: {vegan_diet}, Vegetarian: {vegetarian_diet},"
        f" No Lactose: {no_lactose}, Diabetes: {Diabetes},"
        f" Calories: {Calories}, Meal Type: {Meal_type},"
        f" Preferences: {Preferences}."
    )

    messages = [
        {"role": "system", "content": "You are someone who gives cooking instructions."},
        {"role": "user", "content": user_message_2},
    ]

    response2 = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
    )

    return {"generated_instruction": response2.choices[0].message.content}
