# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
# ]
# ///
import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import pandas as pd

    data = {"rank": [1, 2, 3], "language": ["Python", "Java", "JavaScript"]}
    languages = pd.DataFrame(data)

    print(languages)
    return


if __name__ == "__main__":
    app.run()
