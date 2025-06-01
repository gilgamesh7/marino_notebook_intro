import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    import matplotlib.pyplot as plt
    return mo, plt


@app.cell
def _(ui_fixed_cost, ui_quantity, ui_selling_price, ui_unit_cost):
    # fixed_cost = 50000   # The total fixed costs required for production to commence.
    # unit_cost = 2   # The cost of making one confectionery item.
    # selling_price = 10   # The selling price of one unit of confectionery.
    # upper_production_quantity = 10000   # The upper bound of units you can produce.

    fixed_cost = int(ui_fixed_cost.value)
    unit_cost = ui_unit_cost.value
    selling_price = float(ui_selling_price.value)
    upper_production_quantity = ui_quantity.value
    return fixed_cost, selling_price, unit_cost, upper_production_quantity


@app.cell
def _(fixed_cost, plt, selling_price, unit_cost, upper_production_quantity):
    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = break_even_quantity * selling_price

    units = range(0, upper_production_quantity + 1, 1000)
    total_costs = [(unit * unit_cost) + fixed_cost for unit in units]
    sales_income = [unit * selling_price for unit in units]

    plt.plot(units, total_costs, marker="o")
    plt.plot(units, sales_income, marker="x")

    plt.xlabel("Units Produced")
    plt.ylabel("($)")
    plt.legend(["Total Costs", "Total Income"])
    plt.title("Break-Even Analysis")

    plt.vlines(
        break_even_quantity,
        ymin=100,
        ymax=break_even_income,
        linestyles="dashed",
    )

    plt.text(
        x=break_even_quantity + 100,
        y=int(break_even_income / 2),
        s=int(break_even_quantity),
    )

    plt.grid()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(f"""
    **Adding interactivity**

    - Your fixed costs of $50,000 could be trimmed to $40,000 if you cut back elsewhere in the business

    - You could alter the cost price of your confectionery in increments of $1, between $2 and $5

    - You could change the selling price of your products to any value

    - You also want to ensure the plot can display production quantities of up to 15,000 units
    """)
    return


@app.cell
def _(mo):
    ui_fixed_cost = mo.ui.radio(options=["40000", "50000"], value="50000")
    ui_unit_cost = mo.ui.slider(start=2, stop=5, step=1)
    ui_selling_price = mo.ui.text(value="10")
    ui_quantity = mo.ui.dropdown(
        options={"10000": 10000, "12000": 12000, "15000": 15000},
        value="10000",
    )
    mo.md(
        f"""
        Fixed Costs: {ui_fixed_cost}

        Unit Cost Price: {ui_unit_cost}

        Selling Price: {ui_selling_price}

        Maximum Production Quantity: {ui_quantity}
        """
    )
    return ui_fixed_cost, ui_quantity, ui_selling_price, ui_unit_cost


if __name__ == "__main__":
    app.run()
