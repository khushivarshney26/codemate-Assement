# executor.py

def get_invoices(month):
    return [f"Invoice1_{month}", f"Invoice2_{month}"]

def summarize_invoices(invoices):
    return f"Total amount: ${len(invoices) * 6400}"

def send_email(to, content):
    return f"Email sent to {to} with content: {content}"

function_registry = {
    "get_invoices": get_invoices,
    "summarize_invoices": summarize_invoices,
    "send_email": send_email
}

def resolve_value(val, context):
    val = val.strip().strip('"').strip("'")
    # return the actual object from context if available
    return context.get(val, val)

def execute_plan(plan):
    context = {}

    for call in plan:
        if not call.endswith(")"):
            print(f"Skipping malformed call: {call}")
            continue

        func_name = call.split("(", 1)[0].strip()
        args_str = call[len(func_name) + 1:-1].strip()

        if func_name not in function_registry:
            print(f"⚠️ Unknown function: {func_name}")
            continue

        args = {}
        if args_str:
            pairs = args_str.split(",")
            for pair in pairs:
                pair = pair.strip()
                if "=" in pair:
                    key, val = pair.split("=", 1)
                    key = key.strip()
                    val = resolve_value(val, context)
                    args[key] = val
                else:
                    # fallback for positional argument style
                    val = resolve_value(pair, context)
                    args = {"invoices": val}

        print(f"Running: {func_name}({args})")
        try:
            result = function_registry[func_name](**args)
        except Exception as e:
            result = f"❌ Error in {func_name}: {str(e)}"

        context[func_name] = result

    return context
