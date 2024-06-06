'''
Exercise 1:
    1. A company’s financial reports stored in an Excel file: Structured
    2. Photographs uploaded to a social media platform: unstructured
    3. A collection of news articles on a website. : unstructured
    4. Inventory data in a relational database. : Structured
    5. Recorded interviews from a market research study. : Unstructured
Exercise 2:
     There are many different quantitative data points that can be derived
    from a these data sources, it depends on what the objective of using
    the data is. For example, the number of
    positive references and
    negative references, length of content, constructed observer ratings.
    Overall I think the question is flawed because the source of data doesn't determine it's being structured or unstructured as much as the way it is stored and used because with enough operationalization, limitation, or measurement, any data source can be not just qualitative but stored with structure.
Exercise 3:
    Transaction records can be used to track stock and make informed
    decisions about future inventory. Customer feedback comments can be
    organized into groups based on topic/content to make changes based on
    volume of comments about particular issues rather than each individual
    comment prompting direct action, measuring reactions to social media
    posts such as number of likes or replies can inform future posts efficacy especially in relation to transaction records immediately after the post, and employee work schedules can be manipulated to predictively account for busy periods based on patterns found in the transaction records.

Exercise4:
'''
import numpy as np
import random
from faker import Faker
import pandas as pd

# fake = Faker()
#
# f_data = [(fake.name(), fake.address(), fake.email(),
#            np.random.randint(20, 60), np.random.randint(15000,1000000)) for _
#           in range(100)]
# fake_df = pd.DataFrame(f_data, columns=['Name', 'Address', 'Email',
#                                              'Age', 'Income'])
#
# print(fake_df.head())

#Exercise 5: I don't know how apply the ImageDataGenerator functions and save
# the outcomes. I pasted the code from the module, but I do not know how to
# apply it yet, when the class recording is posted, I will try again
from zipfile import ZipFile
with ZipFile("C:\Users\geffg\OneDrive\devIns "
             "2024\di_tta114_geffen_moser\Week7\Day4\ExercisesXP\day4Exercise"
             "\dog-images.zip", 'r') as zObject:
zObject.extractall(path="C:\Users\geffg\OneDrive\devIns 2024\di_tta114_geffen_moser\Week7\Day4\ExercisesXP\day4Exercise\unzipped dog")
# #The following is pasted from the module
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# data_generator = ImageDataGenerator(rotation_range=20)
#
# # to rotate the image buy exactly 30 degrees
# from scipy.ndimage import rotate
#
# def rotate_image_30_degrees(image):
# # Rotate image by 30 degrees
# return rotate(image, 30, reshape=False, mode='nearest')
# #  Create ImageDataGenerator with custom preprocessing function
# data_generator = ImageDataGenerator(preprocessing_function=rotate_image_30_degrees)

'''
Exercise 6:  Your goal is to generate a dataset that reflects different traffic conditions at various times of the day.
Outline the steps you would take to create this simulation. Consider factors like vehicle types, road types, traffic signals, and peak/off-peak hours.
Describe how you would collect data from this simulation, specifying the types of data (e.g., vehicle count, average speed) you would gather at different time intervals.
Discuss the potential uses of this simulated dataset in traffic management and urban planning.

First I would make classes and subsequently objects of vehicles, roads, 
and traffic signals. I would try to find an API that would give real world 
data on traffic flow patters or alternatively generate fake data measuring 
the number of cars at any given red light per stop and simulate possible 
changes that would result in the least amount of congestion, such as 
expanding lanes and alternate routes.
'''