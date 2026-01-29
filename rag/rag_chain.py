from langchain.memory import ConversationBufferMemory

class RAGChain:
    def __init__(self, retriever, llm, prompt):
        self.retriever = retriever
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=False
        )
        self.chain = prompt | llm

    def format_context(self, doc: dict) -> str:
        if "text" in doc and doc["text"]:
            return doc["text"]
        lines = []
        
        for field in ["command", "category", "syntax", "description", "detailed_explanation", "skill_level"]:
            if field in doc:
                lines.append(f"{field.capitalize()}: {doc[field]}")

            if "common_options" in doc:
                lines.append("Options:")
                for opt in doc["common_options"]:
                    name = opt.get("option", "")
                    desc = opt.get("description", "")
                    example = opt.get("example", "")
                    lines.append(f"- {name}: {desc}")
                    if example:
                        lines.append(f"  Example: {example}")

            if "examples" in doc:
                lines.append("Examples:")
                for ex in doc["examples"]:
                    lines.append(f"- {ex}")

        if "use_cases" in doc:
            lines.append("Use Cases:")
            for use in doc["use_cases"]:
                lines.append(f"- {use}")

        if "security_considerations" in doc:
            lines.append("Security Considerations:")
            for sec in doc["security_considerations"]:
                lines.append(f"- {sec}")
        if "security_notes" in doc:
            lines.append("Security Notes:")
            for note in doc["security_notes"]:
                lines.append(f"- {note}")

        return "\n".join(lines) if lines else str(doc)

    def ask(self, query: str) -> str:
        retrieved_docs = self.retriever.query(query)
        if not retrieved_docs:
            return "I couldn't find relevant information in the knowledge base."

        #flatted all retrieved documents into single string
        context_text = "\n\n".join([self.format_context(doc) for doc in retrieved_docs])
        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")
        response = self.chain.invoke({
            "context": context_text,
            "question": query,
            "chat_history": chat_history
        })

        answer = getattr(response, "content", str(response))
        self.memory.save_context(
            {"question": query},
            {"answer": answer}
        )

        return answer
