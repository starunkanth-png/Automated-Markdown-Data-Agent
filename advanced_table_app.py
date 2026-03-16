import tkinter as tk
from tkinter import messagebox
import requests

# YOUR SECRET KEY GOES HERE
NEWS_API_KEY = "44e47b88879b4d509f1ae3c41c63831a"

def format_logic(data_string):
    if not data_string.strip(): return ""
    delimiter = ";" if ";" in data_string and "," not in data_string else ","
    rows = [line.split(delimiter) for line in data_string.strip().split("\n") if line]
    clean_rows = [[cell.strip()[:40] for cell in row] for row in rows] # Trim long text
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

def fetch_current_affairs():
    query = news_query.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Enter a topic (e.g., 'Elections')")
        return
    
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] != "ok": raise Exception(data.get("message"))
        
        # Convert JSON news to Comma Separated format for the formatter
        csv_data = "Source, Date, Title\n"
        for art in data["articles"]:
            # Clean commas from titles to avoid breaking our own logic
            title = art['title'].replace(",", "")
            source = art['source']['name'].replace(",", "")
            csv_data += f"{source}, {art['publishedAt'][:10]}, {title}\n"
            
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, csv_data.strip())
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, format_logic(csv_data))
    except Exception as e:
        messagebox.showerror("API Error", f"Check your Key or Connection: {e}")

# --- GUI UI ---
root = tk.Tk()
root.title("6th Sem BE CSE: Automated Data Agent")
root.geometry("750x700")

# API Section
tk.Label(root, text="LIVE DATA FETCH (Current Affairs/Sports)", font=("Arial", 11, "bold")).pack(pady=5)
news_query = tk.Entry(root, width=50)
news_query.insert(0, "India Elections")
news_query.pack(pady=2)
api_btn = tk.Button(root, text="Fetch & Format Live News", command=fetch_current_affairs, bg="#FF5722", fg="white")
api_btn.pack(pady=5)

# Manual Section
tk.Label(root, text="Raw Data Editor:", font=("Arial", 10)).pack(pady=5)
input_text = tk.Text(root, height=8, width=85)
input_text.pack()

# Output Section
tk.Label(root, text="Final Markdown Table:", font=("Arial", 10, "bold")).pack(pady=5)
output_text = tk.Text(root, height=12, width=85, bg="#e8f5e9")
output_text.pack()

root.mainloop()