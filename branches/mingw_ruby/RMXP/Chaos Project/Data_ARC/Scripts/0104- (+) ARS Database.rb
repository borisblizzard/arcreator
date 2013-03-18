module CP::ARS
  
  def self.get_recognition(id)
    texts = []
    case id
    when 1
      texts.push('An ordinary machine in the mysterious')
      texts.push('laboratory. Attacks intruders.')
    when 2
      texts.push('Lives in the cave east from Reeva.')
      texts.push('Can poison its enemies.')
    when 3
      texts.push('This is the final battle! We will not')
      texts.push('let Nemesis activate the Chaos Machine!')
    when 4
      texts.push('Dangerous animal that possesses vicious')
      texts.push('attacks. Not to be underestimated.')
    when 5
      texts.push("Sometimes they are so annoying that you")
      texts.push("can lose your voice while shouting,")
      texts.push("because you missed to kill them.")
    when 6
      texts.push('At home in Giada Castle. These creatures')
      texts.push('possess the knowledge of Storm-Shield.')
      texts.push('They use melee attack and various magics.')
    when 7
      texts.push('Big and stupid creatures who live in the')
      texts.push('cave east from Reeva. Can cast Freeze.')
    when 8
      texts.push('Can be found in the library and the')
      texts.push('upper floors in Giada Castle. Uses')
      texts.push('blinding attacks and casts Beast.')
    when 9
      texts.push('Uses Freeze against enemies. Frost Cloaks')
      texts.push('can be found everywhere where it is cold.')
    when 10
      texts.push('They use silence attacks to keep their')
      texts.push('opponents from using magic against them.')
    when 11
      texts.push('Ugly creature with a giant tongue that can')
      texts.push('be found in marshs, swamps, etc. They attack')
      texts.push('their opponents with Bubbles and their tongue.')
    when 12
      texts.push('They are common in areas with much water')
      texts.push('so they use Water-based spells and their teeth.')
      texts.push('They can also cause Stupidity.')
    when 13
      texts.push('Strong wolf monsters who use vicious')
      texts.push('attacks to bring the enemy down.')
    when 14
      texts.push('Poseidons have poisonous tridents to attack enemies.')
      texts.push('They are not too strong, though...')
    when 15
      texts.push('That\'s bad luck for them because we')
      texts.push('broke into Lorence Castle exactly during')
      texts.push('their shift. They can cast Shock.')
    when 16
      texts.push('Patrolling the halls of Lorence Castle.')
      texts.push('Stronger than Soldiers, but more stupid.')
      texts.push('Sometimes they cast Fireburn.')
    when 17
      texts.push('Very strong warriors with grand axes.')
      texts.push('They possess the ability to use Fireburn,')
      texts.push('but they rarely do.')
    when 18
      texts.push('Commanding soldier, rather intelligent')
      texts.push('than just strong. Captains use Fireburn.')
    when 19
      texts.push('The elite force of Lorence Castle.')
      texts.push('They can use Fireburn, Shock and Freeze,')
      texts.push('but their attack is also pretty strong.')
    when 20
      texts.push('Uses its sting to poison and stun enemies.')
      texts.push('Those lizards can be quite tough.')
    when 21
      texts.push('Harpies can be found in the mountains.')
      texts.push('They attack with various techniques')
      texts.push('and can cast Wind-Shield.')
    when 22
      texts.push('Haunting the area around Krato.')
      texts.push('This cold blade often uses ice attacks.')
    when 23
      texts.push('Those mercenaries seem to know a')
      texts.push('couple of nasty techniques and spells.')
    when 24
      texts.push('A furious being that attacks everything it sees.')
    when 25
      texts.push('Haunting the Ghost Ship. Uses its voice to')
      texts.push('to produce extremely high tunes and')
      texts.push('uses this ability to attack enemies.')
    when 27
      texts.push('A vicious machine guarding a treasure chest.')
    when 28
      texts.push('A strange being. I\'ve never seen anything like')
      texts.push('that before. It can use various sword techniques')
      texts.push('with its claws and can cast Master-Shield.')
    when 29
      texts.push('A treacherous enemy disguising himself as a')
      texts.push('treasure box. Uses various vampire techniques')
      texts.push('and can wound enemies.')
    when 30
      texts.push('It doesn\'t seem to be too dangerous for a')
      texts.push('dragon... Burns enemies with its Fire Breath')
      texts.push('and can wound them. But sometimes it can\'t')
      texts.push('attack out of exhaustion.')
    when 31
      texts.push('The source of the monsters dwelling in')
      texts.push('Adel Tower. Seems to be a tough one...')
    when 32
      texts.push('After transformation by the unknown scythe')
      texts.push('wielder even more dangerous. Can cast')
      texts.push('Frost-Shield and uses Sanctus often.')
    when 33
      texts.push('This must be the monster that broke out of')
      texts.push('the capsule in the first room...')
    when 34
      texts.push('Who is she?')
      texts.push('She seems to use Freeze and Breeze...')
    when 35
      texts.push('It stole the key to the cave to Lisk.')
      texts.push('Uses Poison and heals itself when weakened.')
    when 36
      texts.push('It can cast Delay. Nothing else is')
      texts.push('known about these ghost-like beings.')
    when 37
      texts.push('A spooky ghost that normally lives')
      texts.push('in a forest. Ghosts usually use')
      texts.push('Beast to attack their enemies.')
    when 38
      texts.push('Mysterious ghost that appeared at the')
      texts.push('gravelike stone in the Forest of Illusions.')
      texts.push('Uses Poison, Venom, Beast and Mute.')
    when 39
      texts.push('Sighted in the area around Krato.')
      texts.push('It\'s the legendary Leviathan.')
    when 40
      texts.push('This being is unusually familiar...')
      texts.push('It is incredibly powerful, I can tell.')
      texts.push('It might be even stronger than Nemesis...')
    when 41
      texts.push('A monster never seen before... Possesses')
      texts.push('all low level element spells and many more.')
      texts.push('It uses Poison and Venom as well.')
    when 42
      texts.push('Supposed not to exist. Also called')
      texts.push('"The Great Marsh Monster". It is able to')
      texts.push('cast Quake-Shield and some other spells.')
    when 43
      texts.push('Dangerous monster that lives in "dark light"...')
      texts.push('Uses light and Darkness-based')
      texts.push('spells as well as Confusion.')
    when 45
      texts.push('A being purified by the element of Fire.')
      texts.push('She knows the secret of the Flame-Shield and')
      texts.push('is willing to teach anybody who defeats her.')
    when 46
      texts.push('Seems like Terence took over Lorence Castle...')
      texts.push('But why? He uses Beast and Freeze.')
    when 47
      texts.push('Once camouflaged as Terence,')
      texts.push('now he is showing his true self.')
      texts.push('His specialities are ice and evil.')
    when 48
      texts.push('This... this is...')
    when 49
      texts.push('Faberell has transformed. Luckily we')
      texts.push('already dealt over 80% damage to him,')
      texts.push('because his power is now even')
      texts.push('greater and his attacks are stronger.')
    when 50
      texts.push('This sword seems to be the guardian of the')
      texts.push('Ghost Ship. It uses various sword techniques.')
    when 51
      texts.push('This is the true guardian of the Ghost Ship.')
    when 52
      texts.push('An unknown vampire who wants me to leave...')
    when 53
      texts.push('An undead being wandering through')
      texts.push('Katana Desert and attacking travellers.')
      texts.push('Skelletons are known to be tough enemies.')
    when 54
      texts.push('Bats with beautiful wings that seem')
      texts.push('to burn when they fly. Sometimes they')
      texts.push('cast Fireball on themselves and')
      texts.push('surprisingly it doesn\'t hurt them.')
    when 55
      texts.push('Poisonous and dangerous animals. They are')
      texts.push('common in very hot places. Also they can')
      texts.push('protect themselves against the cold.')
    when 56
      texts.push('An agile being living in cold regions.')
      texts.push('It can boost its power and speed.')
    when 57
      texts.push('A powerful ice demon who sometimes')
      texts.push('tends to eat an enemy alive.')
    when 58
      texts.push('Floating light orbs that use a lot of magic.')
      texts.push('They can cast Vitalia what makes them')
      texts.push('pretty dangerous if they attack in groups.')
    when 59
      texts.push('An ancient being dwelling inside of')
      texts.push('White Peak. Dragon typed monsters are')
      texts.push('known to be very strong and resistant.')
      texts.push('This one is no exception.')
    when 60
      texts.push('A spiritual being purified by the element')
      texts.push('of Ice that seems to guard the Ice Temple')
      texts.push('from intruders. Its magic never depletes.')
    when 61
      texts.push('A female vampire having known Nosferatu for a')
      texts.push('long time, it seems. She uses a lot of magic,')
      texts.push('but her physical attacks are not weak at all.')
    when 62
      texts.push('Not Death personally, but no less dangerous.')
      texts.push('Reaper can use attacks that defeat instantly.')
    when 63
      texts.push('A giant dragon-like lizard monster.')
      texts.push('It uses various attacks to kill enemies.')
    when 64
      texts.push('A majestic creature that loves heights.')
      texts.push('It attacks enemies with various aerial spells.')
    when 65
      texts.push('Yet another 300000 HP monster')
      texts.push('in the Tower of Memories.')
    when 66
      texts.push('A being that seems to have escaped from Hell...')
      texts.push('Pah! 3 minutes are enough for me to kill it!')
    when 67
      texts.push('A vicious flying beast. No problem at all.')
    when 68
      texts.push('The Angel of Death can defeat instantly. How cute.')
    when 69
      texts.push('As one of Nemesis\' men Faberell is')
      texts.push('very powerful and strong. He can defeat')
      texts.push('instantly, uses Nova, and Darkness-based')
      texts.push('spells. This won\'t be easy...')
    when 70
      texts.push('Rivy... Wasn\'t he the one')
      texts.push('on top of Adel Tower?')
    when 71
      texts.push('Anoxis left his pet to do his job and')
      texts.push('it doesn\'t seem to be in a good mood...')
    when 72
      texts.push('Let\'s see how strong you are, Lucius...')
    when 73
      texts.push('He doesn\'t stand a chance against a')
      texts.push('true Lexima Warrior. He seems to think')
      texts.push('that his little Disintegrate ability')
      texts.push('can cancel my power. What a fool.')
      texts.push('You can\'t make Lexima just disappear.')
    when 74
      texts.push('This is her transformed form? And then she\'s')
      texts.push('wondering why I chose Silvery over her...')
      texts.push('Same strategy like the last time in Lisk Forest.')
      texts.push('Well... Maybe a little bit modified strategy...')
    when 75
      texts.push('Luckily it seems to be too old to')
      texts.push('trigger the alarm. Since it\'s a machine,')
      texts.push('it uses electricity to attack.')
    when 76
      texts.push('An unusual enemy. It uses its')
      texts.push('electricity and speed to attack.')
    when 77
      texts.push('Something\'s not right with this enemy...')
    when 78
      texts.push('It... it transformed right before our eyes!')
      texts.push('Could it be that this virtual reality')
      texts.push('environment allows such a thing? This form')
      texts.push('doesn\'t seem to regenerate like the other...')
    when 79
      texts.push('You have no idea what the power of')
      texts.push('Lexima and Chaos is capable of...')
      texts.push('I\'ll let you taste it a bit.')
    when 80
      texts.push('What the hell is that thing?!')
    when 81
      texts.push('Wow, that dragon thing is rotting')
      texts.push('away while I am trying to kill it.')
      texts.push('Now, THAT\'s what I call weird.')
    when 82
      texts.push('My... my former self wants to kill me...?')
      texts.push('Am I really nothing more than a useless')
      texts.push('shell? Am I just garbage...? I feel so weak...')
    when 83
      texts.push('I\'m not going down without a fight,')
      texts.push('Leximus! If you want to see me dead,')
      texts.push('obviously you\'ll have to kill me!')
      texts.push('You can transform as much as you want.')
      texts.push('This is my dream, I make the rules here!')
    when 84
      texts.push('Holy shit, that sting is giant! I hate insects...')
      texts.push('We should just burn it down or freeze it up.')
    when 85
      texts.push('I don\'t know what I more surprised of.')
      texts.push('Either that these things exist or that')
      texts.push('they are about to kill us if we don\'t')
      texts.push('kill it first.')
    when 86
      texts.push('It seems to harden and getting more')
      texts.push('resistant on physical attacks.')
      texts.push('Maybe we should try pure magic attacks.')
    when 87
      texts.push('It looks like that thing that\'s coming')
      texts.push('out of its head has a life of its own...')
    when 88
      texts.push('Hm... It looks like the brain of this thing.')
      texts.push('At least it\'s causing us trouble. Maybe things')
      texts.push('will get easier if we take it out first.')
    when 89
      texts.push('That thing is just gross.')
      texts.push('It doesn\'t react on elemental magic.')
      texts.push('We should try physical attacks.')
    when 90
      texts.push('I didn\'t believe it to be possible, but this')
      texts.push('thing is even more gross than Handy Ooze.')
    when 91
      texts.push('They can get pretty nasty if they attack in greater')
      texts.push('numbers. Let\'s fry them with electrical attacks.')
    when 92
      texts.push('This is heavy artillery. It seems like a')
      texts.push('security system down here. Electrical attacks')
      texts.push('are likely to work as well as water attacks.')
      texts.push('It keeps casting status magic when the')
      texts.push('two of them cry in a specific manner.')
    when 93
      texts.push('I\'m not sure if it\'s a mutation or actually a')
      texts.push('normal living creature on Kadro, but it can get')
      texts.push('nasty if it\'s trying to kill you. Except for the')
      texts.push('expected water attacks it keeps using status magic')
      texts.push('when the two of them cry in a specific manner.')
    when 94
      texts.push('I sense a lot of Chaos in this being.')
      texts.push('We should pay attention when it summons')
      texts.push('companions and get rid of them as fast as')
      texts.push('possible. We should also be careful when')
      texts.push('it suddenly changes its color...')
    when 95
      texts.push('Weird guy. He seems to want the gift badly.')
      texts.push('I wonder how electrical attacks will affect his arm...')
    when 96
      texts.push('Now I\'m pissed. That guy needs to get his ass kicked.')
      texts.push('I really thought it was Ariana who tied me up...')
    when 97
      texts.push('That\'s it! I\'ll make sure that this')
      texts.push('is the LAST battle with this asshole!')
    when 98
      texts.push('Probably resistant or even immune to fire.')
      texts.push('Using water attacks could be of use.')
    when 99
      texts.push('Ironicly this plant monster is')
      texts.push('immune to fire and weak to water.')
    when 100
      texts.push('It doesn\'t take a genius to realize')
      texts.push('that water is the best strategy here.')
    when 101, 102
      texts.push('Beside the fact that it\'s ugly, it\'s')
      texts.push('annoying as hell. We should probably get rid')
      texts.push('of it so we can concentrate on Chaos Behemoth.')
    when 103
      texts.push('I thought he was a Lexima Warrior... Well...')
      texts.push('He is one. I can tell that he can...')
      texts.push('do something and... attack us with more power.')
      texts.push('I just don\'t understand why he\'s on Nemesis side')
      texts.push('even though he knows what Nemesis is planning.')
    when 104
      texts.push('It seems to be waterproof and it')
      texts.push('attacks with energy based weapons.')
      texts.push('Resorting to electrical attacks is the answer.')
    when 105
      texts.push('The guns are so heavy that they look like arms.')
    when 106
      texts.push('This machine looks almost alive.')
      texts.push('It\'s even immune to EMP attacks.')
    when 107
      texts.push('I\'ll kick your ass, Lucius!')
      texts.push('Even Frost Nova won\'t help you!')
    when 108
      texts.push('Doesn\'t seem to be native in this region.')
      texts.push('Tactics against normal lizards could work well here.')
    when 109
      texts.push('It\'s huge and heavy, but it doesn\'t')
      texts.push('look like it can take heat very well.')
    when 110
      texts.push('This tiger species is vicious and capable')
      texts.push('of magically summoning a heavy snowstorm.')
      texts.push('It would be already hard enough to take care of it')
      texts.push('even if it didn\'t have claws as hard as metal.')
    when 111
      texts.push('Physical attacks are useless while he\'s invisible.')
      texts.push('Magical attacks are a different story, though...')
    when 112
      texts.push('Spiders are very similar to insects so')
      texts.push('an insect killing strategy is appropriate.')
    when 113
      texts.push('Not a nice gift for a woman except an')
      texts.push('ex-girlfriend. Anti-plant strategies work well here.')
    when 114
      texts.push('It\'s a heavy, but not a slow amphibious monster.')
    when 115
      texts.push('Man, he\'s ugly. I will never understand people who')
      texts.push('want to be ugly. Let\'s "enlighten" him a bit!')
    when 116, 117
      texts.push('This thing is a real pest.')
      texts.push('We should get rid of it fast.')
    when 118
      texts.push('Seems to be some sort of a demon.')
      texts.push('It also seems to be using darkness based attacks.')
    when 119
      texts.push('A huge warrior made of stone.')
      texts.push('What makes stone crumble?')
    when 120
      texts.push('Being cautious is a good idea as this monster')
      texts.push('is able to defeat an enemy with one blow.')
    when 121
      texts.push('Once I thought robots were cool.')
      texts.push('Well, that was BEFORE I had to fight them.')
      texts.push('This one seems to be trying to disrupt our strategy.')
    when 122
      texts.push('Hey, this is easier than I thought!')
      texts.push('Two down, one more to go!')
    when 123
      texts.push('And another one. We\'ll take this')
      texts.push('one down as we did the one before.')
    when 124
      texts.push('It seems to be trying to disrupt our strategy.')
    when 125
      texts.push('I\'m surprised how much ammo this')
      texts.push('android has. It\'s not like bullets')
      texts.push('for railgun-like fire grow on trees.')
    when 126
      texts.push('It has guns and uses magic.')
      texts.push('We should be careful.')
    when 127
      texts.push('That\'s two heads for each of us. I think')
      texts.push('it might be a good idea to find out its')
      texts.push('weakness as ice doesn\'t seem to be to working')
      texts.push('even though it looks like a lizard.')
      texts.push('Wait... The sand... I got it!')
    when 128, 129
      texts.push('I can\'t believe we were helping you all the time...')
      texts.push('We won\'t let you activate the Chaos Machine!')
    when 130
      texts.push('Damn, Setzer! Why won\'t you trust me?!')
      texts.push('Alright, I need to focus. Setzer is')
      texts.push('resistant to earth and aerial attacks.')
      texts.push('I need to keep that in mind when planning my attacks.')
    when 131
      texts.push('I\'m sorry if I disappointed you sometime, Ariana...')
      texts.push('Ariana was always weak to darkness based attacks.')
      texts.push('I need to keep that in mind when planning my attacks.')
    when 132
      texts.push('Too bad you don\'t know the whole story, Sydon...')
      texts.push('You simply don\'t know the true nature of Chaos.')
      texts.push('What were you resistant to again?')
      texts.push('Aerial and electrical attacks, wasn\'t it?')
      texts.push('I need to keep that in mind when planning my attacks.')
    when 133
      texts.push('Your big guns won\'t help you, Coga!')
      texts.push('We\'ll tear you apart and sell you in parts!')
    when 134
      texts.push('For one moment I thought you were going')
      texts.push('turn into something real ugly, Earayl.')
      texts.push('We will stop your evil soul!')
    when 135
      texts.push('Damn... he\'s become resistant to everything except')
      texts.push('light based attacks. And he\'s uglier than ever.')
    when 136
      texts.push('Looks like a machine so electrocution')
      texts.push('is probably a good strategy.')
    when 137
      texts.push('It becomes more annoying the longer the battle')
      texts.push('goes on as it is able to use defensive spells.')
      texts.push('Machine\'s don\'t like rust.')
    when 138
      texts.push('It is a dangerous machine')
      texts.push('Machine is the keyword here.')
    when 139
      texts.push('Has an ironic name, but that doesn\'t')
      texts.push('prevent it from using magical attacks.')
    when 140
      texts.push('The sewers are no place for children.')
      texts.push('Monsters like this one prove that')
      texts.push('adults shouldn\'t be here as well.')
    when 141
      texts.push('It\'s big, ugly and lives in a dark place.')
    when 142
      texts.push('Sometimes it is hard to hit this jelly-like monster.')
    when 143
      texts.push('That\'s one huge and magically poisonous lizard.')
    when 144
      texts.push('It\'s name means "Frost Mane" and it\'s a demon horse.')
    when 145
      texts.push('Can be recognizeg by just looking at it.')
    when 146
      texts.push('The bigger they are, the nastier')
      texts.push('is the sandstorm they cause.')
    when 147
      texts.push('A desert is not a place for plants.')
      texts.push('Just like this one here they all dry out.')
      texts.push('And what kills dry plants fast?')
    when 148
      texts.push('The only thing this vicious fighter is not able')
      texts.push('to use is some sort of magical flame blade.')
      texts.push('But that doesn\'t make it any weaker...')
    when 149
      texts.push('It\'s skin is incredibly hard and it\'s very resistant.')
    when 150
      texts.push('This machine is so advanced that it')
      texts.push('is able to cast and reflect magic.')
    when 151
      texts.push('Deathlord is a master of darkness.')
    when 152
      texts.push('It never seems to attack directly,')
      texts.push('but it can cause quite some problems if')
      texts.push('it\'s serving as support in a group.')
    when 153
      texts.push('Facebook is resistant to all elemental attacks.')
      texts.push('It must be a very evil entity.')
    when 154
      texts.push('Incredibly strong and persistent.')
      texts.push('They are very dangerous when they are in groups.')
    when 155
      texts.push('Yet another machine, but not anything alike others.')
      texts.push('Beside the fact that it\'s huge and powerful,')
      texts.push('it can cause defeating damage with one shot.')
    when 156
      texts.push('I\'m not sure if that thing is cursed or that.')
      texts.push('we are to encounter such a monster.')
      texts.push('Light attacks should work well here.')
    when 157
      texts.push('I don\'t like the look of this monster at all.')
    when 158
      texts.push('It\'s huge! We should take it out as')
      texts.push('quickly as before it knocks us out.')
    when 159
      texts.push('That giant blade she holds in her hand is very')
      texts.push('powerful. I wonder what her weakpoint is.')
    when 160
      texts.push('This demon seems to be good')
      texts.push('with fire and direct attacks.')
    when 161
      texts.push('What creature is this?! It\'s like a nightmare!')
      texts.push('It can hide itself in shadows.')
    when 162
      texts.push('This once noble knight must have sold his soul')
      texts.push('to the devil. He\'s able to defeat an enemy with')
      texts.push('a single strike. We should be very careful.')
    when 163
      texts.push('What is this creature?! It can summon')
      texts.push('those tentacle like beings so quickly...')
    when 164, 165, 166, 167
      texts.push('We should get rid of them. They make this')
      texts.push('battle even harder than it already it.')
    end
    return texts
  end
  
end
