import json

def normalize_and_join(input_texts):
    """
    Pure Python implementation: takes a list of strings, lowercases, strips, 
    collapses whitespace, joins into one string
    """
    output_parts = []
    for part in input_texts:
        if part:
            normalized_part = " ".join(part.lower().strip().split())
            output_parts.append(normalized_part)
    return " ".join(output_parts)

def json_to_payload(doc):
    """
    Transform a JSON document to payload format
    """
    text_content = normalize_and_join([doc.get("title", ""), doc.get("body", "")])
    return {
        "id": str(doc["_id"]),
        "text": text_content,
        "metadata": {
            "author": doc.get("author"),
            "tags": doc.get("tags", [])
        }
    }

def load_and_process_data(json_file_path):
    """
    Load JSON data and process each document
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        documents = json.load(file)
    
    processed_docs = []
    for doc in documents:
        payload = json_to_payload(doc)
        processed_docs.append(payload)
        print(f"Processed document ID: {payload['id']}")
        print(f"Text preview: {payload['text'][:100]}...")
        print(f"Author: {payload['metadata']['author']}")
        print(f"Tags: {payload['metadata']['tags']}")
        print("-" * 50)
    
    return processed_docs

if __name__ == "__main__":
    # Process the sample data
    processed_documents = load_and_process_data("sample.json")
    
    # Optionally save processed data
    with open("processed_documents.json", 'w', encoding='utf-8') as output_file:
        json.dump(processed_documents, output_file, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {len(processed_documents)} documents")
    print("Results saved to processed_documents.json")