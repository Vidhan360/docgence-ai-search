
def generate_answer(query, results):
    if not results:
        return f"No relevant books found for '{query}'."

    answer = f"Here are the most relevant books for '{query}':\n\n"

    for i, book in enumerate(results[:3], start=1):
        answer += (
            f"{i}. {book['title']}\n"
            f"   → {book['reason']}\n\n"
        )

    answer += "These results are based on semantic similarity between your query and book descriptions."

    return answer