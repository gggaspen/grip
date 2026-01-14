import os
import sys
from grip import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    path = os.environ.get("GRIP_PATH", ".")

    if not os.path.exists(path):
        print(f"ERROR: path '{path}' does not exist")
        sys.exit(1)

    try:
        serve(
            path=path,
            host="0.0.0.0",
            port=port
        )
    except Exception as e:
        print("Grip failed to start:")
        print(e)
        sys.exit(1)
