import matplotlib.pyplot as plt
import numpy as np

drop_outs_labels = ["Enrolled", "Signed-up for Moodle module", "Submitted 1st asgmt", "Submitted 2nd asgmt"]

drop_outs_traditional = [154, 150, 89, 69]

x = np.arange(len(drop_outs_labels))

width = 0.5
fig, ax = plt.subplots(figsize=(24, 16))

rects1 = ax.bar(x, drop_outs_traditional, width, label="Traditional")

ax.set_ylabel("# of Students", fontsize=56)
ax.set_xticks(x, drop_outs_labels)
ax.legend()

ax.bar_label(rects1, padding=3, fontsize=56)

fig.tight_layout()
ax.set_axisbelow(True)
ax.grid(axis='y')

plt.tick_params(labelsize=32)

# plt.savefig("dropouts_traditional.pdf", orientation="landscape", bbox_inches="tight")

plt.show()
