from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
 

model = Sequential()
    
model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape= (64, 64, 3)))
    
#model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))
    
#model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))

#model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
   
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))
 
model.add(Flatten())
    
model.add(Dense(units = 128, activation='relu'))
model.add(Dropout(0.5))
    
model.add(Dense(units = 5, activation='sigmoid'))
     
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('Training',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('Validation',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')

model.fit_generator(training_set,
                         steps_per_epoch = 128,
                         epochs = 30,
                         validation_data = test_set,
                         validation_steps = 8)
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('Prediction/e.jpeg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

result  = model.predict(test_image)
tc = training_set.class_indices
res = np.argmax(result)
tc = dict([[v,k] for k,v in tc.items()])
tc[res]