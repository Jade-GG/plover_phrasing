LONGEST_KEY = 1

starters = {	"SWR":"I",
		"KPWR":"you",
		"KWHR":"he",
		"SKWHR":"she",
		"TWH":"they",
		"TWR":"we",
		"KPWH":"it",
		"STKPWHR":""}

__are = {	"SWR":"am",
		"KPWR":"are",
		"KWHR":"is",
		"SKWHR":"is",
		"TWH":"are",
		"TWR":"are",
		"KPWH":"is",
		"STKPWHR":"are",
		"WHAE":"is",
		"WHAU":"are",
		"WHAEU":"am",

		"SKPWE":"is",
		"SKPWU":"are",
		"SKPWEU":"am",

		"STKOE":"is",
		"STKOU":"are",
		"STKOEU":"am",

		"STKPWOE":"is",
		"STKPWOU":"are",
		"STKPWOEU":"am",

		"STHAE":"is",
		"STHAU":"are",
		"STHAEU":"am",
		
		"STPAE":"is",
		"STPAU":"are",
		"STPAEU":"am",

		"SWHE":"is",
		"SWHU":"are",
		"SWHEU":"am"
		}


middles = { 	"A":"really",
		"U":"really",
		"O":"can't",
		"AO":"really can't",
		"OU":"can't really",
		"OE":"don't",
		"AOE":"really don't",
		"OEU":"don't really",
		"E":"doesn't",
		"AE":"really doesn't",
		"EU":"doesn't really",
		"AU":"didn't",
		"AEU":"didn't really",
		"AOU":"really didn't",
		"AOEU":"don't even",
		"":""}




what = {	"WHAE":"what he",
		"WHAU":"what you",
		"WHAEU":"what I",

                "SKPWE":"doesn't he",
                "SKPWU":"don't you",
                "SKPWEU":"don't I",
                
                "STKOE":"does he",
                "STKOU":"do you",
                "STKOEU":"do I",

                "STKPWOE":"did he",
                "STKPWOU":"did you",
                "STKPWOEU":"did I",

                "STHAE":"that he",
                "STHAU":"that you",
                "STHAEU":"that I",

                "STPAE":"if he",
                "STPAU":"if you",
                "STPAEU":"if I",
		
		"SWHE":"when he",
		"SWHU":"when you",
		"SWHEU":"when I"}




ends = {	"PB":"know",
		"PBT":"know that",
		"PBTS":"knows that",
		"*PBT":"know the",
		"*PBTS":"knows the",
		"*PBTD":"knew the",
		"P":"want",
		"PT":"want to",
		"PTS":"wants to",
                "PTD":"wanted to",
		"*PT":"want the",
		"*PTS":"wants the",
                "*PTD":"wanted the",
		"*P":"wanna",
		"RPL":"remember",
		"RPLT":"remember that",
		"RPLTS":"remembers that",
		"RPLTD":"remembered that",
		"*RPLT":"remember the",
		"*RPLTS":"remembers the",
		"*RPLTD":"remembered the",
		"BG":"can",
		"BGT":"can't",
		"BGD":"could",
		"BL":"believe",
		"BLT":"believe that",
		"*BLT":"believe the",
		"D":"had",
		"F":"have",
		"FZ":"has",
		"FS":"was",
		"FT":"have to",
		"FTS":"has to",
		"*FT":"have the",
		"*FTS":"has the",
		"FPLT":"must",
		"L":"will",
		"LD":"would",
		"PBG":"think",
		"PBGT":"think that",
		"PBGTS":"thinks that",
		"*PBGT":"think the",
		"*PBGTS":"thinks the",
		"PL":"may",
		"PLT":"might",
		#"R":"are", # special case this one
		#"RT":"are not", # also special case this
		#"*RT":"aren't", # and this one
		"RB":"shall",
		"RBD":"should",
		"RL":"recall",
		"RP":"were",
		"RPBT":"were not",
		"*RPBT":"weren't",
		"RPT":"were the",
		"*RPT":"were the",
		"RPBD":"understand",
		"*RPBD":"understood",
		"PBD":"need",
		"PBTD":"need to",
		"PBTSD":"needs to",
		"*PBTD":"need the",
		"*PBTSD":"needs the",
		"FL":"feel",
		"FLG":"feel like",
		"FLT":"felt",
		"FLGT":"felt like",
		"PBL":"mean",
		"PBLT":"meant",
		"BLG":"like",
		"BLGT":"like to",
		"BLGTS":"likes to",
		"*BLGT":"like the",
		"*BLGTS":"likes the",
		"LG":"love",
		"LGT":"love to",
		"LGTS":"loves to",
		"*LGT":"love the",
		"*LGTS":"loves the",
		"RBG":"care",
		"RBGT":"care about",
		"RBGTS":"cares about",
		"GT":"get",
		"*GT":"got",
		"PLD":"mind",
		"FG":"forget",
		"FGT":"forgot",
		"FRB":"wish",
		"FRBT":"wish to",
		"*FRBT":"wish the",
		"PGT":"expect",
		"FPB":"even",
		"PBLG":"just",
		"FR":"ever",
		"B":"be",
		"BT":"be the",
		"*BT":"be the",
		"BS":"said",
		"BTS":"said to",
		"*BTS":"said the",
		"BZ":"say",
		"BTZ":"say to",
		"*BTZ":"say the",
		"PLG":"imagine",
		"PLGT":"imagine that",
		"*PLGT":"imagine the",
		"":""}

def lookup(key):
	assert len(key) <= LONGEST_KEY

	# This is the one and only collision in the main dictionary.
	# Save the whales!
	if key[0] == "WHAEUL": return "whale"

	ks = ""
	km = ""
	ke = "*" if ("*" in key[0]) else ""
	c = 0
	for i in key[0]:
		if c == 0:
			if i in "AOEU-*": c+=1
			else: ks += i
		if c == 1:
			if not i in "AOEU-*": c+=1
			elif i in "AOEU": km += i
		if c == 2:
			ke += i

	if ks+km in what:
		ks = ks+km
		stw = what[ks]
	else:
		if not ks in starters: raise KeyError
		if not km in middles: raise KeyError
		stw =  starters[ks] + " " + middles[km]

	# -R special casing
	if not ke in ["R", "RT", "*RT"]:
		if not ke in ends: raise KeyError
		ret = stw + " " + ends[ke]
	else:
		if ke == "R":
			ret = stw + " " + __are[ks]
		elif ke == "RT":
			ret = stw + " " + __are[ks] + " not"
		elif ke == "*RT":
			ret = stw + " " + __are[ks] + "n't"

	if ret in ["  "," ",""]: raise KeyError

	return " ".join(ret.split())
