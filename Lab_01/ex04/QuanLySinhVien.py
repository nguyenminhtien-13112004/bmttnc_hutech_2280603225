from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []
    
    def generateID(self):
        """Tạo ID tự động cho sinh viên mới"""
        if self.soLuongSinhVien() == 0:
            return 1
        return max(sv._id for sv in self.listSinhVien) + 1
    
    def soLuongSinhVien(self):
        """Trả về số lượng sinh viên"""
        return len(self.listSinhVien)
    
    def nhapSinhVien(self):
        """Nhập thông tin sinh viên mới"""
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, ID):
        """Cập nhật thông tin sinh viên theo ID"""
        sv = self.findByID(ID)
        if sv is not None:
            sv._name = input("Nhập tên mới: ")
            sv._sex = input("Nhập giới tính mới: ")
            sv._major = input("Nhập chuyên ngành mới: ")
            sv._diemTB = float(input("Nhập điểm mới: "))
            self.xepLoaiHocLuc(sv)
            print(f"✅ Cập nhật sinh viên {ID} thành công!")
        else:
            print(f"❌ Sinh viên có ID = {ID} không tồn tại.")
    
    def sortByID(self):
        """Sắp xếp danh sách theo ID"""
        self.listSinhVien.sort(key=lambda x: x._id)
    
    def sortByName(self):
        """Sắp xếp danh sách theo tên"""
        self.listSinhVien.sort(key=lambda x: x._name.lower())
    
    def sortByDiemTB(self):
        """Sắp xếp danh sách theo điểm trung bình"""
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)
    
    def findByID(self, ID):
        """Tìm sinh viên theo ID"""
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None
    
    def findByName(self, keyword):
        """Tìm sinh viên theo tên"""
        return [sv for sv in self.listSinhVien if keyword.lower() in sv._name.lower()]
    
    def deleteByID(self, ID):
        """Xóa sinh viên theo ID"""
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            print(f"✅ Sinh viên có ID = {ID} đã bị xóa!")
            return True
        print(f"❌ Không tìm thấy sinh viên có ID = {ID}.")
        return False
    
    def xepLoaiHocLuc(self, sv):
        """Xếp loại học lực dựa trên điểm trung bình"""
        if sv._diemTB >= 8:
            sv._hocluc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocluc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung bình"
        else:
            sv._hocluc = "Yếu"
    
    def showSinhVien(self, listSV=None):
        """Hiển thị danh sách sinh viên"""
        if listSV is None:
            listSV = self.listSinhVien
        
        if len(listSV) == 0:
            print("❌ Không có sinh viên nào trong danh sách.")
            return
        
        print("{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        print("-" * 75)
        
        for sv in listSV:
            print("{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        
        print("\n")
    
    def getListSinhVien(self):
        """Trả về danh sách sinh viên"""
        return self.listSinhVien