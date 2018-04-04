songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Charles Mingus', 'Goodbye Prok Pie Hat'),
    ('Aaron Copeland', 'Fanfare for the Common Man'),
    ('Bootsy Collins', 'Rag Poppin'),
    ('Nickelback', 'Photograph')
}

no_nickelback = [song for song in songs if song[0] != 'Nickelback']

print(no_nickelback)