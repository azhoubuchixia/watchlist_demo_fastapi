from uvicorn import run

from backend.api import app

if __name__ == '__main__':
    run("main:app",
        host='127.0.0.1',
        port=8085,
        log_level="debug",
        reload=True, )
