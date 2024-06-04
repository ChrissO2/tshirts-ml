import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('t-shirts.csv')
sns.set(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 18))

sns.countplot(data=data, x='size', ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Rozkład rozmiarów')

sns.countplot(data=data, x='material', ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Rozkład materiałów')

sns.countplot(data=data, x='color', ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Rozkład kolorów')
axes[1, 0].tick_params(axis='x', rotation=90)

sns.countplot(data=data, x='sleeves', ax=axes[1, 1], palette='viridis')
axes[1, 1].set_title('Rozkład długości rękawów')

sns.countplot(data=data, x='demand', ax=axes[2, 0], palette='viridis')
axes[2, 0].set_title('Rozkład zapotrzebowania')

# Usunięcie pustego wykresu
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()

# Heatmapy do analizy współzależności między cechami a zapotrzebowaniem
fig, axes = plt.subplots(3, 2, figsize=(14, 18))

size_demand = pd.crosstab(data['size'], data['demand'])
sns.heatmap(size_demand, annot=True, fmt="d", cmap='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Rozkład zapotrzebowania według rozmiarów')

material_demand = pd.crosstab(data['material'], data['demand'])
sns.heatmap(material_demand, annot=True, fmt="d",
            cmap='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Rozkład zapotrzebowania według materiałów')

color_demand = pd.crosstab(data['color'], data['demand'])
sns.heatmap(color_demand, annot=True, fmt="d", cmap='viridis', ax=axes[1, 0])
axes[1, 0].set_title('Rozkład zapotrzebowania według kolorów')
axes[1, 0].tick_params(axis='x', rotation=90)

sleeves_demand = pd.crosstab(data['sleeves'], data['demand'])
sns.heatmap(sleeves_demand, annot=True, fmt="d", cmap='viridis', ax=axes[1, 1])
axes[1, 1].set_title('Rozkład zapotrzebowania według długości rękawów')

# Usunięcie pustych wykresów
axes[2, 0].axis('off')
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()
