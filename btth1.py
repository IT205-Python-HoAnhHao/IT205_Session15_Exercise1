inventory_stock = 100
total_revenue = 0.0

def menu():
   print(''' ========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================''')
   
def add_stock():
    global inventory_stock

    while True:
        try:
            add = int(input("Nhập vào số lượng muốn thêm: "))

            if add <= 0:
                print("Số lượng nhập không dc bé hơn hoặc bằng 0")
                continue

            inventory_stock += add

            print(f"Đã nhập thành công {add} sản phẩm")
            print(f"Tồn kho hiện tại: {inventory_stock}")
            break
        except ValueError:
            print("Không dc nhập vào chữ và kí tự đặc biệt !")   

def check_inventory(buy_amount):
    global inventory_stock
    if buy_amount > inventory_stock:
        print("Số lượng vượt quá hàng trong kho !")
    else: 
        return 0
    
def caculate_final_price(buy_amount, buy_cost):
    global inventory_stock, total_revenue
    discount = 0
    # Khi kho đã xác nhận đủ hàng, hệ thống mới gọi hàm tính toán chi phí (Ví dụ tên hàm: calculate_final_price(quantity, price)):
    # - Tính tổng tiền tạm tính = quantity * price.
    total_temp =  buy_amount * buy_cost # 10 * 150 = 1500
    # - Nếu tổng tiền ≥ 1000, giảm giá 10% (Tạo biến cục bộ discount trong hàm).
    if total_temp >= 1000:
        discount = total_temp * 0.1
    # - Cộng thêm 8% thuế VAT vào tổng tiền sau giảm giá.
        vat = (total_temp - discount) * 0.08
    # - return giá trị tổng tiền cuối cùng (final_total).
    final_total = total_temp - discount + vat
    # Hoàn tất giao dịch (Trừ kho và ghi nhận doanh thu):
    # - Trừ đi số lượng bán trong inventory_stock.
    inventory_stock -= buy_amount
    # - Cộng final_total vào tổng doanh thu toàn cục (total_revenue).
    total_revenue += final_total
    # - In hóa đơn thành công ra màn hình cho khách hàng.
    bill = f"""
-> Hóa đơn chi tiết:
Số lượng: {buy_amount} | Đơn giá: ${buy_cost}
Tạm tính: ${total_temp}
Giảm giá (10%): ${discount}
Thuế VAT (8%): ${vat}
Tổng thanh toán: ${final_total}
Đã bán thành công!
"""
    print(bill)

def print_report():
     global inventory_stock, total_revenue
     print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
     print(f"Tổng doanh thu: ${total_revenue}")
     
def main():
   while True:
      menu()
      choice = input("Nhập vào lựa chọn của bạn: ")

      match choice:
        case "1":
            add_stock()
        case "2":
            while True:
                try: 
                    buy_amount = int(input("Nhập vào số lượng muốn mua: "))

                    if buy_amount <= 0:
                        print("Số nhập vào không dc là số âm và bằng 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Không dc nhập vào chữ và kí tự đặc biệt")

            while True:
                try:
                    buy_cost = float(input("Nhập vào đơn giá: "))

                    if buy_cost <= 0:
                        print("Số nhập vào không dc là số âm và bằng 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Không dc nhập vào chữ và kí tự đặc biệt")

            check_inventory(buy_amount)
            caculate_final_price(buy_amount,buy_cost)
        case "3":
            print_report()
        case "4":
            print("Cảm ơn bạn đã sử dụng !")
            break
        case _:
            print("Nhập lựa chọn sai vui lòng nhập lại !")


main()