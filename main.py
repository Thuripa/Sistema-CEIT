from flask import Flask, render_template
import pyrebase
from website import create_app

app = create_app()


# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)