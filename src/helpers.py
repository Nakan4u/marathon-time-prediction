import datetime

# Function to calculate the time as HH:MM:SS from the number of seconds
# Returns HH:MM:SS as a string
def time_in_HHMMSS(ss):
  hours, remainder = divmod(ss, 3600)
  minutes, seconds = divmod(remainder, 60)
  hours = int(hours)
  minutes = int(minutes)
  seconds = int(seconds)
  if seconds < 10:
    SS = '0' + str(seconds)
  else:
    SS = str(seconds)
  if minutes < 10:
    MM = '0' + str(minutes)
  else:
    MM = str(minutes)
  if hours < 10:
    HH = '0' + str(hours)
  else:
    HH = str(hours)
  res = HH + ':' + MM +':' + SS
  return res

# Function to calculate pace time from time HH:MM:SS

def get_pace_time(time_str):
  # Parse the time from the string
  hours, minutes, seconds = map(int, time_str.split(':'))
  total_seconds = hours * 3600 + minutes * 60 + seconds

  # Define the distance of the marathon
  distance_kilometers = 42.195

  # Calculate the pace
  pace_per_kilometer_seconds = total_seconds / distance_kilometers

  # Convert the pace to a time format
  pace_per_kilometer = str(datetime.timedelta(seconds=int(pace_per_kilometer_seconds)))

  return pace_per_kilometer