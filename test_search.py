from app.search import search_manual

results = search_manual("point machine maintenance")

for result in results:
    print(result["source"])
    print(result["text"])