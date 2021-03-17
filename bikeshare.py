import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Def check_input(input_str,input_type):

    """

    test the validity of consumer enter.

    Input_str: is the input of the person

    input_type: is the form of input: A = city, B = month, C = day

    """

    at the same time as real:

        input_read=input(input_str)

        strive:

            if input_read in ['chicago','new york city','washington'] and input_type == A:

                damage

            elif input_read in ['january, february, march, april, june or all'] and input_type == B:

                spoil

            elif input_read in ['sunday, ... Friday, saturday or all'] and input_type == C:

                spoil

            else:

                if input_type == A:

                    print("Sorry, your enter must be: chicago ny town or washington")

                if input_type == B:

                    print("Sorry, your input have to be: january, february, march, april, june or all")

                if input_type == C:

                    print("Sorry, your input should be: sunday, ... Friday, saturday or all")

        besides ValueError:

            print("Sorry, your enter is incorrect")

    go back input_read



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
    
city = check_input("Would you like to see the statistics for chicago, new york city or washington?",A)

    # TO DO: get user input for month (all, january, february, ... , june)
    
month = check_input("Which Month (all, january, ... june)?", B)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
day = check_input("Which day? (all, monday, tuesday, ... sunday)", C)

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
# load information document right into a dataframe

    df = pd.Read_csv(CITY_DATA[city])

    # convert the start Time column to datetime

    df['Start Time'] = pd.To_datetime(df['Start Time'])

    # extract month, day of week, hour from start Time to create new columns

    df['month'] = df['Start Time'].Dt.Month

    df['day_of_week'] = df['Start Time'].Dt.Weekday_name

    df['hour'] = df['Start Time'].Dt.Hour

    # filter out by month if applicable

    if month != 'all':

     # use the index of the months listing to get the corresponding int

       months = ['january', 'february', 'march', 'april', 'may', 'june']

       month = months.Index(month) + 1

        # clear out through month to create the new dataframe

        df = df[df['month'] == month]

    # clear out by using day of week if applicable

    if day != 'all':

        # filter out by way of day of week to create the brand new dataframe

        df = df[df['day_of_week'] == day.Identify()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    Common_month = df['month'].mode()[0]

    print('Most common Month:', common_month)

    # TO DO: display the most common day of week
    
    common_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most common Day Of Week:', common_day_of_week)

    # display the most common start hour

    common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    
    print('common Start Station:', common_start_station)

    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    
    print('common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip

    group_field=df.groupby(['Start Station','End Station'])
    
    frequent_combination_station = group_field.size().sort_values(ascending=False).head(1)

    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('counts of user types:')

    print(df['counts of user types'].value_counts())

    if city != 'washington':
    
    # TO DO: Display counts of gender
    
    print('Gender:')
    
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    
print('common year of birth:')

        most_common_year = df['common year of birth'].mode()[0]

        print('Most Common Year:',most_common_year)

        most_recent_year = df['common year of birth'].max()

        print('Most Recent Year:',most_recent_year)

        earliest_year = df['common year of birth'].min()

        print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
