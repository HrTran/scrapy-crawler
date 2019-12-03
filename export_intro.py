import json


def export_intro(NUM):
    with open("intro_" + str(NUM) + ".json", "r") as file:
        data = json.load(file)
    print("Load intro_" + str(NUM) + ".json completed!")
    output = open("data_intro_" + str(NUM) + ".txt", "w")
    data.sort(key=extract_id, reverse=False)
    for i, article in enumerate(data):
        print(article['fid'])
        # some file need encode('utf-8'), some are not
        output.write(article['desc'])
        output.write("\n")
    print("Write intro to data_intro_" + str(NUM) + ".txt completed!")


def extract_id(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(json['fid'])
    except KeyError:
        return 0


if __name__ == '__main__':
    NUM = 17
    print("Exporting intro from intro_" + str(NUM))
    export_intro(NUM)
