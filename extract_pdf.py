import pymupdf4llm
import sys
import os

input_pdf = sys.argv[1]
output_md = sys.argv[2]

print(f"Extracting '{input_pdf}' to '{output_md}'...")
try:
    md_text = pymupdf4llm.to_markdown(input_pdf)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_text)
    print("Done.")
except Exception as e:
    print(f"Error: {e}")
