import gzip
import xml.etree.ElementTree as ET
from pathlib import Path

def extract_abstracts(xml_gz_file, out_txt_file):
    with gzip.open(xml_gz_file, 'rb') as f:
        tree = ET.parse(f)
        root = tree.getroot()

    abstracts = []
    for article in root.findall(".//Abstract/AbstractText"):
        text = article.text
        if text:
            abstracts.append(text.strip())

    Path(out_txt_file).write_text("\n".join(abstracts), encoding="utf-8")
    print(f"✅ Extracted {len(abstracts)} abstracts into {out_txt_file}")

# Example
extract_abstracts("pubmed25n0001.xml.gz", "pubmed_abstracts_1.txt")
extract_abstracts("pubmed25n0002.xml.gz", "pubmed_abstracts_2.txt")
