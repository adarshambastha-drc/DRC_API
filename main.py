from fastapi import FastAPI
from fastapi.responses import JSONResponse
from faker import Faker
import random
import itertools

app = FastAPI(title="DRC Systems Employee API (Smart IDs)")
fake = Faker()

teams = ["AI/ML", "Web Development", "Mobile", "Data Science", "QA", "DevOps"]

# Map full team names to short codes for the ID
team_codes = {
    "AI/ML": "AI",
    "Web Development": "WEB",
    "Mobile": "MOB",
    "Data Science": "DS",
    "QA": "QA",
    "DevOps": "OPS"
}

degrees = ["B.Tech", "M.Tech", "B.Sc", "MCA", "MBA", "PhD"]
grades = ["Intern", "Junior", "Mid-Level", "Senior", "Lead", "Manager"]

def sometimes_null(value):
    """20% chance of returning None."""
    return None if random.random() < 0.2 else value

def generate_smart_id(joining_date, team_name):
    """
    Creates an ID like: DRC-2023-WEB-4921
    1. Extract Year from joining date.
    2. Get Team Code (e.g., Web -> WEB).
    3. Add a random 4-digit suffix for uniqueness.
    """
    if not joining_date:
        year = "XXXX" # Fallback if date is null
    else:
        year = joining_date.split("-")[0] # Extract '2023' from '2023-05-12'

    # Get team code, default to 'GEN' (General) if team is null
    code = team_codes.get(team_name, "GEN")
    
    # Generate a random 5-digit number
    unique_suffix = random.randint(10000, 99999)
    
    return f"DRC-{year}-{code}-{unique_suffix}"

def employee_generator():
    while True:
        # 1. Generate core data first so we can build the ID based on it
        # We enforce that Team and Date are NOT null initially for the ID generation,
        # but we can apply nulls afterwards if strictly necessary. 
        # However, usually, IDs are permanent. Let's generate raw valid data first.
        
        raw_date = fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
        raw_team = random.choice(teams)
        
        # 2. Create the Meaningful ID
        smart_id = generate_smart_id(raw_date, raw_team)

        emp = {
            "Employee_ID": smart_id,  # e.g., DRC-2021-AI-59102
            "Name": sometimes_null(fake.name()),
            "Age": sometimes_null(random.randint(21, 60)),
            "Gender": sometimes_null(random.choice(["Male", "Female", "Other"])),
            "Team_Name": sometimes_null(raw_team), # Can still be null in the final output
            "Degree": sometimes_null(random.choice(degrees)),
            "Year_of_Passing": sometimes_null(random.randint(2010, 2025)),
            "Date_of_Joining": sometimes_null(raw_date), # Can still be null in final output
            "Skills": sometimes_null(
                random.sample(["Python", "AI", "ML", "React", "Node.js", "Docker", "SQL", "AWS"], k=3)
            ),
            "Mobile_Number": sometimes_null(fake.phone_number()),
            "Email_ID": sometimes_null(fake.email()),
            "Employee_Grade": sometimes_null(random.choice(grades)),
            "Company_Name": "DRC Systems"
        }
        yield emp

gen = employee_generator()

@app.get("/")
def home():
    return {"message": "DRC Systems Smart Employee API is Running."}

@app.get("/employees")
def get_employees(count: int = 5):
    employees = list(itertools.islice(gen, count))
    return JSONResponse(content=employees)