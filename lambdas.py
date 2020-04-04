scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier',
              'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']
sorted_list = sorted(scientists, key=lambda name: name.split()[-1])
print(sorted_list)

last_name = lambda name: name.split()[-1]
print(last_name)

print(last_name("Nikola Tesla"))