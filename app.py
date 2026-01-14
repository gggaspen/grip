import os
from grip import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    path = os.environ.get("GRIP_PATH", ".")

    serve(
        path=path,
        host="0.0.0.0",
        port=port
    )
