from fastapi import FastAPI, HTTPException

app = FastAPI()

robots = [
    {
        "id": 1,
        "name": "Энди",
        "planet": "Марс",
        "status": "Работает"
    },
{
        "id": 1,
        "name": "Роби",
        "planet": "Луна",
        "status": "На зарядке"
    },
{
        "id": 1,
        "name": "Гектор",
        "planet": "Венера",
        "status": "Работает"
    },
]

@app.get("/")
def get_info():
    return {
        "message": "API Robots",
        "enpoints": [
            "/robots"
            "/robots/{id}"
        ]
    }

@app.get("/robots")
def get_robots(status: str = "Работает"):
    if status:
        filtered_robots = []
        for robot in robots:
            if robot["status"].lower() == status.lower():
                filtered_robots.append(robots)
        return filtered_robots
    return robots

@app.get("/robots/{robot_id}")
def get_robot_by_id(robot_id: int):
    for robot in robots:
        if robot["id"] == robot_id:
            return robot
    raise HTTPException(status_code=404, detail="No Robot")