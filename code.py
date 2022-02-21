import pprint
import sys

def find_score(photo1, photo2):
    common_el = len(list(set(photo1["tags"]).intersection(photo2["tags"])))
    return min(common_el, abs(len(photo1["tags"]) - common_el),abs(len(photo2["tags"]) - common_el))

def find_common(photo1, photo2):
    return list(set(photo1["tags"]).union(photo2["tags"]))

def read_file(file):
    photos = []
    with open(file,"r") as file:
        lines = file.readlines()
        N = int(lines[0])
        i = 0
        for line in lines[1:]:
            data = line.split()
            photo = {'num':str(i),'orient':data[0],'num_tags':data[1],'tags':data[2:]}
            photos.append(photo)
            i += 1
    return photos

def nsqrt(slides):
    cur_slide = slides[0]
    while (len(slides) > 0):
        max_score = -1
        slides.remove(cur_slide)
        for slide in slides:
            score = find_score(slide, cur_slide)
            if score > max_score:
                max_score = score
                max_slide = slide

            if max_score > 1:
                break

        print(cur_slide["num"])
        cur_slide = max_slide
    if (len(slides) > 0):
        print(slides[0]["num"])

if __name__=="__main__":
    file = sys.argv[1]
    photos = read_file(file)
    slides = []
    slides_vertical = []
    for photo in photos:
        if photo['orient']=='H':
            slides.append(photo)
        else:
            slides_vertical.append(photo)
    num_vertical = len(slides_vertical)
    for i in range(int(num_vertical/2)):
        photo1 = slides_vertical[i]
        photo2 = slides_vertical[int(num_vertical/2) + i]
        tags = find_common(photo1, photo2)
        new_slide = {'num':photo1['num']+' '+photo2['num'],
                     'orient':'V',
                     'num_tags':len(tags),
                     'tags':tags}
        slides.append(new_slide)

    nsqrt(slides)

