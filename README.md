# langsmith-agent

A simple echo agent deployed on LangSmith, used for prototyping integration with external agent environments.

## Architecture

```
Client (cURL/SDK)
    │
    │  POST /runs/wait
    │  X-Api-Key: <langsmith-api-key>
    │
    ▼
LangSmith Cloud
    │
    │  langgraph.json → agent.py:workflow
    │
    ▼
StateGraph (echo node)
    │
    │  Returns "Echo: <input>"
    │
    ▼
JSON Response
```

## Files

| File | Purpose |
|------|---------|
| `agent.py` | LangGraph StateGraph with a single echo node |
| `langgraph.json` | LangSmith deployment config — maps agent name to graph |
| `requirements.txt` | Dependencies, pinned to match LangSmith server runtime |

## Deployment

1. Push to GitHub
2. In [LangSmith](https://smith.langchain.com/) → Deployments → + New Deployment → select this repo
3. Wait ~15 min for build to complete

> **Important:** `langgraph` version in `requirements.txt` must match the server runtime version. Check with `GET /info` on the deployment URL.

## Usage

```bash
curl -s --request POST \
  --url <DEPLOYMENT_URL>/runs/wait \
  --header 'Content-Type: application/json' \
  --header 'X-Api-Key: <LANGSMITH_API_KEY>' \
  --data '{
    "assistant_id": "agent",
    "input": {
      "messages": [{"role": "human", "content": "Hello!"}]
    }
  }'
```

Response:
```json
{
  "messages": [
    {"type": "human", "content": "Hello!"},
    {"type": "ai", "content": "Echo: Hello!"}
  ]
}
```


