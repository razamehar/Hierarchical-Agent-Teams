from teams.supervisor import top_level_supervisor


while True:
    query = input("Query: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting.")
        break

    result = top_level_supervisor.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": "user-session-1"
            }
        }
    )

    print(result["messages"][-1].content)