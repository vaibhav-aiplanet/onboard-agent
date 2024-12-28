from typing import Annotated
from typing_extensions import TypedDict

from langchain_google_vertexai import ChatVertexAI
import vertexai

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


vertexai.init(project="onboard-agent-langgraph")

llm = ChatVertexAI(model_name="gemini-pro")


# share between all nodes
class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def init_node(state: State):
    # send out welcome email
    pass


def google_node(state: State):
    # create the user's google account and temporary password
    return


def github_node(state: State):
    # create the account
    # add permissions
    return


def jira_node(state: State):
    # TODOs
    # create the user's account
    # add permissions
    # integrate with github_account
    return


def welcome_node(state: State):
    # send the welcome mail on the private email address
    # use an email template
    # give out the user's email and password
    return


graph_builder.add_node("init", init_node)
graph_builder.add_node("google", google_node)
graph_builder.add_node("jira", jira_node)
graph_builder.add_node("github", github_node)
graph_builder.add_node("welcome", welcome_node)

graph_builder.add_edge(START, "init")
graph_builder.add_edge("init", "google")
graph_builder.add_edge("google", "github")
graph_builder.add_edge("github", "jira")

graph_builder.add_edge("jira", "welcome")
graph_builder.add_edge("welcome", END)

graph = graph_builder.compile()

workflow_image = graph.get_graph().draw_mermaid_png()
with open("workflow.png", "wb") as f:
    f.write(workflow_image)
