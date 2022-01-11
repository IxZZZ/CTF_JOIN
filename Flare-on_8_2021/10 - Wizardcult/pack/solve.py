names = ['Eldritch Blast', 'Mass Heal', 'Fireball', 'Dominate Monster', 'Detect Magic', 'Stone Shape', 'Clairvoyance', 'Aid', 'Detect Thoughts', 'Shapechange', 'Fire Shield', 'Pass without Trace', 'Antipathy/Sympathy', 'Sleet Storm', 'Dominate Person', 'Tree Stride', 'Passwall', 'Shatter', 'Giant Insect', 'Revivify', 'Circle of Death', 'Divination', 'Comprehend Languages', 'Faerie Fire', 'True Polymorph', 'Searing Smite', 'Dimension Door', 'Shield', 'Enlarge/Reduce', 'Illusory Script', 'Resistance', 'Earthquake', 'Contagion', 'Bless', 'Raise Dead', 'Guidance', 'Expeditious Retreat', 'Grease', 'Message', 'Elemental Weapon', 'Fear', 'Clone', 'Wrathful Smite', 'Astral Projection', 'Flaming Sphere', 'Disguise Self', 'Maze', 'Slow', 'Polymorph', 'Weird', 'Finger of Death', 'Protection from Energy', 'Nondetection', 'Animal Friendship', 'Spike Growth', 'Goodberry', 'Calm Emotions', 'Antilife Shell', 'Cone of Cold', 'Identify', 'Power Word Stun', 'Control Water', 'Thorn Whip', 'Power Word Kill', 'Blink', 'Locate Creature', 'Command', 'Contingency', 'Prismatic Wall', 'Blade Ward', 'Scrying', 'Dominate Beast', 'Sacred Flame', 'Guards and Wards', 'Arcane Eye', 'Mirage Arcane', 'Magic Mouth', 'Glyph of Warding', 'Friends', 'Sending', 'Stinking Cloud', 'Compulsion', 'Dancing Lights', 'Darkness', 'Invisibility', 'Spare the Dying', 'Wall of Fire', 'Flame Blade', 'Feather Fall', 'Magic Weapon', 'Purify Food and Drink', 'Spirit Guardians', 'Witch Bolt', 'Animate Objects', 'Gaseous Form', 'Lightning Bolt', 'Move Earth', 'Disintegrate', 'Mass Healing Word', 'Meld into Stone', 'Hellish Rebuke', 'Aura of Life', 'Augury', 'Conjure Elemental', 'Spider Climb', 'Hold Person', 'Project Image', 'Heroism', 'Crown of Madness', 'Mirror Image', 'Ray of Sickness', 'Bane', 'Wish', 'Contact Other Plane', 'Etherealness', 'Blinding Smite', 'Shield of Faith', 'Vampiric Touch', 'Shillelagh', 'Programmed Illusion', 'Remove Curse', 'Major Image', 'Insect Plague', 'Color Spray', 'Prismatic Spray', 'Charm Person', 'Arms of Hadar', 'Dream', 'Dissonant Whispers', 'Teleport',
         'Dispel Magic', 'Forbiddance', 'Misty Step', 'Cloud of Daggers', 'Gentle Repose', 'Phantasmal Force', 'Circle of Power', 'Stoneskin', 'Sunbeam', 'Fire Storm', 'Gust of Wind', 'Find Steed', 'Druidcraft', 'Confusion', 'Bestow Curse', 'Flesh to Stone', 'Arcane Gate', 'Ray of Frost', 'Greater Invisibility', 'Regenerate', 'Burning Hands', 'Wall of Ice', 'True Strike', 'Silence', 'Banishing Smite', 'Commune with Nature', 'Time Stop', 'Conjure Celestial', 'Magic Jar', 'True Seeing', 'Transport via Plants', 'Teleportation Circle', 'Spiritual Weapon', 'Prayer of Healing', 'Awaken', 'Conjure Woodland Beings', 'Cloudkill', 'Imprisonment', 'Branding Smite', 'Ray of Enfeeblement', 'See Invisibility', 'Word of Recall', 'Silent Image', 'Eyebite', 'Cordon of Arrows', 'Globe of Invulnerability', 'Wind Walk', 'Continual Flame', 'Power Word Heal', 'Web', 'Protection from Poison', 'Grasping Vine', 'Telekinesis', 'Heat Metal', 'Harm', 'Antimagic Field', 'Jump', 'Greater Restoration', 'Chain Lightning', 'Knock', 'Blade Barrier', 'Scorching Ray', 'Zone of Truth', 'Moonbeam', 'Light', 'Magic Circle', 'Hail of Thorns', 'Heal', 'Blur', 'Water Breathing', 'Cure Wounds', 'Enhance Ability', 'Suggestion', 'Water Walk', 'Conjure Barrage', 'Arcane Lock', 'Reverse Gravity', 'Planar Ally', 'Mass Suggestion', 'False Life', 'Longstrider', 'Detect Evil and Good', 'Guiding Bolt', 'Glibness', 'Speak with Dead', 'Call Lightning', 'Death Ward', 'Create Undead', 'Beacon of Hope', 'Alter Self', 'Acid Splash', 'Phantom Steed', 'Planar Binding', 'Prestidigitation', 'Animate Dead', 'Mind Blank', 'Sleep', 'Divine Favor', 'Telepathy', 'Vicious Mockery', 'Blight', 'Barkskin', 'Counterspell', 'Conjure Fey', 'Find Traps', 'Animal Shapes', 'Speak with Plants', 'True Resurrection', 'Warding Bond', 'Flame Strike', 'Healing Word', 'Wall of Thorns', 'Wind Wall', 'Seeming', 'Chill Touch', 'Lesser Restoration', 'Guardian of Faith', 'Meteor Swarm', 'Shocking Grasp', 'Commune', 'Destructive Wave', 'Staggering Smite', 'Create or Destroy Water', 'Sunburst', 'Forcecage', 'Tongues']


def extract_3_bytes(s):
    name = s.split('I cast ')[1].split(' on')[0]
    num_1 = names.index(name)
    nums = s.split('for ')[1].split(' damage!')[0].split('d')
    return [num_1, nums[0], nums[1]]


f = open('brute_out.txt', 'r')


str = f.read()
arr_str = str.split('\n')


print(len(arr_str))

map_brute = {}
character = 0

for i in range(0, len(arr_str), 8):
    for j in range(8):
        s = arr_str[i+j]
        nums_extract = extract_3_bytes(s)
        map_brute[f'{(3*j)%24}-{nums_extract[0]}'] = character
        map_brute[f'{(3*j+1)%24}-{nums_extract[1]}'] = character
        map_brute[f'{(3*j+2)%24}-{nums_extract[2]}'] = character
    character += 1

print(len(map_brute))

file = open('encrypted_payload.txt', 'r')

file_final = open('pic.png', 'wb')
str_encrypted = file.read().split('\n')

print(len(str_encrypted))
for i in range(0, len(str_encrypted), 8):
    for j in range(8):
        if i + j >= len(str_encrypted):
            break
        s = str_encrypted[i+j]
        try:
            nums = extract_3_bytes(s)
            file_final.write(bytes([map_brute[f'{3*j}-{nums[0]}']]))
            file_final.write(bytes([map_brute[f'{3*j+1}-{nums[1]}']]))
            file_final.write(
                bytes([map_brute[f'{3*j+2}-{nums[2]}']]))
        except :
            print('error')
            print(f'---{s}---')
            continue
        
# wh0_n33ds_sw0rds_wh3n_you_h4ve_m4ge_h4nd@flare-on.com