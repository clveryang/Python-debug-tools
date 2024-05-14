import sys
import runpy
import os

os.chdir("dir for python script")

args = "python3 train.py hparams/train_ASR_transformer.yaml --data_folder=/work/TensorRT/demo/ASR_Speech_Transformer/data/aishell/data_aishell"

args = args.split()
if args[0] == 'python3':
    args.pop(0)

fun = runpy.run_path

sys.argv.extend(args[1:])

fun(args[0], run_name='__main__')
