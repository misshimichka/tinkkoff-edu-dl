import argparse
from model import Model
from dataset import Dataset
from trainer import TextGenerationTrainer
from from_txt_to_pandas import from_txt_to_pd

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', type=str, default="data/")
parser.add_argument('--model', type=str, default="model.pt")
args = parser.parse_args()

csv_dataset = from_txt_to_pd(args.input_dir)

dataset = Dataset(args)
model = Model(dataset)
trainer = TextGenerationTrainer(model, dataset)
trainer.train(args)
