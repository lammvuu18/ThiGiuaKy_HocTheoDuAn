def tinh_tien_dien(kwh):
    """Tính tiền điện theo bậc thang."""
    tien = 0

    if kwh <= 50:
        tien = kwh * 1_600
    elif kwh <= 100:
        tien = (50 * 1_600) + ((kwh - 50) * 2_000)
    else:
        tien = (50 * 1_600) + (50 * 2_000) + ((kwh - 100) * 2_500)

    return tien


def hien_thi_chi_tiet(kwh, tien):
    """Hiển thị bảng chi tiết tiền điện theo từng bậc."""
    print("\n" + "="*45)
    print("        HÓA ĐƠN TIỀN ĐIỆN THÁNG NÀY")
    print("="*45)
    print(f"  Tổng số điện tiêu thụ : {kwh} kWh")
    print("-"*45)
    print(f"  {'Bậc':<20} {'kWh':>6} {'Đơn giá':>10} {'Thành tiền':>12}")
    print("-"*45)

    bac_1_kwh = min(kwh, 50)
    bac_1_tien = bac_1_kwh * 1_600
    print(f"  {'Bậc 1 (≤ 50 kWh)':<20} {bac_1_kwh:>6} {'1.600đ':>10} {bac_1_tien:>11,}đ")

    if kwh > 50:
        bac_2_kwh = min(kwh - 50, 50)
        bac_2_tien = bac_2_kwh * 2_000
        print(f"  {'Bậc 2 (51-100 kWh)':<20} {bac_2_kwh:>6} {'2.000đ':>10} {bac_2_tien:>11,}đ")

    if kwh > 100:
        bac_3_kwh = kwh - 100
        bac_3_tien = bac_3_kwh * 2_500
        print(f"  {'Bậc 3 (> 100 kWh)':<20} {bac_3_kwh:>6} {'2.500đ':>10} {bac_3_tien:>11,}đ")

    print("-"*45)
    print(f"  {'TỔNG CỘNG':<20} {kwh:>6} {'':>10} {tien:>11,}đ")
    print("="*45)


def nhap_kwh():
    """Nhập số kWh với xử lý lỗi, cho phép nhập lại nếu sai."""
    while True:
        try:
            kwh_str = input("\nNhập số điện tiêu thụ trong tháng (kWh): ").strip()

            if kwh_str == "":
                raise ValueError("Không được để trống.")

            kwh = float(kwh_str)

            if kwh < 0:
                raise ValueError("Số kWh không được âm.")

            if kwh != int(kwh):
                raise ValueError("Số kWh phải là số nguyên, không có phần thập phân.")

            return int(kwh)

        except ValueError as e:
            # Phân biệt lỗi do nhập chữ hay lỗi do điều kiện tự đặt ra
            if "could not convert" in str(e) or "invalid literal" in str(e):
                print("Lỗi: Vui lòng nhập số, không nhập chữ hoặc ký tự đặc biệt.")
            else:
                print(f"Lỗi: {e}")
            print("   Vui lòng nhập lại.")


def main():
    print("="*45)
    print("      MÁY TÍNH TIỀN ĐIỆN HÀNG THÁNG")
    print("="*45)

    while True:
        # Nhập số kWh (có xử lý lỗi)
        kwh = nhap_kwh()

        # Tính tiền
        tien = tinh_tien_dien(kwh)

        # Hiển thị hóa đơn chi tiết
        hien_thi_chi_tiet(kwh, tien)

        # Hỏi có muốn tính tiếp không
        print()
        while True:
            tiep = input("Bạn có muốn tính cho tháng khác không? (y/n): ").strip().lower()
            if tiep in ("y", "n"):
                break
            print("Vui lòng nhập 'y' (có) hoặc 'n' (không).")

        if tiep == "n":
            print("\nCảm ơn bạn đã sử dụng máy tính tiền điện!")
            break


if __name__ == "__main__":
    main()