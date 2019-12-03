import json

NUM = 16

list_crawled = []
with open("intro_" + str(NUM) + ".json","r") as intro:
    data_intro = json.load(intro)
print("Load json_" + str(NUM) + ".json completed!")

for i,article in enumerate(data_intro):
	list_crawled.append(article['fid'])
print("Loading id of articles from json_" + str(NUM) + ".json")

list_id = []
url = open("url_" + str(NUM) + ".txt","r")
lines = url.read().split('\n')
for line in lines:
	item = line.split(" ")
	list_id.append(item[0])
print("Loading id of articles from url_" + str(NUM) + ".txt")
url.close()

missing_link = open("missing_" + str(NUM) + ".txt","w")
diff = list(set(list_id) - set(list_crawled))
print("Different in two list:")
print(diff)
for fid in diff:
	check_fid = fid + ' '
	for line in lines:
		if check_fid in line and fid != "":
			print(check_fid + " - " + line)
			missing_link.write(line  + "\n")
missing_link.close()
