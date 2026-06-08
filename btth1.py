# Hệ Thống Quản Lý Kho Hàng & Doanh Thu (TechStore Inventory)
inventory_stock = 100
total_revenue = 0.0

menu = """
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
"""

def add_stock(amount):
    global inventory_stock
    print(f"Đã nhập thành công {amount} sản phẩm.")
    inventory_stock += amount
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")
    else:
        return 0

def calculate_final_price(quantity, price):
    global inventory_stock, total_revenue
    discount = 0
    # Khi kho đã xác nhận đủ hàng, hệ thống mới gọi hàm tính toán chi phí (Ví dụ tên hàm: calculate_final_price(quantity, price)):
    # - Tính tổng tiền tạm tính = quantity * price.
    total_temp = quantity * price # 10 * 150 = 1500
    # - Nếu tổng tiền ≥ 1000, giảm giá 10% (Tạo biến cục bộ discount trong hàm).
    if total_temp >= 1000:
        discount = total_temp * 0.1
    # - Cộng thêm 8% thuế VAT vào tổng tiền sau giảm giá.
        vat = (total_temp - discount) * 0.08
    # - return giá trị tổng tiền cuối cùng (final_total).
    final_total = total_temp - discount + vat

    # Hoàn tất giao dịch (Trừ kho và ghi nhận doanh thu):
    # - Trừ đi số lượng bán trong inventory_stock.
    inventory_stock -= quantity
    # - Cộng final_total vào tổng doanh thu toàn cục (total_revenue).
    total_revenue += final_total
    # - In hóa đơn thành công ra màn hình cho khách hàng.
    bill = f"""
-> Hóa đơn chi tiết:
Số lượng: {quantity} | Đơn giá: ${price}
Tạm tính: ${total_temp}
Giảm giá (10%): ${discount}
Thuế VAT (8%): ${vat}
Tổng thanh toán: ${final_total}
Đã bán thành công!
"""
    print(bill)

def print_report():
    global inventory_stock, total_revenue
    report = f"""
--- BÁO CÁO KINH DOANH ---
Tồn kho hiện tại: {inventory_stock} sản phẩm
Tổng doanh thu: ${total_revenue}
"""
    print(report)

try:
    while True:
        print(menu)
        select = int(input("Chọn chức năng (1-4): "))

        if select == 1:
            print("--- NHẬP HÀNG ---")
            amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
            add_stock(amount)
        elif select == 2:
            print("--- BÁN HÀNG ---")
            quantity = int(input("Nhập số lượng mua: "))
            price = int(input("Nhập đơn giá ($): "))
            if process_sale(quantity) == 0:
                calculate_final_price(quantity, price)
        elif select == 3:
            print_report()
        elif select == 4:
            print("Thoát chương trình thành công!")
            break
        else:
            print("Vui lòng chọn đúng chức năng! Chức năng từ 1 - 4 ")
except ValueError:
    print("Bạn cần nhập số! Yêu cầu nhập lại!")



