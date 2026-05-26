
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import sys
import os

# ─────────────────────────────────────────────
# 1. Carga de imágenes
# ─────────────────────────────────────────────
def load_image(path: str, size=None) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    if size:
        img = img.resize(size, Image.LANCZOS)
    return np.array(img, dtype=np.float32) / 255.0


def compute_ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    """SSIM multicanal sobre imágenes en [0, 1]."""
    return ssim(img1, img2, channel_axis=2, data_range=1.0)


def plot_comparison(img1: np.ndarray, img2: np.ndarray,
                    ssim_val: float,
                    path1: str, path2: str,
                    output: str = "ssim_comparison.png"):
    """
    Genera un plot de 4 columnas:
      1) Imagen 1
      2) Imagen 2
      3) Diferencia RGB amplificada (|img1 - img2| * 5)
      4) Mapa SSIM por canal (media R+G+B)
    """
    diff = np.abs(img1 - img2)
    diff_amplified = np.clip(diff * 5.0, 0, 1)   # amplificar para visibilidad

    # Mapa SSIM pixel a pixel (promedio de los 3 canales)
    _, ssim_map_r = ssim(img1[:, :, 0], img2[:, :, 0], data_range=1.0, full=True)
    _, ssim_map_g = ssim(img1[:, :, 1], img2[:, :, 1], data_range=1.0, full=True)
    _, ssim_map_b = ssim(img1[:, :, 2], img2[:, :, 2], data_range=1.0, full=True)
    ssim_map = (ssim_map_r + ssim_map_g + ssim_map_b) / 3.0

    fig = plt.figure(figsize=(18, 5))
    fig.patch.set_facecolor("white")

    gs = gridspec.GridSpec(1, 4, figure=fig, wspace=0.04,
                           left=0.02, right=0.98, top=0.80, bottom=0.02)

    panels = [
        (img1,          f"Imagen Original", None,    None),
        (img2,          f"Imagen Adversaria", None,    None),
        (diff_amplified, "Diferencia RGB\n|X – XAdv| * 5",      "hot",     None),
        (ssim_map,       "Mapa SSIM",                            "RdYlGn",  [-1, 1]),
    ]

    axes = []
    for col, (data, title, cmap, vlim) in enumerate(panels):
        ax = fig.add_subplot(gs[0, col])
        kwargs = dict(cmap=cmap, interpolation="nearest")
        if vlim:
            kwargs["vmin"], kwargs["vmax"] = vlim[0], vlim[1]
        if data.ndim == 3:
            im = ax.imshow(data, **{k: v for k, v in kwargs.items() if k not in ("cmap",)})
        else:
            im = ax.imshow(data, **kwargs)
            if cmap in ("hot", "RdYlGn"):
                plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        ax.set_title(title, fontsize=10, color="black", pad=6)
        ax.axis("off")
        axes.append(ax)

    # Título principal con SSIM global
    fig.suptitle(
        f"SSIM = {ssim_val:.6f}",
        fontsize=14, color="black", y=0.97, weight="bold"
    )

    plt.savefig(output, dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print(f"[✓] Guardado en: {output}")
    print(f"[✓] SSIM global: {ssim_val:.6f}")


# ─────────────────────────────────────────────
# 2. Punto de entrada
# ─────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso:  python ssim_compare.py imagen1.png imagen2.png [output.png]")
        sys.exit(1)

    path1 = sys.argv[1]
    path2 = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else "ssim_comparison.png"

    img1 = load_image(path1)
    img2 = load_image(path2, size=(img1.shape[1], img1.shape[0]))   # fuerza mismo tamaño

    ssim_val = compute_ssim(img1, img2)
    plot_comparison(img1, img2, ssim_val, path1, path2, output)
