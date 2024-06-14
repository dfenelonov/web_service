from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/health")
async def get_health():
    return {"health": "Ok"}

@app.get("/query")
async def read_item(query: str):
    return process_query(query)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
