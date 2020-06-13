# BeatCancer
Breast Cancer Classification using CNN
Breast cancer develops from the breast tissue and shows different signs such as lumps, change in shape, changes in the texture of skin and pains in some cases. The detection of breast cancer happens through Mammography, ultrasound, analysing tissues, Biopsy and more methods. Each method has its unique way of identification and prone to manual mistakes. The usage of technology in classifying breast cancer improves diagnostic efficiency. The problem of classifying cancer can be done with the histopathology datasets, which is the accurate way of detecting it. 
In this project, the breast cancer classification of benign or malignant is carried out with the help of convolutional neural networks with simple SE-ResNet Model. The approach proposed in this work utilises CNN to extract features of histopathological images and classify the images into benign tumours and malignant tumours. 

## Residual Networks
Residual network gets added as a shortcut connection to the main path. For Identity mapping, the layers are added, and the other layers are derived from the learned model. Residual blocks with the shortcut connection enable to learn an identity function. These facilitate no impact on the training set because of the additional residual blocks getting stacked up
 
<img src="./images/Resnet.jpg">

## Squeeze and Excitation Networks
SE-ResNet is built upon the convolution operation, which extracts informative features by fusing spatial and channel-wise information within local receptive fields.
SE proposed a weighted representation on a layer rather an equal representation. By learning the corresponding weights of each channel in the SE-block, it introduces an addition hyperparameter, r (ratio) to be used. For c number of channels, it attempts to learn a (sigmoidal) vector of size c (a tensor of 1x1xc to be exact) and multiplies it with the current tensor in the given layer.

<img src="./images/SE.jpg">

<ins><b>Solution Approach</b></ins>
<img src="./images/SolutionApproach.jpg">

### Results
<ins><b>SE Resnet</b></ins>
<img src="./images/SimpleSEResnet.jpg">

<ins><b>Resnet50</b></ins>
<img src="./images/Resnet50.jpg">

<ins><b>Results Summary</b></ins>
<img src="./images/Results.jpg">

### References


