import random


def chon_ngau_nhien_may():
    """Máy chọn ngẫu nhiên một trong ba lựa chọn."""
    lua_chon = ["Kéo", "Búa", "Bao"]
    return random.choice(lua_chon)


def xac_dinh_ket_qua(nguoi, may):
    """Xác định kết quả một hiệp: Thắng, Thua hoặc Hòa."""
    if nguoi == may:
        return "Hòa"
    thang = {
        "Búa": "Kéo",
        "Kéo": "Bao",
        "Bao": "Búa"
    }
    if thang[nguoi] == may:
        return "Thắng"
    return "Thua"


def hien_thi_ket_qua_hiep(hiep, tong_hiep, nguoi, may, ket_qua):
    """In kết quả sau mỗi hiệp."""
    print(f"\n  Người chơi : {nguoi}")
    print(f"  Máy chọn   : {may}")
    print(f"  Kết quả    : {ket_qua}!")


def hien_thi_tong_ket(thang, thua, hoa, tong_hiep):
    """In bảng tổng kết sau khi kết thúc tất cả các hiệp."""
    print("\n" + "="*40)
    print("           TONG KET TRAN DAU")
    print("="*40)
    print(f"  {'Tong so hiep':<20}: {tong_hiep}")
    print(f"  {'Thang':<20}: {thang}")
    print(f"  {'Thua':<20}: {thua}")
    print(f"  {'Hoa':<20}: {hoa}")
    print("-"*40)

    if thang > thua:
        print("  Chuc mung! Ban THANG toan tran!")
    elif thua > thang:
        print("  Rat tiec! May THANG toan tran!")
    else:
        print("  Tran dau ket thuc HOA!")
    print("="*40)


def luu_ket_qua(thang, thua, hoa, tong_hiep, lich_su):
    """Lưu tổng kết và lịch sử từng hiệp vào file."""
    with open("ket_qua_game.txt", "w", encoding="utf-8") as f:
        f.write("="*40 + "\n")
        f.write("        TONG KET TRAN DAU\n")
        f.write("="*40 + "\n")
        f.write(f"  {'Tong so hiep':<20}: {tong_hiep}\n")
        f.write(f"  {'Thang':<20}: {thang}\n")
        f.write(f"  {'Thua':<20}: {thua}\n")
        f.write(f"  {'Hoa':<20}: {hoa}\n")
        f.write("-"*40 + "\n")

        if thang > thua:
            f.write("  Ket qua: Nguoi choi THANG toan tran!\n")
        elif thua > thang:
            f.write("  Ket qua: May THANG toan tran!\n")
        else:
            f.write("  Ket qua: Tran dau ket thuc HOA!\n")

        f.write("\n" + "="*40 + "\n")
        f.write("          LICH SU TUNG HIEP\n")
        f.write("="*40 + "\n")
        f.write(f"  {'Hiep':<6} {'Nguoi':<10} {'May':<10} {'Ket qua'}\n")
        f.write("-"*40 + "\n")
        for h in lich_su:
            f.write(f"  {h['hiep']:<6} {h['nguoi']:<10} {h['may']:<10} {h['ket_qua']}\n")
        f.write("="*40 + "\n")

    print("\nDa luu tong ket vao file 'ket_qua_game.txt'")


def nhap_so_hiep():
    """Nhập số hiệp muốn chơi với kiểm tra lỗi."""
    while True:
        try:
            so_hiep = int(input("Nhap so hiep muon choi: "))
            if so_hiep <= 0:
                print("So hiep phai lon hon 0. Vui long nhap lai.")
            else:
                return so_hiep
        except ValueError:
            print("Vui long nhap so nguyen hop le.")


def nhap_lua_chon():
    """Nhập lựa chọn của người chơi với kiểm tra lỗi."""
    bang_chon = {"1": "Kéo", "2": "Búa", "3": "Bao"}
    while True:
        print("  [1] Keo  [2] Bua  [3] Bao")
        lua_chon = input("  Lua chon cua ban: ").strip()
        if lua_chon in bang_chon:
            return bang_chon[lua_chon]
        print("  Vui long nhap 1, 2 hoac 3.")


def main():
    print("="*40)
    print("       TRO CHOI KEO - BUA - BAO")
    print("="*40)

    tong_hiep = nhap_so_hiep()

    thang = thua = hoa = 0
    lich_su = []

    for hiep in range(1, tong_hiep + 1):
        print(f"\n{'─'*40}")
        print(f"  HIEP {hiep}/{tong_hiep}")
        print(f"{'─'*40}")

        nguoi = nhap_lua_chon()
        may   = chon_ngau_nhien_may()

        ket_qua = xac_dinh_ket_qua(nguoi, may)

        if ket_qua == "Thắng":
            thang += 1
        elif ket_qua == "Thua":
            thua += 1
        else:
            hoa += 1

        hien_thi_ket_qua_hiep(hiep, tong_hiep, nguoi, may, ket_qua)

        lich_su.append({"hiep": hiep, "nguoi": nguoi, "may": may, "ket_qua": ket_qua})

        print(f"\n  Ti so: Thang {thang} - Thua {thua} - Hoa {hoa}")

    hien_thi_tong_ket(thang, thua, hoa, tong_hiep)
    luu_ket_qua(thang, thua, hoa, tong_hiep, lich_su)


if __name__ == "__main__":
    main()