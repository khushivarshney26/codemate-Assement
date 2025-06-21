from model_runner import run_model

def process_query(query):
    raw_output = run_model(query)
    print("RAW MODEL OUTPUT:\n", raw_output)

    # Split the response into steps
    rough_steps = raw_output.strip().split(") ")

    steps = []
    for step in rough_steps:
        step = step.strip()
        if step:
            if not step.endswith(")"):
                step += ")"
            steps.append(step)

    if not steps:
        return {"error": "Could not parse function plan", "raw_output": raw_output}

    return {"plan": steps}
