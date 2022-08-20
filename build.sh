#! /bin/sh
pyinstaller --onefile --noconsole main.py --name "code_maker"
cp dist/code_maker code_maker
rm -r dist
rm -r build