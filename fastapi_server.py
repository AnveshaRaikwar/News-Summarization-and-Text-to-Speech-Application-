from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/news/{query}")
async def get_news(query: str):
    return JSONResponse(content={"message": f"Fetching news for {query}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
