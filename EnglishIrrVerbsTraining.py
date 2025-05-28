from tkinter import *
import random
import threading

Verbes = [
	#infinitif
	[
		"be",#1
		"beat",#2
		"become",#3
		"begin",#4
		"bet",#5
		"bind",#6
		"bite",#7
		"bleed",#8
		"blow",#9
		"break",#10

		"bring",#11
		"build",#12
		"burn",#13
		"burst",#14
		"buy",#15
		"catch",#16
		"choose",#17
		"come",#18
		"cost",#19
		"cut",#20
		
		"do",#21
		"draw",#22
		"dream",#23
		"drink",#24
		"drive",#25
		"eat",#26
		"fall",#27
		"feed",#28
		"feel",#29
		"fight",#30

		"find",#31
		"fly",#32
		"forbid",#33
		"forget",#34
		"forgive",#35
		"freeze",#36
		"get",#37
		"give",#38
		"go",#39
		"grow",#40

		"hang",#41
		"have",#42
		"hear",#43
		"hide",#44
		"hit",#45
		"hold",#46
		"hurt",#47
		"keep",#48
		"know",#49
		"lay",#50

		"learn",#51
		"leave",#52
		"lend",#53
		"let",#54
		"lie",#55
		"light",#56
		"lose",#57
		"make",#58
		"mean",#59
		"meet",#60

		"pay",#61
		"put",#62
		"read",#63
		"rent",#64
		"ride",#65
		"ring",#66
		"rise",#67
		"run",#68
		"say",#69
		"see",#70

		"seek",#71
		"sell",#72
		"send",#73
		"set",#74
		"shake",#75
		"shine",#76
		"shoot",#77
		"show",#78
		"shut",#79
		"sing",#80

		"sit",#81
		"sleep",#82
		"smell",#83
		"speak",#84
		"spend",#85
		"stand",#86
		"steal",#87
		"strike",#88
		"swim",#89
		"take",#90

		"teach",#91
		"tear",#92
		"tell",#93
		"think",#94
		"throw",#95
		"understand",#96
		"upset",#97
		"wake up",#98
		"wear",#99
		"win",#100

		"write"#101
	],
	#prétérit
	[
		"was were",#1
		"beat",#2
		"became",#3
		"began",#4
		"bet",#5
		"bound",#6
		"bit",#7
		"bled",#8
		"blew",#9
		"broke",#10

		"brought",#11
		"built",#12
		"burnt",#13
		"burst",#14
		"bought",#15
		"caught",#16
		"chose",#17
		"came",#18
		"cost",#19
		"cut",#20
		
		"did",#21
		"drew",#22
		"dreamt",#23
		"drank",#24
		"drove",#25
		"ate",#26
		"fell",#27
		"fed",#28
		"felt",#29
		"fought",#30

		"found",#31
		"flew",#32
		"forbade",#33
		"forgot",#34
		"forgave",#35
		"froze",#36
		"got",#37
		"gave",#38
		"went",#39
		"grew",#40

		"hung",#41
		"had",#42
		"heard",#43
		"hid",#44
		"hit",#45
		"held",#46
		"hurt",#47
		"kept",#48
		"knew",#49
		"laid",#50

		"learnt",#51
		"left",#52
		"lent",#53
		"let",#54
		"lay",#55
		"lit",#56
		"lost",#57
		"made",#58
		"meant",#59
		"met",#60

		"paid",#61
		"put",#62
		"read",#63
		"rent",#64
		"rode",#65
		"rang",#66
		"rose",#67
		"ran",#68
		"said",#69
		"saw",#70

		"sought",#71
		"sold",#72
		"sent",#73
		"set",#74
		"shook",#75
		"shone",#76
		"shot",#77
		"showed",#78
		"shut",#79
		"sang",#80

		"sat",#81
		"slept",#82
		"smelt",#83
		"spoke",#84
		"spent",#85
		"stood",#86
		"stole",#87
		"struck",#88
		"swam",#89
		"took",#90

		"taught",#91
		"tore",#92
		"told",#93
		"thought",#94
		"threw",#95
		"understood",#96
		"upset",#97
		"woke up",#98
		"wore",#99
		"won",#100

		"wrote"#101
	],
	#participe passé
	[
		"been",#1
		"beaten",#2
		"become",#3
		"begun",#4
		"bet",#5
		"bound",#6
		"bitten",#7
		"bled",#8
		"blown",#9
		"broken",#10

		"brought",#11
		"built",#12
		"burnt",#13
		"burst",#14
		"bought",#15
		"caught",#16
		"chosen",#17
		"come",#18
		"cost",#19
		"cut",#20
		
		"done",#21
		"drawn",#22
		"dreamt",#23
		"drunk",#24
		"driven",#25
		"eaten",#26
		"fallen",#27
		"fed",#28
		"felt",#29
		"fought",#30

		"found",#31
		"flown",#32
		"forbidden",#33
		"forgotten",#34
		"forgiven",#35
		"frozen",#36
		"got",#37
		"given",#38
		"gone",#39
		"grown",#40

		"hung",#41
		"had",#42
		"heard",#43
		"hidden",#44
		"hit",#45
		"held",#46
		"hurt",#47
		"kept",#48
		"known",#49
		"laid",#50

		"learnt",#51
		"left",#52
		"lent",#53
		"let",#54
		"lain",#55
		"lit",#56
		"lost",#57
		"made",#58
		"meant",#59
		"met",#60

		"paid",#61
		"put",#62
		"read",#63
		"rent",#64
		"ridden",#65
		"rung",#66
		"risen",#67
		"run",#68
		"said",#69
		"seen",#70

		"sought",#71
		"sold",#72
		"sent",#73
		"set",#74
		"shaken",#75
		"shone",#76
		"shot",#77
		"shown",#78
		"shut",#79
		"sung",#80

		"sat",#81
		"slept",#82
		"smelt",#83
		"spoken",#84
		"spent",#85
		"stood",#86
		"stolen",#87
		"struck",#88
		"swum",#89
		"taken",#90

		"taught",#91
		"torn",#92
		"told",#93
		"thought",#94
		"thrown",#95
		"understood",#96
		"upset",#97
		"woken up",#98
		"worn",#99
		"won",#100

		"written"#101
	],
	#traduction
	[
		"être",#1
		"battre",#2
		"devenir",#3
		"commencer",#4
		"parier",#5
		"relier(un livre)",#6
		"mordre",#7
		"saigner",#8
		"souffler(se moucher)",#9
		"casser",#10

		"apporter",#11
		"construire",#12
		"brûler",#13
		"éclater",#14
		"acheter",#15
		"attraper",#16
		"choisir",#17
		"venir",#18
		"coûter",#19
		"couper",#20
		
		"faire",#21
		"dessiner",#22
		"rêver",#23
		"boire",#24
		"conduire",#25
		"manger",#26
		"tomber",#27
		"nourrir",#28
		"se sentir,ressentir",#29
		"se battre",#30

		"trouver",#31
		"voler(dans les airs)",#32
		"interdire",#33
		"oublier",#34
		"pardonner",#35
		"geler,se figer",#36
		"obtenir(monter dans)",#37
		"donner",#38
		"aller",#39
		"grandir,pousser(plante)",#40

		"pendre,suspendre(traîner)",#41
		"avoir",#42
		"entendre",#43
		"cacher,se cacher",#44
		"frapper",#45
		"tenir",#46
		"blesser,faire mal,avoir mal",#47
		"garder(continuer)",#48
		"savoir,connaître",#49
		"poser,mettre la table",#50

		"apprendre",#51
		"quitter,partir,laisser",#52
		"prêter",#53
		"permettre,laisser(laisser tomber)",#54
		"s'allonger",#55
		"allumer,éclairer",#56
		"perdre",#57
		"faire,fabriquer",#58
		"signifier,vouloir dire",#59
		"rencontrer",#60

		"payer",#61
		"mettre",#62
		"lire",#63
		"louer",#64
		"aller à bicyclette,à cheval",#65
		"sonner,téléphoner",#66
		"monter,s'élever",#67
		"courir",#68
		"dire",#69
		"voir",#70

		"chercher",#71
		"vendre",#72
		"envoyer",#73
		"mettre,poser,placer",#74
		"trembler",#75
		"briller",#76
		"tirer,marquer,tourner(film)",#77
		"montrer(se vanter)",#78
		"fermer",#79
		"chanter",#80

		"s'assoir",#81
		"dormir",#82
		"sentir(odorat)",#83
		"parler",#84
		"dépenser(de l'argent),passer(du temps)",#85
		"se tenir debout",#86
		"voler,dérober",#87
		"frapper,donner un coup,passer un accord",#88
		"nager",#89
		"prendre",#90

		"enseigner,apprendre",#91
		"déchirer",#92
		"dire,raconter",#93
		"penser",#94
		"jeter,lancer",#95
		"comprendre",#96
		"contrarier",#97
		"se réveiller",#98
		"porter(vêtements)",#99
		"gagner",#100

		"écrire"#101
	]
]

#---------------初始---------------

root = Tk()
root.title("English Verbs Training")
root.geometry("550x525")
root.resizable(0,0)
#root.iconbitmap("icon.ico")

#分数变量
numT : int = 0#练习的次数
Score : int = 0#分数

ENT = []#装Entry
LignV = []#设置每行的词
CoBtn : int = 1 #按钮的当前状态，1=待检查，2=检查完等查看答案，3=下一个
allCorrect : bool

#选词区间
VEntre = [0,len(Verbes[3]) - 1]

#---------------窗口---------------

#函数
def ButtonSet():
	global CoBtn
	if CoBtn == 1:#待检查
		Validation()
		if allCorrect == False:
			btn.config(text="Correction")
			CoBtn = 2
		else:
			btn.config(text="NEXT")
			CoBtn = 3
			Correction()
	elif CoBtn == 2:#检查完等查看答案
		Correction()
		btn.config(text="NEXT")
		CoBtn = 3
	elif CoBtn == 3:#下一个
		btn.config(text="Valider")
		CoBtn = 1
		scoreL.config(text="Average Score: " + str(round(Score/numT/3,2)) + "/5")
		creatTraining()	

def creatTraining():
	global numT
	if len(ENT):
		for i in range(20):
			ENT[i].destroy()
	ENT.clear()
	LignV.clear()
	numT = numT + 1
	#配置
	for i in range(20):#4*5
		ENT.append(Entry(root,width=12,font=("Times New Roman",13)))
	for i in range(5):
		num = random.randint(VEntre[0], VEntre[1])
		while num in LignV:
			num = random.randint(VEntre[0], VEntre[1])
		LignV.append(num)
	#放置
	for l in range(int(len(ENT)/4)):
		for i in range(4):
			ENT[(l*4)+i].place(x=i * 128 + 25,y=l*55+170)
			if i == 3:
				ENT[(l*4)+3].insert(0,Verbes[i][LignV[l]])
				ENT[(l*4)+3].config(state="disabled")

def Validation():
	global Score
	global allCorrect
	allCorrect = True
	for l in range(int(len(ENT)/4)):
		for i in range(4):
			if ENT[(l*4)+i].cget("state") != "disabled":
				if ENT[(l*4)+i].get().lower().strip() == Verbes[i][LignV[l]]:
					Score = Score + 1
					ENT[(l*4)+i].config(fg="green")
				else:
					ENT[(l*4)+i].config(fg="red")
					allCorrect = False
			else:
				continue

def Correction():
	for l in range(int(len(ENT)/4)):
		for i in range(4):
			if ENT[(l*4)+i].cget("state") != "disabled":
				if  ENT[(l*4)+i].get().lower().strip() != Verbes[i][LignV[l]]:
					ENT[(l*4)+i].delete(0,END)
					ENT[(l*4)+i].insert(0,Verbes[i][LignV[l]])
			else:
				continue

#---------------控制台---------------

#控制台输入选择区间
def set_VEntre():
	while True:
		print("Intervalle:",VEntre[0] + 1,";",VEntre[1] + 1)
		UserInput = input("Saisir l'Intervalle des Verbes (; pour Découper)\n")
		if UserInput != "showWord":
			Select = UserInput.strip().split(";")
			if len(Select) == 2:
				if CanConvertToINT(Select[0]) and CanConvertToINT(Select[1]):
					for i in range(2):
						if int(Select[i]) < 1:
							Select[i] = 1
						elif int(Select[i]) > len(Verbes[3]):
							Select[i] = len(Verbes[3])
							
					if abs(int(Select[0]) - int(Select[1])) + 1 >= 5:	
						VEntre[0] = int(Select[0]) - 1
						VEntre[1] = int(Select[1]) - 1
						print("\n")
					else:
						print(">ERREUR! Intervalle est moins de 5 !\n\n")
				else:
					print(">ERREUR! Ecrivez des nombres entier !\n\n")
			else:
				print(">ERREUR! Vous devez saisir 2 valeur !\n\n")
		else:
			showWord()

#判断数字能否转换为int类型
def CanConvertToINT(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

#显示词库
def showWord():
	print("\n")
	print(f"{"Num":<7} {"Infinitif":<14} {"Prétérit":<14} {"P-Passé":<14} {"Traduction"}")
	for n in range(len(Verbes[3])):
		print(f"{n + 1:<7} {Verbes[0][n]:<14} {Verbes[1][n]:<14} {Verbes[2][n]:<14} {Verbes[3][n]}")
	print("\n")

#---------------配置---------------

#标题
BigTl = Label(root,text="English Verbs Training",font=("Arial Black",28))
BigTl.pack()
#分数显示
scoreL = Label(root,text="Average Score: nan/5",font=("Arial",18))
scoreL.pack()
#按钮
btn = Button(root,text="Valider",font=("Arial Black",18),background="#F0F0F0",width=14,command=ButtonSet)
btn.place(anchor=CENTER,x=275,y=475)
#显示动词类型
VType = [
	Label(root,text="Infinitif",font=("Arial",16)),
	Label(root,text="Prétérit",font=("Arial",16)),
	Label(root,text="P-Passé",font=("Arial",16)),
	Label(root,text="Traduction",font=("Arial",16))
]
for v in range(4):
	VType[v].place(anchor=CENTER,x=v * 128 + 80,y=135)

threading.Thread(target=set_VEntre, daemon=True).start()

creatTraining()
root.mainloop()

