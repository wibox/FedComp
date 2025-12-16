import uvicorn

from fedcomp.control_panel.main import app
from fedcomp.hello.hello import hello_world


def start_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    print(f"Starting control panel on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)

def hello(completeness: str) -> str:
    return hello_world(completeness)