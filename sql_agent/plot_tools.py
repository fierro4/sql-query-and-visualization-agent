import pandas as pd
import matplotlib.pyplot as plt


def generate_plot(data: dict):
    """
    Generates BAR chart only.
    """

    try:

        columns = data["columns"]
        rows = data["rows"]

        df = pd.DataFrame(rows, columns=columns)

        if len(df.columns) < 2:
            return "ERROR: Need at least 2 columns"

        x = df.columns[0]
        y = df.columns[1]

        plt.figure(figsize=(10, 6))

        plt.bar(df[x], df[y])

        plt.xlabel(x)
        plt.ylabel(y)

        plt.title(f"{y} by {x}")

        plt.xticks(rotation=45)

        output_file = "chart.png"

        plt.tight_layout()

        plt.savefig(output_file)

        plt.close()

        return {
            "status": "success",
            "chart": output_file
        }

    except Exception as e:

        return f"PLOT ERROR: {str(e)}"