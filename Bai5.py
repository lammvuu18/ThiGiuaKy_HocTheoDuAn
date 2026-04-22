import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Dữ liệu lượng mưa quý 1
luong_mua = {
    'Thang 1': 45.5,
    'Thang 2': 112.0,
    'Thang 3': 89.5
}


def phan_tich_luong_mua(data):
    """Tính tổng lượng mưa và tìm tháng có lượng mưa ít nhất."""
    tong = sum(data.values())
    thang_it_nhat = min(data, key=data.get)
    thang_nhieu_nhat = max(data, key=data.get)
    trung_binh = tong / len(data)
    return tong, trung_binh, thang_it_nhat, thang_nhieu_nhat


def hien_thi_phan_tich(data, tong, trung_binh, thang_it_nhat, thang_nhieu_nhat):
    """In bảng phân tích lượng mưa ra màn hình."""
    print("="*45)
    print("       PHAN TICH LUONG MUA QUY 1")
    print("="*45)
    print(f"  {'Thang':<15} {'Luong mua (mm)':>15}")
    print("-"*45)
    for thang, mm in data.items():
        print(f"  {thang:<15} {mm:>14.1f}")
    print("-"*45)
    print(f"  {'Tong cong':<15} {tong:>14.1f}")
    print(f"  {'Trung binh':<15} {trung_binh:>14.1f}")
    print("="*45)
    print(f"  Thang mua it nhat  : {thang_it_nhat} ({data[thang_it_nhat]:.1f} mm)")
    print(f"  Thang mua nhieu nhat: {thang_nhieu_nhat} ({data[thang_nhieu_nhat]:.1f} mm)")
    print("="*45)


def ve_bieu_do(data, trung_binh):
    """Vẽ biểu đồ đường thể hiện sự biến động lượng mưa."""
    thang = list(data.keys())
    mm    = list(data.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    # Vẽ đường chính
    ax.plot(thang, mm,
            color="#1a73e8",
            linewidth=2.5,
            marker="o",
            markersize=8,
            markerfacecolor="white",
            markeredgewidth=2.5,
            markeredgecolor="#1a73e8",
            label="Luong mua (mm)")

    # Đường trung bình
    ax.axhline(y=trung_binh,
               color="#e53935",
               linewidth=1.5,
               linestyle="--",
               label=f"Trung binh ({trung_binh:.1f} mm)")

    #màu dưới đường
    ax.fill_between(thang, mm, alpha=0.1, color="#1a73e8")

    # Gắn nhãn giá trị lên từng điểm
    for i, (t, m) in enumerate(zip(thang, mm)):
        ax.annotate(f"{m:.1f} mm",
                    xy=(t, m),
                    xytext=(0, 12),
                    textcoords="offset points",
                    ha="center",
                    fontsize=10,
                    color="#1a73e8",
                    fontweight="bold")

    # Định dạng trục và tiêu đề
    ax.set_title("Bieu do luong mua Quy 1", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Thang", fontsize=11)
    ax.set_ylabel("Luong mua (mm)", fontsize=11)
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.set_ylim(0, max(mm) * 1.25)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.3)
    ax.legend(fontsize=10)

    plt.tight_layout()
    plt.show()


def main():
    tong, trung_binh, thang_it_nhat, thang_nhieu_nhat = phan_tich_luong_mua(luong_mua)
    hien_thi_phan_tich(luong_mua, tong, trung_binh, thang_it_nhat, thang_nhieu_nhat)
    ve_bieu_do(luong_mua, trung_binh)


if __name__ == "__main__":
    main()