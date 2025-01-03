# cnn-chickendisease-example
repo contains a CNN pipeline example

dataset : https://www.kaggle.com/datasets/allandclive/chicken-disease-1


Workflows
Update config.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the app.py

In terms of model selection for image classification , we are using VGG16
https://keras.io/api/applications/vgg/#vgg16-function

In artifacts, we download the base model base_model.h5
Model has 2 layers : convo and dense 
we will making changes to the dense layer to make it suitable for our dataset
and merging the model and saving that as updated version 
we save the model in .h5 format

h5 format is a binary format that can be used to save and load models in Keras


Parameters :
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3] # as per VGG 16 model (input shape)
BATCH_SIZE: 16
INCLUDE_TOP: False
EPOCHS: 1
CLASSES: 2
WEIGHTS: imagenet
LEARNING_RATE: 0.01

AUGMENTATION : True, we are using data augmentation to increase the size of the dataset
IMAGE_SIZE : [224, 224, 3] as per VGG 16 model
BATCH_SIZE : 16, we are using batch size of 16
INCLUDE_TOP : False, we are not including the top layer of the VGG 16 model
EPOCHS : 1, we are using 1 epoch for training
CLASSES : 2, we are using 2 classes for classification
WEIGHTS : imagenet, we are using imagenet weights for the model, we want pretrained version


----what is base 64 when working with an image ? -------------

Base64 encoding, when used with images, is a way to represent image data as a text string. Instead of storing an image as a binary file (a sequence of 0s and 1s that computers understand directly), you convert it into a string of ASCII characters (letters, numbers, and symbols that humans can easily read and copy).

----------Why use Base64 for images?----------------------------------------

Text-based Handling: Base64 converts binary data (like image files) into text. This is useful because many systems and protocols are designed to work primarily with text. For example:

Embedding images directly in HTML or CSS without needing separate image files.

Storing images in databases or text files.

Transmitting images over text-based communication channels.

Data Integrity: Base64 encoding helps preserve the integrity of the image data when it's being transferred or stored in systems that might not handle binary data well. It prevents data corruption due to character encoding issues.

-------------------------------------------------------------------------------
Things to Keep in Mind:

Size Increase: Base64 encoding increases the file size by approximately 33% compared to the original binary image. This is because you're representing binary data with a more verbose text format.

Performance: Decoding Base64 on the client-side (e.g., in a web browser) can add a slight performance overhead. For very large images, it's usually more efficient to serve them as separate files.

------------------------------------------------------------------------------

Convert image to base 64 and vice versa : https://base64.guru/

Upload  image and convert to base 64 string and decode it back 

---------------------------------------------------------------------

Performing Dockerization


Inside github/worflows create main.yaml , inside which we put cicd commands


Push the docker image to ECR (alternate to docker hub)
Then launch EC2 instance
Then pull ECR image to EC2 instance
Launch Docker image in EC2




------------------------------------------------------------------------

CI/CD deployemnt (code in cicd.yaml)
Dev A develops a project in dev env (say local machine)
Then code gets commited to Github (code management using git client)
--------------------this is dev env majorly-------------------------------
After implementing this project, it needs to be deployed
say you deploy this on AWS manually created EC2 instance and then endpoint is generated
with this endpoint any user can access the application

now say after 4 months, your model has to be added with more features in application 
Once the new features are coded, again you have to deploy the newer version to AWS

Now, when you are deploying for 2nd time
You have to first stop the older version of application running on EC2 instance
Then upload the new code to EC2 instance

Say it took 3 hours (downtime) , for the source code to be updated to newer 
version and the user was unable to access the application for 3 hours
(typically called server error)

This is where CICD comes in picture
(In simple terms CICD is, when my older application is up and running for users but in the backend the newly made changes are also getting updated)
endpoint is automatically updated here in cicd.

We create the cicd pipeline, push it to github   
github triggers the pipeline and code is updated

How does github trigger ? with cicd automation tool .
Like github actions, jenkins, circle ci , etc .. 

github actions is a cicd automation tool, which is free and open source
for jenkins and circle ci you have to setup servers manually.

---------------------------------------------------------------------

AWS

-create IAM user - search for IAM (indentity access management)
-- create user - give username (say rebitproj)
-Next - Attach policies directly
Policy: (search and select)
AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess
-- Next --- Create User -- Click on the user
-- go to security credentials -- create access key -- 
-- select CLI -- confirm,next 
-- Create user and store the access key and secret key generated
-- Done (you can also download the csv if needed)