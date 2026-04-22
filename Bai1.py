def main():
    students = []
    
    while True:
        name = input("Nhập tên sinh viên (0 để dừng): ").strip()
        if name == "0":
            break
        if not name:
            print("Tên không được để trống. Vui lòng nhập lại.")
            continue
        
        while True:
            try:
                score = float(input(f"Nhập điểm của {name} (0 - 10): "))
                if 0 <= score <= 10:
                    break
                else:
                    print("Điểm phải nằm trong khoảng 0-10. Vui lòng nhập lại.")
            except ValueError:
                print("Điểm không hợp lệ. Vui lòng nhập số.")
        
        students.append({"name": name, "score": score})
        print(f"Đã thêm: {name} - {score:.1f}\n")
    
    if not students:
        print("Không có sinh viên nào được nhập.")
        return
    
    #Tính điểm TB 
    avg_score = sum(s["score"] for s in students) / len(students)
    
    #Tìm sv điểm cao nhất
    max_score = max(s["score"] for s in students)
    top_students = [s for s in students if s["score"] == max_score]
    
    #In
    print("\n" + "="*40)
    print("DANH SÁCH ĐIỂM THI")
    print("="*40)
    print(f"{'STT':<5} {'Tên sinh viên':<25} {'Điểm':>5}")
    print("-"*40)
    for i, s in enumerate(students, 1):
        print(f"{i:<5} {s['name']:<25} {s['score']:>5.1f}")
    print("-"*40)
    print(f"\nĐiểm trung bình cả lớp : {avg_score:.2f}")
    
    #sv điểm cao nhất
    if len(top_students) == 1:
        print(f"Sinh viên điểm cao nhất: {top_students[0]['name']} ({max_score:.1f})")
    else:
        print(f"Các sinh viên cùng điểm cao nhất ({max_score:.1f}):")
        for s in top_students:
            print(f"   - {s['name']}")
    
    #Hỏi có muốn xuất file ko
    print()
    while True:
        choice = input("Bạn có muốn xuất danh sách ra file 'diem_thi.txt' không? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            break
        print("Vui lòng nhập 'y' (có) hoặc 'n' (không).")

    if choice == "y":
        with open("diem_thi.txt", "w", encoding="utf-8") as f:
            f.write("="*40 + "\n")
            f.write("DANH SÁCH ĐIỂM THI CỦA CÁC SINH VIÊN\n")
            f.write("="*40 + "\n")
            f.write(f"{'STT':<5} {'Tên sinh viên':<25} {'Điểm':>5}\n")
            f.write("-"*40 + "\n")
            for i, s in enumerate(students, 1):
                f.write(f"{i:<5} {s['name']:<25} {s['score']:>5.1f}\n")
            f.write("-"*40 + "\n")
            f.write(f"\nĐiểm trung bình cả lớp : {avg_score:.2f}\n")
            f.write(f"Sinh viên điểm cao nhất: {top_students['name']} ({top_students['score']:.1f})\n")
        print("Đã xuất danh sách ra file 'diem_thi.txt'")
    else:
        print("Bỏ qua xuất file.")

if __name__ == "__main__":
    main()