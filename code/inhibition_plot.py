
import matplotlib.pyplot as plt
import numpy as np
‌
# تنظیمات ظاهری برای استایل علمی
plt.style.use('seaborn-v0_8-whitegrid')
‌
# داده‌ها
languages = ["L1\n(Azerbaijani)",
"L2\n(Persian)",
"L3\n(English)\nDominant",
"L4\n(Russian)\nDeveloping",
"L5\n(Spanish)\nTarget"]
‌
# مقادیر پایداری بازداری (فرضی بر اساس مدل شما)
stability = [0.95, 0.9, 0.85, 0.4, 0.1]
x = np.arange(len(languages))
‌
fig, ax = plt.subplots(figsize=(10, 6))
‌
# رسم خط اصلی گرادیان
ax.plot(x, stability, marker='o', color='#2c3e50', linewidth=3, label='Inhibitory Stability')
‌
# برجسته کردن نقطه L4 (روسی) که دچار افت پایداری شده
ax.scatter(3, stability[3], s=300, color='#e74c3c', edgecolors='black', zorder=5, label='Inhibitory Instability (L4)')
‌
# برجسته کردن L3 برای مقایسه
ax.scatter(2, stability[2], s=200, color='#27ae60', edgecolors='black', zorder=5, label='High Entrenchment (L3)')
‌
# اضافه کردن جزئیات نمودار
ax.set_title("The Inhibitory Gradient Across Multilingual Acquisition", fontsize=14, fontweight='bold')
ax.set_ylabel("Inhibitory Stability / Control Efficiency", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(languages)
ax.set_ylim(0, 1.1)
‌
# اضافه کردن فلش برای نشان دادن "پارادوکس"
ax.annotate('The Paradox:\nEasier to suppress', xy=(2, 0.85), xytext=(1.5, 0.6),
arrowprops=dict(facecolor='black', shrink=0.05, width=1))
‌
ax.legend()
plt.tight_layout()
‌
# ذخیره نمودار
plt.savefig('../plots/inhibitory_gradient_plot.png', dpi=300)
print("Graph generated: plots/inhibitory_gradient_plot.png")
plt.show()
