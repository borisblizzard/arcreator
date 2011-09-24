#==============================================================================
# module CP
#==============================================================================

module CP
  
  module Cache
    
    # System
    GameID = 150
    Releases = {}
    Releases['Final Demo'] = 0
    Releases['Demo'] = 1
    Releases['Beta 1'] = 2
    Releases['RC'] = 3
    Releases['Full Game'] = 4
    
    # custom death
    DGhost = 24
    DFallROTL = 25
    DSplat = 26
    DSlicer = 27
    DMachine = 28
    DNone = 29
    DExplode = 30
    DBoss = 31
    DSBoss = 32
    DFinal = 33
    DeathAnimations = [DGhost, DFallROTL, DSplat, DSlicer, DMachine, DNone,
        DExplode, DBoss, DSBoss]
    DummyElements = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] +
                  DeathAnimations
    DummyStates = [28, 32, 33, 35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                   50, 51, 52, 53, 54, 55]
    
    # game basics
    DirsOffsets = {2 => [0, 1], 4 => [-1, 0], 6 => [1, 0], 8 => [0, -1]}
    MapLayers = [2, 1, 0]
    PictureRange = 1..100
    StateProbabilitiesBoss = [0, 80, 60, 40, 20, 10, 0]
    StateProbabilities = [0, 100, 90, 80, 50, 25, 0]
    ElementRates = [0, 200, 150, 100, 50, 0, -100]
    Levels = 2..101
    SaveGames = 0...8
    MessageWindow = [16, 160, 304]

    # game mods
    PositiveStates = (13..16).to_a + (18..27).to_a + (30..34).to_a +
        (37..38).to_a + (40..44).to_a
    NoCritical = [160, 286, 287, 289, 290, 315, 295, 296, 358, 359, 360, 397,
                  404]
    FullHit = [157, 158, 159, 160]
    NoShade = ['', 'faberell X', 'jason float', 'vamp_morph', 'vamp_bat',
               'setzer down', 'sieg down', 'vamp_norm', '190-Down02',
               '191-Down03', 'jason down', 'gangDown', 'endout down',
               'ariana down', 'sydon down', 'jason lex float', 'duke_load',
               'celestia', 'white_tiger', '157-Animal07', 'Salomon', 'HARRR',
               'Sphinx', 'Cerbeclus', 'Slinger', 'Hobo', 'Gnarly', 'Dusa M.',
               'Lux', 'Steve', 'Boss Toss', 'Pest', 'Mutador', 'Falc', 'Ruin',
               'Turega', 'Laplace', 'Pythonia', 'Jungle Jack', 'Ragna']
               
    PanoramaBattleMaps = [210, 335, 528, 575, 769, 819, 820, 822, 824]
    MirrorMaps = [582, 586, 801, 802]
    DirectFadeMaps = [473, 474, 213, 218, 748, 770]
    SilenceMaps = [81, 84, 85, 309]
    HeatstrikeMaps = [713, 714, 715, 716, 719, 720, 721]
    Teleports = [[28, 137, 78],
                 [28, 113, 72],
                 [28, 15, 49],
                 [28, 148, 51],
                 [28, 96, 157],
                 [28, 149, 158],
                 [28, 277, 62],
                 [28, 193, 200],
                 [28, 29, 216],
                 [300, 187, 148],
                 [300, 125, 137],
                 [300, 175, 51],
                 [300, 73, 37],
                 [300, 75, 122],
                 [300, 70, 162],
                 [300, 15, 164],
                 [712, 10, 10],
                 [775, 10, 10]]
    EncList1 = (250..261).to_a
    EncList2 = (262..268).to_a
    NoExtraEXP = [72, 215, 216, 217, 241, 269, 270, 271, 272]
    
    # extended systems
    Lucius = [4, 13, 16]
    Endout = [2, 12]
    MainParty = [2, 4, 6, 9, 10, 12, 13]
    Sydon = 13
    TwoHanded = [14, 15, 18, 20, 24, 38, 49, 53, 72, 75, 80, 82, 89, 90, 91]
    NoLog = [26, 31, 44, 48, 52, 65, 66, 67, 68, 70, 72, 78, 79, 82, 96, 97,
        102, 107, 117, 121, 122, 123, 128, 129, 130, 131, 132, 165, 166, 167]
    UndeadIDs = [8, 22, 25, 36, 37, 38, 50, 51, 53, 62, 65, 68, 81, 101, 102,
                 115, 120, 134, 135, 144, 151, 154, 159, 160, 161, 162, 163,
                 164, 165, 166, 167]
    AbsorbHP = [116, 120, 144, 194, 354]
    AbsorbSP = [81, 117, 195, 321, 410]
    StealSP = [81, 410]
    Immune = [3, 26, 27, 31, 32, 39, 42, 43, 45, 47, 48, 49, 50, 51, 61, 69,
              70, 71, 73, 79, 97, 103, 127, 128, 129, 163]
    CantAnalyze = [70, 71, 82]
    AnalyzeIDs = [110, 217]
    RecognizeIDs = [109, 217]
    Bullets = [122, 123, 128, 137, 149]
    Quest = (33..41).to_a + (43..44).to_a + (53..72).to_a + [80, 82] +
            (107..109).to_a + (111..121).to_a + (124..127).to_a +
            (130..132).to_a + (139..146).to_a + [148, 151] + (161..163).to_a
    Trade = (83..106).to_a
    Skins = ['Original', 'Heavy Gold', 'Hell Breath', 'Liquid Water',
             'Violent Violet', 'Ice Cool', 'Fatal Venom', 'Perfect Chaos',
             'Blizzard Master', 'Mutated Original']
    Fonts = ['Arial', 'Future', 'Impressed', 'Brush Script', 'Papyrus',
             'Geometrix', 'Times New Roman']
    FontOffsets = {'Arial' => 7, 'Future' => 9, 'Impressed' => 8,
                   'Brush Script' => 7, 'Papyrus' => 9, 'Geometrix' => 8,
                   'Times New Roman' => 8}
    SuperStates = ['Transformed', 'Regenerating', 'Devastating', 'Leximized',
                   'Chaosized', 'Mutated', 'Vanished', 'Defeated']
    BadStates = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 39]
    ColorHP = Color.new(0, 192, 255)
    ColorHP2 = Color.new(0, 96, 128)
    ColorMP = Color.new(64, 255, 64)
    ColorMP2 = Color.new(32, 128, 32)
    ColorCritical = Color.new(255, 0, 0)
    ColorCritical2 = Color.new(128, 0, 0)
    ColorMissed = Color.new(255, 255, 0)
    ColorMissed2 = Color.new(128, 128, 0)
    ColorDamage = Color.new(255, 255, 255)
    ColorDamage2 = Color.new(128, 128, 128)
    
    # puzzles and minigames
    SewerDirs = {2 => [85, 89, 88],
                 4 => [86, 90, 87],
                 6 => [87, 91, 86],
                 8 => [88, 92, 85]}
    CriosXCoos = [30, 32, 44, 46]
    CriosTeleport = {
        [64, 22] => [[15, 12], [15, 12], [59, 28]],
        [15, 12] => [[64, 22], [64, 22], [59, 42]],
        [59, 28] => [[59, 42], [59, 42], [64, 22]],
        [59, 42] => [[59, 28], [59, 28], [15, 12]],
        [17, 19] => [[12, 22], [12, 22], [38, 26]],
        [12, 22] => [[17, 19], [17, 19], [61, 43]],
        [61, 43] => [[38, 26], [38, 26], [12, 22]],
        [38, 26] => [[61, 43], [61, 43], [17, 19]],
        [29, 48] => [[34, 46], [34, 46], [22, 41]],
        [34, 46] => [[29, 48], [29, 48], [38, 42]],
        [38, 42] => [[22, 41], [22, 41], [34, 46]],
        [22, 41] => [[38, 42], [38, 42], [29, 48]],
        [24, 9] => [[41, 14], [17, 28]],
        [47, 48] => [[49, 13], [48, 25]],
        [48, 25] => [[38, 15], [47, 48]],
        [17, 28] => [[35, 14], [24, 9]],
        [65, 16] => [54, 41],
        [50, 18] => [58, 22],
        [63, 42] => [20, 34],
        [38, 21] => [30, 19],
        [32, 19] => [45, 40],
        [11, 16] => [13, 42],
        [15, 43] => [23, 47],
        [42, 46] => [53, 47],
        [18, 22] => [35, 24],
        [19, 8] => [22, 18],
        [41, 24] => [46, 19],
        [57, 8] => [44, 19],
        [52, 9] => [56, 34],
        [24, 17] => [27, 13],
        [26, 18] => [28, 25],
        [25, 26] => [15, 41],
        [13, 30] => [17, 42],
        [61, 41] => [31, 40],
        [63, 30] => [59, 19],
        [54, 18] => [61, 12],
        [51, 26] => [52, 17]
    }
    Hyperion1HEvents = [(5..9).to_a, (11..15).to_a]
    Hyperion1VEvents = [(2..6).to_a, (8..12).to_a]
    Hyperion2HEvents = (7..13).to_a
    Hyperion2VEvents = (4..10).to_a
    Hyperion2Colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'CYAN', 'BLUE',
                       'VIOLET']
    PandemoniumCursor = {}
    PandemoniumCursor[[6, 7, 2]] = [2, 2, 2, 2]
    PandemoniumCursor[[6, 7, 6]] = [3, 3, 6, 6]
    PandemoniumCursor[[6, 11, 6]] = [3, 3, 6, 6]
    PandemoniumCursor[[6, 11, 8]] = [8, 8, 8, 8]
    PandemoniumCursor[[10, 5, 2]] = [2, 2, 2, 2]
    PandemoniumCursor[[10, 5, 4]] = [4, 4, 1, 1]
    PandemoniumCursor[[10, 5, 6]] = [6, 6, 3, 3]
    PandemoniumCursor[[10, 9, 2]] = [2, 2, 2, 2]
    PandemoniumCursor[[10, 9, 4]] = [4, 4, 7, 7]
    PandemoniumCursor[[10, 9, 6]] = [6, 6, 9, 9]
    PandemoniumCursor[[10, 9, 8]] = [8, 8, 8, 8]
    PandemoniumCursor[[10, 13, 4]] = [4, 4, 7, 7]
    PandemoniumCursor[[10, 13, 6]] = [6, 6, 9, 9]
    PandemoniumCursor[[10, 13, 8]] = [8, 8, 8, 8]
    PandemoniumCursor[[14, 7, 2]] = [2, 2, 2, 2]
    PandemoniumCursor[[14, 7, 4]] = [1, 1, 4, 4]
    PandemoniumCursor[[14, 11, 4]] = [1, 1, 4, 4]
    PandemoniumCursor[[14, 11, 8]] = [8, 8, 8, 8]
    PandemoniumSpheres = {}
    PandemoniumSpheres[[6, 7]] = [[6, 7], [4, 5], [6, 3], [8, 5]]
    PandemoniumSpheres[[6, 11]] = [[6, 11], [4, 9], [6, 7], [8, 9]]
    PandemoniumSpheres[[10, 5]] = [[8, 5], [6, 3], [8, 1], [12, 1], [14, 3], [12, 5]]
    PandemoniumSpheres[[10, 9]] = [[8, 9], [6, 7], [8, 5], [12, 5], [14, 7], [12, 9]]
    PandemoniumSpheres[[10, 13]] = [[8, 13], [6, 11], [8, 9], [12, 9], [14, 11], [12, 13]]
    PandemoniumSpheres[[14, 7]] = [[14, 7], [12, 5], [14, 3], [16, 5]]
    PandemoniumSpheres[[14, 11]] = [[14, 11], [12, 9], [14, 7], [16, 9]]
    
    Cards = []
    Cards.push(Card.new('♦', [2], '2', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [3], '3', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [4], '4', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [5], '5', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [6], '6', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [7], '7', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [8], '8', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [9], '9', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [10], '10', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [10], 'J', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [10], 'Q', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [10], 'K', Color.new(255, 0, 0)))
    Cards.push(Card.new('♦', [11, 1], 'A', Color.new(255, 0, 0)))
    
    Cards.push(Card.new('♠', [2], '2', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [3], '3', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [4], '4', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [5], '5', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [6], '6', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [7], '7', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [8], '8', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [9], '9', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [10], '10', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [10], 'J', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [10], 'Q', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [10], 'K', Color.new(0, 0, 0)))
    Cards.push(Card.new('♠', [11, 1], 'A', Color.new(0, 0, 0)))
    
    Cards.push(Card.new('♥', [2], '2', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [3], '3', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [4], '4', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [5], '5', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [6], '6', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [7], '7', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [8], '8', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [9], '9', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [10], '10', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [10], 'J', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [10], 'Q', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [10], 'K', Color.new(255, 0, 0)))
    Cards.push(Card.new('♥', [11, 1], 'A', Color.new(255, 0, 0)))
    
    Cards.push(Card.new('♣', [2], '2', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [3], '3', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [4], '4', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [5], '5', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [6], '6', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [7], '7', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [8], '8', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [9], '9', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [10], '10', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [10], 'J', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [10], 'Q', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [10], 'K', Color.new(0, 0, 0)))
    Cards.push(Card.new('♣', [11, 1], 'A', Color.new(0, 0, 0)))

    Roulette = []
    Roulette.push(Roulette_Number.new(0, Color.new(0, 192, 0)))
    Roulette.push(Roulette_Number.new(32, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(15, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(19, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(4, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(21, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(2, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(25, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(17, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(34, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(6, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(27, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(13, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(36, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(11, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(30, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(8, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(23, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(10, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(5, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(24, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(16, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(33, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(1, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(20, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(14, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(31, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(9, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(22, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(18, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(29, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(7, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(28, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(12, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(35, Color.new(0, 0, 0)))
    Roulette.push(Roulette_Number.new(3, Color.new(255, 0, 0)))
    Roulette.push(Roulette_Number.new(26, Color.new(0, 0, 0)))
    
    Slots = [[8, 8, 8, 250], [7, 7, 7, 80], [6, 6, 6, 40], [8, 8, -1, 25],
             [5, 5, 5, 20], [4, 4, 4, 10], [3, 3, 3, 10], [2, 2, 2, 10],
             [1, 1, 1, 10], [8, -1, -1, 5], [0, 0, 0, 5], [0, 0, -1, 3],
             [0, -1, -1, 2]]
    
    # other
    WallTag = 3
    NoEventTag = 2
    ResetMaps = [28, 300]
    ArrowInnerColor = Color.new(0, 0, 0, 128)
    ArrowOuterColor = Color.new(255, 255, 255, 192)

    def self.load
      @images = {}
      @images['arrow'] = self.create_arrow
      Graphics.update
      @images['update_bar'] = self.create_update_bar
      Graphics.update
      @images['ice_bar'] = self.create_ice_bar
      Graphics.update
      @images['ice_indicator'] = self.create_ice_indicator
      Graphics.update
      @images['roulette'] = self.create_roulette
      Graphics.update
      self.create_cards
      Graphics.update
      self.load_damage
      Graphics.update
    end
    
    def self.load_damage
      @damages = {}
      colors = [ColorHP, ColorMP, ColorCritical, ColorMissed, ColorDamage]
      colors.each {|color|
          @damages[color] = RPG::Cache.picture(sprintf('Damage/%d-%d-%d',
              color.red.to_i, color.green.to_i, color.blue.to_i))}
    end
    
    DAMAGES = {
        '0' => Rect.new(0, 0, 19, 32),
        '1' => Rect.new(19, 0, 14, 32),
        '2' => Rect.new(33, 0, 18, 32),
        '3' => Rect.new(51, 0, 18, 32),
        '4' => Rect.new(69, 0, 18, 32),
        '5' => Rect.new(87, 0, 19, 32),
        '6' => Rect.new(107, 0, 17, 32),
        '7' => Rect.new(124, 0, 19, 32),
        '8' => Rect.new(143, 0, 19, 32),
        '9' => Rect.new(162, 0, 17, 32),
        'A' => Rect.new(180, 0, 24, 32),
        'B' => Rect.new(204, 0, 22, 32),
        'C' => Rect.new(226, 0, 21, 32),
        'D' => Rect.new(247, 0, 24, 32),
        'E' => Rect.new(0, 32, 23, 32),
        'F' => Rect.new(23, 32, 23, 32),
        'G' => Rect.new(46, 32, 22, 32),
        'H' => Rect.new(69, 32, 28, 32),
        'I' => Rect.new(97, 32, 17, 32),
        'J' => Rect.new(115, 32, 21, 32),
        'K' => Rect.new(136, 32, 26, 32),
        'L' => Rect.new(162, 32, 20, 32),
        'M' => Rect.new(182, 32, 31, 32),
        'N' => Rect.new(213, 32, 28, 32),
        'O' => Rect.new(242, 32, 22, 32),
        'P' => Rect.new(264, 32, 22, 32),
        'Q' => Rect.new(0, 64, 22, 32),
        'R' => Rect.new(22, 64, 23, 32),
        'S' => Rect.new(45, 64, 20, 32),
        'T' => Rect.new(65, 64, 22, 32),
        'U' => Rect.new(87, 64, 24, 32),
        'V' => Rect.new(111, 64, 24, 32),
        'W' => Rect.new(135, 64, 32, 32),
        'X' => Rect.new(167, 64, 27, 32),
        'Y' => Rect.new(194, 64, 22, 32),
        'Z' => Rect.new(217, 64, 23, 32),
        'a' => Rect.new(240, 64, 18, 32),
        'b' => Rect.new(258, 64, 16, 32),
        'c' => Rect.new(0, 96, 15, 32),
        'd' => Rect.new(15, 96, 20, 32),
        'e' => Rect.new(35, 96, 15, 32),
        'f' => Rect.new(51, 96, 22, 32),
        'g' => Rect.new(73, 96, 18, 32),
        'h' => Rect.new(92, 96, 18, 32),
        'i' => Rect.new(110, 96, 11, 32),
        'j' => Rect.new(121, 96, 17, 32),
        'k' => Rect.new(138, 96, 18, 32),
        'l' => Rect.new(156, 96, 11, 32),
        'm' => Rect.new(167, 96, 26, 32),
        'n' => Rect.new(193, 96, 18, 32),
        'o' => Rect.new(211, 96, 17, 32),
        'p' => Rect.new(228, 96, 21, 32),
        'q' => Rect.new(250, 96, 17, 32),
        'r' => Rect.new(267, 96, 15, 32),
        's' => Rect.new(0, 128, 15, 32),
        't' => Rect.new(15, 128, 13, 32),
        'u' => Rect.new(29, 128, 18, 32),
        'v' => Rect.new(47, 128, 17, 32),
        'w' => Rect.new(64, 128, 24, 32),
        'x' => Rect.new(88, 128, 19, 32),
        'y' => Rect.new(107, 128, 18, 32),
        'z' => Rect.new(125, 128, 17, 32),
        '-' => Rect.new(142, 128, 12, 32),
        '+' => Rect.new(155, 128, 17, 32),
        '%' => Rect.new(172, 128, 25, 32),
        ',' => Rect.new(198, 128, 9, 32),
        '!' => Rect.new(207, 128, 11, 32)}
    
    def self.damages
      return @damages
    end
    
    def self.create_cards
      CP::Cache::Cards.each {|card|
          @images[card] = RPG::Cache.picture('cardback').clone
          @images[card].font.color = card.color
          @images[card].font.name = 'Geometrix'
          @images[card].font.size = 24
          @images[card].draw_text(4, 0, 40, 24, card.character)
          @images[card].draw_text(36, 88, 40, 24, card.character, 2)
          @images[card].font.name = 'Arial'
          @images[card].font.size = 64
          @images[card].draw_text(0, 24, 80, 64, card.sign, 1)}
    end
    
    def self.create_roulette
      b = Bitmap.new(640, 480)
      b.fill_rect(0, 0, 640, 480, Color.new(0, 64, 0))
      b.fill_rect(19, 259, 602, 122, Color.new(255, 255, 255))
      b.fill_rect(59, 381, 482, 80, Color.new(255, 255, 255))
      b.font.name = 'Geometrix'
      numbers = CP::Cache::Roulette.clone
      zero = numbers.shift
      b.font.size = 40
      b.fill_rect(21, 261, 38, 118, zero.color)
      b.draw_text(20, 299, 40, 36, zero.value.to_s, 1)
      numbers.each {|number|
          x = ((number.value - 1) / 3) * 40 + 60
          y = 340 - ((number.value - 1) % 3) * 40
          b.fill_rect(x + 1, y + 1, 38, 38, number.color)
          b.draw_text(x, y - 1, 40, 40, number.value.to_s, 1)}
      b.font.color = Color.new(255, 224, 0)
      b.font.size = 32
      (0...3).each {|i|
          b.fill_rect(541, 261 + i * 40, 78, 38, Color.new(0, 64, 0))
          b.draw_text(541, 260 + i * 40, 80, 40, '2:1', 1)}
      (0...3).each {|i|
          b.fill_rect(61 + i * 160, 381, 158, 38, Color.new(0, 64, 0))}
      b.draw_text(60, 379, 160, 40, '1st 12', 1)
      b.draw_text(220, 379, 160, 40, '2nd 12', 1)
      b.draw_text(380, 379, 160, 40, '3rd 12', 1)
      (0...6).each {|i| b.fill_rect(61 + i * 80, 421, 78, 38, Color.new(0, 64, 0))}
      colors = [Color.new(255, 0, 0), Color.new(0, 0, 0)]
      colors.each_index {|i|
          b.fill_rect(231 + i * 80, 425, 58, 30, Color.new(255, 255, 255))
          b.fill_rect(233 + i * 80, 427, 54, 26, colors[i])}
      b.draw_text(140, 419, 80, 40, 'EVEN', 1)
      b.draw_text(380, 419, 80, 40, 'ODD', 1)
      b.draw_text(60, 419, 80, 40, '-', 1)
      b.draw_text(60, 419, 40, 40, '1', 1)
      b.draw_text(100, 419, 40, 40, '18', 1)
      b.draw_text(460, 419, 80, 40, '-', 1)
      b.draw_text(460, 419, 40, 40, '19', 1)
      b.draw_text(500, 419, 40, 40, '36', 1)
      return b
    end
    
    def self.create_arrow
      b = Bitmap.new(16, 9)
      b.fill_rect(1, 0, 14, 1, ArrowOuterColor)
      b.set_pixel(0, 1, ArrowOuterColor)
      b.fill_rect(1, 1, 7, 1, ArrowInnerColor)
      b.fill_rect(8, 1, 7, 1, ArrowInnerColor)
      b.set_pixel(15, 1, ArrowOuterColor)
      b.set_pixel(1, 2, ArrowOuterColor)
      b.fill_rect(2, 2, 6, 1, ArrowInnerColor)
      b.fill_rect(8, 2, 6, 1, ArrowInnerColor)
      b.set_pixel(14, 2, ArrowOuterColor)
      b.set_pixel(2, 3, ArrowOuterColor)
      b.fill_rect(3, 3, 5, 1, ArrowInnerColor)
      b.fill_rect(8, 3, 5, 1, ArrowInnerColor)
      b.set_pixel(13, 3, ArrowOuterColor)
      b.set_pixel(3, 4, ArrowOuterColor)
      b.fill_rect(4, 4, 4, 1, ArrowInnerColor)
      b.fill_rect(8, 4, 4, 1, ArrowInnerColor)
      b.set_pixel(12, 4, ArrowOuterColor)
      b.set_pixel(4, 5, ArrowOuterColor)
      b.fill_rect(5, 5, 3, 1, ArrowInnerColor)
      b.fill_rect(8, 5, 3, 1, ArrowInnerColor)
      b.set_pixel(11, 5, ArrowOuterColor)
      b.set_pixel(5, 6, ArrowOuterColor)
      b.fill_rect(6, 6, 2, 1, ArrowInnerColor)
      b.fill_rect(8, 6, 2, 1, ArrowInnerColor)
      b.set_pixel(10, 6, ArrowOuterColor)
      b.set_pixel(6, 7, ArrowOuterColor)
      b.set_pixel(7, 7, ArrowInnerColor)
      b.set_pixel(8, 7, ArrowInnerColor)
      b.set_pixel(9, 7, ArrowOuterColor)
      b.fill_rect(7, 8, 2, 1, ArrowOuterColor)
      return b
    end
    
    def self.create_update_bar
      bi = Bitmap.new(480, 24)
      c1 = Color.new(0, 80, 0, 255)
      c2 = Color.new(0, 240, 0, 255)
      r1, g1, b1, r2, g2, b2 = c1.red, c1.green, c1.blue, c2.red, c2.green, c2.blue
      (1...20).each {|i|
          b, g = 255, 0
          if i == 1
            b, r = i * 64, i * 32
          elsif i >= 2 && i < 6
            r, g = 128 + (i-2) * 25, (i-2) * 51
          elsif i >= 6 && i < 8
            r = g = 255
          elsif i >= 8 && i < 11
            r, g = 128 + (11-i) * 32, (11-i) * 64
          else
            b, r = (21-i) * 25, (21-i) * 12
          end
          bi.fill_rect(0, i, 480, 1, Color.new(r, g, b))}
      (0...48).each {|i|
          bi.fill_rect(10*i, 0, 1, 20, Color.new(0, 0, 0, 160))
          bi.fill_rect(10*i+9, 0, 1, 20, Color.new(0, 0, 0, 160))}
      return bi
    end
    
    def self.create_ice_bar
      b = Bitmap.new(242, 10)
      b.fill_rect(0, 0, 242, 10, Color.new(0, 0, 0))
      (0...240).each {|i|
          if i < 10 || i >= 230
            r, g = 255, 0
          elsif i >= 10 && i < 80 || i >= 160 && i < 230
            r, g = 255, (i > 120 ? 255 * (230-i)/70 : 255 * (i-10)/70)
          elsif i >= 80 && i < 160
            r, g = 255 * (i-120).abs/40, 255
          end
          b.fill_rect(i+1, 1, 1, 8, Color.new(r, g, 0, 160))}
      return b
    end
    
    def self.create_ice_indicator
      b = Bitmap.new(6, 16)
      b.fill_rect(2, 0, 2, 1, Color.new(255, 255, 255, 31))
      b.set_pixel(1, 1, Color.new(255, 255, 255, 56))
      b.fill_rect(2, 1, 2, 1, Color.new(255, 255, 255, 94))
      b.set_pixel(4, 1, Color.new(255, 255, 255, 56))
      b.set_pixel(0, 2, Color.new(255, 255, 255, 37))
      b.set_pixel(1, 2, Color.new(255, 255, 255, 112))
      b.fill_rect(2, 2, 2, 12, Color.new(255, 255, 255))
      b.set_pixel(4, 2, Color.new(255, 255, 255, 112))
      b.set_pixel(5, 2, Color.new(255, 255, 255, 37))
      b.set_pixel(0, 3, Color.new(255, 255, 255, 50))
      b.set_pixel(1, 3, Color.new(255, 255, 255, 150))
      b.set_pixel(4, 3, Color.new(255, 255, 255, 150))
      b.set_pixel(5, 3, Color.new(255, 255, 255, 50))
      b.fill_rect(0, 4, 1, 8, Color.new(255, 255, 255, 56))
      b.fill_rect(1, 4, 1, 8, Color.new(255, 255, 255, 169))
      b.fill_rect(4, 4, 1, 8, Color.new(255, 255, 255, 169))
      b.fill_rect(5, 4, 1, 8, Color.new(255, 255, 255, 56))
      b.set_pixel(0, 12, Color.new(255, 255, 255, 50))
      b.set_pixel(1, 12, Color.new(255, 255, 255, 150))
      b.set_pixel(4, 12, Color.new(255, 255, 255, 150))
      b.set_pixel(5, 12, Color.new(255, 255, 255, 50))
      b.set_pixel(0, 13, Color.new(255, 255, 255, 37))
      b.set_pixel(1, 13, Color.new(255, 255, 255, 112))
      b.set_pixel(4, 13, Color.new(255, 255, 255, 112))
      b.set_pixel(5, 13, Color.new(255, 255, 255, 37))
      b.set_pixel(1, 14, Color.new(255, 255, 255, 56))
      b.fill_rect(2, 14, 2, 1, Color.new(255, 255, 255, 94))
      b.set_pixel(4, 14, Color.new(255, 255, 255, 56))
      b.fill_rect(2, 15, 2, 1, Color.new(255, 255, 255, 31))
      return b
    end
    
    def self.image(id)
      return @images[id]
    end
    
    def self.compressed_map
      @compressed_map = {} if @compressed_map == nil
      return @compressed_map
    end
    
    def self.world_map_data
      @world_map_data = {} if @world_map_data == nil
      return @world_map_data
    end
    
    def self.clear
      RPG::Cache.clear
      @compressed_map, @world_map_data = {}, {}
    end
    
  end
  
end
