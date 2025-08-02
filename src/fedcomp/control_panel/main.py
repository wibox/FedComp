from fastapi import FastAPI

from fedcomp.control_panel.api.routes import router as api_router
from fedcomp.control_panel.core.config import settings

app = FastAPI(title="My FastAPI App")

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": f"{settings.app_name} is running"}
