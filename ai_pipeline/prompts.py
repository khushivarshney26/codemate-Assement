def build_prompt(user_query, functions):
    func_descs = "\n".join(
        f"- **{f['name']}**: {f['description']}" for f in functions
    )

    return f"""
You are a smart function planner. Given a user request, select a sequence of functions to fulfill it.

## Function Library:
{func_descs}

## User Request:
"{user_query}"

## Output format:
[
  {{
    "function": "function_name",
    "params": {{ "param1": "value", ... }},
    "id": "step1"
  }},
  ...
]
Only use functions from the library. Refer to earlier steps' outputs using "stepX.result".
""".strip()