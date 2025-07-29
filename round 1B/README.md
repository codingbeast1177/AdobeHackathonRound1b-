
# Round 1B – Persona-Driven Document Intelligence

##  Challenge Overview
This project is a submission for **Adobe India Hackathon Round 1B**: _“Connect What Matters – For the User Who Matters”_.  
The goal is to build an intelligent document analysis system that extracts and ranks the most relevant sections and subsections from a collection of PDFs based on a given **persona** and their **job-to-be-done**.

---

##  Project Structure

.
├── processor/
│   ├── main.py              # Pipeline entrypoint
│   ├── reader.py            # Extracts structured data from PDFs
│   ├── ranker.py            # Ranks relevant sections
│   ├── writer.py            # Writes final output JSON
│   ├── utils.py             # Helper functions
├── round1B_webapp/          # Optional UI
├── requirements.txt         # Python dependencies
├── Dockerfile               # Backend docker image
├── docker-compose.yml       # Docker orchestration
├── approach_explanation.md  # Methodology explanation
├── README.md                # This file
├── input/                   # Input PDFs (mounted at /app/input)
└── output/                  # Output JSONs (mounted at /app/output)

---

##  How to Run

Make sure you’re in the root directory of the project and run the following commands:

cd "$HOME/Desktop/round 1B"
docker compose down --volumes --remove-orphans
docker compose build --no-cache
docker compose up

Alternatively, for Adobe’s evaluation, the following standard command will be used:

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier

---

##  Output Format

The system outputs a structured JSON file containing:

1. Metadata
   - Document names
   - Persona
   - Job-to-be-done
   - Timestamp

2. Extracted Sections
   - Document name
   - Page number
   - Section title
   - Importance rank

3. Subsection Analysis
   - Document
   - Page number
   - Refined text summary

Sample Output:
https://drive.google.com/file/d/1NWYhvksHgdTmYaIWnFfhg0RY5ZXbrLYF/view 

---

##  Libraries & Tools Used

- PyMuPDF – PDF parsing and layout extraction
- Scikit-learn – TF-IDF vectorization and cosine similarity
- NLTK / Regex – Preprocessing and keyword extraction
- Docker – Containerization for platform-independent deployment
- Python 3.9+

---

##  Highlights

- Runs fully offline, without internet dependency
- Model size < 1GB (if any used)
- Completes within 60 seconds for 3–5 documents
- CPU-only and optimized for amd64 architecture
- Modular structure, reusable for Round 2

---

##  Testing

- Evaluated on multiple domains (research, finance, education)
- Supports ranking of headings and sub-headings by relevance
- Can be integrated into web-based interfaces

---

##  Notes

- Headings are not hardcoded; generic logic ensures adaptability
- Designed with flexibility for varied personas and goals
- Uses no external API calls or large cloud-based models

---

##  Deliverables

- README.md – Overview and instructions
- approach_explanation.md - Explanation of methodology
- Dockerfile, docker-compose.yml - For reproducible builds
- Codebase – Modular and extensible for future improvements

---

##  Contact

Feel free to reach out if you'd like to discuss the solution or suggestions.  
Let’s connect the dots - for real!
