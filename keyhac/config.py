from keyhac import *

def configure(keymap):

	# config.py編集用のテキストエディタの設定
	keymap.editor = u"D:\Documents\Tools\vim\gvim.exe"	

	# ユーザモディファイアキーの定義
	# keymap.defineModifier("Space", "User1") # スペース
	keymap.defineModifier(28, "User0") # 変換
	keymap.defineModifier(29, "User0") # 無変換
	#keymap.defineModifier(242, "User0") # カタカナ
	#keymap.defineModifier(240, "User0") # カタカナ

	# どのウインドウにフォーカスがあっても効くキーマップ
	keymap_global = keymap.defineWindowKeymap()
	
	if 1:
		# SandS
		keymap.replaceKey("Space", "RShift")
		keymap_global["O-RShift"] = "Space"
		keymap.replaceKey("RShift", "LShift")
		keymap_global["S-161"] = "S-Space"
		keymap_global["C-161"] = "C-Space"

		keymap_global["O-Space"] = "Space"
		
		# Appsを単純なスペースにする
		keymap.replaceKey("Apps", "Space")
		
		#　;をBackspaceとして使用する
		keymap_global["S-Plus"] = "S-Plus"
		keymap_global["C-Plus"] = "Plus"
		keymap_global["Plus"] = "Back"
		
		# 下段の\をアンダースコアに置き換える
		keymap_global["226"] = "S-226"
		keymap_global["S-226"] = "226"

		# Ctrl-H でバックスペース
		# keymap_global["C-H"] = "Back"

		# Ctrl-T でDelete
		# keymap_global["C-T"] = "Delete"
		
		# Ctrl+カタカナでInsert
		# InsertはIMEのショートカットとして使用している
		# keymap_global["C-242"] = "Insert"
		
		# 変換をShiftにする
		# keymap.replaceKey("28", "RShift")
		# keymap_global["O-RShift"] = "Enter"
		# keymap.replaceKey("RShift", "LShift")
		# keymap_global["S-28"] = "S-28"
		# keymap_global["C-28"] = "C-28"
		# keymap_global["S-C-28"] = "S-C-28"
		# 無変換をShiftにする
		# keymap.replaceKey("29", "LShift")
		
		# Alt-Eでエクスプローラ起動
		keymap_global["A-E"] = "W-E"
		# keymap_global["C-242"] = "Insert"
		keymap_global["C-242"] = "Insert"
	# if 1:
		# for i in range(1, 12):
			# keymap_global["F" + str(i)] = "W-" + str(i)
	if 0:
		for i in ("A", "B", "C",):
			keymap_global["U2-" + i] = "Insert"
		keymap_global["O-242"] = "242"
	if 1:
		# keymap_global["U0-F1"] = keymap.command_ReloadConfig
		# keymap_global["U0-F2"] = keymap.command_EditConfig
		# keymap_global["S-F8"] = "C-S-P"
		# keymap_global["S-F9"] = "W-C-Left"
		# keymap_global["S-F10"] = "W-C-Right"
		# 最上段
		for i in range(1, 12):
			keymap_global["U0-" + str(i)] = "W-" + str(i)
		# 上段
		keymap_global["U0-Q"] = "A-F4"
		keymap_global["U0-W"] = "242"
		keymap_global["U0-E"] = "Insert"
		keymap_global["U0-R"] = "A-F"
		keymap_global["U0-Y"] = "C-C"
		keymap_global["U0-U"] = "C-Z"
		keymap_global["U0-I"] = "Home"
		keymap_global["U0-O"] = "End"
		keymap_global["U0-P"] = "C-V"
		keymap_global["U0-219"] = "W-Left"
		keymap_global["U0-221"] = "W-Right"
		# 中段
		keymap_global["U0-A"] = "Esc"
		keymap_global["U0-S"] = "Backspace"
		keymap_global["U0-D"] = "Delete"
		keymap_global["U0-F"] = "Enter"
		keymap_global["U0-186"] = "W-Down"
		keymap_global["U0-220"] = "W-Up"
		# vim風移動
		keymap_global["U0-H"] = "Left"
		keymap_global["U0-J"] = "Down"
		keymap_global["U0-K"] = "Up"
		keymap_global["U0-L"] = "Right"
		# 下段
		keymap_global["U0-X"] = "C-S-Tab"
		keymap_global["U0-C"] = "C-Tab"
		keymap_global["U0-N"] = "Pagedown"
		keymap_global["U0-N"] = "Pagedown"
		keymap_global["U0-M"] = "Pageup"

		# 変換をEnterに
		keymap_global["O-28"] = "Enter"
		keymap_global["O-S-28"] = "S-Enter"
		keymap_global["O-C-28"] = "C-Enter"
		keymap_global["O-A-28"] = "A-Enter"
		keymap_global["O-29"] = "29"

		# vim には無いが便利なので
		keymap_global["U0-Plus"] = "Left"
		
		# Home
		# keymap_global["U0-0"] = "Home"
		# keymap_global["U0-222"] = "Home" # 222 = ^
		# End
		# 実際は$が正しいが4の方が便利なので4にする
		# keymap_global["U0-4"] = "End"
		# keymap_global[""]

		# 単語単位移動
		# keymap_global["U0-W"] = "C-Right"
		# keymap_global["U0-B"] = "C-Left"
		
		# 下に新しい行を作って編集
		# keymap_global["U0-O"] = "End", "Enter"
		# 上に新しい行を作って編集
		# keymap_global["U0-S-O"] = "Up", "End", "Enter"
		
		# 行削除
		# vimではddだが、単純なdに割り当てる
		# keymap_global["U0-D"] = "Home", "S-End", "Delete", "Back"

