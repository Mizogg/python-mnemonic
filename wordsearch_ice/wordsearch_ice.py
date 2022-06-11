import random, codecs, binascii, bip32utils
import hashlib
import base58
from mnemonic import Mnemonic
from rich.console import Console
from lxml import html
import secp256k1 as ice
import requests
console = Console()
console.clear()


def xBal(address):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + address
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal1(uaddr):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + uaddr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol1 = str(treetxid[0].text_content())
    return xVol1

mylist = []

with open('words.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

mynumbers = []

with open('numbers.txt', newline='', encoding='utf-8') as f2:
    for line in f2:
        mynumbers.append(line.strip())

wordlist = ["abandon","ability","able","about","above","absent","absorb","abstract","absurd","abuse","access","accident","account","accuse","achieve","acid","acoustic","acquire","across","act","action","actor","actress","actual","adapt","add","addict","address","adjust","admit","adult","advance","advice","aerobic","affair","afford","afraid","again","age","agent","agree","ahead","aim","air","airport","aisle","alarm","album","alcohol","alert","alien","all","alley","allow","almost","alone","alpha","already","also","alter","always","amateur","amazing","among","amount","amused","analyst","anchor","ancient","anger","angle","angry","animal","ankle","announce","annual","another","answer","antenna","antique","anxiety","any","apart","apology","appear","apple","approve","april","arch","arctic","area","arena","argue","arm","armed","armor","army","around","arrange","arrest","arrive","arrow","art","artefact","artist","artwork","ask","aspect","assault","asset","assist","assume","asthma","athlete","atom","attack","attend","attitude","attract","auction","audit","august","aunt","author","auto","autumn","average","avocado","avoid","awake","aware","away","awesome","awful","awkward","axis","baby","bachelor","bacon","badge","bag","balance","balcony","ball","bamboo","banana","banner","bar","barely","bargain","barrel","base","basic","basket","battle","beach","bean","beauty","because","become","beef","before","begin","behave","behind","believe","below","belt","bench","benefit","best","betray","better","between","beyond","bicycle","bid","bike","bind","biology","bird","birth","bitter","black","blade","blame","blanket","blast","bleak","bless","blind","blood","blossom","blouse","blue","blur","blush","board","boat","body","boil","bomb","bone","bonus","book","boost","border","boring","borrow","boss","bottom","bounce","box","boy","bracket","brain","brand","brass","brave","bread","breeze","brick","bridge","brief","bright","bring","brisk","broccoli","broken","bronze","broom","brother","brown","brush","bubble","buddy","budget","buffalo","build","bulb","bulk","bullet","bundle","bunker","burden","burger","burst","bus","business","busy","butter","buyer","buzz","cabbage","cabin","cable","cactus","cage","cake", "call", "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry", "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category", "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "century", "cereal", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase", "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child", "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle", "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk", "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close", "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut", "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort", "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control", "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost", "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle", "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek", "crew", "cricket", "crime", "crisp", "critic", "crop", "cross", "crouch", "crowd", "crucial", "cruel", "cruise", "crumble", "crunch", "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard", "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad", "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn", "day", "deal", "debate", "debris", "decade", "december", "decide", "decline", "decorate", "decrease", "deer", "defense", "define", "defy", "degree", "delay", "deliver", "demand", "demise", "denial", "dentist", "deny", "depart", "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk", "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram", "dial", "diamond", "diary", "dice", "diesel", "diet", "differ", "digital", "dignity", "dilemma", "dinner", "dinosaur", "direct", "dirt", "disagree", "discover", "disease", "dish", "dismiss", "disorder", "display", "distance", "divert", "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain", "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft", "dragon", "drama", "drastic", "draw", "dream", "dress", "drift", "drill", "drink", "drip", "drive", "drop", "drum", "dry", "duck", "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf", "dynamic", "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo", "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight", "either", "elbow", "elder", "electric", "elegant", "element", "elephant", "elevator", "elite", "else", "embark", "embody", "embrace", "emerge", "emotion", "employ", "empower", "empty", "enable", "enact", "end", "endless", "endorse", "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough", "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode", "equal", "equip", "era", "erase", "erode", "erosion", "error", "erupt", "escape", "essay", "essence", "estate", "eternal", "ethics", "evidence", "evil", "evoke", "evolve", "exact", "example", "excess", "exchange", "excite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit", "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend", "extra", "eye", "eyebrow", "fabric", "face", "faculty", "fade", "faint", "faith", "fall", "false", "fame", "family", "famous", "fan", "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father", "fatigue", "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female", "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field", "figure", "file", "film", "filter", "final", "find", "fine", "finger", "finish", "fire", "firm", "first", "fiscal", "fish", "fit", "fitness", "fix", "flag", "flame", "flash", "flat", "flavor", "flee", "flight", "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly", "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot", "force", "forest", "forget", "fork", "fortune", "forum", "forward", "fossil", "foster", "found", "fox", "fragile", "frame", "frequent", "fresh", "friend", "fringe", "frog", "front", "frost", "frown", "frozen", "fruit", "fuel", "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy", "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas", "gasp", "gate", "gather", "gauge", "gaze", "general", "genius", "genre", "gentle", "genuine", "gesture", "ghost", "giant", "gift", "giggle", "ginger", "giraffe", "girl", "give", "glad", "glance", "glare", "glass", "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue", "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern", "gown", "grab", "grace", "grain", "grant", "grape", "grass", "gravity", "great", "green", "grid", "grief", "grit", "grocery", "group", "grow", "grunt", "guard", "guess", "guide", "guilt", "guitar", "gun", "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy", "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head", "health", "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help", "hen", "hero", "hidden", "high", "hill", "hint", "hip", "hire", "history", "hobby", "hockey", "hold", "hole", "holiday", "hollow", "home", "honey", "hood", "hope", "horn", "horror", "horse", "hospital", "host", "hotel", "hour", "hover", "hub", "huge", "human", "humble", "humor", "hundred", "hungry", "hunt", "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea", "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense", "immune", "impact", "impose", "improve", "impulse", "inch", "include", "income", "increase", "index", "indicate", "indoor", "industry", "infant", "inflict", "inform", "inhale", "inherit", "initial", "inject", "injury", "inmate", "inner", "innocent", "input", "inquiry", "insane", "insect", "inside", "inspire", "install", "intact", "interest", "into", "invest", "invite", "involve", "iron", "island", "isolate", "issue", "item", "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel", "job", "join", "joke", "journey", "joy", "judge", "juice", "jump", "jungle", "junior", "junk", "just", "kangaroo", "keen", "keep", "ketchup", "key", "kick", "kid", "kidney", "kind", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife", "knock", "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp", "language", "laptop", "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn", "lawsuit", "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture", "left", "leg", "legal", "legend", "leisure", "lemon", "lend", "length", "lens", "leopard", "lesson", "letter", "level", "liar", "liberty", "library", "license", "life", "lift", "light", "like", "limb", "limit", "link", "lion", "liquid", "list", "little", "live", "lizard", "load", "loan", "lobster", "local", "lock", "logic", "lonely", "long", "loop", "lottery", "loud", "lounge", "love", "loyal", "lucky", "luggage", "lumber", "lunar", "lunch", "luxury", "lyrics", "machine", "mad", "magic", "magnet", "maid", "mail", "main", "major", "make", "mammal", "man", "manage", "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin", "marine", "market", "marriage", "mask", "mass", "master", "match", "material", "math", "matrix", "matter", "maximum", "maze", "meadow", "mean", "measure", "meat", "mechanic", "medal", "media", "melody", "melt", "member", "memory", "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message", "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind", "minimum", "minor", "minute", "miracle", "mirror", "misery", "miss", "mistake", "mix", "mixed", "mixture", "mobile", "model", "modify", "mom", "moment", "monitor", "monkey", "monster", "month", "moon", "moral", "more", "morning", "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie", "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music", "must", "mutual", "myself", "mystery", "myth", "naive", "name", "napkin", "narrow", "nasty", "nation", "nature", "near", "neck", "need", "negative", "neglect", "neither", "nephew", "nerve", "nest", "net", "network", "neutral", "never", "news", "next", "nice", "night", "noble", "noise", "nominee", "noodle", "normal", "north", "nose", "notable", "note", "nothing", "notice", "novel", "now", "nuclear", "number", "nurse", "nut", "oak", "obey", "object", "oblige", "obscure", "observe", "obtain", "obvious", "occur", "ocean", "october", "odor", "off", "offer", "office", "often", "oil", "okay", "old", "olive", "olympic", "omit", "once", "one", "onion", "online", "only", "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard", "order", "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other", "outdoor", "outer", "output", "outside", "oval", "oven", "over", "own", "owner", "oxygen", "oyster", "ozone", "pact", "paddle", "page", "pair", "palace", "palm", "panda", "panel", "panic", "panther", "paper", "parade", "parent", "park", "parrot", "party", "pass", "patch", "path", "patient", "patrol", "pattern", "pause", "pave", "payment", "peace", "peanut", "pear", "peasant", "pelican", "pen", "penalty", "pencil", "people", "pepper", "perfect", "permit", "person", "pet", "phone", "photo", "phrase", "physical", "piano", "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot", "pink", "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic", "plate", "play", "please", "pledge", "pluck", "plug", "plunge", "poem", "poet", "point", "polar", "pole", "police", "pond", "pony", "pool", "popular", "portion", "position", "possible", "post", "potato", "pottery", "poverty", "powder", "power", "practice", "praise", "predict", "prefer", "prepare", "present", "pretty", "prevent", "price", "pride", "primary", "print", "priority", "prison", "private", "prize", "problem", "process", "produce", "profit", "program", "project", "promote", "proof", "property", "prosper", "protect", "proud", "provide", "public", "pudding", "pull", "pulp", "pulse", "pumpkin", "punch", "pupil", "puppy", "purchase", "purity", "purpose", "purse", "push", "put", "puzzle", "pyramid", "quality", "quantum", "quarter", "question", "quick", "quit", "quiz", "quote", "rabbit", "raccoon", "race", "rack", "radar", "radio", "rail", "rain", "raise", "rally", "ramp", "ranch", "random", "range", "rapid", "rare", "rate", "rather", "raven", "raw", "razor", "ready", "real", "reason", "rebel", "rebuild", "recall", "receive", "recipe", "record", "recycle", "reduce", "reflect", "reform", "refuse", "region", "regret", "regular", "reject", "relax", "release", "relief", "rely", "remain", "remember", "remind", "remove", "render", "renew", "rent", "reopen", "repair", "repeat", "replace", "report", "require", "rescue", "resemble", "resist", "resource", "response", "result", "retire", "retreat", "return", "reunion", "reveal", "review", "reward", "rhythm", "rib", "ribbon", "rice", "rich", "ride", "ridge", "rifle", "right", "rigid", "ring", "riot", "ripple", "risk", "ritual", "rival", "river", "road", "roast", "robot", "robust", "rocket", "romance", "roof", "rookie", "room", "rose", "rotate", "rough", "round", "route", "royal", "rubber", "rude", "rug", "rule", "run", "runway", "rural", "sad", "saddle", "sadness", "safe", "sail", "salad", "salmon", "salon", "salt", "salute", "same", "sample", "sand", "satisfy", "satoshi", "sauce", "sausage", "save", "say", "scale", "scan", "scare", "scatter", "scene", "scheme", "school", "science", "scissors", "scorpion", "scout", "scrap", "screen", "script", "scrub", "sea", "search", "season", "seat", "second", "secret", "section", "security", "seed", "seek", "segment", "select", "sell", "seminar", "senior", "sense", "sentence", "series", "service", "session", "settle", "setup", "seven", "shadow", "shaft", "shallow", "share", "shed", "shell", "sheriff", "shield", "shift", "shine", "ship", "shiver", "shock", "shoe", "shoot", "shop", "short", "shoulder", "shove", "shrimp", "shrug", "shuffle", "shy", "sibling", "sick", "side", "siege", "sight", "sign", "silent", "silk", "silly", "silver", "similar", "simple", "since", "sing", "siren", "sister", "situate", "six", "size", "skate", "sketch", "ski", "skill", "skin", "skirt", "skull", "slab", "slam", "sleep", "slender", "slice", "slide", "slight", "slim", "slogan", "slot", "slow", "slush", "small", "smart", "smile", "smoke", "smooth", "snack", "snake", "snap", "sniff", "snow", "soap", "soccer", "social", "sock", "soda", "soft", "solar", "soldier", "solid", "solution", "solve", "someone", "song", "soon", "sorry", "sort", "soul", "sound", "soup", "source", "south", "space", "spare", "spatial", "spawn", "speak", "special", "speed", "spell", "spend", "sphere", "spice", "spider", "spike", "spin", "spirit", "split", "spoil", "sponsor", "spoon", "sport", "spot", "spray", "spread", "spring", "spy", "square", "squeeze", "squirrel", "stable", "stadium", "staff", "stage", "stairs", "stamp", "stand", "start", "state", "stay", "steak", "steel", "stem", "step", "stereo", "stick", "still", "sting", "stock", "stomach", "stone", "stool", "story", "stove", "strategy", "street", "strike", "strong", "struggle", "student", "stuff", "stumble", "style", "subject", "submit", "subway", "success", "such", "sudden", "suffer", "sugar", "suggest", "suit", "summer", "sun", "sunny", "sunset", "super", "supply", "supreme", "sure", "surface", "surge", "surprise", "surround", "survey", "suspect", "sustain", "swallow", "swamp", "swap", "swarm", "swear", "sweet", "swift", "swim", "swing", "switch", "sword", "symbol", "symptom", "syrup", "system", "table", "tackle", "tag", "tail", "talent", "talk", "tank", "tape", "target", "task", "taste", "tattoo", "taxi", "teach", "team", "tell", "ten", "tenant", "tennis", "tent", "term", "test", "text", "thank", "that", "theme", "then", "theory", "there", "they", "thing", "this", "thought", "three", "thrive", "throw", "thumb", "thunder", "ticket", "tide", "tiger", "tilt", "timber", "time", "tiny", "tip", "tired", "tissue", "title", "toast", "tobacco", "today", "toddler", "toe", "together", "toilet", "token", "tomato", "tomorrow", "tone", "tongue", "tonight", "tool", "tooth", "top", "topic", "topple", "torch", "tornado", "tortoise", "toss", "total", "tourist", "toward", "tower", "town", "toy", "track", "trade", "traffic", "tragic", "train", "transfer", "trap", "trash", "travel", "tray", "treat", "tree", "trend", "trial", "tribe", "trick", "trigger", "trim", "trip", "trophy", "trouble", "truck", "true", "truly", "trumpet", "trust", "truth", "try", "tube", "tuition", "tumble", "tuna", "tunnel", "turkey", "turn", "turtle", "twelve", "twenty", "twice", "twin", "twist", "two", "type", "typical", "ugly", "umbrella", "unable", "unaware", "uncle", "uncover", "under", "undo", "unfair", "unfold", "unhappy", "uniform", "unique", "unit", "universe", "unknown", "unlock", "until", "unusual", "unveil", "update", "upgrade", "uphold", "upon", "upper", "upset", "urban", "urge", "usage", "use", "used", "useful", "useless", "usual", "utility", "vacant", "vacuum", "vague", "valid", "valley", "valve", "van", "vanish", "vapor", "various", "vast", "vault", "vehicle", "velvet", "vendor", "venture", "venue", "verb", "verify", "version", "very", "vessel", "veteran", "viable", "vibrant", "vicious", "victory", "video", "view", "village", "vintage", "violin", "virtual", "virus", "visa", "visit", "visual", "vital", "vivid", "vocal", "voice", "void", "volcano", "volume", "vote", "voyage", "wage", "wagon", "wait", "walk", "wall", "walnut", "want", "warfare", "warm", "warrior", "wash", "wasp", "waste", "water", "wave", "way", "wealth", "weapon", "wear", "weasel", "weather", "web", "wedding", "weekend", "weird", "welcome", "west", "wet", "whale", "what", "wheat", "wheel", "when", "where", "whip", "whisper", "wide", "width", "wife", "wild", "will", "win", "window", "wine", "wing", "wink", "winner", "winter", "wire", "wisdom", "wise", "wish", "witness", "wolf", "woman", "wonder", "wood", "wool", "word", "work", "world", "worry", "worth", "wrap", "wreck", "wrestle", "wrist", "write", "wrong", "yard", "year", "yellow", "you", "young", "youth", "zebra", "zero", "zone", "zoo"]


console.print("[purple]Starting search... Please Wait [/purple]")
console.print("==========================================================")
divs = int(input(" 📋How Many Derivation Paths m/44'/0'/0'/0/0/ to m/44'/0'/0'/0/999/ ✍️ -> "))

def data_wallet():
    for child in range(0,divs):
        bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
        bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN ).ChildKey(0).ChildKey(child)
        first_encode = base58.b58decode(bip32_child_key_obj.WalletImportFormat())
        private_key_full = binascii.hexlify(first_encode)
        private_keyhex = private_key_full[2:-10]
        wifu = ice.btc_pvk_to_wif(private_keyhex.decode(), False)
        dec = int(private_keyhex.decode(), 16)
        uaddr = ice.privatekey_to_address(0, False, int(dec))  #Uncompressed
        data.append({
                'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
                'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
                'path': f"m/44'/0'/0'/0/{child}",
                'address': bip32_child_key_obj.Address(),
                'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
                'privatekey': bip32_child_key_obj.WalletImportFormat(),
                'privatekeyhex': private_keyhex.decode(),
                'seed': dec,
                'wifu': wifu,
                'uaddr': uaddr,

            })

prompt= console.print('''[yellow]
    *************** WORD Menu Version ***************[/yellow]
    *                                               *
    *    Option 1. Words  From File List       =  1 *
    *    Option 2. Words 1-12Random From File  =  2 *
    *    Option 3. Numbers From File           =  3 *
    *    Option 4. 12 Random Words  Generated  =  4 *
    *    Option 5. 24 Random Words  Generated  =  5 *    
    *                                               *
    [yellow]*************** WORD Menu Version ***************[/yellow]
    
 Enter Your Choice 1/2/3/4/5 ''')
count=0
start=int(input('Type HERE : '))
while True:
    count+=1
    if start == 1:
        mylistwords = []

        with open('wordlist.txt', newline='', encoding='utf-8') as f1:
            for line in f1:
                mylistwords.append(line.strip())
        for i in range(0,len(mylistwords)):
            data = []
            mnemonic_words = mylistwords[i]
            mnemo = Mnemonic("english")
            seed = mnemo.to_seed(mnemonic_words, passphrase="")
            ammount = '0 BTC'
            data_wallet()
            for target_wallet in data:
                bal = xBal(target_wallet['address'])
                bal1 = xBal1(target_wallet['uaddr'])
                if bal != str(ammount) or bal1 != str(ammount):
                    console.print('[green]\nmnemonic_words  : [/green]', mnemonic_words)
                    console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[green] : Bitcoin AddressCompressed   : [/green]', target_wallet['address'], '[green] : Balance : [/green]', bal)
                    console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[green] : Bitcoin AddressUnCompressed : [/green]', target_wallet['uaddr'], '[green] : Balance : [/green]', bal1)
                    console.print('[green]Privatekey WIF Compressed   : [/green]', target_wallet['privatekey'])
                    console.print('[green]Privatekey WIF UnCompressed : [/green]', target_wallet['wifu'])
                    console.print('[green]Privatekey HEX  : [/green]', target_wallet['privatekeyhex'])
                    console.print('[green]Privatekey DEC  : [/green]', target_wallet['seed'])
                    with open("winner.txt", "a") as f:
                        f.write(f"""\nMnemonic_words:  {mnemonic_words}
                        Derivation Path:  {target_wallet['path']}    Public Address BitcoinCompressed   :  {target_wallet['address']} : Balance : {bal}
                        Derivation Path:  {target_wallet['path']}    Public Address BitcoinUnCompressed :  {target_wallet['uaddr']} : Balance : {bal1}
                        Privatekey WIF Compressed  :  {target_wallet['privatekey']}
                        Privatekey WIF UnCompressed:  {target_wallet['wifu']}
                        Privatekey HEX:  {target_wallet['privatekeyhex']}
                        Privatekey DEC:  {target_wallet['seed']}""")
                else:
                    console.print('[red]\nmnemonic_words  : [/red]', mnemonic_words)
                    console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[red] : Bitcoin AddressCompressed   : [/red]', target_wallet['address'], '[red] : Balance : [/red]', bal)
                    console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[red] : Bitcoin AddressUnCompressed : [/red]', target_wallet['uaddr'], '[red] : Balance : [/red]', bal1)
                    console.print('[red]Privatekey WIF Compressed   : [/red]', target_wallet['privatekey'])
                    console.print('[red]Privatekey WIF UnCompressed : [/red]', target_wallet['wifu'])
                    console.print('[red]Privatekey HEX  : [/red]', target_wallet['privatekeyhex'])
                    console.print('[red]Privatekey DEC  : [/red]', target_wallet['seed'])
        
    if start == 2:
        CWords = ' '.join(random.sample(mylist, random.randint(1,12)))
        #CWords = ''.join(random.sample(mylist, random.randint(1,12))) # no space

    if start == 3:
        CWords = ' '.join(random.sample(mynumbers, random.randint(1,12)))
        #CWords = ''.join(random.sample(mynumbers, random.randint(1,12))) # no space
    if start == 4:
        c1 = random.choice(wordlist)
        c2 = random.choice(wordlist)
        c3 = random.choice(wordlist)
        c4 = random.choice(wordlist)
        c5 = random.choice(wordlist)
        c6 = random.choice(wordlist)
        c7 = random.choice(wordlist)
        c8 = random.choice(wordlist)      
        c9 = random.choice(wordlist)
        c10 = random.choice(wordlist)
        c11 = random.choice(wordlist)
        c12 = random.choice(wordlist)
        CWords = "".join(c1+' '+c2+' '+c3+' '+c4+' '+c5+' '+c6+' '+c7+' '+c8+' '+c9+' '+c10+' '+c11+' '+c12)
    if start == 5:
        c1 = random.choice(wordlist)
        c2 = random.choice(wordlist)
        c3 = random.choice(wordlist)
        c4 = random.choice(wordlist)
        c5 = random.choice(wordlist)
        c6 = random.choice(wordlist)
        c7 = random.choice(wordlist)
        c8 = random.choice(wordlist)      
        c9 = random.choice(wordlist)
        c10 = random.choice(wordlist)
        c11 = random.choice(wordlist)
        c12 = random.choice(wordlist)
        c13 = random.choice(wordlist)
        c14 = random.choice(wordlist)
        c15 = random.choice(wordlist)
        c16 = random.choice(wordlist)
        c17 = random.choice(wordlist)
        c18 = random.choice(wordlist)
        c19 = random.choice(wordlist)
        c20 = random.choice(wordlist)
        c21 = random.choice(wordlist)
        c22 = random.choice(wordlist)
        c23 = random.choice(wordlist)
        c24 = random.choice(wordlist)
        CWords = "".join(c1+' '+c2+' '+c3+' '+c4+' '+c5+' '+c6+' '+c7+' '+c8+' '+c9+' '+c10+' '+c11+' '+c12+' '+c13+' '+c14+' '+c15+' '+c16+' '+c17+' '+c18+' '+c19+' '+c20+' '+c21+' '+c22+' '+c23+' '+c24)
    data = []
    mnemonic_words = CWords
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_words, passphrase="")
    ammount = '0 BTC'
    data_wallet()
    for target_wallet in data:
        bal = xBal(target_wallet['address'])
        bal1 = xBal1(target_wallet['uaddr'])
        if bal != str(ammount) or bal1 != str(ammount):
            console.print('[green]\nmnemonic_words  : [/green]', mnemonic_words)
            console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[green] : Bitcoin AddressCompressed   : [/green]', target_wallet['address'], '[green] : Balance : [/green]', bal)
            console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[green] : Bitcoin AddressUnCompressed : [/green]', target_wallet['uaddr'], '[green] : Balance : [/green]', bal1)
            console.print('[green]Privatekey WIF Compressed   : [/green]', target_wallet['privatekey'])
            console.print('[green]Privatekey WIF UnCompressed : [/green]', target_wallet['wifu'])
            console.print('[green]Privatekey HEX  : [/green]', target_wallet['privatekeyhex'])
            console.print('[green]Privatekey DEC  : [/green]', target_wallet['seed'])
            with open("winner.txt", "a") as f:
                f.write(f"""\nMnemonic_words:  {mnemonic_words}
                Derivation Path:  {target_wallet['path']}    Public Address BitcoinCompressed   :  {target_wallet['address']} : Balance : {bal}
                Derivation Path:  {target_wallet['path']}    Public Address BitcoinUnCompressed :  {target_wallet['uaddr']} : Balance : {bal1}
                Privatekey WIF Compressed  :  {target_wallet['privatekey']}
                Privatekey WIF UnCompressed:  {target_wallet['wifu']}
                Privatekey HEX:  {target_wallet['privatekeyhex']}
                Privatekey DEC:  {target_wallet['seed']}""")
        else:
            console.print('[red]\nmnemonic_words  : [/red]', mnemonic_words)
            console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[red] : Bitcoin AddressCompressed   : [/red]', target_wallet['address'], '[red] : Balance : [/red]', bal)
            console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[red] : Bitcoin AddressUnCompressed : [/red]', target_wallet['uaddr'], '[red] : Balance : [/red]', bal1)
            console.print('[red]Privatekey WIF Compressed   : [/red]', target_wallet['privatekey'])
            console.print('[red]Privatekey WIF UnCompressed : [/red]', target_wallet['wifu'])
            console.print('[red]Privatekey HEX  : [/red]', target_wallet['privatekeyhex'])
            console.print('[red]Privatekey DEC  : [/red]', target_wallet['seed'])
