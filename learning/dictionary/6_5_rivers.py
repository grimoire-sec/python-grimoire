rivers = {'nile' : 'egypt',
          'elbe' : 'germany',
          'amazon' : 'brasil'}

for k, v in rivers.items():
    print(f'The {k.title()} runs through {v.title()}.')

print("\nRivers included in this dictonary are:")
for k in rivers.keys():
    print(k.title())

print("\nThis dictonary contains the following countries:")
for v in rivers.values():
    print(v.title())