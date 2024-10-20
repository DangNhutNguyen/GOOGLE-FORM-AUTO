# GOOGLE-FORM-AUTO

Script Python này cho phép bạn tự động gửi phản hồi đến một Google Form. Script đọc ID của Google Form và dữ liệu phản hồi từ một tệp văn bản, cho phép gửi nhiều phản hồi một cách hiệu quả và lặp lại.

## Tính năng

- Đọc dữ liệu form từ một tệp văn bản đã chỉ định.
- Cho phép gửi nhiều lần trong một vòng lặp.
- Thời gian trễ có thể cấu hình giữa các lần gửi.

## Yêu cầu

- Python 3.x
- Thư viện `requests`

## Cài đặt

1. **Clone kho lưu trữ hoặc tải xuống script:**

   ```bash
   git clone https://github.com/DangNhutNguyen/GOOGLE-FORM-AUTO.git
   cd google-form-auto-submission
   ```

2. **Cài đặt thư viện cần thiết:**

   Bạn có thể cài đặt thư viện `requests` bằng cách sử dụng pip:

   ```bash
   pip install requests
   ```

## Cách sử dụng

1. **Tạo một Tệp Văn Bản:**

   Tạo một tệp văn bản có tên `form_data.txt` trong cùng thư mục với script với định dạng sau:

   ```
   form_id: your_form_id
   entry_id_1: response_1
   entry_id_2: response_2
   entry_id_3: response_3
   ...
   ```

   **Cách thu thập `form_id`:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/67e2985e-358f-4509-b46a-0950df23076c" alt="form_id" width="700"/>
</p>

   Giá trị phía trên các dòng đỏ có nghĩa là `form_id`. Liên kết hoàn chỉnh của Google Form là `https://docs.google.com/forms/d/form_id/formResponse`

   **Cách thu thập `entry.value`:**
   1. Nhấn `Ctrl + Shift + I` để mở Developer Tools. Điều này sẽ hiển thị bảng điều khiển nơi bạn có thể nhập các script tùy chỉnh.

      | Hệ điều hành | Phím |
      | :----------------: | :----: |
      | macOS | <kbd>alt</kbd><kbd>cmd</kbd><kbd>i</kbd> |
      | Windows | <kbd>ctrl</kbd><kbd>shift</kbd><kbd>i</kbd> |
      | Linux | <kbd>ctrl</kbd><kbd>shift</kbd><kbd>i</kbd> |

   2. Truy cập vào tab `Elements` (Gần tab `Console`)
   3. Nhấn `Ctrl + F` để mở công cụ Tìm kiếm
   
      | Hệ điều hành | Phím |
      | :----------------: | :----: |
      | macOS | <kbd>cmd</kbd><kbd>f</kbd> |
      | Windows | <kbd>ctrl</kbd><kbd>f</kbd> |
      | Linux | <kbd>ctrl</kbd><kbd>f</kbd> |
   4. Gõ vào
   ```
   entry.
   ```
   ![image](https://github.com/user-attachments/assets/f675d419-1a88-46be-9597-f1ab246a3d72)

   5. Tìm `entry_id` cho từng câu hỏi (Có nghĩa là `names:`) và `response` trong `form_data.txt` (Có nghĩa là `values`) cho từng câu trả lời
   <p align="center">
   <img src="https://github.com/user-attachments/assets/547eacde-bb6b-48c3-98a4-2a7029e810a3" alt="entry" width="500"/>
   </p>
   
   **Ví dụ nội dung của `form_data.txt`:**

   ```
   form_id: 1FAIpQLSd1XexampleId
   entry.1864374387: 18 - 25
   entry.1101225596: 4
   entry.634083696: 4
   ```
2. **Chạy Script:**

   Thực thi script bằng Python:

   ```bash
   python main.py
   ```

3. **Nhập Số Lần Gửi:**

   Khi được nhắc, nhập số lần bạn muốn gửi form.

## Lưu ý Quan Trọng

- Hãy cẩn thận với tần suất gửi để tránh bị đánh dấu là spam. Đảm bảo rằng việc sử dụng script này tuân thủ các chính sách sử dụng của Google Forms.
- Nếu bạn gặp sự cố với việc gửi form, hãy kiểm tra xem ID form và ID entry có đúng không.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem tệp [LICENSE](LICENSE) để biết chi tiết.

## Lời Cảm ơn

- [Tài liệu Requests](https://docs.python-requests.org/en/latest/) cho thư viện HTTP.

---

Let me know if you need any adjustments or further assistance!
