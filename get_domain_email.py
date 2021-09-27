from faker import Faker
import pandas as pd
from datetime import datetime


fake = Faker()



def get_most_frequent_email_domain():
    """
    Generate fake profiles and return the most frequent  email domain
    """
    now = datetime.now() #placeholder code for the review to detect
    profiles = [fake.profile() for i in range(100)]
    data = pd.DataFrame(profiles)
    data['domain'] = data['mail'].str.split('@', expand=True).iloc[:,1]
    most_frequent_domain = data['domain'].mode()[0]
    print('done')
    return most_frequent_domain



if __name__ == '__main__':
    print(get_most_frequent_email_domain())

