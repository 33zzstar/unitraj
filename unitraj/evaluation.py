import pytorch_lightning as pl
import torch
import os
torch.set_float32_matmul_precision('medium')
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader
from models import build_model
from datasets import build_dataset
from utils.utils import set_seed
import hydra
from omegaconf import OmegaConf
import wandb

@hydra.main(version_base=None, config_path="configs", config_name="config")
def evaluation(cfg):
    set_seed(cfg.seed)
    OmegaConf.set_struct(cfg, False)  # Open the struct
    cfg = OmegaConf.merge(cfg, cfg.method)
    cfg['eval'] = True
    # 检查是否禁用wandb
    if cfg.get('disable_wandb', False):

        os.environ["WANDB_MODE"] = "disabled"
    else:
        wandb.init(project="unitraj")
    model = build_model(cfg)

    val_set = build_dataset(cfg, val=True)

    eval_batch_size = cfg.method['eval_batch_size']

    val_loader = DataLoader(
        val_set, batch_size=eval_batch_size, num_workers=cfg.load_num_workers, shuffle=False, drop_last=False,
        collate_fn=val_set.collate_fn)

    trainer = pl.Trainer(
        inference_mode=True,
        logger=None if cfg.debug else WandbLogger(project="unitraj", name=cfg.exp_name),
        devices=[3],
        accelerator="gpu" if cfg.debug else "gpu",
        profiler="simple",
    )

    trainer.validate(model=model, dataloaders=val_loader, ckpt_path=cfg.ckpt_path)


if __name__ == '__main__':
    
    evaluation()
