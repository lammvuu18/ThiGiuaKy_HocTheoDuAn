def chuan_hoa_ma_san_pham(ma):
    """Xóa khoảng trắng thừa và viết hoa tất cả ký tự."""
    return ma.strip().upper()


def sap_xep_giam_dan(danh_sach):
    """Sắp xếp danh sách theo thứ tự giảm dần của bảng chữ cái."""
    return sorted(danh_sach, reverse=True)


def hien_thi_danh_sach(tieu_de, danh_sach):
    """In danh sách mã sản phẩm theo định dạng bảng."""
    print(f"\n{tieu_de}")
    print("-" * 30)
    for i, ma in enumerate(danh_sach, 1):
        print(f"  {i}. {ma}")
    print("-" * 30)


def main():
    # Danh sách mã sản phẩm nhập sai quy cách
    ma_san_pham = [" sp-001 ", "SP-002 ", " sP-003", "  sp-005  ", "Sp-004"]

    print("=== CHUẨN HÓA MÃ SẢN PHẨM ===")

    # Hiển thị danh sách gốc
    hien_thi_danh_sach("Danh sách GỐC (chưa chuẩn hóa):", ma_san_pham)

    # Chuẩn hóa từng mã sản phẩm
    da_chuan_hoa = [chuan_hoa_ma_san_pham(ma) for ma in ma_san_pham]

    # Hiển thị sau khi chuẩn hóa
    hien_thi_danh_sach("Danh sách sau khi CHUẨN HÓA:", da_chuan_hoa)

    # Sắp xếp giảm dần
    da_sap_xep = sap_xep_giam_dan(da_chuan_hoa)

    # Hiển thị sau khi sắp xếp
    hien_thi_danh_sach("Danh sách sau khi SẮP XẾP GIẢM DẦN:", da_sap_xep)


if __name__ == "__main__":
    main()