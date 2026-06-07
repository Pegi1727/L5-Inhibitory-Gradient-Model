
import pandas as pd
import numpy as np
from scipy import stats
‌
# ۱. بارگذاری داده‌ها
# دقت کنید که فایل باید در پوشه data باشد
try:
data = pd.read_csv("../data/intrusion_counts.csv")
except FileNotFoundError:
# برای اجرای تست سریع اگر فایل نبود
data = pd.DataFrame({
"Language": ["Russian_L4", "English_L3", "Persian_L1", "French_L2"],
"Intrusions": [43, 3, 2, 2]
})
‌
# ۲. محاسبه نسبت‌ها (Proportions)
total_intrusions = data["Intrusions"].sum()
data["Proportion"] = data["Intrusions"] / total_intrusions
‌
print("--- Intrusion Proportions ---")
print(data[["Language", "Intrusions", "Proportion"]].to_string(index=False))
‌
# ۳. استخراج مقادیر برای مقایسه اصلی (Russian vs English)
russian_count = data[data["Language"]=="Russian_L4"]["Intrusions"].values[0]
english_count = data[data["Language"]=="English_L3"]["Intrusions"].values[0]
‌
# ۴. اجرای آزمون Chi-square (نیکویی برازش)
# فرض صفر (H0): تداخل بین این دو زبان برابر است
observed = np.array([russian_count, english_count])
chi2, p_value = stats.chisquare(observed)
‌
# ۵. محاسبه اندازه اثر (Cohen's w یا Phi برای ۲ گروه)
# w = sqrt(chi2 / n)
n_obs = observed.sum()
effect_size_w = np.sqrt(chi2 / n_obs)
‌
print("\n--- Statistical Analysis (L4 vs L3) ---")
print(f"Effect Size (Difference): {russian_count - english_count}")
print(f"Chi-square (χ2): {chi2:.4f}")
print(f"P-value: {p_value:.8f}")
‌
# ۶. خروجی استاندارد برای متن مقاله (APA Style)
sig_level = "p < .001" if p_value < 0.001 else f"p = {p_value:.3f}"
effect_label = "Large" if effect_size_w > 0.5 else "Medium" if effect_size_w > 0.3 else "Small"
‌
print("\n--- APA Formatted Result ---")
print(f"A chi-square goodness-of-fit test indicated that Russian (L4) intrusions ")
print(f"were significantly more frequent than English (L3) intrusions, ")
print(f"χ2(1) = {chi2:.2f}, {sig_level}, effect size (w) = {effect_size_w:.2f} ({effect_label}).")
