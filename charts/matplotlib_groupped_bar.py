import matplotlib.pyplot as plt
import numpy as np

drop_outs_labels = ["Enrolled", "Signed-up for moodle module", "Submitted 1st asgmt", "Submitted 2nd asgmt"]
drop_outs_traditional_2018_2 = [56, 55, 28, 16]
drop_outs_traditional_2019_1 = [57, 54, 37, 29]
drop_outs_traditional_2019_2 = [41, 41, 24, 24]
drop_outs_traditional = [154, 150, 89, 69]

x = np.arange(len(drop_outs_labels))

width = 0.18
fig, ax = plt.subplots()

rects1 = ax.bar(x - (width * 1.5), drop_outs_traditional_2018_2, width, label="2018/2")
rects2 = ax.bar(x - (width / 2), drop_outs_traditional_2019_1, width, label="2019/1")
rects3 = ax.bar(x + (width / 2), drop_outs_traditional_2019_2, width, label="2019/2")
rects4 = ax.bar(x + (width * 1.5), drop_outs_traditional, width, label="Total")

ax.set_ylabel("Students/Assignments")
ax.set_xticks(x, drop_outs_labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()