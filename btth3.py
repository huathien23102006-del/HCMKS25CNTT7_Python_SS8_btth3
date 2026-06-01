note = ""
sender_phone = ""
receiver_phone = ""

while True:

    print("\nHỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú đơn hàng")
    print("5. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    # Bẫy 6
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    # Bẫy 5
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ")
        continue

    # ================= CHỨC NĂNG 1 =================

    if choice == "1":

        sender = input("Tên người gửi: ")

        if sender.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue

        sender_phone = input("SĐT người gửi: ")

        if sender_phone.strip() == "":
            print("SĐT người gửi không được bỏ trống")
            continue

        pickup = input("Địa chỉ lấy hàng: ")

        if pickup.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue

        receiver = input("Tên người nhận: ")

        if receiver.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue

        receiver_phone = input("SĐT người nhận: ")

        if receiver_phone.strip() == "":
            print("SĐT người nhận không được bỏ trống")
            continue

        delivery = input("Địa chỉ giao hàng: ")

        if delivery.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue

        note = input("Ghi chú giao hàng: ")

        if note.strip() == "":
            print("Ghi chú giao hàng không được bỏ trống")
            continue

        print("\n===== BÁO CÁO =====")

        print("Tên người gửi:",
              sender.strip().title())

        print("Tên người nhận:",
              receiver.strip().title())

        print("Địa chỉ lấy hàng:",
              " ".join(pickup.strip().split()))

        print("Địa chỉ giao hàng:",
              " ".join(delivery.strip().split()))

        print("Ghi chú:",
              note.strip())

        print("Độ dài ghi chú:",
              len(note.strip()))

        print("Số lượng từ:",
              len(note.strip().split()))

        print("Ghi chú chữ thường:",
              note.lower())

        print("Ghi chú chữ hoa:",
              note.upper())

    # ================= CHỨC NĂNG 2 =================

    elif choice == "2":

        code = input("Nhập mã đơn hàng: ")

        if code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue

        print("Mã ban đầu:", code)

        code = code.strip().upper()

        code = "-".join(code.split())

        if not code.startswith("GRAB-"):
            code = "GRAB-" + code

        print("Mã sau chuẩn hóa:", code)

    # ================= CHỨC NĂNG 3 =================

    elif choice == "3":

        if sender_phone == "" or receiver_phone == "":
            print("Chưa có dữ liệu số điện thoại")
            continue

        # SĐT người gửi
        if not sender_phone.isdigit():
            print("Số điện thoại người gửi không hợp lệ")

        elif len(sender_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")

        else:
            hide_sender = (
                sender_phone[:3]
                + "*****"
                + sender_phone[-2:]
            )

            print("SĐT người gửi:", hide_sender)

        # SĐT người nhận
        if not receiver_phone.isdigit():
            print("Số điện thoại người nhận không hợp lệ")

        elif len(receiver_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")

        else:
            hide_receiver = (
                receiver_phone[:3]
                + "*****"
                + receiver_phone[-2:]
            )

            print("SĐT người nhận:", hide_receiver)

    # ================= CHỨC NĂNG 4 =================

    elif choice == "4":

        # Bẫy 4
        if note.strip() == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        find_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        count = note.count(find_word)

        if count == 0:
            print("Không tìm thấy từ khóa")
        else:
            note = note.replace(find_word,
                                replace_word)

            print("Số lần xuất hiện:", count)

            print("Ghi chú sau khi thay thế:")
            print(note)

    # ================= CHỨC NĂNG 5 =================

    elif choice == "5":
        print("Thoát chương trình")
        break