def health():
    return {"service": "testing-repo-public", "status": "ok"}


def metrics():
    return {"requests_per_minute": 42, "error_rate": 0.0}


if __name__ == "__main__":
    print(health())
    print(metrics())

