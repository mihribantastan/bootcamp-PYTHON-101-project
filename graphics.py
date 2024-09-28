import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasını yükleme
df = pd.read_csv('housing_filtered.csv')

# Scatter plot: Area vs Price
plt.figure(figsize=(10,6))
plt.scatter(df['area'], df['price'],
            color='purple',
            edgecolors="black",)
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price')
plt.show()

# Scatter plot: Bedrooms vs Price
plt.figure(figsize=(10,6))
plt.scatter(df['bedrooms'], df['price'],
            color='green',
            edgecolors="black",)
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.title('Bedrooms vs Price')
plt.show()

# Scatter plot: Stories vs Price
plt.figure(figsize=(10,6))
plt.scatter(df['stories'], df['price'],
            color='orange',
            edgecolors="black",)
plt.xlabel('Stories')
plt.ylabel('Price')
plt.title('Stories vs Price')
plt.show()


# Ortalama fiyat: Banyo sayısına göre
avg_price_by_bathrooms = df.groupby('bathrooms')['price'].mean()

plt.figure(figsize=(10,6))
avg_price_by_bathrooms.plot(kind='bar', color='purple', edgecolor='black')
plt.xlabel('Bathrooms')
plt.ylabel('Average Price')
plt.title('Average Price by Number of Bathrooms')
plt.show()

# Ortalama fiyat: Furnishing status'a göre
avg_price_by_furnishing = df.groupby('furnishingstatus')['price'].mean()

plt.figure(figsize=(10,6))
avg_price_by_furnishing.plot(kind='bar', color=['red', 'green', 'blue'], edgecolor='black')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.title('Average Price by Furnishing Status')
plt.xticks(rotation=0)
plt.show()

# Korelasyon matrisi hesaplama
correlation_matrix = df.corr()

# Korelasyon matrisi görselleştirme 
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Housing Data')
plt.show()

