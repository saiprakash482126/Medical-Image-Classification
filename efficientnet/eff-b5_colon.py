_base_ = [
    '../_base_/models/efficientnet_b4.py', '../_base_/datasets/colon.py',
    '../_base_/schedules/imagenet_bs256_coslr.py',
    '../_base_/default_runtime.py', '../_base_/custom_imports.py'
]

model = dict(
    backbone=dict(
        init_cfg=dict(
            type='Pretrained',
            checkpoint=
            'pretrain/efficientnet-b4_3rdparty_8xb32-aa_in1k_20220119-45b8bd2b.pth',
            prefix='backbone',
        )),
    head=dict(num_classes=2),
)
