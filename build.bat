pyinstaller --onefile --noconsole --name code_maker main.py
copy dist/code_maker code_maker
rmdir /s /q dist
rmdir /s /q build