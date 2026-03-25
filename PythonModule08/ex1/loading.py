# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 15:55:59 by npillet         #+#    #+#               #
#  Updated: 2026/03/25 09:02:34 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import importlib.util


def loading() -> None:
    try:
        print("\nChecking dependencies:")
        dependencies_list = ["pandas", "requests", "matplotlib"]
        for dependency in dependencies_list:
            name = importlib.util.find_spec(dependency)
            if name is None:
                print(f"[KO] {dependency} is not installed")
                print("pip install -r requirements.txt")
                print("python3 loading.py")
                print("or")
                print("poetry install")
                print("poetry run python loading.py")
                return
            else:
                name = __import__(dependency)
                version = name.__version__
                if dependency == "pandas":
                    print(f"[OK] {dependency} ({version}) - Data manipulation"
                          " ready")
                elif dependency == "requests":
                    print(f"[OK] {dependency} ({version}) - Network access "
                          "ready")
                elif dependency == "matplotlib":
                    print(f"[OK] {dependency} ({version}) - Visualization "
                          "ready")

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        import numpy as np
        import pandas
        data = np.random.randn(1000)
        df = pandas.DataFrame(data, columns=['Matrix_Value'])

        print("Generating visualization...")
        import matplotlib.pyplot as plt
        file = "matrix_analysis.png"
        plt.plot(df['Matrix_Value'])
        plt.title("Matrix Analysis")
        plt.savefig(file)

        print("\nAnalysis complete!")
        print(f"Results saved to: {file}")
    except ImportError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")

    loading()
