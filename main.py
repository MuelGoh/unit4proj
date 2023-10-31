from fastapi import FastAPI
import uvicorn

app = FastAPI()


# First we make some fake data to be able to use as our "database calls"
users = [
    {"name": "Smith", "rank": 1, "total": 2406257},
    {"name": "Johnson", "rank": 2, "total": 1882473},
    {"name": "Brown", "rank": 3, "total": 1755836},
    {"name": "Jones", "rank": 4, "total": 1684065},
    {"name": "Williams", "rank": 5, "total": 1526321},
    {"name": "Davis", "rank": 6, "total": 1440585},
    {"name": "Miller", "rank": 7, "total": 1433425},
    {"name": "Wilson", "rank": 8, "total": 1269737},
    {"name": "Moore", "rank": 9, "total": 1186701},
    {"name": "Taylor", "rank": 10, "total": 1178108},
    {"name": "Anderson", "rank": 11, "total": 1141153},
    {"name": "Thomas", "rank": 12, "total": 1112443},
    {"name": "Jackson", "rank": 13, "total": 973095},
    {"name": "White", "rank": 14, "total": 969012},
    {"name": "Harris", "rank": 15, "total": 907042},
    {"name": "Martin", "rank": 16, "total": 905418},
    {"name": "Thompson", "rank": 17, "total": 886358},
    {"name": "Garcia", "rank": 18, "total": 879962},
    {"name": "Martinez", "rank": 19, "total": 870712},
    {"name": "Robinson", "rank": 20, "total": 833494}
]


@app.get("/names")
async def get_names(api_key: str | None = None):
    if api_key == 'python3class':
        names = []
        for user in users:
            names.append(user['name'])
        return names
    return {"msg": "Api Key missing"}


@app.get("/lastnames/{name}")
async def get_name(name: str, api_key: str | None = None):
    if api_key == 'python3class':
        for user in users:
            if name.lower() == user["name"].lower():
                return user
        return {"msg": "Name not found"}
    return {"msg": "Api Key missing"}


# Here we see that order matters. Going to this path will trigger this route first rather than the next because it
# comes first
# @app.get("/users/name")
# async def get_name():
#     return {"name": "My Name"}
#
# @app.get("/users/rank")
# async def get_rank():
#     return {"rank": "This is the the rank for the name"}
#
# @app.get("/users/total")
# async def get_total():
#     return {"total": "This is the population for this name"}
#
# # Parameters in our route definitions allow us to match multiple paths
# @app.get("/users/{user_name}")
# async def get_profile(user_name: str):
#     for user in users:
#         if user_name.capitalize() in user["name"]:
#             return user
#     return {"msg": "User not found"}
#
#
# @app.get('/users')
# async def users_list():
#     names = []
#     for user in users:
#         names.append(user["name"])
#     return names
#
# # Here we see another way to create dynamic routes using query parameters
# @app.get("/documents")
# async def get_document(api_key: str | None = None):
#     if api_key == 'python3class':
#         return {"msg": f"Document {api_key} successfully retrieved", "doc": api_key}
#     return {"msg": "Name was not passed as a query"}
#
# @app.get('/secret')
# async def get_secret():
#     return {'secret': 'there are only two genders.'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)


