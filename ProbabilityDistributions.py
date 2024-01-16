import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Configuración de estilo con seaborn
sns.set(style="whitegrid")

# 1. Distribución Uniforme
datos_uniforme = np.random.uniform(0, 10, 1000)

# 2. Distribución Binomial
n_binomial = 10
p_binomial = 0.5
datos_binomial = np.random.binomial(n_binomial, p_binomial, 1000)

# 3. Distribución Normal
media_normal = 0
desviacion_estandar_normal = 1
datos_normal = np.random.normal(media_normal, desviacion_estandar_normal, 1000)

# 4. Distribución Exponencial
lambda_exponencial = 0.5
datos_exponencial = np.random.exponential(1/lambda_exponencial, 1000)

# 5. Distribución de Poisson
lambda_poisson = 3
datos_poisson = np.random.poisson(lambda_poisson, 1000)

# Crear subgráficos
fig, axs = plt.subplots(2, 3)

# Graficar la Distribución Uniforme
axs[0, 0].hist(datos_uniforme, bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Distribución Uniforme')

# Graficar la Distribución Binomial
axs[0, 1].hist(datos_binomial, bins=np.arange(0, n_binomial+2)-0.5, color='skyblue', edgecolor='black')
axs[0, 1].set_title('Distribución Binomial')

# Graficar la Distribución Normal
axs[0, 2].hist(datos_normal, bins=20, color='skyblue', edgecolor='black')
axs[0, 2].set_title('Distribución Normal')

# Graficar la Distribución Exponencial
axs[1, 0].hist(datos_exponencial, bins=20, color='skyblue', edgecolor='black')
axs[1, 0].set_title('Distribución Exponencial')

# Graficar la Distribución de Poisson
axs[1, 1].hist(datos_poisson, bins=np.arange(0, 2*lambda_poisson+2)-0.5, color='skyblue', edgecolor='black')
axs[1, 1].set_title('Distribución de Poisson')

# Ajustar la disposición de los subgráficos
plt.tight_layout()
plt.show()
