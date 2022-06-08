import argparse
# import pytorch_lightning as pl
# from models.ultra_swin import UltraSwin
# from datamodules.EchoNetDataModule import EchoNetDataModule
# from pytorch_lightning.loggers import TensorBoardLogger
# from pytorch_lightning.callbacks.early_stopping import EarlyStopping

parser = argparse.ArgumentParser()
parser.add_argument("-mode", type=str, default="train", help="Put train, test or validate")
parser.add_argument("-logs", type=str, default="active", help="Option : activate (default) and deactivate")
parser.add_argument("-logs_dir", type=str, default="default_logs", help="Opt: select logs_dir")

params = parser.parse_args()

if __name__ == '__main__':
    mode = params.mode
    logs = params.logs
    logs_dir = params.logs_dir

    # logger = TensorBoardLogger(save_dir=logs_dir, name="ultraswin")

    if mode == 'train':
        print("train mode")

    if mode == 'validate':
        print("validation mode")

    if mode == 'test':
        print("test mode")

    if mode == 'predict':
        print("predict mode")
