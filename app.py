Python
from flask import Flask, render_template, request, jsonify
from scanner import scan
import os

app = Flask(name)
def home():
    return render_template("index.html")
@app.route("/scan",methods=["POST"])
def run_scan():
    url = request.form.get("url","").strip()
    if not url.startswith(("http://","https://")):
        url = "http://" + url

        issues = scan(url)
report_path = os.path.join("static", "report.txt")

with open(report_path, "w") as f:
    if issues:
        f.write("VULNERABILITIES FOUND:\n" + "\n".join(f"- {item}" for item in issues))
    else:
        f.write("No vulnerabilities found. The site appears secure.")

return jsonify({
    "issues": issues,
    "report_url": f"/static/report.txt?t={os.path.getmtime(report_path)}"
})
if name == "main":
    app.run(debug=True)
