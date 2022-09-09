from train import trainer
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--prefix', type=str, default="i was")
parser.add_argument('--model', type=str, default="model.pt")
parser.add_argument("--length", type=int, default=10)
args = parser.parse_args()

words = trainer.generate(args)
print(" ".join(words))