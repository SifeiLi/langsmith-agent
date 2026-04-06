from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from agent import workflow

app = FastAPI()

class RunRequest(BaseModel):
    assistant_id: str = "agent"
    input: dict

@app.post("/runs/wait")
def run_wait(req: RunRequest, x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=403, detail="Forbidden")
    result = workflow.invoke(req.input)
    return {"messages": [{"role": m.type, "content": m.content} for m in result["messages"]]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8123)
