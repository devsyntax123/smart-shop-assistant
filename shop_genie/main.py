from dotenv import load_dotenv
from graph.graph import graph

load_dotenv()


if __name__ == "__main__":
    initial_state = {"query": "Best smartphone under 30k rupees","email":"sruthi.bandiii@gmail.com"}
    #print(graph.invoke(input=initial_state))
    for event in graph.stream(input=initial_state,stream_mode="updates"):
        print(event)
