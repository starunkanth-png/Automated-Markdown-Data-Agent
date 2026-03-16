import tkinter as tk
from tkinter import messagebox

def format_to_markdown():
    # Get data from the text box
    data_string = input_text.get("1.0", tk.END).strip()
    
    if not data_string:
        messagebox.showwarning("Input Error", "Please enter some data first!")
        return

    try:
        # The logic you already mastered
        rows = [line.split(",") for line in data_string.split("\n")]
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
        
        # Display the result in the output box
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "\n".join(formatted_table))
    except Exception as e:
        messagebox.showerror("Format Error", "Make sure your data is comma-separated!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Markdown Table Generator Agent")
root.geometry("600x500")

# Input Label
tk.Label(root, text="Enter Raw Data (Comma Separated):", font=("Arial", 10, "bold")).pack(pady=5)
input_text = tk.Text(root, height=8, width=70)
input_text.pack(pady=5)

# Convert Button
convert_btn = tk.Button(root, text="Generate Markdown Table", command=format_to_markdown, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
convert_btn.pack(pady=10)

# Output Label
tk.Label(root, text="Markdown Output:", font=("Arial", 10, "bold")).pack(pady=5)
output_text = tk.Text(root, height=10, width=70, bg="#f0f0f0")
output_text.pack(pady=5)

root.mainloop()