import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(f"**Use Pythagoras theorem to calculate hypotenuse**")
    return


@app.cell
def _(math):
    def calculate_hypotenuse(opposite, adjacent):
        return math.sqrt(opposite**2 + adjacent**2)
    return (calculate_hypotenuse,)


@app.cell
def _():
    # opposite = 3
    return


@app.cell
def _():
    adjacent = 4
    return (adjacent,)


@app.cell
def _(adjacent, calculate_hypotenuse, mo, opposite):
    mo.md(text=f"**Hypotenuse** = {calculate_hypotenuse(opposite,adjacent)}")
    return


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(mo):
    mo.md(text=f"""
        Comment this code to run the notebook
    """)
    # adjacent = 10
    return


if __name__ == "__main__":
    app.run()
