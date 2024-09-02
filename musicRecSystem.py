import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity

data = music_df
#Function to calculate the weighted popularity scores based on their release
def calculate_weighted_popularity(release_date):
    #Convert the release date to datetime object
    release_date = datetime.strptime(release_date, '%Y-%m-%d')

    #Calculate the time span between release date and today's date
    time_span = datetime.now() - release_date

    #Calculate the weighted popularity score based on time span (the more recent, the more weighted)
    weight = 1/(time_span.days + 1)
    return weight
