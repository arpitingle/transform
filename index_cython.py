import json
from utils import normalize_and_join  # compiled from utils.pyx

def json_to_payload(doc):
    """
    Transform a JSON document to payload format using Cython normalize_and_join
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

def load_and_process_data_cython(json_file_path):
    """
    Load JSON data and process each document using Cython functions
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
    # Process the sample data using Cython functions
    processed_documents = load_and_process_data_cython("sample.json")
    
    # Optionally save processed data
    with open("processed_documents_cython.json", 'w', encoding='utf-8') as output_file:
        json.dump(processed_documents, output_file, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {len(processed_documents)} documents using Cython")
    print("Results saved to processed_documents_cython.json")