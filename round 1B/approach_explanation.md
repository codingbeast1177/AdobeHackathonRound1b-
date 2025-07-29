
# Round 1B – Approach Explanation

##  Objective
To build an intelligent system that identifies and ranks the most relevant document sections tailored to a persona and their job-to-be-done. The goal is to simulate a domain expert’s reading behavior — focusing only on what matters.

---

##  Methodology

1. Preprocessing & Parsing  
   Using PyMuPDF, we extract text content along with metadata like section titles and page numbers from all input PDFs. Each document is split into logical chunks (sections and paragraphs) using layout heuristics and heading detection.

2. Keyword Extraction from Persona & Task  
   We derive key concepts from the persona and job description using TF-IDF, RAKE, and basic NER (if needed). This forms the query vector representing user intent.

3. Relevance Ranking  
   Each section and paragraph is scored against the query vector using cosine similarity. Sections are filtered and importance-ranked based on threshold scores and contextual matches.

4. Subsection Analysis  
   For the top-ranked sections, deeper paragraphs are analyzed and summarized if necessary. This helps in capturing refined insights and supports deeper task understanding.

5. Final Output Construction  
   The final output is a structured JSON containing:
   - Metadata (documents, persona, job-to-be-done)
   - Ranked sections with titles, page numbers, and ranks
   - Subsection-level refined text analysis

---

##  Design Choices

- No large models are used to stay within the 1GB model size and runtime constraint.
- The pipeline is entirely CPU-based and runs under 60 seconds for 3–5 PDFs.
- The modular pipeline allows future integration with frontends or APIs.

---

##  Example

Persona: Investment Analyst  
Job: "Analyze revenue trends, R&D investments, and market positioning strategies."  
Our system surfaces sections from annual reports that mention financial growth, innovation budgets, and competitor comparisons — ranked in priority based on keyword density and semantic overlap.

---

##  Compliance

-  No network calls used
-  Model-free / under 1GB limit
-  CPU-only, runs offline
-  Docker-compatible for amd64 systems

---

##  Future Extensions

- Incorporate summarization using LLMs (offline-compatible)
- Add support for tabular financial data extraction
- Expand to multilingual documents
