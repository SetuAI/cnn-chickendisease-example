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

Parameters Explanation :

AUGMENTATION: True
This enables data augmentation, a powerful technique where your training images are automatically modified (rotated, flipped, zoomed) during training. Think of it like teaching your model to recognize chicken diseases from different angles and distances, even if your original dataset doesn't have all these variations. Setting this to True helps your model become more robust and generalize better.

IMAGE_SIZE: [224, 224, 3]
This defines the dimensions of images your model will process: 224 pixels wide, 224 pixels high, and 3 color channels (Red, Green, Blue). This specific size isn't arbitrary - it's chosen to match VGG16's requirements, the pre-trained model you're using. Every image fed into your model will be resized to these dimensions, ensuring consistency in processing.

BATCH_SIZE: 16
During training, your model processes images in groups of 16. Think of it like a teacher grading papers - instead of grading one at a time or all at once, they grade in manageable stacks. This batch size is a good balance between training speed and memory usage for most modern GPUs.

INCLUDE_TOP: False
This tells the VGG16 model to exclude its original classification layers. By setting this to False, you're keeping VGG16's powerful feature extraction capabilities but removing its original classification system, allowing you to add your own layers specifically for identifying chicken diseases.

EPOCHS: 1
This defines how many times your model will process the entire dataset during training. While 1 epoch might seem low (and in practice, you'd typically use more), it's often used for testing the training pipeline before running longer training sessions.

CLASSES: 2
This indicates your model needs to distinguish between two categories - healthy chickens and those with Coccidiosis. This parameter determines the size of your model's final classification layer.

WEIGHTS: imagenet
This tells VGG16 to initialize using weights pre-trained on ImageNet, a massive dataset of various images. It's like giving your model a head start with general image recognition skills before it specializes in chicken disease detection.

LEARNING_RATE: 0.01
This controls how much your model adjusts its understanding based on each batch of training data. A value of 0.01 is relatively standard - not so high that training becomes unstable, but not so low that learning becomes too slow.
These parameters work together synergistically. For example, the BATCH_SIZE and LEARNING_RATE interact to influence how smoothly your model learns, while AUGMENTATION helps make the most of your training data given the number of EPOCHS.

----------------------------------------------------------------------------------------
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

-- Now the IAM user is created
---------------------------------------------------------------------
--- Now creating the ECR Repository

-- Search for ECR (Elastic Container Registry)
(make sure you have selected the region)

-- create repo
-- give the namespace/repo (rebitproj)
-- keep the other details as it is and create 
-- after that, copy paste the uri and save it

-------------------------------------------------------------------------------

-- Creating EC2 instance (Ubuntu)

-- In the console, search for EC2 instance
-- click on Launch Instance
-- enter the server name (ml-rebit)
-- select ubuntu
-- select instance type  -- t2.large (8gb)
-- in key pair login , name it -- (mlrebitproject) -- create key pair
(if you want to access this instance with any 3rd party tool, you have to create a key pair)

-- scrolling down check on : Allow HTTPS traffic and HTTP traffic

-- configure storage 1 X 30 GB

-- After this , click on Launch Instance

-- Once done, click on View all instances -- and refresh it
-- You will see the status running
-- Click on Instance ID
-- Click on Connect and Connect

-- you will see a terminal opening up and that is your prod server

------------------------------------------------------------------------------

