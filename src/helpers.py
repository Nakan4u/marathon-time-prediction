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