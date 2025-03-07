from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while(1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÍ SINH VIÊN")
    print("****************************************MENU****************************************")
    print("****** 1. Thêm sinh viên                                      **********************")
    print("****** 2. Cập nhật thông tin sinh viên                        **********************")
    print("****** 3. Xóa sinh viên bởi ID                                **********************")
    print("****** 4. Tìm kiếm sinh viên theo tên                         **********************")
    print("****** 5. Sắp xếp sinh viên theo điểm trung bình              **********************")
    print("****** 6. Săp xếp sinh viên theo điểm chuyên ngành            **********************")
    print("****** 7. Hiển thị danh sách sinh viên                        **********************")
    print("****** 0. Thoát                                               **********************")
    
    key = int(input("Nhập tùy chọn: "))
    if(key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công")
        
    elif (key == 2):
        if(qlsv.soLuongSinhVien()):
            print("\n2. Cập nhật thông tin sinh viên")
            print("\nNhập ID: ")
            ID = input ()
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            if(qlsv.deleteByID(ID)):
                print("\nSinh viên có ID = ", ID, " đã bị xóa")
            else:
                print("\nSinh viên có ID = ", ID, " không tồn tại")
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên. ")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Tìm kiếm sinh viên theo tên. ")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên. ")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien)
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống !!!")
    elif(key == 0):
        print("Bạn đã thoát chương trình !!!")
        break
    else:
        print("\nKhông có chức năng này !!!")
        print("\nXin mời bạn chọn lại chức năng khác trong menu")