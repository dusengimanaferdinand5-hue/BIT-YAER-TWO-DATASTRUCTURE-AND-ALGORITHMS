#import libraries
import array

# List that contains the Gym Membership Records
gym_visits = [12, 15, 8, 20, 10, 14, 17, 9, 16]

#Generate Report using f-strings
report = (
    f" The report of Gym Membership Visits is: {gym_visits} \n"
    f" The Total Visits is: {sum(gym_visits)} \n"
    f" The Average Visits is: {round(sum(gym_visits) / len(gym_visits), 2)} \n"
    f" The Minimum Visits is: {min(gym_visits)} \n"
    f" The Maximum Visits is: {max(gym_visits)} \n"
)
print(report)

# Threshold condition (Booleans)
average_visits = sum(gym_visits) / len(gym_visits)
threshold = 12
if average_visits > threshold and max(gym_visits) > 15:
    print(f" The average visits exceed the threshold: {round(average_visits, 2)} → Above Standard")
else:
    print(f" The average visits exceed the threshold: {round(average_visits, 2)} → Below Standard")

#Maintain list: Add, Remove, Sort
new_visit = 13
gym_visits.append(new_visit)
print(f"\n You already appended {new_visit} in this array {gym_visits} on your Gym Membership log.")

# Remove a visit entry if it's less than or equal to 9
for visit in gym_visits:
    if visit <= 9:
        gym_visits.remove(visit)
        print(f" Removed {visit} from your Gym Membership log.")
        break

print(f"\nGym Membership log before sort: {gym_visits}")
gym_visits.sort()
print(f" Sorted Gym Membership log: {gym_visits}")

# Arrays - Fixed-size Subset
gym_array = array.array('i', gym_visits[:6])  # First 6 visits
array_sum = sum(gym_array)
list_sum = sum(gym_visits)

print(f"\nArray Sum (first 6 Gym Visits): {array_sum}")
print(f"List Sum (all Gym Visits): {list_sum}")

if array_sum == list_sum:
    print("All Gym Visits are equal")
else:
    print("All Gym Visits are different")

#Dictionaries: Manage Gym Membership Records
gym_members = [
    {'id': 1, 'name': 'Alice', 'value': 14},
    {'id': 2, 'name': 'Bob', 'value': 12},
    {'id': 3, 'name': 'Charlie', 'value': 18},
    {'id': 4, 'name': 'Diana', 'value': 10}
]

# Update one record
for record in gym_members:
    print(f"{record} ")
    if record['id'] == 3:
        record['value'] = 20  
        print(f"\n Updated Record: {record} \n")

# Delete one record
gym_members = [record for record in gym_members if record['id'] != 2]

# Compute total visits from remaining records
total_value = sum(record['value'] for record in gym_members)
print("Total Gym Visit Value from all Members:", total_value)