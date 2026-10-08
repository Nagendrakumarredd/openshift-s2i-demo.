import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style='text-align:center; margin-top:10%; font-family:Arial, sans-serif;'>
        <h1 style='color:#0066cc;'>🚀 Success! Your OpenShift App is Alive!</h1>
        <p style='font-size:1.2em;'>OpenShift successfully built your raw code using Source-to-Image (S2I).</p>
        <div style='background:#f4f4f4; padding:15px; display:inline-block; border-radius:5px;'>
            <strong>Pod Status:</strong> Running & Healthy Natively
        </div>
    </div>
    """

if __name__ == "__main__":
    # OpenShift automatically defines the PORT variable. 
    # If it is not found, we fall back to the corporate standard 8080.
    port = int(os.environ.get("PORT", 8080))
    # Binding to 0.0.0.0 lets the internal cluster routing layer access the container.
    app.run(host="0.0.0.0", port=port)
