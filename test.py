from cashier import Transaction
transaksi = Transaction()

# Test Case 1
print("Test Case 1")

transaksi.add_item(["Sabun Muka", 2, 35000])
transaksi.add_item(["Odol Gigi", 1, 12500])
print("Item yang dibeli adalah: ", transaksi.transaction)
print(" ")

# Test Case 2
print("Test Case 2")

transaksi.delete_item("Odol Gigi")
print("Item yang dibeli setelah didelete : ", transaksi.transaction)
print(" ")

# Test Case 3
print("Test Case 3")

transaksi.reset_transaction()
print("Semua item berhasil dihapus!")
print(" ")

# Test Case 4
print("Test Case 4")

transaksi.add_item(["Sabun Muka", 2, 35000])
transaksi.add_item(["Odol Gigi", 1, 12500])
transaksi.add_item(["Minyak Goreng", 4, 40000])
transaksi.add_item(["Santan", 3, 15000])
transaksi.hitung_total_price()
transaksi.check_order()
