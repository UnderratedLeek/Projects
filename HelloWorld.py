print ("Hello World")

# Dictionary of vehicle information
vehicle = {
1: {'Make': 'Toyota', 'Model': 'Highlander', 'Year': '2021', 'Cylinders': 6, 'Drive': 'AWD'},
2: {'Make': 'Mercedes-Benz', 'Model': 'AMG GT63 SE Performance', 'Year': '2024', 'Cylinders': 8, 'Drive': 'AWD'},
3: {'Make': 'Jaguar', 'Model': 'F-Type 75', 'Year': '2024', 'Cylinders': 8, 'Drive': "AWD"},
4: {'Make': 'Mercedes-Benz', 'Model': 'A45 AMG', 'Year': '2024', 'Cylinders': 4, 'Drive': 'AWD'},
5: {'Make': 'Lamborghini', 'Model': 'Huracan EVO', 'Year': '2021', 'Cylinders': 12, 'Drive': 'RWD'},
}

# Sort the list of vehicles by the 'Make'
sorted_vehicle = dict(sorted(vehicle.items(),
key=lambda item: item[1]['Make']))

# Print the sorted Dictionary
for key, value in sorted_vehicle.items():
    print(f"vehicle {key}:")
    for attribute, detail in value.items():
        print(f"  {attribute}: {detail}")
        print()
