

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 
 22        [15, 18, 21]  1    751702  ultralytics.nn.modules.head.Detect           [2, 16, None, [64, 128, 256]] 
Model summary: 130 layers, 3,011,238 parameters, 3,011,222 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
train: Fast image access ✅ (ping: 0.0±0.0 ms, read: 485.3±199.5 MB/s, size: 12.9 KB)
train: Scanning /content/datasetv2/train/labels... 24 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 24/24 305.8it/s 0.1s
train: New cache created: /content/datasetv2/train/labels.cache
WARNING ⚠️ Box and segment counts should be equal, but got len(segments) = 130, len(boxes) = 134. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access ✅ (ping: 0.0±0.0 ms, read: 415.6±108.2 MB/s, size: 13.8 KB)
val: Scanning /content/datasetv2/valid/labels... 14 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 14/14 966.5it/s 0.0s
val: New cache created: /content/datasetv2/valid/labels.cache
WARNING ⚠️ Box and segment counts should be equal, but got len(segments) = 71, len(boxes) = 74. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.001667, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to /content/runs/detect/train2/labels.jpg... 
Image sizes 640 train, 640 val
Using 0 dataloader workers
Logging results to /content/runs/detect/train2
Starting training for 50 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/50         0G      1.388      3.912       1.12         47        640: 100% ━━━━━━━━━━━━ 2/2 14.5s/it 29.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.2s/it 5.2s
                   all         14         74    0.00471      0.374     0.0164    0.00419

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/50         0G      1.459      3.958      1.099         54        640: 100% ━━━━━━━━━━━━ 2/2 13.7s/it 27.4s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74    0.00632      0.518     0.0487     0.0165

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/50         0G      1.214      3.757      1.068         86        640: 100% ━━━━━━━━━━━━ 2/2 10.5s/it 21.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74     0.0124      0.737     0.0749     0.0431

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/50         0G      1.056      3.411     0.9779         58        640: 100% ━━━━━━━━━━━━ 2/2 10.3s/it 20.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74     0.0162      0.867      0.099     0.0631

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/50         0G      1.093      2.975     0.9357         62        640: 100% ━━━━━━━━━━━━ 2/2 9.9s/it 19.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.9s/it 5.9s
                   all         14         74      0.017      0.913      0.158      0.102

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/50         0G      1.114      2.577     0.9725         57        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.7s/it 4.7s
                   all         14         74     0.0163      0.929      0.242      0.155

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/50         0G      1.032      1.945     0.9655         50        640: 100% ━━━━━━━━━━━━ 2/2 9.9s/it 19.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74     0.0152      0.892      0.331      0.236

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/50         0G     0.8318      1.634     0.9004         42        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74     0.0156       0.91      0.363      0.278

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/50         0G     0.9046       1.54     0.9144         95        640: 100% ━━━━━━━━━━━━ 2/2 10.1s/it 20.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0151      0.892      0.359      0.275

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/50         0G     0.9635       1.58      0.925         78        640: 100% ━━━━━━━━━━━━ 2/2 10.1s/it 20.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74     0.0151      0.892      0.349      0.265

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/50         0G     0.9046      1.675     0.9326         69        640: 100% ━━━━━━━━━━━━ 2/2 9.9s/it 19.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0149      0.882      0.327       0.25

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/50         0G      0.838      1.551     0.9018         49        640: 100% ━━━━━━━━━━━━ 2/2 9.7s/it 19.4s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0157       0.91      0.329      0.242

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/50         0G     0.8371      1.609     0.8892         63        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74     0.0155      0.901      0.302      0.216

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/50         0G      0.827      1.591      0.927         62        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74     0.0161      0.929       0.27      0.194

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/50         0G     0.8975      1.543     0.9095         65        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0154      0.901      0.264       0.19

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/50         0G     0.8695      1.501     0.9018         82        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.2s/it 5.2s
                   all         14         74     0.0137       0.82      0.277      0.206

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/50         0G     0.7762      1.411     0.9344         53        640: 100% ━━━━━━━━━━━━ 2/2 10.4s/it 20.8s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0141      0.839      0.301      0.237

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/50         0G      0.746      1.355     0.8949         98        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.0s/it 5.0s
                   all         14         74     0.0142      0.848      0.288      0.218

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/50         0G     0.7696      1.268     0.9114         54        640: 100% ━━━━━━━━━━━━ 2/2 11.6s/it 23.3s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.8s/it 4.8s
                   all         14         74     0.0144      0.842      0.276      0.207

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/50         0G      0.752      1.306     0.8751         53        640: 100% ━━━━━━━━━━━━ 2/2 10.3s/it 20.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.7s/it 4.7s
                   all         14         74     0.0151      0.885      0.282       0.22

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/50         0G     0.7019      1.229     0.8821         65        640: 100% ━━━━━━━━━━━━ 2/2 11.0s/it 22.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.7s/it 4.7s
                   all         14         74     0.0156      0.904      0.288      0.226

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      22/50         0G     0.8178      1.251     0.9055         78        640: 100% ━━━━━━━━━━━━ 2/2 10.3s/it 20.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74     0.0162      0.947       0.31      0.248

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      23/50         0G     0.8154      1.207     0.8795         58        640: 100% ━━━━━━━━━━━━ 2/2 10.2s/it 20.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74     0.0161      0.947      0.347      0.289

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      24/50         0G     0.7982      1.129     0.8946         68        640: 100% ━━━━━━━━━━━━ 2/2 10.2s/it 20.4s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74     0.0162      0.956       0.45      0.374

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      25/50         0G     0.7944      1.112     0.8715         83        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74     0.0161      0.956      0.511      0.435

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      26/50         0G     0.7851      1.036     0.8508        118        640: 100% ━━━━━━━━━━━━ 2/2 10.1s/it 20.2s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74     0.0164      0.966      0.569      0.497

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      27/50         0G     0.7361      1.038     0.8997         48        640: 100% ━━━━━━━━━━━━ 2/2 9.9s/it 19.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74     0.0164      0.966      0.671       0.59

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      28/50         0G     0.8398      1.043     0.8642         85        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.7s/it 4.7s
                   all         14         74     0.0164      0.966      0.671       0.59

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      29/50         0G     0.7407     0.9475     0.8894         68        640: 100% ━━━━━━━━━━━━ 2/2 10.3s/it 20.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74     0.0164      0.966      0.673      0.582

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      30/50         0G     0.7059     0.9548      0.885         51        640: 100% ━━━━━━━━━━━━ 2/2 10.2s/it 20.4s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74      0.884      0.407      0.768      0.664

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      31/50         0G     0.7294     0.9193      0.885         73        640: 100% ━━━━━━━━━━━━ 2/2 10.3s/it 20.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74      0.884      0.407      0.768      0.664

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      32/50         0G     0.6921     0.9509      0.863         67        640: 100% ━━━━━━━━━━━━ 2/2 10.1s/it 20.2s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74      0.922      0.186      0.801      0.697

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      33/50         0G     0.6831     0.9643      0.874         67        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74      0.946      0.314       0.81      0.691

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      34/50         0G     0.7329     0.9052     0.9118         62        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 19.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74      0.946      0.314       0.81      0.691

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      35/50         0G     0.6731     0.8671      0.841         79        640: 100% ━━━━━━━━━━━━ 2/2 10.2s/it 20.4s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.5s/it 4.5s
                   all         14         74      0.968      0.509      0.847      0.717

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      36/50         0G     0.7065     0.8502      0.849         66        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74      0.939       0.61      0.867      0.747

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      37/50         0G     0.6693     0.8474      0.859         49        640: 100% ━━━━━━━━━━━━ 2/2 9.9s/it 19.8s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74      0.939       0.61      0.867      0.747

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      38/50         0G     0.5889     0.8907      0.836         36        640: 100% ━━━━━━━━━━━━ 2/2 10.0s/it 20.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74      0.934       0.69      0.889      0.787

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      39/50         0G     0.7228     0.9638     0.8663         56        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.8s/it 4.8s
                   all         14         74      0.971      0.728      0.896      0.784

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      40/50         0G     0.6239     0.8058     0.8622         59        640: 100% ━━━━━━━━━━━━ 2/2 10.1s/it 20.2s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.7s/it 4.7s
                   all         14         74      0.971      0.728      0.896      0.784
Closing dataloader mosaic
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      41/50         0G      0.623     0.8321     0.8626         40        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74      0.971      0.751      0.899      0.779

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      42/50         0G     0.6043     0.8322     0.8569         44        640: 100% ━━━━━━━━━━━━ 2/2 9.7s/it 19.3s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74      0.947      0.781       0.91      0.788

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      43/50         0G      0.583     0.8149     0.8266         50        640: 100% ━━━━━━━━━━━━ 2/2 9.4s/it 18.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74      0.947      0.781       0.91      0.788

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      44/50         0G     0.5611     0.7972      0.843         39        640: 100% ━━━━━━━━━━━━ 2/2 9.6s/it 19.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74       0.95      0.795      0.928      0.807

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      45/50         0G     0.6104     0.9082     0.8191         40        640: 100% ━━━━━━━━━━━━ 2/2 9.6s/it 19.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74       0.95      0.795      0.928      0.807

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      46/50         0G     0.6225     0.8262     0.8272         40        640: 100% ━━━━━━━━━━━━ 2/2 9.6s/it 19.3s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 5.1s/it 5.1s
                   all         14         74      0.956      0.827      0.945      0.826

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      47/50         0G     0.5654     0.7632     0.8243         52        640: 100% ━━━━━━━━━━━━ 2/2 9.4s/it 18.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74      0.956      0.827      0.945      0.826

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      48/50         0G     0.5912      0.817     0.8547         49        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.9s/it 4.9s
                   all         14         74      0.959      0.834      0.951      0.829

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      49/50         0G     0.5716     0.8042      0.839         37        640: 100% ━━━━━━━━━━━━ 2/2 9.6s/it 19.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.6s/it 4.6s
                   all         14         74      0.959      0.834      0.951      0.829

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      50/50         0G     0.5737     0.8051     0.8272         42        640: 100% ━━━━━━━━━━━━ 2/2 9.8s/it 19.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.4s/it 4.4s
                   all         14         74      0.957      0.853      0.957      0.838

50 epochs completed in 0.353 hours.
Optimizer stripped from /content/runs/detect/train2/weights/last.pt, 6.2MB
Optimizer stripped from /content/runs/detect/train2/weights/best.pt, 6.2MB

Validating /content/runs/detect/train2/weights/best.pt...
Ultralytics 8.4.13 🚀 Python-3.12.12 torch-2.9.0+cpu CPU (Intel Xeon CPU @ 2.20GHz)
Model summary (fused): 73 layers, 3,006,038 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 4.2s/it 4.2s
                   all         14         74      0.957      0.853      0.957      0.839
           Allen screw         14         54          1      0.856      0.989      0.845
                 screw         10         20      0.914       0.85      0.926      0.833
Speed: 2.9ms preprocess, 246.6ms inference, 0.0ms loss, 41.5ms postprocess per image






