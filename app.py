import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
import warnings
warnings.simplefilter("ignore", ResourceWarning)


async def run_memory_chat():

    load_dotenv()

    config_file = "browser_mcp.json"

    print("Initializing chat...")

    # Create MCP client and agent with memory enabled
    client = MCPClient.from_config_file(config_file)

    llm = ChatOpenAI()

    # Create agent with memory_enabled=True
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,  # Enable built-in conversation memory
    )

    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")

    try:
        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")


    finally:
        if client and client.sessions:
            await client.close_all_sessions()

        # Ensure all asyncio tasks are completed
        tasks = asyncio.all_tasks()
        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run_memory_chat())