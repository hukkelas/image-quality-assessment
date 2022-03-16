import json
import numpy as np
import cv2
with open("result.json") as fp:
    data = json.load(fp)

data = {item["image_id"]: item["mean_score_prediction"] for item in data}
impaths = list(data.keys())
impaths.sort(key=lambda k: data[k])
n = 20
top10 = impaths[:n]
bot10 = impaths[-n:]
print([data[k] for k in top10])
print([data[k] for k in bot10])


def imread(p):
    im = cv2.imread(f"images/{p}.png")
    print(f"images/{p}.png")
    return cv2.resize(im, (224, 224))

top10 = np.concatenate([imread(p) for p in top10], 1)
bot10 = np.concatenate([imread(p) for p in bot10], 1)
ims = np.concatenate((top10, bot10))
cv2.imshow("frame", ims)
cv2.waitKey(0)

