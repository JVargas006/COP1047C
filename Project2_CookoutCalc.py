#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
hotdogs_perpack = 10
hotdogs_bunsperpack = 8

#program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given.
ppl_attending = int(input('Enter the number of people attending the cookout: '))
hotdogs_pp = int(input('Enter the number of hot dogs for each person: '))

#calculations
hotdog_total = ppl_attending * hotdogs_pp
hotdog_packs_needed = hotdog_total / hotdogs_perpack
hotdog_bun_packs_needed = hotdog_total / hotdogs_bunsperpack 
hotdogs_leftover = hotdog_total / hotdogs_perpack
hotdog_buns_leftover = hotdog_total / hotdogs_bunsperpack 

if hotdogs_leftover:
    hotdog_packs_needed += 1
    hotdogs_leftover = hotdogs_perpack - hotdogs_leftover
if hotdog_buns_leftover:
    hotdog_bun_packs_needed += 1
    hotdog_buns_leftover = hotdogs_bunsperpack - hotdog_buns_leftover

#The minimum number of packages of hot dogs required
print('Minimum packages of hot dogs needed: ', hotdog_packs_needed)
#The minimum number of packages of hot dog buns required
print('Minimum packages of hot dog buns needed: ', hotdog_bun_packs_needed)
#The number of hot dogs that will be left over
print('Hot dogs left over: ', hotdogs_leftover)
#The number of hot dog buns that will be left over
print('Hot dog buns left over: ', hotdog_buns_leftover)