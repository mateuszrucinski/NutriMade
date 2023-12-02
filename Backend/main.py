from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()


#   class that contains types of requested information in the first method (/generate-dish-propositions/)
class DishRequest(BaseModel):
    vegan_diet: bool = Query(...)
    vegetarian_diet: bool = Query(...)
    no_lactose: bool = Query(...)
    Diabetes: bool = Query(...)
    Calories: int = Query(...)
    Meal_type: str = Query(...)
    Preferences: str = Query(...)

#   class that takes from the user index of prevoiously generated dish

# API key to connect to gpt-3.5-turbo
openai = OpenAI(api_key="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")

# method that generates dish propositions and stores them in global variable generated_propositions
# ingredients are stored in global variable named ingredients
@app.post("/generate-dish-propositions/")
async def generate_dish_propositions(request: DishRequest):

    user_message = (
        f"Give me 5 dish propositions (only the names of the dishes) with the following preferences:"
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
        temperature=0.7,
    )

    global generated_propositions
    generated_propositions = [{"name": name.strip()} for name in response.choices[0].message.content.split("\n")]
    return {"ok": "ok"}

#method that sends generated dishes back to the website
@app.get("/generate-dish-propositions/sending-with-get-method")
async def get_generated_dish_propositions():
    global generated_propositions
    if not generated_propositions:
        raise HTTPException(status_code=404, detail="No generated dish propositions available.")
    return {"generated_propositions": generated_propositions}