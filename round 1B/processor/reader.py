import fitz  # PyMuPDF

def get_heading_level(font_size):
    if font_size >= 17:
        return "H1"
    elif font_size >= 14:
        return "H2"
    elif font_size >= 11.5:
        return "H3"
    return None

def process_and_rank(pdf_bytes):
    data = []
    doc = fitz.open("pdf", pdf_bytes)  # Read PDF from bytes

    current_section = None
    buffer_text = ""
    page_start = 0
    section_level = None

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b:
                continue
            for line in b["lines"]:
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not line_text:
                    continue

                font_size = max([span["size"] for span in line["spans"]])
                heading_level = get_heading_level(font_size)

                if heading_level:
                    if current_section:
                        data.append({
                            "page": page_start + 1,
                            "text": buffer_text.strip(),
                            "section_title": current_section,
                            "level": section_level
                        })
                    current_section = line_text
                    section_level = heading_level
                    buffer_text = ""
                    page_start = i
                else:
                    buffer_text += line_text + "\n"

    if current_section and buffer_text:
        data.append({
            "page": page_start + 1,
            "text": buffer_text.strip(),
            "section_title": current_section,
            "level": section_level
        })

    return data
