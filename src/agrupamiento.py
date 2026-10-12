"""Agrupamiento exploratorio de estaciones del Metro de Madrid con K-Means.

Los nombres de estaciones son referencias conocidas; las variables numéricas del
CSV son simuladas y no representan estadísticas oficiales de Metro de Madrid.
Ejecutar desde la raíz del repositorio: python src/agrupamiento.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "datos" / "estaciones_metro.csv"
RESULTS_DIR = ROOT / "resultados"
FEATURES = ["lineas", "conexiones", "afluencia"]


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    datos = pd.read_csv(DATA_FILE)

    required = {"estacion", *FEATURES}
    missing = required.difference(datos.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")
    if datos.empty:
        raise ValueError("El dataset no contiene estaciones.")
    if datos[FEATURES].isnull().any().any():
        raise ValueError("Hay valores vacíos en las variables numéricas.")

    escalador = StandardScaler()
    datos_escalados = escalador.fit_transform(datos[FEATURES])

    modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
    datos["grupo"] = modelo.fit_predict(datos_escalados)

    print("\nAGRUPAMIENTO DE ESTACIONES DEL METRO DE MADRID")
    print("(Variables numéricas simuladas para fines académicos)\n")
    print(datos[["estacion", "grupo"]].to_string(index=False))
    print(f"\nEstaciones analizadas: {len(datos)}")
    print(f"Grupos generados: {datos['grupo'].nunique()}")
    print(f"Inercia del modelo: {modelo.inertia_:.3f}")

    resumen = datos.groupby("grupo")[FEATURES].mean().round(2)
    print("\nPromedio de variables por grupo:")
    print(resumen.to_string())

    # Gráfico de dos variables para visualizar los grupos.
    plt.figure(figsize=(11, 7))
    for grupo in sorted(datos["grupo"].unique()):
        subset = datos[datos["grupo"] == grupo]
        plt.scatter(subset["lineas"], subset["afluencia"],
                    label=f"Grupo {grupo}", s=90)
        for _, fila in subset.iterrows():
            plt.annotate(fila["estacion"],
                         (fila["lineas"], fila["afluencia"]),
                         xytext=(5, 4), textcoords="offset points",
                         fontsize=8)

    plt.xlabel("Cantidad de líneas (dato simulado)")
    plt.ylabel("Índice simulado de afluencia (1-100)")
    plt.title("Agrupamiento K-Means de estaciones (datos simulados)")
    plt.legend()
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "agrupamiento.png", dpi=160)
    plt.close()

    # Guardar las asignaciones para facilitar la revisión.
    datos.to_csv(RESULTS_DIR / "estaciones_agrupadas.csv", index=False)
    print(f"\nResultados guardados en: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
