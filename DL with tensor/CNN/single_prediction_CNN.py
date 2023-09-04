#Convolutional neural network to recognize a dog or a cat using tensorflow

#import the libraries
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

#check the version of tensorflow
print("Version :",tf.__version__)

#Data Preprocessing
#----------------------------------------------------------------------------
#--apply some transformation on the images on the training set to avoid overfitting
#image augmentation -- prevent over-train on the training set
#1.shear_range 2.zoom_range and 3. horizontal_flip
train_datagen=ImageDataGenerator(
    rescale=1./255 ,
    #feature scaling,each an every single pixel value of 0-255 
    # devided by 255 to get in the form of 0/1
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True 
)
training_set=train_datagen.flow_from_directory(
    "path to training set",
    target_size=(64,64),
    batch_size=32,
    class_mode='binary')

#Preprocessing the test set
#same target size batch size and class mode
test_datagen=ImageDataGenerator(rescale=1./255)
test_set=test_datagen.flow_from_directory(
        "path to test set",
        target_size=(64,64),
        batch_size=32,
        class_mode='binary'
)

##############################################################################################
#Building the CNN 
#1.Convolution
cnn=tf.keras.models.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=32,
        #kernel=3,
        kernel_size=3,
        activation='relu',
        input_shape=[64,64,3]))

#2.adding the pooling layer
cnn.add(tf.keras.layers.MaxPool2D(
    pool_size=2,
    strides=2
))
#3.adding the second convolution layer
cnn.add(tf.keras.layers.Conv2D(filters=32,
                               kernel_size=3,
                               activation='relu'))
#again pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2)
        )

#========================================================================================
#Flattening
#Converting to one dimessional vector which will be input to Fully connected layer
cnn.add(tf.keras.layers.Flatten())


#========================================================================================
#Fully Connected Layer
cnn.add(tf.keras.layers.Dense(units=128,activation='relu'))

#========================================================================================
#Output Layer :  Binary class 0 or 1 : 1 neuron
#sigmoid gives 0 or 1 classification results
cnn.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))


#==========================================================
#TRAIN THE CNN NETWORK

#step 1:
#Compile the CNN
cnn.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#step 2:
#Training the CNN on Training set and evaluating it on the Test set
cnn.fit(x=training_set,validation_data=test_set,epochs=25)



#=========================================================
#making the single prediction
import numpy as np
from keras.preprocessing import image
test_image=image.load_img("path to target dataset to predict the class",target_size=(64,64))
#predict method expects an 2D array
test_image_updated=image.img_to_array(test_image)
test_image_updated=np.expand_dims(test_image_updated,axis=0)
result=cnn.predict(test_image_updated/255.0)
indices=training_set.class_indices
if result[0][0]>0.5:
    prediction='Dog'
else:
    prediction='Cat'
print(prediction)
print("\n Image :\n")
plt.imshow(test_image)
plt.show()
