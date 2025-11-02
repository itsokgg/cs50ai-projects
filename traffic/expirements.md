# Experimentation Process
- first tried model used in lecture:
    - convolutional layer = 32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    - pooling layer = max-pooling with pool size of 2x2
    - hidden layer(s) = 1 @ 128 relu
    - dropout = 0.5
    - output activation = softmax
    after 10 epochs: accuracy: 0.0606 - loss: 3.4964 

- second tried same as first model except:
    hidden layer(s) = 4 @ 128 relu
    after 10 epochs: accuracy: 0.9228 - loss: 0.3179

- third went back to to using 2 layers and then 3 layers
    2 layers after 10 epochs: accuracy: 0.0552 - loss: 3.5068
    3 layers ofter 10 epocks: accuracy: 0.8813 - loss: 0.4884

- fourth tried 5 layers:
    accuracy: 0.9039 - loss: 0.4914
    seems to have gotten worse from 4 layers
    ran it again and:
    accuracy: 0.9316 - loss: 0.2731

- fifth tried 10 layers twice and got:
    1) accuracy: 0.8879 - loss: 0.3664 
    2) accuracy: 0.8565 - loss: 0.5091
    *going too high in layers definetly makes it less acurrate*

- sixth tried 8 layers thrice:
    1) accuracy: 0.9285 - loss: 0.2793
    2) accuracy: 0.9225 - loss: 0.2825
    3) accuracy: 0.9482 - loss: 0.2111 

- next tried 6 layers thrice:
    1) accuracy: 0.8973 - loss: 0.5475
    2) accuracy: 0.8864 - loss: 0.5097
    3) accuracy: 0.9317 - loss: 0.3018

- next tried 7 layers thrice:
    1) accuracy: 0.8814 - loss: 0.4593
    2) accuracy: 0.9083 - loss: 0.3388
    3) accuracy: 0.9418 - loss: 0.2386 

- next tried 9 layers 
    1) accuracy: 0.8991 - loss: 0.3963
    2) accuracy: 0.8979 - loss: 0.4335

*conclusion: for this model, 7-8 layers seems to be limit above or below it seems to make it les accurate*

- next changed:
convolution filter to 64
used 7 layers:
1) accuracy: 0.9330 - loss: 0.2716
2) accuracy: 0.9200 - loss: 0.3060
3) accuracy: 0.9184 - loss: 0.3202

- next changed convolution filter to 128
1) accuracy: 0.9362 - loss: 0.2920
2) accuracy: 0.9322 - loss: 0.2703

filter 32: steps: about 5-8 ms
filter 64: steps: about 13-15 ms
filter 128 steps: about 28-35 ms

- changed convolution filter to 64 and from max-pooling to average pooling
    1) 0.9374 - loss: 0.2776
    2) 0.9256 - loss: 0.3288
    3) 0.9057 - loss: 0.4904

- switched optimizer to nadam:
    1) accuracy: 0.9480 - loss: 0.2363
    2) accuracy: 0.9164 - loss: 0.3703
    3) accuracy: 0.9493 - loss: 0.2312
- switched kernel_initializer from default: glorot_uniform to he_normal
    1) accuracy: 0.8675 - loss: 0.5075

- switch back to default and switched the dropout to 0.1
    1) accuracy: 0.9320 - loss: 0.2833
    2) accuracy: 0.9203 - loss: 0.3554

- switched pool size to 3x3
    half the speed
    1) accuracy: 0.9508 - loss: 0.2015
    2) accuracy: 0.9503 - loss: 0.2025

- switched pool size to 4x4
    1) accuracy: 0.9342 - loss: 0.2555

- switched convolution filter to 128
    1) accuracy: 0.8496 - loss: 0.6046
    2) accuracy: 0.9138 - loss: 0.3161
*somehow increasing the pool size to 3x3 made it more accurate, but to 4x4 less
- switched to 3x3 and 128
    1) accuracy: 0.9301 - loss: 0.2730
    2) accuracy: 0.9484 - loss: 0.2009

- swithced back to 64 to test again with 3x3:
    1) accuracy: 0.9549 - loss: 0.1870
    * (3x3) pool size is better at 64 than 128

- switched layers to 64 nodes from 128
    1) accuracy: 0.9145 - loss: 0.3462

- switched back to 10 layers
    accuracy: 0.9107 - loss: 0.4188

- 8 layers:
    1) accuracy: 0.9267 - loss: 0.2795

- 7 layers:
    1) accuracy: 0.9577 - loss: 0.1600

- 6 layers:
    1) accuracy: 0.9530 - loss: 0.1882
    2) accuracy: 0.9276 - loss: 0.2888

*7 layers seems to be the best when each layer is 128 nodes*

- 7 128 node layers + 1 64 node layer
    1) accuracy: 0.9310 - loss: 0.2850

- switched 64 node layer to beginning
    1) accuracy: 0.9344 - loss: 0.2555

- 7 layers with 256 nodes:
    time doubled 5/7ms per step to 11/14 ms per step
    1) accuracy: 0.9487 - loss: 0.1922
    2) accuracy: 0.9368 - loss: 0.2543

- 7 layers with 196 nodes:
    time is 10 ms
    1) accuracy: 0.9343 - loss: 0.2955

- 7 layers 144 nodes:
    1) accuracy: 0.9419 - loss: 0.2176
    2) accuracy: 0.9315 - loss: 0.2910

- 7 strides 128 nodes with added stride of (2,1)
    2ms/step - accuracy: 0.9342 - loss: 0.2453
    double speed a little less accuracy