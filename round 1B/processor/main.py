import os
import json
from reader import extract_pdf_structure
from ranker import rank_sections
from writer import write_output

COLLECTIONS = ["Collection_1", "Collection_2", "Collection_3"]

def process_collection(collection):
    input_path = os.path.join(collection, "challenge1b_input.json")
    pdf_folder = os.path.join(collection, "PDFs")
    output_path = os.path.join(collection, "challenge1b_output.json")

    with open(input_path) as f:
        task_input = json.load(f)

    documents_data = extract_pdf_structure(pdf_folder)
    ranked_data = rank_sections(documents_data, task_input)
    write_output(ranked_data, task_input, output_path)

def main():
    for collection in COLLECTIONS:
        if os.path.exists(collection):
            print(f"Processing: {collection}")
            process_collection(collection)

if __name__ == "__main__":
    main()
