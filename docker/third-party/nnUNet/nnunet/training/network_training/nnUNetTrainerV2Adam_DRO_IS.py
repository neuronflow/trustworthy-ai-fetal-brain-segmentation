from nnunet.training.network_training.nnUNetTrainerV2Adam_DRO import nnUNetTrainerV2Adam_DRO
from nnunet.training.network_training.nnUNetTrainerV2_DRO import CLIP_IMPORTANCE_WEIGHTS


class nnUNetTrainerV2Adam_DRO_IS(nnUNetTrainerV2Adam_DRO):
    def __init__(self, plans_file, fold, output_folder=None, dataset_directory=None,
                 batch_dice=True, stage=None, unpack_data=True, deterministic=True, fp16=False):
        super().__init__(plans_file, fold, output_folder, dataset_directory, batch_dice, stage,
                         unpack_data, deterministic, fp16)
        # parameter for dro
        self.importance_sampling = True
        print('DRO importance sampling is used')
        print('Importance weights are clipped to [%f, %f].' %
            (CLIP_IMPORTANCE_WEIGHTS[0], CLIP_IMPORTANCE_WEIGHTS[1]))
