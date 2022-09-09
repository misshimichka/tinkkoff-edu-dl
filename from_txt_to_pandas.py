import pandas as pd
import os


def from_txt_to_pd(filedir):
    files = []
    for i in os.walk(filedir):
        files = i[2]

    ds = []

    for file in files:
        text = open(filedir + file).read()
        text = text.lower()
        text = text.replace("\n", " ").replace("\t", " ").replace("!", " ") \
            .replace(".", " ").replace(",", " ").replace(")", " ").replace("(", " ") \
            .replace("?", " ").replace("/", " ").replace("'", " ").replace('"', " ") \
            .replace("-", " ").replace("=", " ").replace("+", " ").replace("{", " ") \
            .replace("}", " ").replace("[", " ").replace("]", " ").replace(";", " ") \
            .replace(":", " ")

        ds += text.split()

    pandas_dataset = pd.DataFrame({
        "Words": ds
    })

    pandas_dataset.to_csv(filedir + "dataset.csv", sep=";", index=None)
