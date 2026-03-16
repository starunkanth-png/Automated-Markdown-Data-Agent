def format_to_markdown(data_string, delimiter=","):
    # Step 1: Split the raw string into rows and then into cells
    rows = [line.split(delimiter) for line in data_string.strip().split("|")]
    
    clean_rows = [[cell.strip() for cell in row] for row in rows]
    
    num_columns = len(clean_rows[0])
    col_widths = [max(len(row[i]) for row in clean_rows) for i in range(num_columns)]
    
    formatted_table = []
    for index, row in enumerate(clean_rows):
        formatted_row = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"
        formatted_table.append(formatted_row)
        
        if index == 0:
            separator = "| " + " | ".join("-" * col_widths[i] for i in range(num_columns)) + " |"
            formatted_table.append(separator)
            
    return "\n".join(formatted_table)

# --- Improved Multi-line Interactive Part ---
print("--- Markdown Table Agent ---")
print("1. Type your header (e.g., Name, Age)")
print("2. Type each player on a new line (e.g., Neymar, 35)")
print("3. Type 'DONE' when you are finished.")
print("-" * 30)

all_lines = []
while True:
    line = input("> ")
    if line.upper() == "DONE":
        break
    all_lines.append(line)

if all_lines:
    # We join them with '|' so the original function still works
    user_input = " | ".join(all_lines)
    result = format_to_markdown(user_input)
    print("\nGenerated Markdown Table:\n")
    print(result)