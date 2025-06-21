FUNCTIONS = [
    {
        "name": "get_invoices",
        "description": "Retrieve all invoices for a given month.",
        "parameters": {
            "month": "string"
        },
        "returns": "List[Dict]"
    },
    {
        "name": "summarize_invoices",
        "description": "Calculate total from a list of invoices.",
        "parameters": {
            "invoices": "List[Dict]"
        },
        "returns": "Dict"
    },
    {
        "name": "send_email",
        "description": "Send an email with a subject and body.",
        "parameters": {
            "to": "string",
            "subject": "string",
            "body": "string"
        },
        "returns": "bool"
    },
    {
        "name": "get_user_email",
        "description": "Fetch a user's email address.",
        "parameters": {
            "user_id": "string"
        },
        "returns": "string"
    },
    {
        "name": "filter_by_date",
        "description": "Filter records by date range.",
        "parameters": {
            "items": "List[Dict]",
            "start_date": "string",
            "end_date": "string"
        },
        "returns": "List[Dict]"
    }
]