import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city', 'washington']
    months = ['january', 'february','march', 'april', 'may', 'june', 'all']
    days = ['saturday', 'sunday','monday','tuesday', 'wednesday', 'thursday', 'friday','all']
    city = input('Enter City Name: ').lower()
    month = input('Enter Month: ').lower()
    day = input('Enter Day of Week: ').lower()
    while city in cities:
        break
    else:
        print('Invalid Input')
    while month in months:
        break
    else:
        print('Invalid Input')
    while day in days:
        break
    else:
        print('Invalid Input')
        
    # TO DO: get user input for month (all, january, february, ... , june)cls
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january','february','march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]                              

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The Most Common Month Is : {}' .format(most_common_month))                                 


    # TO DO: display the most common day of week
    print('The Most Common Day Of Week Is : {} '.format (df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The Most Common Start Hour Is : {} '.format(df['hour'].mode()[0]))                                   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station : {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station: {}'.format(df['End Station'].mode()[0]))                                  


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + " " + df['End Station']
    print('Most Frequent Combination Of Start Station And End Station Trip: {}'.format(df['Combination'].mode()[0]))                                  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
      
    print('Total Travel Time : {}'.format(df['Trip Duration'].sum()))                                 


    # TO DO: display mean travel time
    print('Mean Travel Time : {}'.format(df['Trip Duration'].mean()))
          


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('User Types Count:{}'.format(user_types))

    # TO DO: Display counts of gender
    
   # print('Gender Counts: {}'.format(gender))
    if 'Gender' in df.columns:
        gender = df.groupby(['Gender'])['Gender'].count()
        print('Gender Counts: {}'.format(gender))
    else:
        print('No Available Data')
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year of Birth: {}'.format(df['Birth Year'].min()))   
        print('Most Recent: {}'.format(df['Birth Year'].max()))
        print('Most Common: {}'.format(df['Birth Year'].mode()))
    else:
        print('No Available Data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    while True:
        raw = input('\nDo You Like To See Some Raw Data? yes Or no: \n')
        if raw == 'yes':
            print(df.head()) 
        else:
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
