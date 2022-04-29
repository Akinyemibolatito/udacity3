

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
df['Start Time'] = to_datatime(['Start Time'])
# extract hour from the Start Time column to create an hour column
df['month'] = pd.to_datetime(df['Start Time']).dt.month

# find the most common month 
popular_month = df['month'].mode()[0]
    
print('Most Frequent Start month:', popular_month)

    # TO DO: display the most common day of week
    
df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day
popular_month = df['day_of_week'].mode()[0]
    
print('Most Frequent Start day:', common_day_of_week)


    # TO DO: display the most common start hour
df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
popular_month = df['hour'].mode()[0]
    
print('Most Frequent Start hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station =pd.print(df.start station).mode()[0]
    print ('Most Popular Start station:', common_start_station)
    

    # TO DO: display most commonly used end station
    common_end_station =pd.print(df.end station).mode()[0]
    print ('Most Popular end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df[['start station', 'End Station']].mode()[0]
    print ('Most Popular start end station:', common_start_end_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #change the start time to hours and rename and change the end time to hours and rename then do a difference btw d 2 columns
     total_travel_time = df['trip duration'].sum()

    # TO DO: display mean travel time
     mean_travel_time = df['trip duration'].mean()
     print(mean_travel_time)

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
   
    df = pd.parse_dates=['Birth Year] #column to datetimes

#filter output first by column ID and then get min and max
 # Earliest year of birth
    Earliest = df.loc[ df['ID'] == 7, 'Birth Year'].min()
     print (earliest)

 #Most recent year of birth
     Most_recent = df.loc[ df['ID'] == 7, 'Birth Year'].max()
     Print (most_recent)
                         
 #most common year of birth
    df['Year_Of_Birth'] = pd.to_datetime(df['Birth Year']).dt.year
    popular_year = df['year_of_Birth'].mode()[0] 
     print (popular_year)                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    pri                                     while True:
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

    
    
    
    
    