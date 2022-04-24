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
    print('Hi there! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago','new york city','washington')
    while True:
        city = input('Cities available are Chicago, New york city and Washington. Please choose one of them:\n').lower()
        if city not in cities:
            print('hmmm!! your input is invalid, let\'s try this again:')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('We have got data from January to June. please one of them or choose all to see all data from January to June: \n').lower()
        if month not in ('january','february','march','april','may','june','all'):
            print('oop! your request doesn\'t match what we have,please choose an option from the suggested months')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ('Please choose any day of the week you would like to analyze. or choose all to see data for every day:\n').lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('That doesn\'t count as a valid input, please try again')
        else:
            break


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june'.lower()]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
  
    common_month=df['month'].mode()[0]
    print('The most common month is:',common_month)

    # TO DO: display the most common day of week
    df['day'] =df['Start Time'].dt.day
    common_day=df['day'].mode()[0]
    print('the most common week is: ',common_day)
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most commonly used start station is:',common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most commonly used end station is:',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start_end_station'] = df['Start Station']+"-" +df['End Station']
    common_start_and_end_station = df['Start_end_station'].mode()[0]
    print('the most commonly used start and end stations is:',common_start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total travel time is:',total_trip_duration)

    # TO DO: display mean travel time
    Mean_trip_duration = df['Trip Duration'].mean()
    print('The mean travel time is:',Mean_trip_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
  

    # TO DO: Display counts of gender
    Gender = df['Gender'].value_counts()
    print(Gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    common_year_of_birth= df['Birth Year'].value_counts()
    print('most common year of birth is: {} '.format(common_year_of_birth.max()))
    
    earliest = df['Birth Year'].min()
    print('the earliest year of birth is: {}'.format(earliest))
    
    recent = df['Birth Year'].max()
    print('the most recent year of birth is: {}'.format(recent))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """Allow the user to view subsets of raw data if the user is interested"""
    start = 0
    stop = 5
    interest = input("Interested in seeing some raw data? please Enter yes or no. Don't worry it's just five rows.\n").lower()
    while interest.lower() == 'yes':
        data_view = df.iloc[start:stop, :]
        print(data_view)
        interest = input("Are you still interested in seeing some more raw data? please enter yes or no. please note that any other option also means a no .\n").lower()
        start += 5
        stop += 5
                    
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'washington':
            pass
        else:
            user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
