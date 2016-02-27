import indicoio

# single example
print(indicoio.sentiment('I love writing code!'))

# batch example
print(indicoio.sentiment([
    'I love writing code!',
    'Alexander and the Terrible, Horrible, No Good, Very Bad Day'
]))