from fastapi import FastAPI
from OSINT import OSINTScanner

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OSINT Tool v1.0"}

@app.get("/search")
def search(username: str, timeout: int = 5):
    scanner = OSINTScanner(username=username, timeout=timeout)
    scanner.scan()

    results = [
        {"url": url, "status": status}
        for status, url in scanner.results
    ]

    found_count = sum(1 for s, u in scanner.results if s == "found")

    return {
        "username": username,
        "total": len(results),
        "found_count": found_count,
        "results": results
    }
