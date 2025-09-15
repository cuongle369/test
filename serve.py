# serve.py

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

# Import graph và các config/schema từ file của bạn
from task_maistro import graph
import configuration
from langchain_core.runnables import RunnableConfig

# Define input schema cho endpoint /run
class RunRequest(BaseModel):
    messages: List[Dict[str, Any]]  # giống state["messages"] kiểu messages list
    # Nếu cần thêm các thông số khác (ví dụ user_id, todo_category, role)
    user_id: str
    todo_category: str
    task_maistro_role: str

# FastAPI app
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
async def run_graph(req: RunRequest):
    try:
        # Tạo config từ request
        config = RunnableConfig(
            configurable={
                "user_id": req.user_id,
                "todo_category": req.todo_category,
                "task_maistro_role": req.task_maistro_role
            }
        )
        # Gọi graph với input + config
        result = graph.invoke(
            input={"messages": req.messages},
            config=config
        )
        # graph.invoke trả dạng dict (thường {"messages": [...]} hoặc tương tự)
        return {"result": result}
    except Exception as e:
        # catch lỗi để trả HTTP 500 nếu có gì sai
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "10000"))
    uvicorn.run("serve:app", host="0.0.0.0", port=port)
