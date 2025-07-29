from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import io
from processor.reader import process_and_rank
from processor.ranker import rank_sections

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/rank")
async def rank_pdf(
    file: UploadFile = File(...),
    persona: str = Form(...),
    job: str = Form(...)
):
    pdf_bytes = await file.read()
    sections = process_and_rank(pdf_bytes)
    ranked_sections = rank_sections(sections, persona, job)
    doc_id = file.filename
    result = {
        "document_id": doc_id,
        "relevant_sections": [
            {
                "heading": s.get("section_title", ""),
                "rank": s.get("importance_rank", 0),
                "score": float(s.get("score", 0.0)) if "score" in s else None,
                "level": s.get("level", "")
            } for s in ranked_sections
        ]
    }
    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
