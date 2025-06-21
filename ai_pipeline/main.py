from pipeline import process_query
from executor import execute_plan

if __name__ == "__main__":
    query = "Retrieve all invoices for March, summarize the total amount, and send the summary to my email."
    
    result = process_query(query)
    print("\nGenerated Plan:\n", result)

    if "plan" in result:
        execution_result = execute_plan(result["plan"])
        print("\nExecution Output:\n", execution_result)
