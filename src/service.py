def health():
    return {"service": "testing-repo-public", "status": "ok"}


if __name__ == "__main__":
    print(health())

