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
    file_name = input("Would you like to see data for Chicago, New York City, or Washington? \n  ")# Or type 'Q' for Quit! \n ")
    file_name = file_name.strip().lower()

    while file_name not in CITY_DATA.keys():
         file_name = input("\n invalid input .. plz try again \n ")
         file_name = file_name.strip().lower()

 
    # TO DO: get user input for month (all, january, february, ... , june)
    month_filter =['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month_input  = input("Which month? January, February, March, April, May, or June?\)! Or type all for all months \n ")
    month_input = month_input.strip().lower()

    while month_input not in month_filter:
         month_input = input("\n invalid input .. plz try again \n ")
         month_input = month_input.strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_week = ['saturday', 'sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day_input = input("Which Day of Week? 1 for Saturday, \n 2 for Sunday,\n 3 for Monday,\n 4 for Tuesday,\n 5 for Wednesday,\n 6 for Thursday or \n 7 for Friday?\n and 8 for All \n")
    while not day_input.isdigit() or not (int(day_input) >= 1 and int(day_input) <=8) :
         day_input = input("Invalid input.. try again please\n")
  

    #day_week[int(day_input)-1]
    '''
      print(f'\n You select  to view data for : \n 1. city: { file_name.capitalize() }, \n 2. month: { month_input.capitalize()}  \n and 3. day: { day_week[int(day_input)-1]}.')
     print('-'*40)
    # return selected data 
     #return file_name.lower() , month_input.lower(),day_week[int(day_input-1)]  
   '''
    print('-'*40)
    #print (file_name.lower())print (month_input.lower())   print (day_week[int(day_input)-1]  )
    return file_name.lower() , month_input.lower(),day_week[int(day_input)-1]  

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

    print("\n let’s start loading data based on ur selections  \n...")
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime("%B")
    #print (month.capitalize() )
    #print (df['month'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name # day_name()
    #print (f"Day,  { day.capitalize() }")
    # start filer pd to get selected data only ( month and day)
    if month!= 'all':
       df = df[df['month'] == month.capitalize()] #.strftime("%B")
    if day != 'all':
       df = df[df['day_of_week'] == day.capitalize()] # dt.day_name()
 
    return df 




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]  
    print(f'Most Popular Month: {popular_month} \n')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]  
    print(f'Most Popular Day of the week: {popular_day} \n')

    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]  
    print(f'Most Popular Start Hour:  {popular_hour} \n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station: {common_start_station} \n ')

    # TO DO: display most commonly used end station
    common_end_station = df['Start Station'].mode()[0]
    print(f'The most commonly used to end station: {common_end_station} \n')


    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f'\n The most frequent combination is {combo}.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    Sum_du = df['Trip Duration'].sum()
    print(f'The total trip duration is : { Sum_du }.')

    # TO DO: display mean travel time
    avg_du = round(df['Trip Duration'].mean())
    print(f'The mean travel time is : { avg_du }.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f' counts of user types:\n {user_type}')

    # TO DO: Display counts of gender
    try:
       gender = df['Gender'].value_counts()
       print(f' \n counts of gender:\n {gender}')
    except:
       print("\n  No 'Gender' column .")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       earliest = int(df['Birth Year'].min())
       recent = int(df['Birth Year'].max())
       common_year = int(df['Birth Year'].mode()[0])
       print(f' \n The earliest year of birth: {earliest} \n The most recent year of birth: {recent}\n The most common year of birth: {common_year}')
    except:
       print("\n  No 'Birth Year' column .")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#from user
def display_data(df):
    """Displays 5 rows  
    Args:
        Df (df): The data frame you wish to work with.

    Returns:
        None.
    """
    resp_option = ['yes', 'no']
    input_r = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while input_r not in resp_option:
        print("\n Do u wish to view the raw data? YES/NO") 
        input_r = input().lower() 
        if input_r == "yes":
            print(df.head())
        elif input_r not in resp_option:
            print("\n Invalid Input .. plz check .") 
             

    # continue view  data
    while input_r == 'yes':
        print("Do you want to view more raw data?")
        counter += 5
        input_r = input().lower()
        # next to display 5 rows of data
        if input_r == "yes":
             print(df[counter:counter+5])
        elif input_r!= "yes":
             break

    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df) 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break
   
'''
change1 in bikeshare
change2 in bikeshare
'''
if __name__ == "__main__":
	main()
