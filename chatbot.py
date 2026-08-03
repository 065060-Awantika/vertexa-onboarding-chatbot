import os
from dotenv import load_dotenv
from groq import Groq
from search import search  # reuses your existing search function

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_bot(question):
    # Step 1: retrieve relevant chunks
    results = search(question, top_k=3)
    context = "\n\n".join([r["text"] for r in results])

    # Step 2: build the prompt
    prompt = f"""You are an onboarding assistant for new employees at Vertexa Systems.
Answer the question using ONLY the context below. If the answer isn't in the context, say you don't have that information and suggest who they should contact.

Context:
{context}

Question: {question}

Answer clearly and concisely:"""

    # Step 3: call the LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    print("Onboarding Assistant (type 'quit' to exit)\n")
    while True:
        question = input("You: ")
        if question.lower() == "quit":
            break
        answer = ask_bot(question)
        print(f"\nBot: {answer}\n")