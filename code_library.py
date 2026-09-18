from flask import Flask, request, redirect, url_for

app = Flask(__name__)

SNIPPETS = [
    {"id": 1, "title": "Flask Route Decorator", "category": "Flask", "code": "@app.route('/')\ndef home():\n    return 'Hello'"}
]

@app.route('/')
def library_home():
    snippet_html = ""
    for s in SNIPPETS:
        snippet_html += f'''
        <div style="background: #1b2230; border-radius: 8px; padding: 12px; margin-bottom: 12px; border: 1px solid #2a3447;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 14px; font-weight: bold; color: #fff;">{s['title']}</span>
                <span style="font-size: 11px; background: #0284c7; color: #fff; padding: 2px 6px; border-radius: 4px;">{s['category']}</span>
            </div>
            <pre style="background: #121824; padding: 10px; border-radius: 6px; border: 1px solid #334155; color: #38bdf8; overflow-x: auto; font-size: 12px; margin: 0;"><code>{s['code']}</code></pre>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Code Library</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; background: #121824; color: #fff; margin: 0; padding: 12px; }}
            h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 6px; }}
            .card {{ background: #1b2230; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2a3447; }}
            input, select, textarea {{ width: 100%; padding: 10px; margin: 6px 0 12px 0; background: #121824; border: 1px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; font-family: monospace; }}
            button {{ width: 100%; padding: 12px; background: #3b82f6; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Python & Flask Code Library</h2>
        <div class="card">
            <h3 style="margin-top:0; color:#38bdf8; font-size:15px; font-family:sans-serif;">Add Code Snippet</h3>
            <form action="/add_snippet" method="POST">
                <input type="text" name="title" placeholder="Snippet Title (e.g., File Uploads)" style="font-family:sans-serif;" required>
                <select name="category" style="font-family:sans-serif;">
                    <option value="Flask">Flask</option>
                    <option value="Python Logic">Python Logic</option>
                    <option value="CSS Layout">CSS Layout</option>
                </select>
                <textarea name="code" rows="4" placeholder="Paste code snippet here..." required></textarea>
                <button type="submit" style="font-family:sans-serif;">+ Save Snippet</button>
            </form>
        </div>
        <h3 style="color: #38bdf8; margin-top: 20px; font-family:sans-serif;">Saved Snippets</h3>
        {snippet_html}
    </body>
    </html>
    '''

@app.route('/add_snippet', methods=['POST'])
def add_snippet():
    title = request.form.get('title')
    category = request.form.get('category')
    code = request.form.get('code')
    if title and code:
        SNIPPETS.insert(0, {"id": len(SNIPPETS) + 1, "title": title, "category": category, "code": code})
    return redirect(url_for('library_home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
