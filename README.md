# GOOGLE-FORM-AUTO

This Python script allows you to automatically submit responses to a Google Form. The script reads the Google Form ID and response data from a text file, enabling efficient and repeatable submissions.

README in VietNamese find that [here](GOOGLE-FORM-AUTO/READMEvn.md)
## Features

- Reads form data from a specified text file.
- Allows for multiple submissions in a loop.
- Configurable delay between submissions.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository or download the script:**

   ```bash
   git clone https://github.com/DangNhutNguyen/GOOGLE-FORM-AUTO.git
   cd google-form-auto-submission
   ```

2. **Install the required library:**

   You can install the `requests` library using pip:

   ```bash
   pip install requests
   ```

## Usage

1. **Create a Text File:**

   Create a text file named `form_data.txt` in the same directory as the script with the following format:

   ```
   form_id: your_form_id
   entry_id_1: response_1
   entry_id_2: response_2
   entry_id_3: response_3
   ...
   ```

   **How to collect the `form_id`:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/67e2985e-358f-4509-b46a-0950df23076c" alt="form_id" width="700"/>
</p> 

   The value above the red lines means `form_id`. Complete Goolge Form links is `https://docs.google.com/forms/d/form_id/formResponse`
   
   **How to collect the `entry.value`:**
   1. Press `Ctrl + Shift + I` to open the Developer Tools. This will bring up the console where you can enter custom scripts.

      | Operating System | Keys |
      | :----------------: | :----: |
      | macOS | <kbd>alt</kbd><kbd>cmd</kbd><kbd>i</kbd> |
      | Windows | <kbd>ctrl</kbd><kbd>shift</kbd><kbd>i</kbd> |
      | Linux | <kbd>ctrl</kbd><kbd>shift</kbd><kbd>i</kbd> |

   2. Visit the `Elements` (Near the `Console`)
   3. Press `Ctrl + F` to open the Find tools
   
      | Operating System | Keys |
      | :----------------: | :----: |
      | macOS | <kbd>cmd</kbd><kbd>f</kbd> |
      | Windows | <kbd>ctrl</kbd><kbd>f</kbd> |
      | Linux | <kbd>ctrl</kbd><kbd>f</kbd> |
   4. Type in
   ```
   entry.
   ```
   ![image](https://github.com/user-attachments/assets/f675d419-1a88-46be-9597-f1ab246a3d72)

   5. Find the `entry_id` for each question (Which means `names:`) and the `response` in `form_data.txt` (Which means `values`) in each response answer
   <p align="center">
   <img src="https://github.com/user-attachments/assets/547eacde-bb6b-48c3-98a4-2a7029e810a3" alt="entry" width="500"/>
   </p>
   
   **Example content of `form_data.txt`:**

   ```
   form_id: 1FAIpQLSd1XexampleId
   entry.1864374387: 18 - 25
   entry.1101225596: 4
   entry.634083696: 4
   ```
3. **Run the Script:**

   Execute the script using Python:

   ```bash
   python main.py
   ```

4. **Input Number of Submissions:**

   When prompted, enter the number of times you wish to submit the form.

## Important Notes

- Be mindful of the frequency of submissions to avoid being flagged for spam. Ensure that your use of this script complies with Google Forms' usage policies.
- If you encounter issues with form submissions, check that the form ID and entry IDs are correct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Requests Documentation](https://docs.python-requests.org/en/latest/) for the HTTP library.
