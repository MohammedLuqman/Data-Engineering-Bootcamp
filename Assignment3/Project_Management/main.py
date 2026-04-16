from fastapi import FastAPI
from fastapi.responses import FileResponse
from database import engine,Base
from models import Users,Projects,Tasks
from routes import user,project,task

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(project.router)
app.include_router(task.router)

@app.get("/")
def read_root():
    return FileResponse("index.html")