import pandas as pd
import matplotlib.pyplot as plt

# ── Load dataset ──────────────────────────────────────────────
df = pd.read_csv("datos/global_temp.csv")

# Use only GCAG source for consistency
df_gcag = df[df["Source"] == "GCAG"].copy()
df_gcag = df_gcag.sort_values("Year").reset_index(drop=True)

# ── Calculate indicators ──────────────────────────────────────
temp_mean = df_gcag["Mean"].mean()
temp_max = df_gcag["Mean"].max()
temp_min = df_gcag["Mean"].min()
year_max = df_gcag.loc[df_gcag["Mean"].idxmax(), "Year"]
year_min = df_gcag.loc[df_gcag["Mean"].idxmin(), "Year"]

print("=" * 45)
print("   ANÁLISIS DE TEMPERATURA GLOBAL (GCAG)")
print("=" * 45)
print(f"  Anomalía promedio histórica : {temp_mean:.4f} °C")
print(f"  Anomalía máxima             : {temp_max:.4f} °C (año {year_max})")
print(f"  Anomalía mínima             : {temp_min:.4f} °C (año {year_min})")
print("=" * 45)

# ── Generate chart ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))

colors = ["crimson" if v >= 0 else "steelblue" for v in df_gcag["Mean"]]
ax.bar(df_gcag["Year"], df_gcag["Mean"], color=colors, width=0.8, alpha=0.85)

ax.axhline(0, color="black", linewidth=0.8, linestyle="--")

df_gcag["MA20"] = df_gcag["Mean"].rolling(window=20).mean()
ax.plot(df_gcag["Year"], df_gcag["MA20"], color="orange",
        linewidth=2, label="Media móvil (20 años)")

ax.set_title("Anomalía de Temperatura Global (1850–2024)", fontsize=14, fontweight="bold")
ax.set_xlabel("Año", fontsize=11)
ax.set_ylabel("Anomalía de Temperatura (°C)", fontsize=11)
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png", dpi=150)
plt.show()
print("Gráfico guardado en /resultados/grafico_temperatura.png")
