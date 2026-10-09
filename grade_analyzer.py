

japanese = {
	"漢字":80,
	"文法":50,
	"読解":70
}

math = {
	"方程式": 65,
	"関数": 90,
    "図形": 75
}

all_subjects = {
	"国語": japanese,
	"数学": math
}


def find_dislike(pointgroup,subject_name):
	average = sum(pointgroup.values())/ len(pointgroup.values())
	
	print(f"【{subject_name}】")
	print(f"平均点({average:.1f}点)")

	dislike = []
	
	for subject,score in pointgroup.items():
		if score < average:
			dislike.append((subject,score))
		
	if dislike:
		print("平均点より低い範囲")
		for subject,score in dislike:
			print(f"{subject}({score}点)")
		
	else:
		print("平均点より低い範囲はありません。")



for subject_name, pointgroup in all_subjects.items():
	find_dislike(pointgroup,subject_name)