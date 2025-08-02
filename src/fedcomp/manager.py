import uvicorn

from fedcomp.control_panel.main import app


def start_server(host="127.0.0.1", port=8000):
    print(f"Starting control panel on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)